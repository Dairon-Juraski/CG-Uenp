#imports de bibliotecas
import cv2 as cv
import imutils
import numpy as np

# declaração inicial da imagem
img = cv.imread('images/porcas.jpg')

#Conversão para escala de cinza
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Aplicação da mediana com abertura linear de 3                                                                                 '
blur = cv.medianBlur(gray, 5)

# Aplicação do Thresolder de OTSU
ret, thresh_otsu = cv.threshold(blur, 0, 255, cv.THRESH_OTSU)

# Aplicação da morfologia de dilatação com espaçamento de 1
kernel = np.ones((1, 1), np.uint8)
opening = cv.morphologyEx(thresh_otsu, cv.MORPH_OPEN, kernel, iterations=1)

# aplicaçã da dilatação em sim
dilated = cv.dilate(opening, kernel, iterations=3)

# metodo para a contagem de bordas usando FindContours
counter = cv.findContours(dilated.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
counter = imutils.grab_contours(counter)
objects = len(counter)

# Graça
text = "Amount:" + str(objects)
cv.putText(dilated, text, (10, 25),  cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)

# Concatenação vertical
images = np.concatenate((gray, dilated), axis=1)

# exibição de tela
cv.imshow('Originals -> Dilated(qtd)', images)
cv.waitKey(0)
