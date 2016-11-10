StationNaam = " Test"

from tkinter import *

window = Tk()
window.title("OV-stations")


w = Canvas(window, width=800, height=600, bg="black")
w.pack()

w.create_rectangle(5,5,795,595, fill="#FFCF1A")
w.create_rectangle(0,70,800,120, fill="black")
w.create_rectangle(5,75,795,115, fill="white")
w.create_rectangle(140,75,145,800, fill="black")
w.create_rectangle(360,75,365,800, fill="black")
w.create_rectangle(640,75,645,800, fill="black")

label1 = Label(window, text='Huidige station:' + StationNaam, font=("Calibri", 28, "bold"), background='#FFCF1A')
label1.place(x=20, y=10)
label2 = Label(window, text="Tijd", bg = "white", font=("Calibri", 11, "bold",))
label2.place(x=15, y=80)
label3 = Label(window, text="Naar", bg = "white", font=("Calibri", 11, "bold",))
label3.place(x=150, y=80)
label4 = Label(window, text="Vervoerder", bg = "white", font=("Calibri", 11, "bold",))
label4.place(x=370, y=80)
label5 = Label(window, text="Spoor", bg = "white", font=("Calibri", 11, "bold",))
label5.place(x=650, y=80)

tijd1 = Label(window, text="Tijd1", bg ="#FFCF1A", font=("Calibri", 10))
tijd1.place(x=15, y=130)
tijd2 = Label(window, text="Tijd2", bg ="#FFCF1A", font=("Calibri", 10))
tijd2.place(x=15, y=150)
tijd3 = Label(window, text="Tijd3", bg ="#FFCF1A", font=("Calibri", 10))
tijd3.place(x=15, y=170)
tijd4 = Label(window, text="Tijd4", bg ="#FFCF1A", font=("Calibri", 10))
tijd4.place(x=15, y=190)
tijd5 = Label(window, text="Tijd5", bg ="#FFCF1A", font=("Calibri", 10))
tijd5.place(x=15, y=210)

naar1 = Label(window, text="Naar1", bg ="#FFCF1A", font=("Calibri", 10))
naar1.place(x=150, y=130)
naar2 = Label(window, text="Naar2", bg ="#FFCF1A", font=("Calibri", 10))
naar2.place(x=150, y=150)
naar3 = Label(window, text="Naar3", bg ="#FFCF1A", font=("Calibri", 10))
naar3.place(x=150, y=170)
naar4 = Label(window, text="Naar4", bg ="#FFCF1A", font=("Calibri", 10))
naar4.place(x=150, y=190)
naar5 = Label(window, text="Naar5", bg ="#FFCF1A", font=("Calibri", 10))
naar5.place(x=150, y=210)

#even een loop geknald
c = 1
Ycord = 130
v = 1
while v < 11:
    C = str(c)
    Xcord = 370
    v1 = Label(window, text="Vervoerder" +C, bg="#FFCF1A", font=("Calibri", 10))
    v1.place(x=Xcord, y=Ycord)
    c = c + 1
    Ycord = Ycord + 20
    v = v + 1

a = 1
Ycord = 130
v = 1
while v < 11:
    A = str(a)
    Xcord = 650
    v1 = Label(window, text="Spoor " +A, bg="#FFCF1A", font=("Calibri", 10))
    v1.place(x=Xcord, y=Ycord)
    a = a + 1
    Ycord = Ycord + 20
    v = v + 1



window.mainloop()

