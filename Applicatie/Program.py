import tkinter as tk

from pages.Reisoverzicht import *
from pages.Start import *


class Program(tk.Frame):


  def __init__(self, *args, **kwargs):
    tk.Frame.__init__(self)
    # config
    backgroundColor = kwargs.get('backgroundColor', "#FFCF1A")
    tintColor = kwargs.get("tintColor", "#2007FF")
    startStation = kwargs.get('startStation', "Utrecht")

    startPage = Start(self)
    reisoverzichtPage = ReisOverzicht(self, backgroundColor=backgroundColor, startStation=startStation)

    # creeër container
    container = tk.Frame(self)
    container.pack(side="top", fill="both", expand=True)

    #plaats in container
    startPage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
    reisoverzichtPage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

    test = tk.Button(startPage, text="page2", command=reisoverzichtPage.lift)
    test.pack(side="left")
    #startPage.lift()
    reisoverzichtPage.lift()



root = tk.Tk()
root.minsize(800, 600)
root.title("NS kaart automaat")
main = Program(root, startStation="Utrecht", backgroundColor="#FFCF1A", tintColor="#2007FF")

main.pack(side="top", fill="both", expand=True)


root.mainloop()