# import de bibliotecas cv2 e numpy
import cv2 as cv
import numpy as np

# declaração inicial da imagem
img = cv.imread("images/salt_pepper.png")

##
# Processamento da imagem em si:
# \_usando o calculo de média,
# \_com uma abertura linear de 3
##
median = cv.medianBlur(img, 3)

##
# Apenas Graça aki
##
text1 = "Original"
cv.putText(img, text1, (10, 25), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
text2 = "Treated"
cv.putText(median, text2, (10, 25), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)

# Concatenação vertical
images = np.concatenate((img, median), axis=1)

# exibição de tela
cv.imshow('Originals -> Treated', images)
cv.waitKey(0)
