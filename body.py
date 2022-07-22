from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msb


root = Tk()
root.title("EMPRESA - Reunión de Programación")
root.geometry("450x420")
root.resizable(0, 0)


def titulos():
    Label(root).grid(row=0)
    Label(root, text="Cumplimiento Semana: ").grid(row=1, column=1)
    Label(root, text="L3     --> ").grid(row=2, column=1)
    Label(root, text="%").grid(row=2, column=3)
    Label(root, text="L6     --> ").grid(row=3, column=1)
    Label(root, text="%").grid(row=3, column=3)
    Label(root).grid(row=4)
    Label(root, text="Actividades Semana: ").grid(row=5, column=1)
    Label(root, text="L6").grid(row=6, column=2)
    Label(root, text="L3").grid(row=6, column=5)
    Label(root, text="Lunes").grid(row=7, column=1)
    Label(root, text="Martes").grid(row=8, column=1)
    Label(root, text="Miercoles").grid(row=9, column=1)
    Label(root, text="Jueves").grid(row=10, column=1)
    Label(root, text="Viernes").grid(row=11, column=1)
    Label(root, text="Sabado").grid(row=12, column=1)
    Label(root, text="Domingo").grid(row=13, column=1)


def casillas():
    weeks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
             25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,
             46,47,48,49,50,51,52,53]

    comb1 = ttk.Combobox(root, values=weeks)
    comb1.grid(row=1, column=2)

    # Campo porcentaje L3
    dato1 = Entry(root)
    dato1.grid(row=2, column=2)

    # Campo porcentaje L6
    dato2 = Entry(root)
    dato2.grid(row=3, column=2)

    comb2 = ttk.Combobox(root, values=weeks)
    comb2.grid(row=5, column=2)

    # Linea 6
    datLunL6 = Entry(root)
    datLunL6.grid(row=7, column=2)

    datMarL6 = Entry(root)
    datMarL6.grid(row=8, column=2)

    datMieL6 = Entry(root)
    datMieL6.grid(row=9, column=2)

    datJueL6 = Entry(root)
    datJueL6.grid(row=10, column=2)

    datVieL6 = Entry(root)
    datVieL6.grid(row=11, column=2)

    datSabL6 = Entry(root)
    datSabL6.grid(row=12, column=2)

    datDomL6 = Entry(root)
    datDomL6.grid(row=13, column=2)

    # Linea 3
    datLunL3 = Entry(root)
    datLunL3.grid(row=7, column=5)

    datMarL3 = Entry(root)
    datMarL3.grid(row=8, column=5)

    datMieL3 = Entry(root)
    datMieL3.grid(row=9, column=5)

    datJueL3 = Entry(root)
    datJueL3.grid(row=10, column=5)

    datVieL3 = Entry(root)
    datVieL3.grid(row=11, column=5)

    datSabL3 = Entry(root)
    datSabL3.grid(row=12, column=5)

    datDomL3 = Entry(root)
    datDomL3.grid(row=13, column=5)

    def clearInput():
        dato1.delete(0, "end"), dato2.delete(0, "end"),
        datLunL6.delete(0, "end"), datMarL6.delete(0, "end"), datMieL6.delete(0, "end"), datJueL6.delete(0, "end"),
        datVieL6.delete(0, "end"), datSabL6.delete(0, "end"), datDomL6.delete(0, "end"), datLunL3.delete(0, "end"),
        datMarL3.delete(0, "end"), datMieL3.delete(0, "end"), datJueL3.delete(0, "end"), datVieL3.delete(0, "end"),
        datSabL3.delete(0, "end"), datDomL3.delete(0, "end")

    # Generando el TXT
    def docTXT():
        lista = []

        # Validacion de casillas
        if comb1.get() == '' or dato1.get() == '' or dato2.get() == '' or comb2.get() == '':
            msb.showerror('Campo vacio!!', 'Verifique que todos los campos cuentan con información.')

        elif int(dato1.get()) < 0 or int(dato1.get()) > 100 or int(dato2.get()) < 0 or int(dato2.get()) > 100:
            msb.showerror('ERROR!', 'El valor del porcentaje debe ser entre 0% y 100%')

        elif comb1.get() == comb2.get():
            msb.showerror('ERROR!', 'Las semanas no pueden ser iguales')

        elif int(comb1.get()) > int(comb2.get()):
            msb.showerror('ERROR!', '"Cumplimiento Semana" no puede ser mayor que "Actividades Semana".')

        else:
            getting = "Cumplimiento Semana: " + comb1.get(),\
                      "L3: " + dato1.get() + "%",\
                      "L6: " + dato2.get() + "%",\
                      "\nActividades Semana: " + comb2.get(),\
                      "\nL6:",\
                      "Lunes: " + datLunL6.get(), "Martes: " + datMarL6.get(), "Miercoles: " + datMieL6.get(),\
                      "Jueves: " + datJueL6.get(), "Viernes: " + datVieL6.get(), "Sabado: " + datSabL6.get(),\
                      "Domingo: " + datDomL6.get(),\
                      "\nL3:",\
                      "Lunes: " + datLunL3.get(), "Martes: " + datMarL3.get(), "Miercoles: " + datMieL3.get(),\
                      "Jueves: " + datJueL3.get(), "Viernes: " + datVieL3.get(), "Sabado: " + datSabL3.get(),\
                      "Domingo: " + datDomL3.get()

            for datos in getting:
                lista.append(datos)

            f = open("resumen.txt", "w+")

            for i in lista:
                f.write(i + "\n")

            f.close()

            clearInput()
            msb.showinfo('Todo correcto!!', 'El TXT ya fue generado, revisa el escritorio!!')

    Label(root).grid(row=14)
    Label(root).grid(row=16)

    # El boton
    boton = Button(root, text="Generar TXT", command=docTXT)
    boton.config(bg='lightgreen')
    boton.grid(row=17, column=2, columnspan=2)


