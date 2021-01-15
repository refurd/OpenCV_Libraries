# Sablon program állóképek feldolgozásához
# Általánosabb verzió: választható megjelenítés, fájlnév-bekérés...

# szokásos importálások
import numpy as np
import cv2
import os
import tkinter as tk
from tkinter import filedialog


#------- beállítások
# os.chdir("...........")   # ha szükséges....

in_file="be.png"   # beolvasandó fájl alapértemlezett neve
in_request=True    # True: inkább kérjük be a fájlnevet interaktívan
                   # False: maradjon az előbb megadott fájlnév
in_window=True     # Megjelenítsük-e az eredeti képet ablakban
out_window=True    # Megjelenítsük-e a kimenetet ablakban

out_file="ki.png"  # kiírandó fájl alapértelmezett neve
out_request=True  # True: kérdezzük meg a felhasználót a kimeneti fájlról
#-------

root=tk.Tk()
root.withdraw()   # ne látszódjon a root ablak
wdir=os.getcwd()

if in_request:     # bemeneti fájl nevét bekérő ablak megnyitása, ha kell
	in_file=filedialog.askopenfilename(parent=root,title="Bemeneti fájl",initialdir=wdir)
	# ha ez meg volt hívva, akkor felülírtuk az in_file változót

in_img=cv2.imread(in_file)  # beolvasás, mindenképp ezen a néven

#------------------------
# FELDOLGOZÁS
print("Feldolgozás indul...")

# ide jönnek a saját utasítások

out_img=255-in_img # egyszerű példa, ezt kell lecserélni

# Feldolgozás vége
print("Feldolgozás vége.")

#------------------------
if in_window: 
	cv2.namedWindow("Bemenet")   # ablak megnyitása, ha kell
	cv2.imshow("Bemenet", in_img)

if out_window:
	cv2.namedWindow("Kimenet")   # ablak megnyitása, ha kell
	cv2.imshow("Kimenet",out_img)

if in_window or out_window:
	cv2.waitKey(0)               # ha megjelenítettünk ablakot, akkor várunk 
#------------------------

if out_request:       # kiírás helyének bekérése, ha kell
	out_file=filedialog.asksaveasfilename(parent=root,title="Kimeneti fájl",initialdir=wdir)

cv2.imwrite(out_file,out_img) # kiírás

#------------------------

root.destroy()  # menj innen, te gyökér!
if in_window or out_window: 
	cv2.destroyAllWindows()  # ne legyen huzat....
