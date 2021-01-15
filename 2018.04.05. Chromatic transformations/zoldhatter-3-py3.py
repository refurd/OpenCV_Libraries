# -*- coding: utf8 -*-

# "Zöld háttér technika": egyszerű változat.
# az in_hatter-ben megadott kép lesz a háttér, amit bemásol 
# in_minta azon pixelei helyére, ahol in_minta élénkzöld pixeleket 
# tartalmaz.
# 
#  Harmadik változat: elkülönített programrészek, értékek a kép tetjéről
#
# Még ez sem tökéletes, de szabad továbbfejleszteni...


# szokásos importálások
import numpy as np
import cv2
import os

#------------------------------------------------------
def greenbox_params(im):
	"""A képre számol egy H0, dH párt és egy Smin értéket."""

	im_HSV=cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
	Hmin=im_HSV[:,:,0].min()
	Hmax=im_HSV[:,:,0].max()
	Smin=im_HSV[:,:,1].min()

	H0=int((float(Hmin)+Hmax)/2.0)
	dH=int((Hmax-Hmin)/2.0+1)   # +1: hogy biztos elég legyen

	return H0,dH,Smin


def greenbox(img_h, img_m, H0=60.0, dH=10.0, Smin=140):
	"""igm_h háttér elé teszi img_m azon pixeleit, melyek nem a megadott H,S tartományban vannak."""
	m_HSV=cv2.cvtColor(img_m, cv2.COLOR_BGR2HSV)
	zold_mask=(abs(m_HSV[:,:,0]-H0)<dH) & (m_HSV[:,:,1]>Smin)  

	result=img_h.copy()  # kimenet: alapból a háttér
	result[~zold_mask,0:3]=img_m[~zold_mask,0:3] # ahol nem zöld az előtér, ott a "minta" kép pixeleit vesszük

	return result


#------------------------------------------------------


#------- beállítások
# os.chdir("......")   # ha szükséges, adjuk meg ezt is

in_hatter="kicsi-felho-1.jpg"  # ez legyen, amit bevágunk a megfelelő helyre
in_minta="repulos.jpg" # ez a "zöld háttér" előtt készült kép
out_file="ki3.png"   # kiírandó fájl
#------------------------
img_h=cv2.imread(in_hatter)
img_m=cv2.imread(in_minta)
#------------------------
# FELDOLGOZÁS
print("Feldolgozás indul...")


# meghatározzuk a háttér paramétereit
H0,dH,Smin=greenbox_params(img_m[:10,:]) # a kép első 10 sorából számolunk

print("Debug:", H0,dH,Smin)  # hibakeresés: csak hogy tudjuk, mivel számol

out_img=greenbox(img_h, img_m, Smin=100) # átírjuk a minimális telítettséget

# Feldolgozás vége
print("Feldolgozás vége.")

#------------------------
cv2.imwrite(out_file, out_img) # kiírás

