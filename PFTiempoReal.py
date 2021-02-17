import cv2
import dlib
from os import environ
from Delaunay import Delaunay2D
import numpy as np
from scipy.spatial import Delaunay


def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

if __name__ == "__main__":
    suppress_qt_warnings()

pointsX = []
pointsY = []

def llenarArray(X, Y):
    tam = len(X)
    points = []
    for i in range(0, tam):
        points.append([X[i], Y[i]])
    seeds = np.array(points)
    return seeds

def triangulacionPuntos(X, Y):
    seeds = llenarArray(X, Y)
    triangulacion = Delaunay(seeds)
    return triangulacion


detector = dlib.get_frontal_face_detector() #Carga el detector

predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") #Carga el predictor (predice)

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()

    gray = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)

    faces = detector(gray)

    for face in faces:
        landmarks = predictor(image=gray, box=face)
        triangulacion = []
        pointsX = []
        pointsY = []
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            pointsX.append(x)
            pointsY.append(y)
            cv2.circle(img=frame, center=(x, y), radius=3, color=(0, 255, 0), thickness=-1)

        triangulacion = triangulacionPuntos(pointsX, pointsY)
        for m in range(0, len(triangulacion.simplices)):
            # Obtiene las posiciones de los puntos para la triangulacion
            a = triangulacion.simplices[m][0]
            b = triangulacion.simplices[m][1]
            c = triangulacion.simplices[m][2]
            cv2.line(img=frame, pt1=(pointsX[a], pointsY[a]), pt2=(pointsX[b], pointsY[b]), color=(0, 255, 0))  # Trazo 1
            cv2.line(img=frame, pt1=(pointsX[b], pointsY[b]), pt2=(pointsX[c], pointsY[c]), color=(0, 255, 0))  # Trazo 2
            cv2.line(img=frame, pt1=(pointsX[c], pointsY[c]), pt2=(pointsX[a], pointsY[a]), color=(0, 255, 0))  # Trazo 3 (Cierre del triangulo)

        cv2.imshow(winname="Face", mat=frame)

        if cv2.waitKey(delay=1) == 27:
            break

cap.release()
cv2.destroyAllWindows()

