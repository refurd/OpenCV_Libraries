
# Cél: ugyanazokat az eljárásokat máshogy megvalósítani és figyelni a sebességet.
#
# Futási időmérése :
#
# import time     # az elején
# t0=time.clock(); aminek_az_idejet_merjuk(im); print time.clock()-t0
#
# Magyarázat: a time modul clock() fgv-e kiadja az adott program kezdetétől elhasznált másodperceket. 
# Figyelem! nem túl pontos! (~0.01s)

# Az elején csak sok definíció van, lentebb lehet a sebességet tesztelni.

import cv2
import numpy as np
import os
import time

#---------------------------------------------------------------------
# különféle megoldások kép invertálására, hogy tesztelhessük a sebességet

# legegyszerűbb megoldás(nak tűnik):

def inverz1(im):
	"""Legegyszerűbben invertál egy képet"""  # az ide írt szövegek az IDLE is látja!
	maxsor, maxoszl=im.shape[:2]

	for sor in range(maxsor):
		for oszl in range(maxoszl):
			pix=im[sor, oszl]
			R=pix[2]
			G=pix[1]
			B=pix[0]
			im[sor, oszl]=[255-G, 255-B, 255-R]
	return(im)

# gyorsít, ha nem használunk ideiglenes változókat?:
def inverz2(im):
	"""Ideiglenes változók kiírtása"""  # az ide írt szövegek az IDLE is látja!
	maxsor, maxoszl=im.shape[:2]

	for sor in range(maxsor):
		for oszl in range(maxoszl):
			pix=im[sor, oszl]
			im[sor, oszl]=[255-pix[0], 255-pix[1], 255-pix[2]]

	return(im)


# while-lal esetleg gyorsabb?:
def inverz3(im):
	"""Gyorsabb verzió while-lal?"""
	maxsor, maxoszl=im.shape[:2]

	sor=0
	while sor<maxsor:
		oszl=0
		while oszl<maxoszl:
			pix=im[sor, oszl]
			R=pix[2]
			G=pix[1]
			B=pix[0]
			im[sor, oszl]=[255-G, 255-B, 255-R]

			oszl+=1
		sor+=1
	return(im)


# a színcsatornákon is ciklussal megyünk végig:
def inverz4(im):
	"""Színcsatornákon is ciklussal megyünk"""
	maxsor, maxoszl, maxcsat=im.shape

	for sor in range(maxsor):
		for oszl in range(maxoszl):
			for csat in range(maxcsat):
				im[sor, oszl, csat]=255-im[sor, oszl, csat]

	return(im)

# tartomány-kijelöléses verzió:
def inverz5(im):
	"""Tartomány-kijelöléses verzió"""

	im[:,:,:]=255-im[:,:,:]

	return(im)

# tartomány-kijelöléses verzió, tömörebb:
def inverz6(im):
	"""Tartomány-kijelöléses verzió ; még tömörebb"""

	im=255-im
	
	return(im)


#---------------------------------------------------------------
# különféle poszterizáló megoldások

def poszter1(im):
	"""Legegyszerűbben poszterizál egy képet"""  
	maxsor, maxoszl=im.shape[:2]

	for sor in range(maxsor):
		for oszl in range(maxoszl):
			pix=im[sor, oszl]
			R=pix[2]
			G=pix[1]
			B=pix[0]
			if (R<G) or (R<B): 
				R=0
			if (G<B) or (G<R):
				G=0
			if (B<R) or (B<G):
				B=0
			im[sor, oszl]=[B,G,R]
	return im

# trükkös megoldás logikai értékekkel való szorzással
def poszter2(im):
	"""Trükkösen poszterizál egy képet"""  

	# A logikai "True" 1-gyé, a "False" 0-vá alakul

	im[:,:,0]*=(im[:,:,1]<=im[:,:,0])   # a zárójeles kifejezés ott 0, ahol az 1-es színcsatorna megahaldja a 0-s értékét; itt nullázunk
	im[:,:,0]*=(im[:,:,2]<=im[:,:,0])   # hasonlóan a többi esetre
	im[:,:,1]*=(im[:,:,0]<=im[:,:,1])
	im[:,:,1]*=(im[:,:,2]<=im[:,:,1])
	im[:,:,2]*=(im[:,:,0]<=im[:,:,2])
	im[:,:,2]*=(im[:,:,1]<=im[:,:,2])

	return im

# trükkös megoldás logikai értékekkel való szorzással; tömörebben
def poszter3(im):
	"""Még trükkösebben poszterizál egy képet"""  

	im[:,:,0]*=(im[:,:,1]<=im[:,:,0]) * (im[:,:,2]<=im[:,:,0]) 
	im[:,:,1]*=(im[:,:,0]<=im[:,:,1]) * (im[:,:,2]<=im[:,:,1])
	im[:,:,2]*=(im[:,:,0]<=im[:,:,2]) * (im[:,:,1]<=im[:,:,2])

	return im

