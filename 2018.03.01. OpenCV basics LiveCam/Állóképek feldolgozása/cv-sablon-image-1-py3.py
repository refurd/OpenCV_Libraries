# Sablon program állóképek feldolgozásához
# Alapverzió: csak fájl beolvasás és kiírás

# szokásos importálások
import numpy as np
import cv2
import os

#------- beállítások
# os.chdir(r"......")   # ha szükséges, adjuk meg ezt is

in_file="be.png"    # beolvasandó fájl
out_file="ki.png"   # kiírandó fájl
#------------------------
in_img=cv2.imread(in_file)
#------------------------
# FELDOLGOZÁS
print("Feldolgozás indul...")

out_img=255-in_img # egyszerű példa, ezt kell lecserélni a saját utasításokra

# Feldolgozás vége
print("Feldolgozás vége.")

#------------------------
cv2.imwrite(out_file, out_img) # kiírás

