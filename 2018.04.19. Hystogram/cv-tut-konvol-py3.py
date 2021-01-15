import cv2
import numpy as np

#---------------------------------------
def simple_konvol(image, kern):
	"""Egyszerű konvolúció, normalizálás nélkül"""
	result=cv2.filter2D(image, -1, kern)
	#                           ^ -1: a kimenet azonos típusú a bemenettel
	return(result)
#---------------------------------------
def norm_konvol(image, kern):
	"""Konvolúció előtt normalizálja a kernelt túlcsordulás ellen.
	   Negatív elemekkel hibát okozhat!"""
	norm=kern.sum()
	result=cv2.filter2D(image, -1, kern/norm)
	return(result)
#--------------------------------------
def norm_shift_konvol(image, kern):
	"""Konvolúció után olyan eltolást alkalmaz, hogy ne lehessen negatív érték."""

	kmin=kern.min()
	if kmin>=0.0: # nincs negatív a kernelben: egyszerű normálás
		return(norm_konvol(image, kern))
	# van negatív a kernelben: vigyázni kell a negatív elemekre a kimenetben!
	pos_sum=kern[kern>0.0].sum()
	neg_sum=kern[kern<0.0].sum()

	norm=max(pos_sum, -neg_sum)*2.0*255.0/254.0 # a kimenet +-(1/2)*255 közé essen
	float_result=cv2.filter2D(image.astype(np.float32), -1, kern/norm)
	#                                

	return ( (float_result+127.0).astype(np.uint8) )



#--------------------------------------------------------
# főprogram
#--------------------------------------------------------

im1=cv2.imread("teszt-konvol.png")

#--- simítások

kern=np.array([
  [0.0, 0.0, 0.0],
  [1.0, 1.0, 1.0], 
  [0.0, 0.0, 0.0]], 
  np.float32)

# normalizálás nélkül:
im1_s_nonorm=simple_konvol(im1, kern)
cv2.imwrite("konv-smooth3-nonorm.png", im1_s_nonorm)
# normalizálással:
im1_s_norm=norm_konvol(im1, kern)
cv2.imwrite("konv-smooth3-norm.png", im1_s_norm)

# Cirkuláris simítás 5x5
kern=np.array([
  [0.0, 1.0, 1.0, 1.0, 0.0],
  [1.0, 1.0, 1.0, 1.0, 1.0], 
  [1.0, 1.0, 1.0, 1.0, 1.0], 
  [1.0, 1.0, 1.0, 1.0, 1.0], 
  [0.0, 1.0, 1.0, 1.0, 0.0]], 
  np.float32)
# normalizálással:
im1_s_norm=norm_konvol(im1, kern)
cv2.imwrite("konv-smooth5-norm.png", im1_s_norm)



# beépített konvolúciós eljárások:
# (a Gauss-simítás csak páratlan méretű kernellel működik!)
gauss=cv2.GaussianBlur(im1,(11,11),5) # 11x11-es kernellel, 5-ös szórással
cv2.imwrite("konv-gauss11.png", gauss)
# kicsit jobban:
gauss=cv2.GaussianBlur(im1,(45,45),15) # 45x45-ös kernellel, 15-ös szórással
cv2.imwrite("konv-gauss45.png", gauss)
# a szórást rá is bízhatjuk, ha nem lényeges a pontos értéke
gauss=cv2.GaussianBlur(im1,(15,15),-1) # 15x15-ös kernellel, automatikus szórással
cv2.imwrite("konv-gauss15.png", gauss)

# Laplace:
laplace=cv2.Laplacian(im1, -1)
cv2.imwrite("konv-laplace.png", laplace)
# puszta kézzel:
kern=np.array([
  [0.0, 1.0,  0.0],
  [1.0, -4.0, 1.0], 
  [0.0, 1.0,  0.0]], 
  np.float32)
laplace=norm_shift_konvol(im1, kern) 
cv2.imwrite("konv-laplace-sajat.png", laplace)
# nem ugyanaz lesz, mert az opencv máshogy skáláz!

