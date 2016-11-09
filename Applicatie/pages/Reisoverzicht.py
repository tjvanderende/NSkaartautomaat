from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import xmltodict
from Applicatie.pages.SelectStation import *
from Applicatie.pages.Page import *
from Applicatie.api.nsAPI import NsRequest


class ReisOverzicht(Page):
  def __init__(self, *args, **kwargs):
    """
    Reisoverzicht extend Page en dit is een pagina waarheen genavigeerd kan worden door lift() aan te roepen.
    :type kwargs: Optionele argumenten die zijn meegegeven.
    """
    super(ReisOverzicht, self).__init__(*args, **kwargs)

    self.api_vetrek = 'http://webservices.ns.nl/ns-api-avt?station='  # de URL om vetrek actuele tijden mee op te halen
    self.api_stationlijst = 'http://webservices.ns.nl/ns-api-stations-v2'  # URL om lijst met stations op te halen.

    self.currentStation = StringVar()  # bind de huidige waarde van station aan GUI.

    # kleuren
    self.backgroundColor = kwargs.get("backgroundColor")  # haal achtergrond kleur op
    self.tintColor = kwargs.get("tintColor")  # haal tint kleur op

    # titleprefix die samen met self.openmenu de titel vormt.
    titlePrefix = Label(self, text="Huidige station:", font=48, background=self.backgroundColor)
    titlePrefix.grid(row=0, column=0, padx=2, pady=2, sticky=N + S + W)

    # knop om menu mee te openen.
    self.openMenu = Label(self, textvariable=self.currentStation, font=48, background=self.backgroundColor)
    self.openMenu.bind('<Button-1>', self.openSelection)
    self.openMenu.grid(row=0, column=1, padx=2, pady=2, sticky=N + S + E)

    self.currentStation.set(kwargs.get('startStation'))  # bind variabele met start station
    self.loadReisinfo()  # toon reisinformatie de eerste keer.

  def openSelection(self, event=None):
    """
    Open het selectiepaneel (SelectStation)
    :param event: deprecated
    """
    SelectStation(self, self.currentStation, self.backgroundColor, self.api_stationlijst)

  def loadReisinfo(self):
    """
    laad reisinformatie in.
    """
    request = NsRequest(url=self.api_vetrek + self.currentStation.get(), filename="vetrektijden.xml")
    request.start()

    self.printReisinfo(filename='assets/database/vetrektijden.xml') #laad sowieso in (anders van cache).

   # if (not request.run()):  # anders dan code 200 (success)
    #  print("error")


  def printReisinfo(self, filename):
    """
    Haal de data op uit de database (file).
    :param filename: .xml file die gebruikt wordt om de data uit te lezen.
    """
    try:
      with open(filename, 'r') as Vetrektijden:
        vetrektijden = xmltodict.parse(Vetrektijden.read())
        print(vetrektijden['ActueleVertrekTijden'])
    except FileNotFoundError:
      print("File could not be loaded")
    except KeyError:
      print(vetrektijden)

  def refreshData(self, station):
    """
    Opgeroepen vanuit SelectStation

    :param station: String, station waarvan de actuele reisdata van getoond moet worden.
    """
    self.currentStation.set(station)  # update station
    self.loadReisinfo()  # laad reisinfo opnieuw
