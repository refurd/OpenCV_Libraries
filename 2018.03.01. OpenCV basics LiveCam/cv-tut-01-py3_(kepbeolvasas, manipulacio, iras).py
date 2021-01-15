Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> # elemi műveletek OpenCV-ben
>>> # modulok be:
>>> import cv2
>>> import os
>>> 
>>> # kép beolvasási kísérlet:
>>> im1=cv2.imread("kicsi-felho-1.jpg")
>>> # im1: most elvileg egy tömb
>>> # ellenőrzés:
>>> print(im1[0,0])
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(im1[0,0])
TypeError: 'NoneType' object is not subscriptable
>>> # hiba! Mi történt?
>>> print(type(im1))
<class 'NoneType'>
>>> # üres objektum! Nem sikerült a beolvasás
>>> # sajnos ilyenkor nem kapunk hibajelzést...
>>> 
>>> # de mi volt a hiba oka? Nem váltottunk könyvtárat.
>>> # pótoljuk:
>>> # hol is vagyunk most?
>>> os.getcwd()
'/home/horvatha/ownCloud/Oktat/DigiKep/Python3'
>>> # váltsunk a megfelelő helyre:
>>> os.chdir(r"/home/horvatha/Képek")
>>> # !!! Minden gépen más lehet a megfelelő könyvtár!
>>> # most olvassuk be újra és teszteljük le:
>>> im1=cv2.imread("kicsi-felho-1.jpg")
>>> print(im1[0,0])
[150 125 105]
>>> # úgy tűnik, sikerült.
>>> 
>>> # kép paraméterek:
>>> print(im1.shape)
(480, 640, 3)
>>> # 480 sor, 640 oszlop, 3 színcsatorna
>>> print(im1.size)
921600
>>> print(480*640*3)
921600
>>> print(im1.max())
243
>>> print(im1.min())
0
>>> # tehát ez a kép 480*640*3=921600 adatot tartalmaz,
>>> # 243 a maximum, 0 a minimum
>>> # normál képnek tűnik....
>>> 
>>> # változtassuk meg!
>>> im1[10,10]=[0,0,0]    # egy pixel átírása feketére
>>> im1[20:200, 50]=[0,0,255]  # piros csík (B, G, R a színsorrend)
>>> im1[200:300, 200:300] += 20  # világosítunk egy négyzeten belül
>>> 
>>> # kiírás:
>>> cv2.imwrite("proba-1.jpg", im1)
True
>>> # most megnézhetjük képnézegetővel
>>> 
>>> # bonyolultabb átalakítás:
>>> for sor in range(200,300):
	for oszl in range(400,450):
		im1[sor,oszl]=[sor % 255, oszl % 255, (sor+oszl)%255]

		
>>> cv2.imwrite("proba-2.jpg",im1)
True
>>> # ez nagyon eltorzult!
>>> # olvassuk be újra:
>>> im1=cv2.imread("kicsi-felho-1.jpg")
>>> # készítsünk másolatot:
>>> im1bak=im1.copy()
>>> 
>>> # most egy általános ciklus:
>>> max_sor=im1.shape[0] # sorok száma
>>> max_oszl=im1.shape[1] # oszlopok száma
>>> print(max_sor, max_oszl)
480 640
>>> for sor in range(max_sor):
	for oszl in range(max_oszl):
		pix=im1[sor, oszl]  # pix: aktuális pixel másolata
		R=pix[2]
		G=pix[1]
		B=pix[0]
		im1[sor, oszl] = [255-B, 255-G, 255-R]  # invertálás

		
>>> cv2.imwrite("proba-3.jpg", im1)
True
>>> im1=im1bak.copy()  # vissza az eredetit!
>>> for sor in range(max_sor):
	for oszl in range(max_oszl):
		pix=im1[sor, oszl]  # pix: aktuális pixel másolata
		R=pix[2]
		G=pix[1]
		B=pix[0]
		if (B>G) and (B>R): # kék a domináns szín
			im1[sor, oszl]=[0,0,0] # lenullázzuk

			
>>> cv2.imwrite("proba-4.jpg", im1)
True
>>> im1=im1bak.copy()  # vissza az eredetit!
>>> for sor in range(max_sor):
	for oszl in range(max_oszl):
		pix=im1[sor, oszl]  # pix: aktuális pixel másolata
		R=pix[2]
		G=pix[1]
		B=pix[0]
		if (B>G) and (B>R): # kék a domináns szín
			im1[sor, oszl]=[0,0,0] # lenullázzuk

			
>>> cv2.imwrite("proba-5.jpg", im1)
True
>>> # mit is csinál ez az utóbbi?
>>> 
>>> # az ilyen összetett dolgokat értemesebb programszerkesztő módba írni be
>>> 
