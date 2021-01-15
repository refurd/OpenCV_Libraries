Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import cv2
>>> import os
>>> # kép közvetlen megjelenítése OpenCV-ből
>>> # a legegyszerűbb módszer# a szokásos chdir:
>>> os.chdir(r"/home/horvatha/Képek/DigiKep/")
>>> im1=cv2.imread("kicsi-felho-1.jpg")
>>> print(im1.shape)
(480, 640, 3)
>>> # úgy tűnik, rendben
>>> # jelenítsük meg!
>>> # deklarálunk egy ablakot:
>>> cv2.namedWindow("Ablak 1")
>>> # most beletesszük a képet:
>>> cv2.imshow("Ablak 1", im1)
>>> cv2.waitKey()
100
>>> # arra várt, hogy az "Ablak 1"-en egy billentyűt üssünk
>>> # a "d"-t ütöttük, ennek kódját, a 100-at adta vissza.
>>> 
>>> im2=255-im1
>>> cv2.imshow("Ablak 2", im2)
>>> # nem is feltétlen kell a cv2.namedWindow()
>>> cv2.waitKey()
32
>>> # most space-t ütöttünk, aminek a kódje 32
>>> # becsukjuk az első ablakot:
>>> cv2.destroyWindow("Ablak 1")
>>> # most minden ablakot, ami maradt:
>>> cv2.destroyAllWindows()
>>> 
>>> # Ez nagyon egyszerű mód volt. Nem kezeli jól a túl nagy képeket, stb.
>>> # Nagyobb program részeként jól lehet használni
>>> # vagy egyszerű ellenőrzésre.
>>> 
