Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> # egyszerű programszerkezetek: ciklusok és feltételek
>>> 
>>> # a 'for' ciklus a Pythonban listaelemeken megy végig:
>>> for elem in ['a', 'b', 'c', 'd']:
	print(elem)

	
a
b
c
d
>>> # igen fontos a ':' a ciklusfej végén
>>> # és a ciklustörzs beljebb tördelése!
>>> # több utasítás: mind beljebb tördelve:
>>> for elem in ['a', 'b', 'c', 'd']:
	print(elem)
	print(elem*3)

	
a
aaa
b
bbb
c
ccc
d
ddd
>>> # számolós ciklusokhoz: range() parancs, ami listát készít
>>> print(range(5))
range(0, 5)
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> for i in range(5): 
	print(i, end='')   # ha nem akarunk mindig új sort kezdeni

	
01234
>>> for i in range(5):
	print(i, end=', ')   # ha azért akarunk valami elválasztót

	
0, 1, 2, 3, 4, 
>>> # a range() tud alsó-felső határt és lépsközt is:
>>> for i in range(3,8): 
	print(i, end=', ')

	
3, 4, 5, 6, 7, 
>>> # az alsó határt beleérti, a felsőt nem!
>>> for i in range(3,17,4):
	print(i, end=', ')

	
3, 7, 11, 15, 
>>> # 4-esével lépked
>>> # Figyelem! A Python2 range()-e kicsit máshogy működött....
>>> 
>>> # egy kis táblázatolás:
>>> import math
>>> for i in range(11):
	x=math.pi*i/10
	print("%6.4f\t%6.4f" % (x, math.sin(x)))

	
0.0000	0.0000
0.3142	0.3090
0.6283	0.5878
0.9425	0.8090
1.2566	0.9511
1.5708	1.0000
1.8850	0.9511
2.1991	0.8090
2.5133	0.5878
2.8274	0.3090
3.1416	0.0000
>>> 
>>> # a ciklusban nemcsak print lehet, hanem pl értékadások is:
>>> 
>>> ossz1=0
>>> for i in range(1,1000,2):
	ossz1=ossz1+i   # a páratlan számokat adjuk össze

	
>>> print(ossz1)
250000
>>> 
>>> # most kicsit bonyolultabb:
>>> ossz1=0
>>> ossz2=0
>>> for i in range(1,1000,2):
	ossz1=ossz1+i   # a páratlan számokat adjuk össze
	ossz2=ossz2+i**2 # még a négyzetüket is

	
>>> print(ossz1, ossz2)
250000 166666500
>>> 
>>> # C-hez hasonló while ciklus:
>>> 
>>> ossz=0
>>> i=0
>>> while(ossz<10000):
	i +=1    # rövidítés i=i+1 -re
	ossz += i*i   # a számok négyzetét adjuk össze

	
>>> print(i, ossz)
31 10416
>>> # eszerint 1**2+2**2+3**2+...+31**2 már épp túllépte a 10000-et
>>> 
>>> # feltételes szerkezetek:
>>> a=8
>>> if (a%2==0): # ha 'a' páros
	print("páros")
else:
	print("páratlan")

	
páros
>>> # Betördelés fontos! a feltétel magja mindig beljebb, a fejléc végén mindig ':'
>>> for i in range(100):
	if (i%3==0) and (i%5==1):  # speciális számok keresése
		print("%d egy jó szám!"%i)

		
6 egy jó szám!
21 egy jó szám!
36 egy jó szám!
51 egy jó szám!
66 egy jó szám!
81 egy jó szám!
96 egy jó szám!
>>> # bonyolultabb példák később
>>> # ezeket érdemes már nem interaktívan, hanem program módból szerkeszteni
