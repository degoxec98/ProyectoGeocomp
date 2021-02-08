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

pointsX = []
pointsY = []

detector = dlib.get_frontal_face_detector() #Carga el detector

predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") #Carga el predictor (predice)

img = cv2.imread("face.jpg") #Lee la imagen

gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY) #Convierte la imagen en escala de grises

faces = detector(gray) #Usa el detector para encontrar puntos de referencia

for face in faces:
    x1 = face.left() #Punto izquierdo
    y1 = face.top() #Punto superior
    x2 = face.right() #Punto derecho
    y2 = face.bottom() #Punto de botón
    # cv2.rectangle(img=img, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=4) # Dibuja el rectangulo
    # Busca los puntos de referencia
    landmarks = predictor(image=gray, box=face)
    for n in range(0, 68):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        #Dibuja el circulo
        cv2.circle(img=img, center=(x, y), radius=2, color=(0, 255, 0), thickness=-1)
        #Restaca los puntos(X y Y) de la cara
        pointsX.append(x)
        pointsY.append(y)

print("Puntos X: ", pointsX)
print("Puntos Y: ", pointsY)

cv2.imshow(winname="Face", mat=img) #Muestra la imagen

cv2.waitKey(delay=0) #Espera para salir

cv2.destroyAllWindows() #Cierra todas las ventanas

