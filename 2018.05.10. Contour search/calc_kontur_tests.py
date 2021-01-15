#!/usr/bin/python3
# -*- coding: utf8 -*-

# Ez számolja ki a prezentációban bemutatott példákat

import cv2
import numpy as np
import sys


fname="kontur-3.png" # ezt a fájlt olvassuk be és elemezzük
base="aa"   # minden kimeneti fájlnév ezzel kezdődik, hogy azonosíthatók legyenek

# beolvasás és szürkeárnyalatossá alakítás
im1=cv2.imread(fname)
im1g=cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)

cv2.imwrite(base+"-orig.png", im1)
cv2.imwrite(base+"-gray.png", im1g)

#------------------------------------------
# kipróbáljuk a küszöbölést (thresholding)

# józan eszes, vektorizálós megoldás
mask=255*(im1g>127)
cv2.imwrite(base+"-bw127.png", mask)

# cv2 megoldás:
lim, mask=cv2.threshold(im1g, 120, 255, cv2.THRESH_BINARY)
print("lim=",lim)
# visszakapjuk a 120-at! mi az értleme? meglátjuk nemsokára...
cv2.imwrite(base+"-bw120.png", mask)

lim, mask=cv2.threshold(im1g, 40, 255, cv2.THRESH_BINARY)
cv2.imwrite(base+"-bw040.png", mask)

lim, mask=cv2.threshold(im1g, 200, 255, cv2.THRESH_BINARY)
cv2.imwrite(base+"-bw200.png", mask)

