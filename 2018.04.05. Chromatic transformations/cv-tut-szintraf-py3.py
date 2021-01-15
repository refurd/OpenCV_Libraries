
# Gyakran használatos színkezelési fogásokat mutat be.
# rutinok definiálása, aztán használatuk

import cv2
import numpy as np
import os

#---- Üres képek létrehozása

def black_image(size):
	"""Az argumentumban megadott méretű fekete képpel tér vissza. 
	size=(maxsor, maxoszl, maxcsat).
	Pl.: black_image((100,200,3))"""
	result=np.zeros(size, np.uint8)
        # size tartalmazza a méretet és a színcsatorna számot is!
        # np.uint8: a numpy u(nsigned)int(eger)8(bit) típusa, azaz egy bájt
	return(result)


def BGR_image(size, BGR):
	"""Az argumentumban megadott méretű adott [B,G,R]-ű képpel tér vissza. 
	size=(maxsor, maxoszl, maxcsat).
	Pl.: BGR_image((100,200,3), [100, 200, 10])"""
	result=black_image(size)
	result[:,:,:]=np.uint8(BGR)
	return(result)


def white_image(size):
	"""Az argumentumban megadott méretű adott fehér képpel tér vissza. 
	size=(maxsor, maxoszl, maxcsat).
	Pl.: white_image((100,200,3))"""
	return( BGR_image(size,[255,255,255]) )



#---- Átlagos szín számítása

def color_average(im):
        """Kiszámolja egy kép pixelértékeinek átlagát színcsatornánként. 3 színcsatornát feltételez.
           Józan eszes változat."""
        nrow, ncol = im.shape[:2]
        npix=nrow*ncol # ennyi pixel van a képben

        Rsum=im[:,:,2].sum()  # összegzés
        Gsum=im[:,:,1].sum()
        Bsum=im[:,:,0].sum()

        average=np.asarray([Rsum, Gsum, Bsum], np.float64) # ezek még csak az összegek
        average/=npix # most lesz belőlük átlag
	
        return(average)


def color_average2(im):
	"""Kiszámolja egy kép pixelértékeinek átlagát színcsatornánként. 3 színcsatornát feltételez.
           Tömörebb változat."""
	average=im.mean(axis=(0,1), dtype=np.float64) # ezek még csak az összegek
	average=average[::-1]  # fordított sorrend, hogy R,G,B legyen a kiíráskor
	
	return(average)


#--- átlagos szín számítás maszkolással

def color_average_mask(im, mask):
        """Csak ott számol átlagot, ahol a mask nem 0 értéket vesz fel.
        im és mask sor és oszlopszáma meg kell egyezzen, mask 1 csatornás kell legyen."""

        nrow, ncol = im.shape[:2]
	
        # a maszk méreteink kezelése
        if (len(mask.shape)==2):     
                nrow_mask, ncol_mask = mask.shape
                nch_mask=1
        else:
                nrow_mask, ncol_mask, nch_mask=mask.shape

        #-- hibakezelés, finomítható....
        if (nch_mask!=1):
                print("Hiba: Egy színcsatornás maszk kell!")
                return([0,0,0])
        if ( (nrow!=nrow_mask) or (ncol!=ncol_mask) ): 
                print("Hiba: a kép és a maszk mérete azonos kell legyen!")
                return([0,0,0])

        # most jön a lényeg

        mask2=(mask>0) # minden, ami  nem 0, legyen 1
        npix=mask2.sum() # ennyi aktív pixel van
        if (npix==0):
                print("Hiba: a maszk teljesen elfed mindent!")
                return([0,0,0])

        im2=im.copy()
        im2[:,:,0]*=mask2 # kinullázzuk, ahol a maszk nem 0
        im2[:,:,1]*=mask2 # kinullázzuk, ahol a maszk nem 0
        im2[:,:,2]*=mask2 # kinullázzuk, ahol a maszk nem 0

        average=im2.sum(axis=(0,1), dtype=np.float64) # ezek még csak az összegek
        average/=npix # most lesz belőlük átlag
        average=average[::-1]  # fordított sorrend, hogy R,G,B legyen a kiíráskor
	
        return(average)




# csak a fényesek átlagának számolása
def color_average_light(im, limit):
	"""Csak ott számol átlagot, ahol kép "fényesebb" limit-nél."""

	# elkészítjük a szürkeárnyalatos változatot:
	im_gray=cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)  # így csinálunk szürkeárnyalatos képet
		
	# ezt használuk maszkként
	mask = (im_gray>=limit)   # ott 1, ahol teljesül az egyenlőtlenség

	return (color_average_mask(im, mask))

#-----------------------------------------------------------------------------
# bonyolultabb transzformációk HSV-vel
#-----------------------------------------------------------------------------

