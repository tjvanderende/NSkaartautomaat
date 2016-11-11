import tkinter as tk
from Applicatie.pages.Reisoverzicht import *
from Applicatie.pages.Start import *

class Program(tk.Frame):


  def __init__(self, *args, **kwargs):
    tk.Frame.__init__(self)
    # config
    backgroundColor = kwargs.get('backgroundColor', "#FFCF1A")
    tintColor = kwargs.get("tintColor", "#2007FF")
    startStation = kwargs.get('startStation', "Utrecht Centraal")

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
    test = tk.Button(startPage.buttonFrame, width=150, text="Reisoverzicht", command=reisoverzichtPage.lift)
    test.grid(row=0, column=4, sticky=N + S + E + W, padx=5)
    test.config(foreground=backgroundColor, background=tintColor)

    #plaats selectStation button op reisoverzichtPage
    stationButton = tk.Button(reisoverzichtPage, text="Selecteer station", command=selectstationPage.lift)
    stationButton.place(height=35, width=100, x=682, y=5)
    stationButton.config(foreground=backgroundColor, background=tintColor)

    #plaats vorige button op reisoverzichtPage
    prevButton0 = tk.Button(reisoverzichtPage, text="Vorige", command=startPage.lift)
    prevButton0.place(height=35, width=100, x=572, y=5)
    prevButton0.config(foreground=backgroundColor, background=tintColor)

    #plaats reisoverzicht button op selectstationPage
    selectButton = tk.Button(selectstationPage, text="Selecteer", command=reisoverzichtPage.lift)
    selectButton.place(height=35, width=100, x=682, y=5)
    selectButton.config(foreground=backgroundColor, background=tintColor)

    #plaats vorige button op selectstationPage
    prevButton1 = tk.Button(selectstationPage, text="Vorige", command=reisoverzichtPage.lift)
    prevButton1.place(height=35, width=100, x=572, y=5)
    prevButton1.config(foreground=backgroundColor, background=tintColor)

    startPage.lift()



root = tk.Tk()
root.minsize(800, 600)
root.title("NS kaart automaat")
main = Program(root, startStation="Utrecht Centraal", backgroundColor="#FFCF1A", tintColor="#2007FF")

main.pack(side="top", fill="both", expand=True)


root.mainloop()