# automatikus globális küszöb megválasztása:
lim, mask=cv2.threshold(im1g, 200, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print("lim=",lim)
# ez már az automatikus eljárás (Otsu) ereménye
# többnyire elfogadható érték.
cv2.imwrite(base+"-bwOtsu.png", mask)
# azért nem tökéletes

#-----------------------------
# adaptív küszöbölés: 
# 1) a kép másolatát elmossa
# 2) akkor fehér (előtér) a kimenet, ha az eredti pixelérték
#    legalább egy C értékkel meghaladja az elmosott értéket
# Az elmosás sugár és az elmosási módszer sokat meghatároz

# egyszerű, súlyozatlan elmosás
mask=cv2.adaptiveThreshold(im1g, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, C=0)
cv2.imwrite(base+"-bw_a_mean_15.png", mask)

mask=cv2.adaptiveThreshold(im1g, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 45, C=-1)
cv2.imwrite(base+"-bw_a_mean_45.png", mask)


mask=cv2.adaptiveThreshold(im1g, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, C=-3)
cv2.imwrite(base+"-bw_a_gauss_15.png", mask)

mask=cv2.adaptiveThreshold(im1g, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 45, C=-3)
cv2.imwrite(base+"-bw_a_gauss_45.png", mask)

#mask=cv2.adaptiveThreshold(im1g, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 75, C=-3)
#cv2.imwrite(base+"-bw_a_gauss_75.png", mask)
#----------------------------------
# most kontúrokat illesztünk



# belső és külső kontúrok meghatározása
conts, hier=cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# hier: egymásba ágyzási hierarchia, nem foglalkozunk vele
# conts: kontúrok listája

# halványított másolat az eredeti képről: erre fogunk rajzolni
out_img=im1.copy()//2

for cont in conts:
        cv2.drawContours(out_img, cont, -1, (255,0,255))

cv2.imwrite(base+"-list.png", out_img)


# csak a külső kontúrok meghatározása
conts, hier=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# halványított másolat az eredeti képről: erre fogunk rajzolni
out_img=im1.copy()//2

for cont in conts:
        cv2.drawContours(out_img, cont, -1, (255,0,255))

cv2.imwrite(base+"-external.png", out_img)


#------
out_img=im1.copy()//2

for cont in conts:
        # konvex burkok rajzolása
        cv2.drawContours(out_img, [cv2.convexHull(cont)], -1, (0,255,255))

cv2.imwrite(base+"-hull.png", out_img)

# befoglaló körök
out_img=im1.copy()//2
for cont in conts:
        cv2.drawContours(out_img, cont, -1, (255,0,255))
        # körülírt körök rajzolása
        center, r=cv2.minEnclosingCircle(cont) # ez kiszámolja
        # de át kell váltani egészre
        ic=(int(center[0]), int(center[1]))
        ir=int(r)
        # most kirajzolni a kört
        cv2.circle(out_img, ic, ir, (255,127,0))

cv2.imwrite(base+"-circ.png", out_img)


# illeszkedő ellipszisek
out_img=im1.copy()//2
for cont in conts:
        cv2.drawContours(out_img, cont, -1, (255,0,255))
        # körülírt körök rajzolása
        if len(cont)<5: continue # nem lehet ellipszist illeszteni
        ellipse=cv2.fitEllipse(cont) # ez kiszámolja
        # most kirajzolni az ellipszist
        cv2.ellipse(out_img, ellipse, (255,127,0))

cv2.imwrite(base+"-ellipse.png", out_img)

#----------------------------------
# beleírunk a képekbe: sorszámozás

out_img=im1.copy()/2
i=1 # sorszámozás
for cont in conts:
        # momentum-számítás:
        mom=cv2.moments(cont)

        area=mom['m00'] # 0. momentum: terület
        if area<=0: continue # 1 pontos kontúr
        xc=int(mom['m10']/area) # 1. momentumok normalizálva: 
        yc=int(mom['m01']/area) # ... tömegközéppont

        cv2.drawContours(out_img, cont, -1, (255,0,255))
        cv2.putText(out_img,"%d" % i,(xc-8,yc), cv2.FONT_HERSHEY_PLAIN,1.0,(196,196,255))
        i+=1

cv2.imwrite(base+"-sorszam.png", out_img)

# beleírunk a képekbe: terület és kerület
out_img=im1.copy()//2
i=1 # sorszámozás
for cont in conts:
        # momentum-számítás:
        mom=cv2.moments(cont)

        area=mom['m00'] # 0. momentum: terület
        if area<=0: continue # 1 pontos kontúr
        xc=int(mom['m10']/area) # 1. momentumok normalizálva: 
        yc=int(mom['m01']/area) # ... tömegközéppont
        perim=cv2.arcLength(cont, True) # True: zárd be a végét!

        cv2.drawContours(out_img, cont, -1, (255,0,255))
        cv2.putText(out_img,"T=%5.0f" % area,(xc-20,yc), cv2.FONT_HERSHEY_PLAIN,1.0,(196,196,255))
        cv2.putText(out_img,"K=%5.1f" % perim,(xc-20,yc+15), cv2.FONT_HERSHEY_PLAIN,1.0,(196,196,255))
        i+=1

cv2.imwrite(base+"-TerKer.png", out_img)

# beleírunk a képekbe: körszerűség, konvexitás
out_img=im1.copy()//2
i=1 # sorszámozás
for cont in conts:
        # momentum-számítás:
        mom=cv2.moments(cont)

        area=mom['m00'] # 0. momentum: terület
        if area<=0: continue # 1 pontos kontúr
        xc=int(mom['m10']/area) # 1. momentumok normalizálva: 
        yc=int(mom['m01']/area) # ... tömegközéppont
        perim=cv2.arcLength(cont, True) # True: zárd be a végét!

        # Mennyire körszerű? Körre circ=1.0, máskor kisebb
        circ=4.0*3.14159265*area/perim**2
        # mennyire konvex? Konvexre sol=1.0, máskor kisebb
        sol=area/cv2.contourArea(cv2.convexHull(cont))

        cv2.drawContours(out_img, cont, -1, (255,0,255))
        cv2.putText(out_img,"circ=%4.3f" % circ,(xc-30,yc), cv2.FONT_HERSHEY_PLAIN,1.0,(196,196,255))
        cv2.putText(out_img,"sol =%4.3f" % sol,(xc-30,yc+15), cv2.FONT_HERSHEY_PLAIN,1.0,(196,196,255))
        i+=1

cv2.imwrite(base+"-CircSol.png", out_img)


# beleírunk a képekbe: Hu-momentumok
out_img=im1.copy()//2
i=1 # sorszámozás
for cont in conts:
        # momentum-számítás:
        mom=cv2.moments(cont)

        area=mom['m00'] # 0. momentum: terület
        if area<=0: continue # 1 pontos kontúr
        xc=int(mom['m10']/area) # 1. momentumok normalizálva: 
        yc=int(mom['m01']/area) # ... tömegközéppont

        hu=cv2.HuMoments(mom)

        cv2.drawContours(out_img, cont, -1, (255,0,255))
        for ihu in range(4):  # 7 van, de nem fér ki
                cv2.putText(out_img,"%6f" % hu[ihu],(xc-30,yc+10*ihu), cv2.FONT_HERSHEY_PLAIN,0.6,(196,196,255))
        i+=1

cv2.imwrite(base+"-Hu.png", out_img)

