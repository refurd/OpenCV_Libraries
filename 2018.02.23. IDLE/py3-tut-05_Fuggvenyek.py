Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> # egyszerű függvények Pytohnban
>>> 
>>> # függvény definíció: def név(argumentumok, ...):

>>> def fgv(x):
	return (x+1.0/x)

>>> fgv(3)
3.3333333333333335
>>> fgv(2)
2.5
>>> fgv(0)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    fgv(0)
  File "<pyshell#3>", line 2, in fgv
    return (x+1.0/x)
ZeroDivisionError: float division by zero
>>> # érthető a hiba: 0-val osztás
>>> 
>>> def fgv2(x):
	if float(x)==0.0:
		return 1.0
	else:
		return math.sin(x)/x

>>> import math   # jobb későn, mint soha.... Még nem hívtuk meg fgv2-t
>>> fgv2(1.0)
0.8414709848078965
>>> fgv2(0.1)
0.9983341664682815
>>> fgv2(0.001)
0.9999998333333416
>>> fgv2(0.0)
1.0
>>> 
>>> # lehet több argumentum is:

>>> def atlo(x,y):
	return (x*x+y*y)**0.5

>>> 
>>> atlo(3,4)
5.0
>>> atlo(5,12)
13.0
>>> atlo(5,13)
13.92838827718412
>>> 
>>> 
>>> 
>>> # a Python függvények több visszatérési értékkel is rendelkezhetnek

>>> def hany_mar(n1, n2):
	hanyados=int(n1)//int(n2)
	maradek=int(n1) % int(n2)
	return hanyados, maradek

>>> hany_mar(13,3)

(4, 1)
>>> hany_mar(15,3)
(5, 0)
>>> 
>>> # többszörös értékadással tudjuk ezeket eltárolni:

>>> a,b = hany_mar(13,3)

>>> print(a)
4
>>> print(b)
1
>>> # akár teljes lista is lehet a visszatérési érték:

>>> def erdekesek(meddig):
	kimenet=[] # üres lista
	for i in range(meddig):
		if (i%3==2) and (i%5==3):
			kimenet.append(i)
	return kimenet

>>> erdekesek(100)

[8, 23, 38, 53, 68, 83, 98]
>>>  # egy listát kaptunk eredményül
 
>>>  # ha akarjuk, lehet alapértelmezett értéket is megadni

>>> def erdekesek2(mar3, mar5, meddig=100):
	kimenet=[]
	for i in range(meddig):
		if (i%3==mar3) and (i%5==mar5):
			kimenet.append(i)
	return kimenet


>>> erdekesek2(0,0)

[0, 15, 30, 45, 60, 75, 90]
>>> erdekesek2(0,0,100)
[0, 15, 30, 45, 60, 75, 90]
>>> erdekesek2(0,0,200)
[0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195]
>>> # akárhány alapértelmezést megadhatunk:

>>> def erdekesek3(mar3=0, mar5=0, meddig=100):
	kimenet=[]
	for i in range(meddig):
		if (i%3==mar3) and (i%5==mar5):
			kimenet.append(i)
	return(kimenet)

>>> 
>>> # most akár az összes argumentum elhagyható:

>>> erdekesek3()

[0, 15, 30, 45, 60, 75, 90]
>>> erdekesek3(1)
[10, 25, 40, 55, 70, 85]
>>> erdekesek3(mar3=2, meddig=200)
[5, 20, 35, 50, 65, 80, 95, 110, 125, 140, 155, 170, 185]
>>> 
>>> 
>>> # sok hasonlóság a C-hez, de bővebbek a lehetőségek!
>>> 
