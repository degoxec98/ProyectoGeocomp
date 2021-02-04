import cv2
import dlib
from os import environ

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

if __name__ == "__main__":
    suppress_qt_warnings()


"""
import export
export QT_DEVICE_PIXEL_RATIO=0
export QT_AUTO_SCREEN_SCALE_FACTOR=1
export QT_SCREEN_SCALE_FACTORS=1
export QT_SCALE_FACTOR=1
"""


#Carga el detector
detector = dlib.get_frontal_face_detector()

#Lee la imagen
img = cv2.imread("face.jpg")

#Convierte la imagen en escala de grises
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

#Usa el detector para encontrar puntos de referencia
faces = detector(gray)

for face in faces:
    x1 = face.left() #Punto izquierdo
    y1 = face.top() #Punto superior
    x2 = face.right() #Punto derecho
    y2 = face.bottom() #Punto de botón
    # Dibuja el rectangulo
    cv2.rectangle(img=img, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=4)

#Muestra la imagen
cv2.imshow(winname="Face", mat=img)

#Espera para salir
cv2.waitKey(delay=0)

#Cierra todas las ventanas
cv2.destroyAllWindows()

