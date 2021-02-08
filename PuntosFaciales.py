import cv2
import dlib
from os import environ

class PuntosFaciales:

    def __init__(self, img):
        self.pointsX = []
        self.pointsY = []
        self.img = img

    def suppress_qt_warnings(self):
        environ["QT_DEVICE_PIXEL_RATIO"] = "0"
        environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
        environ["QT_SCREEN_SCALE_FACTORS"] = "1"
        environ["QT_SCALE_FACTOR"] = "1"

    def obtencionPuntosFaciales(self):
        if __name__ == "__main__":
            self.suppress_qt_warnings()
        detector = dlib.get_frontal_face_detector() #Carga el detector
        predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") #Carga el predictor (predice)
        img = cv2.imread(self.img) #Lee la imagen
        gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY) #Convierte la imagen en escala de grises
        faces = detector(gray) #Usa el detector para encontrar puntos de referencia
        for face in faces:
            # Busca los puntos de referencia
            landmarks = predictor(image=gray, box=face)
            for n in range(0, 68):
                x = landmarks.part(n).x
                y = landmarks.part(n).y
                #Restaca los puntos(X y Y) de la cara
                self.pointsX.append(x)
                self.pointsY.append(y)
        return self.pointsX, self.pointsY
