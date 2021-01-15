# -*- coding: utf8 -*-

# A sablon programot írtam át
# "Zöld háttér technika": egyszerű változat.
# az in_hatter-ben megadott kép lesz a háttér, amit bemásol 
# in_minta azon pixelei helyére, ahol in_minta élénkzöld pixeleket 
# tartalmaz.
# 
#  Második változat: elkülönített programrészek, "beégetett" értékek


# szokásos importálások
import numpy as np
import cv2
import os

#------------------------------------------------------
def greenbox(img_h, img_m, H0=60.0, dH=10.0, Smin=140):
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
out_file="ki2.png"   # kiírandó fájl
#------------------------
img_h=cv2.imread(in_hatter)
img_m=cv2.imread(in_minta)
#------------------------
# FELDOLGOZÁS
print("Feldolgozás indul...")


#out_img=greenbox(img_h, img_m)  # így is lehet hívni: default értékek

out_img=greenbox(img_h, img_m, Smin=100) # átírjuk a minimális telítettséget

# Feldolgozás vége
print("Feldolgozás vége.")

#------------------------
cv2.imwrite(out_file, out_img) # kiírás

