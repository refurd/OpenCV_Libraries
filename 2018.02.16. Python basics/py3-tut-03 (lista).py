Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> # egyszerű listakezelés
>>> # a lista a Python alapvető, gyakran használt struktúrája
>>> # kicsit hasonlít a C tömbjére, de rugalmasabb, viszont lassabb
>>> 
>>> list1=[1,2,3,4]
>>> print(list1[0], list1[1])
1 2
>>> # 0-tól számoz, ugyanúgy, mint a C
>>> 
>>> # bármi lehet listaelem, eltérő típusok is:
>>> list2=['kakukk', 2, 6.5, 'jankó', 22]
>>> print(list2[0])
kakukk
>>> print(list2[1])
2
>>> print(list2[4])
22
>>> print(list2[5])
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(list2[5])
IndexError: list index out of range
>>> #érvénytelen lekérdezés: nincs is 5-ös elem
>>> 
>>> # lista hossza: len()
>>> print(len(list1), len(list2))
4 5
>>> # egyszerű műveletek:
>>> list3=list1+list2
>>> print(list3)
[1, 2, 3, 4, 'kakukk', 2, 6.5, 'jankó', 22]
>>> print(['V']*5)
['V', 'V', 'V', 'V', 'V']
>>> 
>>> # sok hasznos függvény:
>>> list1.reverse()  # megfordítja helyben
>>> print(list1)
[4, 3, 2, 1]
>>> list1.sort() # rendezi
>>> print(list1)
[1, 2, 3, 4]
>>> list2.sort() # rendezi?
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    list2.sort() # rendezi
TypeError: unorderable types: int() < str()
>>> # hiba: nem tud stringet és int-et összehasonlítani
>>> 
>>> list2.index('kakukk')
0
>>> # a 'kakukk' a 0. elem
>>> list2.index(22)
4
>>> # a 22 a 4-es
>>> list2.index(333)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    list2.index(333)
ValueError: 333 is not in list
>>> # ilyen nincs a listában
>>> 333 in list2   # ez egy logikai kifejezés: benne van ez a listában?
False
>>> # ilyen nincs a listában, de most nem hibauzenetet kaptunk
>>> bennevan=333 in list2
>>> print(bennevan)   # 'bennevan' egy logikai változó; később használjuk
False
>>> 
>>> list1.append(9) # append=hozzáfűz
>>> print(list1)
[1, 2, 3, 4, 9]
>>> # és még sok egyéb. lásd a Python leírást, pl itt:
>>> # https://docs.python.org/3/tutorial/datastructures.html
