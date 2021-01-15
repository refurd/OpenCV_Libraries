# Keretprogram kameraképek feldolgozásához
# a kimeneti kép a mostanitól és az előzőtől is függhet
# szokásos importálások
import numpy as np
import cv2

#-------------- beállítások
kamera=0   # hányas kamerát használjuk? esetleg átírandó 1,2,3,...-ra
#----------------------

cv2.namedWindow("Bemenet") # egy ablak az eredeti képnek
cv2.namedWindow("Output") # egy ablak a feldolgozott képnek

cap = cv2.VideoCapture(kamera) # kapcsolat létrehozása

ret, last_frame=cap.read()   # egy kép kezdetnek
# ************* most jön a feldolgozó ciklus
while(True):   # végtelen ciklus
	ret, frame = cap.read() # aktuális kép a "frame"-be
				# ret: True vagy False, sikeres-e a beolvasás

	# FELDOLGOZÁS
	# saját utasításokra cserélni!

	# frame: mindig az aktuális képkocka
	# last_frame: az előző képkocka

	#out_frame=255-frame   # kimenet= bemenet inverze
	out_frame=cv2.cvtColor(cv2.absdiff(frame, last_frame), cv2.COLOR_BGR2GRAY)    # egyszerű művelet: különbség, mozgásérzékelés
	#out_frame=cv2.absdiff(frame, cv2.blur(frame, (25,25)))*4   # bonyolultabb: élkeresés

	# mostani kép megjegyzése, hogy később ez legyen az előző
	last_frame=frame.copy()
	
	# kijelzés
	cv2.imshow('Bemenet',frame)
	cv2.imshow('Output',out_frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):   # ha 'q'-t üt valaki a kijelző ablakban, ...
		break				# akkor kilépünk

# ************** feldolgozó ciklus vége

# takarítás a ciklus után
cap.release()  # kapcsolat bontása a kamerával
cv2.destroyAllWindows()  # ablakok bezárása
