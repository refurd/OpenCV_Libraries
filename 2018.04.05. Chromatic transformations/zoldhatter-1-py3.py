# -*- coding: utf8 -*-

# A sablon programot írtam át
# "Zöld háttér technika": egyszerű változat.
# az in_hatter-ben megadott kép lesz a háttér, amit bemásol 
# in_minta azon pixelei helyére, ahol in_minta élénkzöld pixeleket 
# tartalmaz.
# 
# Első változat: nem elkülönített programrészek, "beégetett" értékek


# szokásos importálások
import numpy as np
import cv2
import os

#------- beállítások
# os.chdir("......")   # ha szükséges, adjuk meg ezt is

in_hatter="kicsi-felho-1.jpg"  # ez legyen, amit bevágunk a megfelelő helyre
in_minta="repulos.jpg" # ez a "zöld háttér" előtt készült kép
out_file="ki.png"   # kiírandó fájl
#------------------------
img_h=cv2.imread(in_hatter)
img_m=cv2.imread(in_minta)
#------------------------
# FELDOLGOZÁS
print("Feldolgozás indul...")

m_HSV=cv2.cvtColor(img_m, cv2.COLOR_BGR2HSV)
zold_mask=(abs(m_HSV[:,:,0]-60.0)<10.0) & (m_HSV[:,:,1]>140)  
#     60*2=120 fok: zöld szín              140-nél nagyobb S: élénk

out_img=img_h.copy()  # kimenet: alapból a háttér
out_img[~zold_mask,0:3]=img_m[~zold_mask,0:3] # ahol nem zöld az előtér, ott a "minta" kép pixeleit vesszük

# Feldolgozás vége
print("Feldolgozás vége.")

#------------------------
cv2.imwrite(out_file, out_img) # kiírás