# Sobel-gradiens:
sobel=cv2.Sobel(im1, -1, 1, 1)  # True, True = x és y irányban is
cv2.imwrite("konv-sobel.png", sobel)


# Laplace-javítás
b=0.1 # gyenge javítás
kern=np.array([
  [0.0,   -b, 0.0],
  [-b, 1.0+4.0*b, -b], 
  [0.0,   -b,  0.0]], 
  np.float32)
eles=simple_konvol(im1,kern)
cv2.imwrite("konv-eles01.png", eles)


b=0.5 # erős javítás
kern=np.array([
  [0.0,   -b, 0.0],
  [-b, 1.0+4.0*b, -b], 
  [0.0,   -b,  0.0]], 
  np.float32)
eles=simple_konvol(im1,kern)
cv2.imwrite("konv-eles05.png",eles)


#-------------------------------------
# morfológiai op.

# struktúráló elemek
# 3x3-as négyzet
SE3R=cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
# 3x3-as kereszt
SE3C=cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
# 7x7-es "ellipszis" (azaz körféle)
SE7E=cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))


# legegyszerűbb műveletek 
ero=cv2.erode(im1, SE3R)
dil=cv2.dilate(im1, SE3R)
mgrad=dil-ero
cv2.imwrite("morph-ero3r.png",ero)
cv2.imwrite("morph-dil3r.png",dil)
cv2.imwrite("morph-mgrad3r.png",mgrad)
# már SE-vel:
ero=cv2.erode(im1, SE7E)
dil=cv2.dilate(im1, SE7E)
mgrad=dil-ero
cv2.imwrite("morph-ero7e.png",ero)
cv2.imwrite("morph-dil7e.png",dil)
cv2.imwrite("morph-mgrad7e.png",mgrad)

#-----------
# medián szűrés
med=cv2.medianBlur(im1, 3)
cv2.imwrite("med-3.png",med)
med=cv2.medianBlur(im1, 7)
cv2.imwrite("med-7.png",med)

#-----------------------------------
# komplex műveletek

# lencsehiba szimuláció: R, G, B más mértékben elmosva

im_rossz=im1.copy()
im_rossz[:,:,0]=cv2.GaussianBlur(im_rossz[:,:,0], (19,19), -1) # B-t mossuk el legjobban
im_rossz[:,:,1]=cv2.GaussianBlur(im_rossz[:,:,1], (11,11), -1)
im_rossz[:,:,2]=cv2.GaussianBlur(im_rossz[:,:,2], (7,7), -1)

cv2.imwrite("konvol-rosszlencse.png", im_rossz)

# maszk morf. op.

HSV=cv2.cvtColor(im1,cv2.COLOR_BGR2HSV)
elenkek=(HSV[:,:,1]>50).astype(np.uint8)

csakelenk=im1.copy()
for ch in range(3):
	csakelenk[:,:,ch]*=elenkek
cv2.imwrite("elenk-mask-00.png", csakelenk)
# most szélesítjük a maszkot:
elenkek=cv2.dilate(elenkek, SE3R)
csakelenk=im1.copy()
for ch in range(3):
	csakelenk[:,:,ch]*=elenkek
cv2.imwrite("elenk-mask-01.png", csakelenk)
# többszörösen szélesítjük:

elenkek=cv2.dilate(elenkek, SE3R, iterations=5)
csakelenk=im1.copy()
for ch in range(3):
	csakelenk[:,:,ch]*=elenkek
cv2.imwrite("elenk-mask-02.png", csakelenk)

# csak az élénk foltok megtartása:
elenkek=(HSV[:,:,1]>50).astype(np.uint8)
# ez kiírtja a kicsi pöttyöket
elenkek=cv2.erode(elenkek, SE3R, iterations=2)
# ez visszanöveli a nagyobb foltokat, még kicsit jobban is
elenkek=cv2.dilate(elenkek, SE3R, iterations=5)
csakelenk=im1.copy()
for ch in range(3):
	csakelenk[:,:,ch]*=elenkek
cv2.imwrite("elenk-mask-03.png", csakelenk)


