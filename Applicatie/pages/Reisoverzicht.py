from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import xmltodict
from Applicatie.pages.SelectStation import *
from Applicatie.pages.Page import *
from Applicatie.api.nsAPI import NsRequest


class ReisOverzicht(Page):
  def __init__(self, *args, **kwargs):
    super(ReisOverzicht, self).__init__(*args, **kwargs)

    self.api_vetrek = 'http://webservices.ns.nl/ns-api-avt?station='
    self.api_stationlijst = 'http://webservices.ns.nl/ns-api-stations-v2'

    self.currentStation = StringVar()
    self.backgroundColor = kwargs.get("backgroundColor")
    self.tintColor = kwargs.get("tintColor")

    #knop om menu mee te openen.
    titlePrefix = Label(self, text="Huidige station:", font=48, background=self.backgroundColor)
    titlePrefix.grid(row=0, column=0, padx=2, pady=2, sticky=N+S+W)

    self.openMenu = Label(self, textvariable=self.currentStation, font=48, background=self.backgroundColor)
    self.openMenu.bind('<Button-1>', self.openSelection)
    self.openMenu.grid(row=0, column=1, padx=2, pady=2, sticky=N+S+E)


    self.currentStation.set(kwargs.get('startStation')) # bind variabele
    self.loadReisinfo() # toon reisinformatie de eerste keer.

  def openSelection(self, event=None):
    SelectStation(self, self.currentStation, self.backgroundColor, self.api_stationlijst)

  def loadReisinfo(self):
    print(self.api_stationlijst+self.currentStation.get())
    request = NsRequest(url=self.api_vetrek+self.currentStation.get(), filename="vetrektijden.xml")
    if(request.run()): # success (200 code)
      self.printReisinfo(filename='vetrektijden.xml')
    else:
      print("error")

  def printReisinfo(self, filename):
    with open(filename, 'r') as Vetrektijden:
      vetrektijden = xmltodict.parse(Vetrektijden.read())
      print(vetrektijden['ActueleVertrekTijden'])


  def refreshData(self, station):
    self.currentStation.set(station) # update station
    self.loadReisinfo() # laad reisinfo opnieuw

