Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> # tartomány-kijelölések Pythonban
>>> 
>>> # listák, stringek, tömbök esetén hatékony kijelölési mód
>>> 
>>> # kezdjük stringgel:
>>> s1="Én vagyok a híres egyfejű."
>>> 
>>> print(s1)
Én vagyok a híres egyfejű.
>>> print(s1[0:3]) # 0., 1. és 2. elem, 3. már nem:
Én 
>>> print(s1[3:9]) # 3., 4., ..., 8. elem, 9. már nem:
vagyok
>>> s1[4:5]='as'
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s1[4:5]='as'
TypeError: 'str' object does not support item assignment
>>> # string részeit így felülírni nem lehet
>>> 
>>> # -1. elem: utolsó, -2. elem: utolsó előtti, stb.
>>> print(s1[-1])
.
>>> print(s1[-2])
ű
>>> print(s1[-5:])  # az utolsü 5 elem
fejű.
>>> # Az elejéről a 0 lehagyható
>>> print(s1[0:2])
Én
>>> print(s1[:2])
Én
>>> s1[0:2]==s1[:2]
True
>>> # lehet csak minden 3 elemet venni:
>>> print(s1[0:13:3])
Évy h
>>> print(s1[0:13:-3])

>>> print(s1[13:0:-3])
íaoan
>>> print(s1[12:1:-3])
h yv
>>> 
>>> # listákra hasonló, de ott felülírni is lehet:
>>> li1=['a','b','c','d','e','f','g','h']
>>> 
>>> li1[0:3]
['a', 'b', 'c']
>>> li1[-3:]
['f', 'g', 'h']
>>> li1[::2]  # minden 2. elem
['a', 'c', 'e', 'g']
>>> li1[::-2]  # minden 2. elem
['h', 'f', 'd', 'b']
>>> 
>>> li1[3:4]=['xxx','yyy','zzz']  # lista részeit felülírhatom!
>>> li1
['a', 'b', 'c', 'xxx', 'yyy', 'zzz', 'e', 'f', 'g', 'h']
>>> 
>>> # stringből lista: split()
>>> 
>>> li2=s1.split(" ")
>>> print(li2)
['Én', 'vagyok', 'a', 'híres', 'egyfejű.']
>>> 
>>> # mondat első 3 szava:
>>> s1.split(" ")[:3]
['Én', 'vagyok', 'a']
>>> # könvytárnév utolsó eleme:
>>> import os
>>> os.getcwd()
'/home/horvatha/ownCloud/Oktat/DigiKep/UjVazlat/Python3-tut'
>>> os.getcwd().split("/")[-1:]
['Python3-tut']
>>> 
>>> 
>>> # listából string: join
>>> 
>>> s2="/".join(li1)
>>> s2
'a/b/c/xxx/yyy/zzz/e/f/g/h'
>>> # jpg helyett png fájlnév
>>> fnev1="kakukk.jpg"
>>> bnev1=fnev1.split(".")[:-1]
>>> bnev1
['kakukk']
>>> fnev2=bnev1+".png"
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    fnev2=bnev1+".png"
TypeError: can only concatenate list (not "str") to list
>>> # lista és string nem adható össze!
>>> fnev2=".".join(bnev1+["png"])
>>> fnev2
'kakukk.png'
>>> 
