import tkinter as tk
from Applicatie.pages.Reisoverzicht import *
from Applicatie.pages.Start import *

class Program(tk.Frame):


  def __init__(self, *args, **kwargs):
    tk.Frame.__init__(self)
    # config
    backgroundColor = kwargs.get('backgroundColor', "#FFCF1A")
    tintColor = kwargs.get("tintColor", "#2007FF")
    startStation = kwargs.get('startStation', "Utrecht")

    startPage = Start(self, backgroundColor=backgroundColor)
    reisoverzichtPage = ReisOverzicht(self, backgroundColor=backgroundColor, startStation=startStation)

    # creeër container
    container = tk.Frame(self)
    container.pack(side="top", fill="both", expand=True)

    #plaats in container
    startPage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
    reisoverzichtPage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

    test = tk.Button(startPage, text="Reisoverzicht", command=reisoverzichtPage.lift)
    test.place(height=80, width=150, x=632, y=450)
    test.config(background=tintColor)
    startPage.lift()
    #eisoverzichtPage.lift()




root = tk.Tk()
root.minsize(800, 600)
root.title("NS kaart automaat")
main = Program(root, startStation="Utrecht", backgroundColor="#FFCF1A", tintColor="#2007FF")

main.pack(side="top", fill="both", expand=True)


root.mainloop()