def keep_saturated(im, S_limit):
	"""Az im-ben lenullázza azokat, ahol S nem éri el a limitet"""

	im_HSV=cv2.cvtColor(im, cv2.COLOR_BGR2HSV)  # !!! így konvertálunk HSV-re
	# !!! vigyázat! H 0-tól 180-ig megy 360 helyett! S és V meg 0-tól 255-ig a számábrázolás miatt

	# lenullázzuk mindegyik színcsatornát, ahol nem elég nagy az S (saturation)
	im[:,:,0]*=(im_HSV[:,:,1]>S_limit)
	im[:,:,1]*=(im_HSV[:,:,1]>S_limit)
	im[:,:,2]*=(im_HSV[:,:,1]>S_limit)


def keep_H_range(im, H0, deltaH):
	"""A képen kinullázza azokat a pixeleket, melyek H-ja
	távolabb van H0-tól, mint deltaH. A bemeneten H-ról 0 és 360 közti
	értékeket tételezünk fel."""

	# áttérünk HSV-re
	im_HSV=cv2.cvtColor(im, cv2.COLOR_BGR2HSV) 

	# a cv2 0 és 180 fok közé teszi H-t...
	H0/=2
	deltaH/=2

	# különvesszük H-t egy tömbbe és int-té alakítjuk:
	H_array=(im_HSV[:,:,0].copy()).astype(int)

	# hol maradhat, hol kell 0-zni?
	mask=( abs(H_array - H0) < deltaH )

	# vigyázat! körbefordulás 
	mask+=( abs((H_array-180) - H0) < deltaH )

	# ahol a mask pozitív, ott maradhatnak az értékek
	im[:,:,0]*=(mask>0)
	im[:,:,1]*=(mask>0)
	im[:,:,2]*=(mask>0)


def keep_S_range(im, S0, deltaS):
	"""A képen kinullázza azokat a pixeleket, melyek S-e
	távolabb van S0-tól, mint deltaS. """

# ÖNÁLLÓ FELADAT

def keep_V_range(im, V0, deltaV):
	"""A képen kinullázza azokat a pixeleket, melyek V-je
	távolabb van V0-tól, mint deltaV. """

# ÖNÁLLÓ FELADAT


#----------------

def saturation_mul(im, fac):
	"""A telítettséget növeli fac-szorosára"""

	# áttérünk HSV-re
	im_HSV=cv2.cvtColor(im, cv2.COLOR_BGR2HSV) 
	
	# egy másolaton dolgozunk, ami float
	S=(im_HSV[:,:,1].copy()).astype(float)
	S=(S*fac<255.0)*(S*fac) + (S*fac>=255.0)*255.0

	# visszaírjuk
	im_HSV[:,:,1]=S[:,:]
	# most visszatranszformáljuk:
	im=cv2.cvtColor(im_HSV, cv2.COLOR_HSV2BGR)

	return(im)

def value_mul(im, fac):
	"""A fényességet növeli fac-szorosára"""

# ÖNÁLLÓ FELADAT


def hue_mul(im, fac):
	"""A színezetet növeli fac-szorosára"""

# ÖNÁLLÓ FELADAT
# de van ennek értelme?
# H ciklikus: vigyázni kell!

#-----------------------------------
# főprogram
#
# most használjuk a rutinokat



# képek létrehozása a semmiből
feher=white_image((100,100,3))
cv2.imwrite("teszt-feher.png", feher)
lila=BGR_image((100,100,3),[200,20,200])
cv2.imwrite("teszt-lila.png", lila)


# egy kép átlagszínének számítása
#os.chdir(r"...")  # ha kell
im0=cv2.imread("virag-2.jpg")

im=im0.copy() # másolaton dolgozunk

print("Teljes kép átlaga:")
print(color_average(im))   # egyik változat
print(color_average2(im))  # másik változat

print("Középső rész átlaga (20-as keret lehagyása mindenütt):")
mask=np.zeros(im.shape[:2], np.uint8)  # üres maszk
mask[20:-20, 20:-20]=1   # 1-es ott, ahol nem a kereten vagyunk
print(color_average_mask(im, mask))

print("Középső rész átlaga (méret negyede lehagyva körben):")
mask=np.zeros(im.shape[:2], np.uint8)  # üres maszk
border1, border2=mask.shape[:2] 
border1//=4
border2//=4
mask[border1:-border1, border2:-border2]=1   # 1-es ott, ahol nem a kereten vagyunk
print(color_average_mask(im, mask))

print("Fényes részek átlaga:")
print(color_average_light(im, 150))

#-----------------

# élénk részek kikeresése
elenk=im0.copy()
keep_saturated(elenk, 100)  # helyben felülírja!
cv2.imwrite("teszt-csakelenk.png", elenk)

# csak a pirosak meghagyása
piros=im0.copy()
keep_H_range(piros, -10,10)  # helyben felülírja!
cv2.imwrite("teszt-csakpiros.png", piros)

# élénkített
elenkebb=saturation_mul(im0, 3) # ezt most nem helyben csinálja. ízlés dolga
cv2.imwrite("teszt-elenkebb.png", elenkebb)


