import numpy as np
import cv2

captura = cv2.VideoCapture(0)
captura.set(3, 160)
captura.set(4, 120)

while(True):
    # Captura de frames
    ret, frame = captura.read()
    # Obtener imagen
    img = frame[60:120, 0:160]
    #Convertir a escala de grises 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Gaussian blur
    blur = cv2.GaussianBlur(gray,(5,5),0)
    # Umbralizar color 
    ret,thresh = cv2.threshold(blur,60,255,cv2.THRESH_BINARY_INV)
    # Encontrar colores en el frame
    contours,hierarchy = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)
    # Encontrar el contorno mas grande 
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.line(img,(cx,0),(cx,720),(255,0,0),1)
        cv2.line(img,(0,cy),(1280,cy),(255,0,0),1)
        cv2.drawContours(img, contours, -1, (0,255,0), 1)
        if cx >= 120:
            print ("Ir ala izquierda")

        if cx < 120 and cx > 50:

            print ("Derecho")
        if cx <= 50:

            print ("Ir a la derecha")
    else:
        print ("No veo la línea")

    #Mostrar frame
    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break