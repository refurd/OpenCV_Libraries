Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> # elemi string műveletek:
>>> a='egy kis szöveg'
>>> b="folytatás"
>>> # Pythonban ' és " egyaránt használható!
>>> 
>>> print(a,b)
egy kis szöveg folytatás
>>> print(a,"...",b)
egy kis szöveg ... folytatás
>>> 
>>> c='Eleje'+"folytatása"+'vége'
>>> print(c)
Elejefolytatásavége
>>> # ajaj! az összeadás nem tesz pluszt szóközt. (a print igen)
>>> c='Eleje '+"folytatása "+'vége'
>>> print(c)
Eleje folytatása vége
>>> d="Azt mondta: 'A válasz: negyvenkettő'"
>>> print(d)
Azt mondta: 'A válasz: negyvenkettő'
>>> 
>>> # C-hez hasonlóan '\'-t használ speciális jelekre, pl. újsor, tabulátor,...
>>> a='XXXX\nYYYY'
>>> print(a)
XXXX
YYYY
>>> print("A\tB\nCCC\tDD")
A	B
CCC	DD
>>> # '\\'= egyetlen '\' a stringbe:
>>> könyvtár='C:\\users\\juzer'
>>> print(könyvtár)
C:\users\juzer
>>> # más módszer: r"..." string használata
>>> # r='raw', azaz nyers. Ekkor nem értelmezi a '\'-t különlegesen
>>> a=r'XXXX\nYYYY'
>>> print(a)
XXXX\nYYYY
>>> könyvtár='C:\users\juzer'
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape
>>> könyvtár=r'C:\users\juzer'
>>> print(könyvtár)
C:\users\juzer
>>> 
>>> # A C-hez hasonló formátum-stringek is vannak, csak itt a formátum és
>>> # az értékek közé '%'-t kell írni:
>>> 
>>> a=3
>>> b=1.5
>>> print("Darabszám=%d; átlagérték=%f"% (a,b))
Darabszám=3; átlagérték=1.500000
>>> print("Darabszám=%3d; átlagérték=%4.2f"% (a,b))
Darabszám=  3; átlagérték=1.50
>>> # ez nemcsak a 'print' paranccsal használható:
>>> fájlnév="data-%04d.csv" % (a)
>>> print(fájlnév)
data-0003.csv
>>> 
