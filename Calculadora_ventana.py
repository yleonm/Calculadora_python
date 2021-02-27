from tkinter import *

raiz = Tk()

mi_frame = Frame(raiz)
mi_frame.pack()


#---------- PANTALLA ----------------------
pantalla = Entry(mi_frame)
pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

#-------------Fila 1-----------------------
boton_7 = Button(mi_frame, text= "7", width=3)
boton_7.grid(row=2,column=1)

boton_8 = Button(mi_frame, text= "8", width=3)
boton_8.grid(row=2,column=2)

boton_9 = Button(mi_frame, text= "9", width=3)
boton_9.grid(row=2,column=3)

boton_dividir = Button(mi_frame, text= "/", width=3)
boton_dividir.grid(row=2,column=4)

#------------ Fila 2-------------------------------------
boton_4 = Button(mi_frame, text= "4", width=3)
boton_4.grid(row=3,column=1)

boton_5 = Button(mi_frame, text= "5", width=3)
boton_5.grid(row=3,column=2)

boton_6 = Button(mi_frame, text= "6", width=3)
boton_6.grid(row=3,column=3)

boton_multiplicar = Button(mi_frame, text= "*", width=3)
boton_multiplicar.grid(row=3,column=4)

raiz.mainloop()