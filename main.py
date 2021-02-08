from PuntosFaciales import PuntosFaciales
from os import environ
import cv2

class main:

    def __init__(self, img):
        self.pointsX = []
        self.pointsY = []
        self.img = img
        self.pf = PuntosFaciales(img)

    def suppress_qt_warnings(self):
        environ["QT_DEVICE_PIXEL_RATIO"] = "0"
        environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
        environ["QT_SCREEN_SCALE_FACTORS"] = "1"
        environ["QT_SCALE_FACTOR"] = "1"

    def mostrar(self):
        if __name__ == "__main__":
            self.suppress_qt_warnings()
        img = cv2.imread(self.img)  # Lee la imagen
        X = self.pointsX
        Y = self.pointsY
        for n in range(0, 68):
            # Dibuja el circulo
            cv2.circle(img=img, center=(X[n], Y[n]), radius=2, color=(0, 255, 0), thickness=-1)
        cv2.imshow(winname="IMAGEN", mat=img)  # Muestra la imagen
        cv2.waitKey(delay=0)  # Espera para salir
        cv2.destroyAllWindows()  # Cierra todas las ventanas

    def unir(self):
        self.pointsX, self.pointsY = self.pf.obtencionPuntosFaciales() #Obtiene los puntos faciales (X y Y)

        self.mostrar()

img = "face.jpg"
principal = main(img)
principal.unir()