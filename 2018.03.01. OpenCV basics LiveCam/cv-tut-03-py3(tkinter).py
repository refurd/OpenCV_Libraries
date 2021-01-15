Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import tkinter as tk # rövidítsünk!
>>> from tkinter import filedialog   # modul nagyméretű részének behozása
>>> import cv2
>>> 
>>> # most megnézzük, hogy lehet egyszerűen fájlnevet bekérni
>>> 
>>> # kell egy "gyökér" ablak, ami most üres lesz:
>>> root=tk.Tk()
>>> # ennek "gyereke" lehet fájlbekérő ablak
>>> fájlnév=filedialog.askopenfilename(parent=root,title='Mit nyissak meg?')
>>> # most előbb felugrott egy ablak, ahol kiválaszthattam egy fájlt!
>>> # a teljes nevét betette a fájlnév változóba:
>>> print(fájlnév)
/home/horvatha/ownCloud/Oktat/DigiKep/Python3/be.png
>>> im1=cv2.imread(fájlnév) # beolvassuk
>>> im1.shape
(480, 640, 3)
>>> # siker!
>>> # tüntessük el a nyomokat:
>>> root.destroy()
>>> 
>>> # kezdjük újra:
>>> root=tk.Tk()
>>> # kimeneti fájlnév kérés:
>>> fájlnév=filedialog.asksaveasfilename(parent=root,title='Mit nyissak meg?')
>>> print(fájlnév)
/home/horvatha/ownCloud/Oktat/DigiKep/Python3/kimenet.png
>>> # ezt adtuk meg!
>>> # írjuk ki:
>>> cv2.imwrite(fájlnév, im1)
True
>>> # sok variáció van.
>>> # néhány hasznos:
>>> 
>>> # a zavaró gyökérablak eltüntetése:
>>> root.withdraw()
''
>>> # könyvtár név megnyitás kiinduló könyvtár megadással:
>>> dirname=filedialog.askdirectory(parent=root,initialdir=r"C:\Users\Me",title='Valassz konyvtarat!')
>>> print(dirname)
/home/horvatha/ownCloud/Oktat/DigiKep
>>> # máshol is adhatunk meg kezdő könyvtárat:
>>> fájlnév=filedialog.askopenfilename(parent=root,title='Mit nyissak meg?', initialdir=r"C:\Users\Me")
>>> # ha csak bizonyos fájlokat akarunk megjeleníteni:
>>> kepek=[("JPG", "*.jpg"), ("PNG", "*.png"), ("BMP", "*.bmp")]
>>> fájlnév=filedialog.askopenfilename(parent=root,title='Mit nyissak meg?', initialdir=r"C:\Users\Me", filetypes=kepek)
>>> # most csak a megadott fájlokat listázta
>>> 
>>> # a tkinter modul sok funkciójából csak igen keveset néztünk meg.
>>> # ennyi elég nekünk. Aki grafikus felületű programokat akar írni, annak
>>> # utána kell olvasnia.
>>> 
