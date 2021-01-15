# Keretprogram kameraképek feldolgozásához
# a kimeneti kép a mostanitól és az előzőtől is függhet

# szokásos importálások
from harvesters.core import Harvester
import numpy as np
import vispy
import scipy.misc
from PIL import Image
import os
import cv2
import asyncio

#-------------- Harverster Config

h = Harvester()
h.add_file(r'C:\Users\dgyorkos\Desktop\GIGE\11117626_SW_Baumer_GAPI_SDK_Win64_v2.10.0.25119\Tools\GigE\IpConfigTool\bgapi2_gige.cti')
h.update()
ia = h.create_image_acquirer(0)

async def Harvester():
        ia.start_acquisition()
        with ia.fetch_buffer() as buffer:
                component = buffer.payload.components[0]
                _1d = component.data

        buffer = ia.fetch_buffer()

        payload = buffer.payload
        component = payload.components[0]

        im = np.array(Image.fromarray(component.represent_pixel_location()))
        return im
        Harverster()
	
#--------------------------------

#-------------- beállítások
kamera=0   # hányas kamerát használjuk? esetleg átírandó 1,2,3,...-ra
#----------------------

cv2.namedWindow("Bemenet") # egy ablak az eredeti képnek
cv2.namedWindow("Output") # egy ablak a feldolgozott képnek

ret, last_frame=Harvester()   # egy kép kezdetnek

# ************* most jön a feldolgozó ciklus
while(True):   # végtelen ciklus
        try:
                ret, frame = Harvester()
                out_frame=cv2.cvtColor(cv2.absdiff(frame, last_frame), cv2.COLOR_BGR2GRAY)    # egyszerű művelet: különbség, mozgásérzékelés
                last_frame=frame.copy()

                cv2.imshow('Bemenet',frame)
                cv2.imshow('Output',out_frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):   # ha 'q'-t üt valaki a kijelző ablakban, ...
                        break
        except:
                continue

# ************** feldolgozó ciklus vége

# takarítás a ciklus után
cap.release()  # kapcsolat bontása a kamerával
cv2.destroyAllWindows()  # ablakok bezárása
