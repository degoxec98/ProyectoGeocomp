from tkinter import *
from main import iniciar
from PFTiempoReal import iniciar2

class InterfazAlgoSH():

    def __init__(self):
        self.raiz = Tk()
        self.myFrame = Frame(self.raiz, width="500", height="400")


    def foto(self):
        principal = iniciar()
        principal.ejecutar()
        print("Entro")


    def tiempoReal(self):
        principal2 = iniciar2()
        principal2.ejecutar()
        print("Entro2")


    def corriendo(self):

        self.raiz.title("TRIANGULACION DE PUNTOS FACIALES")

        self.myFrame.pack()
        self.myFrame.config(bg="light blue")
        self.myFrame.config(cursor="pirate")

        labelP = Label(self.myFrame, text="ELIGA UNA OPCIÓN")
        labelP.config(font=("Arial Black", 12), bg="light green")
        labelP.place(x=180, y=30)

        botonFoto = Button(self.myFrame, text="FOTO", bg="indian red", width=10,
                      command=lambda: self.foto())
        botonFoto.place(x=50, y=80)

        botonReal = Button(self.myFrame, text="TIEMPO REAL", bg="indian red", width=10,
                           command=lambda: self.tiempoReal())
        botonReal.place(x=350, y=80)

        self.raiz.mainloop()

iniciar3 = InterfazAlgoSH()
iniciar3.corriendo()