def checkActividades():
    Label(root, text="¿Actividades Aprobadas?").grid(row=15, column=0, columnspan=2)

    clickValueYes = IntVar()
    clickValueNo = IntVar()

    # Verificacion del Check
    def clickYes():
        if clickValueYes.get() == 1:
            checkNo.config(state='disabled')
            msb.showinfo("SI!", "Pusiste el Check en SI.")

        elif clickValueYes.get() == 0:
            checkNo.config(state='normal')
            msb.showinfo("SI!", "Quitaste el Check en SI.")

    def clickNo():
        if clickValueNo.get() == 1:
            checkYes.config(state='disabled')

            # Creando nueva ventana
            newframe = Toplevel(root)
            newframe.geometry("400x400")
            Label(newframe).grid(row=0)
            Label(newframe, text="Ingrese las observaciones: ").grid(row=1, column=1, columnspan=2)
            Label(newframe).grid(row=2)
            obsBox = Text(newframe)
            obsBox.grid(row=3, column=1, columnspan=2)
            obsBox.config(width=40, heigh=10, padx=15, pady=15)
            newframe.mainloop()

            # msb.showinfo("NO!", "Pusiste el Check en NO.")

        elif clickValueNo.get() == 0:
            checkYes.config(state='normal')
            msb.showinfo("NO!", "Quitaste el Check en NO.")

    checkYes = Checkbutton(root, text="Si", variable=clickValueYes, onvalue=1, offvalue=0, command=clickYes)
    checkYes.grid(row=15, column=2, columnspan=2)

    checkNo = Checkbutton(root, text="No", variable=clickValueNo, onvalue=1, offvalue=0, command=clickNo)
    checkNo.grid(row=15, column=4, columnspan=2)






titulos()
casillas()
checkActividades()

# Información del creador
derechos = Label(root, text="Made in Pedro version 1.1 / All rights reserved © 2022")
derechos.place(x=77, y=400, width=300, height=20)

root.mainloop()
