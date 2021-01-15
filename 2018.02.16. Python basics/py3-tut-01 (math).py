Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> # első, módszeres tutorial
>>> # alapműveletek, típusok
>>> # Megyjegyzés: minden, ami a '#' jel után kerül
>>> 
>>> # a változókat nem kell deklarálni:
>>> a=7
>>> # magától 'int'-nek veszi:
>>> print(type(a))
<class 'int'>
>>> # Figyelem!!! A Python2-ben a "print" után nem kellett "("
>>> # pl. Ptyhon2-ben "print type(a)" jó volt.
>>>
>>> # másik példa:
>>> b=1.9
>>> print(type(b))
<class 'float'>
>>> type(b)
<class 'float'>
>>> # az interaktív móbdan a "print" többnyire lehagyható
>>> 
>>> # átalatíktás:
>>> c=float(a)
>>> print(c, type(c))
7.0 <class 'float'>
>>> 
>>> # műveletek:
>>> a*b
13.299999999999999
>>> print(a*b)
13.299999999999999
>>> a/3
2.3333333333333335
>>> # Figyelem!!! A Python 3 itt eltér a Python 2-től
>>> # Python 2-ben int/int=int, ugyanúgy, mint C-ben.
>>> # Python 3-ban az osztás mindig float eredményt ad:
>>> print(type(a/3))
<class 'float'>
>>> # egész osztás: '//' operátor
>>> # Ez ugyanaz, mint a Python 2-beli '/'
>>> print(a//3)
2
>>> print(b//3)
0.0
>>> # ez is egészre van kerekítve, de float típusú
>>> print(b/3)
0.6333333333333333
>>> # na, ez volt a hagyományos osztás
>>> 
>>> # hagyományos műveletek:
>>> d=(a-3)*b/5
>>> print(d)
1.52
>>> # maradék meghatározása:
>>> print(7 % 3)
1
>>> # hatványozás:
>>> print(2**10)
1024
>>> 
>>> # matematikai függvények: modulban
>>> import math   # modul betöltése
>>> print(math.sin(1.0))
0.8414709848078965
>>> print(math.sin( math.pi ))
1.2246467991473532e-16
>>> # ez majdnem 0! csak a kerekítési hiba miatt nem az
>>> # a szögfüggvények radiánt használnak!
>>> 
>>> print(math.log(3.0))
1.0986122886681098
>>> # math.log: 'e' alapú logaritmus
>>> print(math.log10(1000))
3.0
>>> print(math.log2(1024))
10.0
>>> # van 10 és 2 alapú is
>>> 
>>> print(math.pi, math.e)
3.141592653589793 2.718281828459045
>>> # és még sok függvény:
>>> print(math.acos(1.0))
0.0
>>> print(math.asin(1.0))
1.5707963267948966
>>> print(math.floor(2.4), math.floor(2.6))   # lefelé kerekít
2 2
>>> print(math.ceil(2.4), math.ceil(2.6))   # felfelé kerekít
3 3
>>> 
>>> # ha valaki kevesebbet akar gépelni: (magyarázat később)
>>> from math import *
>>> print(sin(1.0))
0.8414709848078965
>>> print(acos(1.0))
0.0
>>> # de ez veszélyes, mert pl. az 'e' állandó sima 'e' lesz:
>>> print(e)
2.718281828459045
>>> # amit felülírhatunk:
>>> e=4
>>> print(e)
4
>>> # megoldás később....
>>> 
