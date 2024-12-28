import cv2

webcan = cv2.VideoCapture(0)

while True:
    sucesso, imagem = webcan.read()
    cv2.imshow("Projeto 4 - IA", imagem)

    if cv2.waitKey(1) != -1:
        break

webcan.release()
cv2.destroyAllWindows()