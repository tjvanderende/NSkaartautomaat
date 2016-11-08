__author__ = 'Jeroen'

from tkinter import *

window = Tk()
window.title('NS Vertrektijden')
window.configure(background="#FFCF1A")
window.minsize(800, 600)

photo = PhotoImage(file="OvChipkaart.png")
label = Label(window, image=photo)
label.place(x=230, y=180)

frame1 = Frame(window, width=150, height=80)
button1 = Button(frame1, text="Ik wil naar Amsterdam")

frame1.grid_propagate(False)
frame1.columnconfigure(0, weight=1)
frame1.rowconfigure(0, weight=1)

frame1.grid(row=0, column=1)
button1.grid(sticky="wens")

frame1.place(x=15, y=450)

frame2 = Frame(window, width=150, height=80)
button2 = Button(frame2, text="Los kaartje kopen")

frame2.grid_propagate(False)
frame2.columnconfigure(0, weight=1)
frame2.rowconfigure(0, weight=1)

frame2.grid(row=0, column=1)
button2.grid(sticky="wens")

frame2.place(x=168, y=450)

frame3 = Frame(window, width=150, height=80)
button3 = Button(frame3, text="Los kaartje kopen")

frame3.grid_propagate(False)
frame3.columnconfigure(0, weight=1)
frame3.rowconfigure(0, weight=1)

frame3.grid(row=0, column=1)
button3.grid(sticky="wens")

frame3.place(x=323, y=450)

frame4 = Frame(window, width=150, height=80)
button4 = Button(frame4, text="Los kaartje kopen")

frame4.grid_propagate(False)
frame4.columnconfigure(0, weight=1)
frame4.rowconfigure(0, weight=1)

frame4.grid(row=0, column=1)
button4.grid(sticky="wens")

frame4.place(x=478, y=450)

frame5 = Frame(window, width=150, height=80)
button5 = Button(frame5, text="Los kaartje kopen")

frame5.grid_propagate(False)
frame5.columnconfigure(0, weight=1)
frame5.rowconfigure(0, weight=1)

frame5.grid(row=0, column=1)
button5.grid(sticky="wens")

frame5.place(x=632, y=450)

window.mainloop()