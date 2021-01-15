
# Sablon program mozgókép-fájlok feldolgozásához
# alap verzió: kimeneti kép a mostanitól és az előzőtől függ, nincs hibakezelés
 
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
while(True):   # végtelen ciklus
	ret, frame = cap.read()    # aktuális kép a "frame"-be

	# FELDOLGOZÁS
	# saját utasításokra cserélni!

	out_frame=cv2.absdiff(frame, last_frame)    # egyszerű művelet: különbség

	# mostani kép megjegyzése, hogy később ez legyen az előző
	last_frame=frame.copy()

	# kijelzés
	cv2.imshow('Bemenet',frame)
	cv2.imshow('Kimenet',out_frame)
	if cv2.waitKey(40) & 0xFF == ord('q'):   # ha 'q'-t üt valaki a kijelző ablakban, akkor kilépünk
		break

# ************** feldolgozó ciklus vége

# takarítás a ciklus után
root.destroy()
cap.release()  # kapcsolat bontása a fájllal
cv2.destroyAllWindows()  # ablakok bezárása