# másféle vektorizálás
def poszter4(im):
	"""Poszterizálás: csatornánkénti maximum számítással."""  

	immax=im.max(axis=2)  # pixelen belül kiszámolja a max értékeket
	im[:,:,0]*=(im[:,:,0]<immax[:,:])  # ha a maximum alatt vagyunk, inkább nullázunk
	im[:,:,1]*=(im[:,:,1]<immax[:,:])  # ha a maximum alatt vagyunk, inkább nullázunk
	im[:,:,2]*=(im[:,:,2]<immax[:,:])  # ha a maximum alatt vagyunk, inkább nullázunk

	return im

def poszter5(im):
	"""Poszterizálás: Feltételes indexelés."""  

	R=im[:,:,2]
	G=im[:,:,1]
	B=im[:,:,0]

	R[R<G]=0
	R[R<B]=0
	G[G<R]=0
	G[G<B]=0
	B[B<G]=0
	B[B<R]=0

	return im

#-------------------------------------------------------------------------
# fényesség-növelés túlcsorduás-védelemmel

def fenyes1(im):
	"""Fényességnövelés, egyszerű ciklussal."""
	maxsor, maxoszl, maxcsat=im.shape

	mul=1.5
	for sor in range(maxsor):
		for oszl in range(maxoszl):
			for csat in range(maxcsat):
				if (im[sor, oszl, csat]*mul>255.0):
					im[sor, oszl, csat]=255
				else:
					im[sor, oszl, csat]=(im[sor, oszl, csat]*mul).astype(np.uint8)

	return im

def fenyes2(im):
	"""Fényességnövelés, matematikai művelettel"""

	mul=1.5
	im=(im*mul>255.0)*255+(im*mul<=255)*im
	return im


def fenyes3(im):
	"""Fényességnövelés, feltételes indexeléssel"""

	mul=1.5
	kicsik=im<np.uint8(255/mul)  # azon helyek "térképe", ahol nem lesz túlcsordulás
	im[kicsik]=im[kicsik]*mul    # itt bátran szorozhatunk
	im[~kicsik]=255              # ~kicsik = kicsik logikai inverze

	return im


def fenyes4(im):
	"""Fényességnövelés, lookup table"""

	mul=1.5
	# feltöltjük a lookup table-t Ezt elég egyszer megtenni, 
	lt=np.zeros(256, np.uint8)
	for i in range(256):
		if i*mul>255:
			lt[i]=255
		else:
			lt[i]=np.uint8(i*mul)

	im=lt[im]

	return im


def fenyes5(im):
	"""Fényességnövelés, speciális függvényhívással"""

	mul=1.5
	im=np.clip(im*mul, 0.0, 255.0).astype(np.uint8)
	return im
	

#-------------------------------------------------------------------------
# egyszerű tesztelési rutin, időt mér és ír ki
def test(im, nev, eljaras):
	im_test=im.copy()  # másolaton dolgozunk, hogy ne legyen baja az eredetinek
	t0=time.clock()
	out=eljaras(im_test)
	print("%s:\t%f s"%(nev,time.clock()-t0))
	return out


#----------------------


# os.chdir(r"") # ha kellene

in_file="kicsi-felho-1.jpg"  # ez átírandó!

im=cv2.imread(in_file)

#---------------------

# most jönnek az igazi tesztelések
if (True): # True: csináld meg, False: hagyd ki
	im_out=test(im, "Inverz eredeti", inverz1)
	im_out=test(im, "Inverz tomor", inverz2)
	im_out=test(im, "Inverz while", inverz3)
	im_out=test(im, "Inverz 3-as for", inverz4)
	im_out=test(im, "Inverz tartomany", inverz5)
	im_out=test(im, "Inverz teljes tomb", inverz6)

	cv2.imwrite("output-inv.png", im_out) # tegyük oda, aminek a kimenete érdekel

	print("\n"+"-"*50)

if (True):
	im_out=test(im, "Poszter for ciklus", poszter1)
	im_out=test(im, "Poszter matematika 1", poszter2)
	im_out=test(im, "Poszter matematika 2", poszter3)
	im_out=test(im, "Poszter maximum", poszter4)
	im_out=test(im, "Poszter felt.index", poszter5)

	cv2.imwrite("output-poszt.png", im_out) # tegyük oda, aminek a kimenete érdekel

	print("\n"+"-"*50)

if (True):
	im_out=test(im, "Fényesítés for ciklus", fenyes1)
	im_out=test(im, "Fényesítés matematika", fenyes2)
	im_out=test(im, "Fényesítés felt.index", fenyes3)
	im_out=test(im, "Fényesítés lookup tab", fenyes4)
	im_out=test(im, "Fényesítés spec.muv.", fenyes5)

	cv2.imwrite("output-feny.png", im_out) # tegyük oda, aminek a kimenete érdekel



