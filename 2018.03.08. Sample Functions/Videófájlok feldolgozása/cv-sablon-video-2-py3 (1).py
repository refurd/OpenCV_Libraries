# -*- coding: utf8 -*-

# Sablon program mozgókép-fájlok feldolgozásához
# alap verzió: kimeneti kép a mostanitól és az előzőtől függ, 
# egyszerű billentyűzet-kezelés: space=állj-indulj, 'q'=kilép
 
# szokásos importálások
import numpy as np
import cv2
import os
import tkinter 
from tkinter import filedialog

#-------------- beállítások
# os.chdir("......")   # ha szükséges, adjuk meg ezt is

in_file="be.avi"       # beolvasandó fájl
in_request=True          # True: inkább kérjük be a fájlnevet interaktívan
                       # False: maradjon az előbb megadott fájlnév
#----------------------
cv2.namedWindow("Bemenet") # egy ablak az eredeti képnek
cv2.namedWindow("Kimenet") # egy ablak a feldolgozott képnek

root=tkinter.Tk()
root.withdraw()
wdir=os.getcwd()

if in_request:        # beolvasandó fájlnév bekérő ablak megnyitása, ha kell
	in_file=filedialog.askopenfilename(parent=root,title="Bemenet",initialdir=wdir)

# egy kis "mágia":
cap = cv2.VideoCapture(in_file) # kapcsolat létrehozása a fájl olvasásához

ret, last_frame=cap.read()   # egy kép kezdetnek
# ************* most jön a feldolgozó ciklus
dontstop = True    # váltzó amijelzi, folytatnunk kell-e 
while(dontstop): # amíg nem kell leáallni, addig újra és újra kezdjük előről
	cap = cv2.VideoCapture(in_file) # kapcsolat létrehozása a fájl olvasásához
	ret, last_frame=cap.read()   # egy kép kezdetnek
	while(dontstop):   # ciklus a képkockákon át
		ret, frame = cap.read()    # aktuális kép a "frame"-be	
		if ret==False:       # nincs újabb képkocka! vége a videónak
			break        # kilépünk a belső ciklusból

		# FELDOLGOZÁS
		# saját utasításokra cserélni!

		out_frame=cv2.absdiff(frame, last_frame)    # egyszerű művelet: különbség

		# mostani kép megjegyzése, hogy később ez legyen az előző
		last_frame=frame.copy()

		# kijelzés
		cv2.imshow('Bemenet',frame)
		cv2.imshow('Kimenet',out_frame)

		# innentől kezeljük a billentyű-leütéseket
		key=cv2.waitKey(40) & 0xFF  # billentyűkód várakozás 40 ms-ig (25 fps)
		if key==ord('q'):   # ha 'q'-t üt valaki a kijelző ablakban, akkor kilépünk
			dontstop=False
		if key==ord(' '):   # space: várunk egy új space-ig
			while (True):
				key=cv2.waitKey(1) & 0xFF
				if key==ord(' '):  # újab space-re abbahagyjuk a várakozást
					break

	cap.release()  # kapcsolat bontása a fájllal


# ************** feldolgozó ciklus vége

# takarítás a ciklus után
root.destroy()
cv2.destroyAllWindows()  # ablakok bezárása
