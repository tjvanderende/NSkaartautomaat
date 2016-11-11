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

    startPage = Start(self, backgroundColor=backgroundColor, tintColor=tintColor)
    reisoverzichtPage = ReisOverzicht(self, backgroundColor=backgroundColor, startStation=startStation)
    selectstationPage = SelectStation(parent=reisoverzichtPage, backgroundColor=backgroundColor, tintColor=tintColor)

    # creeër container
    container = tk.Frame(self)
    container.pack(side="top", fill="both", expand=True)

    #plaats in container
    startPage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
    reisoverzichtPage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
    selectstationPage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

    #plaats Reisoverzicht button op startPage
    test = tk.Button(startPage, text="Reisoverzicht", command=reisoverzichtPage.lift)
    test.place(height=80, width=150, x=632, y=450)
    test.config(foreground=backgroundColor, background=tintColor)

    #plaats selectStation button op reisoverzichtPage
    stationButton = tk.Button(reisoverzichtPage, text="Selecteer station", command=selectstationPage.lift)
    stationButton.place(height=35, width=100, x=682, y=5)
    stationButton.config(foreground=backgroundColor, background=tintColor)

    #plaats reisoverzicht button op selectstationPage
    selectButton = tk.Button(selectstationPage, text="Selecteer", command=reisoverzichtPage.lift)
    selectButton.place(height=35, width=100, x=682, y=5)
    selectButton.config(foreground=backgroundColor, background=tintColor)

    #plaats vorige button op selectstationPage
    prevButton = tk.Button(selectstationPage, text="Vorige", command=reisoverzichtPage.lift)
    prevButton.place(height=35, width=100, x=572, y=5)
    prevButton.config(foreground=backgroundColor, background=tintColor)

    startPage.lift()



root = tk.Tk()
root.minsize(800, 600)
root.title("NS kaart automaat")
main = Program(root, startStation="Utrecht", backgroundColor="#FFCF1A", tintColor="#2007FF")

main.pack(side="top", fill="both", expand=True)


root.mainloop()
