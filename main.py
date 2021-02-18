from PuntosFaciales import PuntosFaciales
from os import environ
from Delaunay import Delaunay2D
import numpy as np
import cv2

class main:

    def __init__(self, img):
        self.pointsX = []
        self.pointsY = []
        self.img = img
        self.pf = PuntosFaciales(img)
        self.triangulacion = []

    def suppress_qt_warnings(self):
        environ["QT_DEVICE_PIXEL_RATIO"] = "0"
        environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
        environ["QT_SCREEN_SCALE_FACTORS"] = "1"
        environ["QT_SCALE_FACTOR"] = "1"

    def llenarArray(self):
        X = self.pointsX
        Y = self.pointsY
        tam = len(X)
        points = []
        for i in range(0,tam):
            points.append([X[i], Y[i]])
        seeds = np.array(points)
        return seeds

    def triangulacionPuntos(self):
        seeds = self.llenarArray()
        dt = Delaunay2D() #Crea una instancia de la clase Delaunay
        for s in seeds:
            dt.addPoint(s) #Inserta los puntos
        self.triangulacion = dt.exportTriangles() #Extrae la triangulacion

    def mostrar(self):
        self.suppress_qt_warnings()
        img = cv2.imread(self.img)  # Lee la imagen
        X = self.pointsX
        Y = self.pointsY
        for n in range(0, 68):
            # Dibuja el circulo
            cv2.circle(img=img, center=(X[n], Y[n]), radius=3, color=(0, 255, 0), thickness=-1)
        for m in range(0, len(self.triangulacion)):
            # Obtiene las posiciones de los puntos para la triangulacion
            a = self.triangulacion[m][0]
            b = self.triangulacion[m][1]
            c = self.triangulacion[m][2]
            cv2.line(img=img, pt1=(X[a], Y[a]), pt2=(X[b], Y[b]), color=(0, 255, 0))  # Trazo 1
            cv2.line(img=img, pt1=(X[b], Y[b]), pt2=(X[c], Y[c]), color=(0, 255, 0))  # Trazo 2
            cv2.line(img=img, pt1=(X[c], Y[c]), pt2=(X[a], Y[a]), color=(0, 255, 0))  # Trazo 3 (Cierre del triangulo)
        cv2.imshow(winname="IMAGEN", mat=img)  # Muestra la imagen
        cv2.waitKey(delay=0)  # Espera para salir
        cv2.destroyAllWindows()  # Cierra todas las ventanas

    def unir(self):
        self.pointsX, self.pointsY = self.pf.obtencionPuntosFaciales() #Obtiene los puntos faciales (X y Y)
        self.triangulacionPuntos() #Obtiene la triangulacion de acuerdo a los puntos obtenidos
        self.mostrar() #Muestra en pantalla los resultados obtenidos

class iniciar:
    def ejecutar(self):
        img = "face.jpg"
        principal = main(img)
        principal.unir()