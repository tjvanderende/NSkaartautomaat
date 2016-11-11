import tkinter as tk
from tkinter.ttk import *
import xmltodict
from Applicatie.api.nsAPI import NsRequest
from Applicatie.pages.Page import *
import math

class SelectStation(Page):
  def __init__(self, *args, **kwargs):

    super(SelectStation, self).__init__(*args, **kwargs)

    self.api_stationlijst = 'http://webservices.ns.nl/ns-api-stations-v2'  # URL om lijst met stations op te halen.
    self.valuesLang = []  # waarden die getoond worden in list.
    self.valuesMiddel = []
    self.parent = kwargs.get("parent")
    self.backgroundColor = kwargs.get("backgroundColor")
    self.tintColor = kwargs.get("tintColor")

    label1 = Label(self, text='Zoeken naar\nstation:', font=("Calibri", 14, "bold"), foreground=self.backgroundColor, background=self.tintColor, width=12, height= 2)
    label1.place(x=10, y=10)

    #alle letter buttons maken
    buttonA = tk.Button(self, text="A", font=("Calibri", 14, "bold"), foreground=self.tintColor, background=self.backgroundColor, width=2, height=1, command=lambda: self.showStations("A"))
    buttonA.place(x=10, y=75)
    buttonB = tk.Button(self, text="B", font=("Calibri", 14, "bold"), foreground=self.tintColor, background=self.backgroundColor, width=2, height=1, command=lambda: self.showStations("B"))
    buttonB.place(x=50, y=75)
    buttonC = tk.Button(self, text="C", font=("Calibri", 14, "bold"), foreground=self.tintColor, background=self.backgroundColor, width=2, height=1, command=lambda: self.showStations("C"))
    buttonC.place(x=90, y=75)
    buttonD = tk.Button(self, text="D", font=("Calibri", 14, "bold"), foreground=self.tintColor, background=self.backgroundColor, width=2, height=1, command=lambda: self.showStations("D"))
    buttonD.place(x=130, y=75)
    buttonE = tk.Button(self, text="E", font=("Calibri", 14, "bold"), foreground=self.tintColor, background=self.backgroundColor, width=2, height=1, command=lambda: self.showStations("E"))
    buttonE.place(x=170, y=75)
    buttonF = tk.Button(self, text="F", font=("Calibri", 14, "bold"), foreground=self.tintColor, background=self.backgroundColor, width=2, height=1, command=lambda: self.showStations("F"))
    buttonF.place(x=210, y=75)
    buttonG = tk.Button(self, text="G", font=("Calibri", 14, "bold"), foreground=self.tintColor, background=self.backgroundColor, width=2, height=1, command=lambda: self.showStations("G"))
    buttonG.place(x=250, y=75)
    buttonH = tk.Button(self, text="H", font=("Calibri", 14, "bold"), foreground=self.tintColor, background=self.backgroundColor, width=2, height=1, command=lambda: self.showStations("H"))
    buttonH.place(x=290, y=75)
    buttonI = tk.Button(self, text="I", font=("Calibri", 14, "bold"), foreground=self.tintColor, background=self.backgroundColor, width=2, height=1, command=lambda: self.showStations("I"))
    buttonI.place(x=330, y=75)
    buttonJ = tk.Button(self, text="J", font=("Calibri", 14, "bold"), foreground=self.tintColor, background=self.backgroundColor, width=2, height=1, command=lambda: self.showStations("J"))
    buttonJ.place(x=370, y=75)
    buttonK = tk.Button(self, text="K", font=("Calibri", 14, "bold"), foreground=self.tintColor, background=self.backgroundColor, width=2, height=1, command=lambda: self.showStations("K"))
    buttonK.place(x=410, y=75)
    buttonL = tk.Button(self, text="L", font=("Calibri", 14, "bold"), foreground=self.tintColor, background=self.backgroundColor, width=2, height=1, command=lambda: self.showStations("L"))
    buttonL.place(x=450, y=75)
    buttonM = tk.Button(self, text="M", font=("Calibri", 14, "bold"), foreground=self.tintColor, background=self.backgroundColor, width=2, height=1, command=lambda: self.showStations("M"))
    buttonM.place(x=490, y=75)
    buttonN = tk.Button(self, text="N", font=("Calibri", 14, "bold"), foreground=self.tintColor, background=self.backgroundColor, width=2, height=1, command=lambda: self.showStations("N"))
    buttonN.place(x=10, y=120)
    buttonO = tk.Button(self, text="O", font=("Calibri", 14, "bold"), foreground=self.tintColor, background=self.backgroundColor, width=2, height=1, command=lambda: self.showStations("O"))
    buttonO.place(x=50, y=120)
    buttonP = tk.Button(self, text="P", font=("Calibri", 14, "bold"), foreground=self.tintColor, background=self.backgroundColor, width=2, height=1, command=lambda: self.showStations("P"))
    buttonP.place(x=90, y=120)
    buttonQ = tk.Button(self, text="Q", font=("Calibri", 14, "bold"), foreground=self.tintColor, background=self.backgroundColor, width=2, height=1, command=lambda: self.showStations("Q"))
    buttonQ.place(x=130, y=120)
    buttonR = tk.Button(self, text="R", font=("Calibri", 14, "bold"), foreground=self.tintColor, background=self.backgroundColor, width=2, height=1, command=lambda: self.showStations("R"))
    buttonR.place(x=170, y=120)
    buttonS = tk.Button(self, text="S", font=("Calibri", 14, "bold"), foreground=self.tintColor, background=self.backgroundColor, width=2, height=1, command=lambda: self.showStations("S"))
    buttonS.place(x=210, y=120)
    buttonT = tk.Button(self, text="T", font=("Calibri", 14, "bold"), foreground=self.tintColor, background=self.backgroundColor, width=2, height=1, command=lambda: self.showStations("T"))
    buttonT.place(x=250, y=120)
    buttonU = tk.Button(self, text="U", font=("Calibri", 14, "bold"), foreground=self.tintColor, background=self.backgroundColor, width=2, height=1, command=lambda: self.showStations("U"))
    buttonU.place(x=290, y=120)
    buttonV = tk.Button(self, text="V", font=("Calibri", 14, "bold"), foreground=self.tintColor, background=self.backgroundColor, width=2, height=1, command=lambda: self.showStations("V"))
    buttonV.place(x=330, y=120)
    buttonW = tk.Button(self, text="W", font=("Calibri", 14, "bold"), foreground=self.tintColor, background=self.backgroundColor, width=2, height=1, command=lambda: self.showStations("W"))
    buttonW.place(x=370, y=120)
    buttonX = tk.Button(self, text="X", font=("Calibri", 14, "bold"), foreground=self.tintColor, background=self.backgroundColor, width=2, height=1, command=lambda: self.showStations("X"))
    buttonX.place(x=410, y=120)
    buttonY = tk.Button(self, text="Y", font=("Calibri", 14, "bold"), foreground=self.tintColor, background=self.backgroundColor, width=2, height=1, command=lambda: self.showStations("Y"))
    buttonY.place(x=450, y=120)
    buttonZ = tk.Button(self, text="Z", font=("Calibri", 14, "bold"), foreground=self.tintColor, background=self.backgroundColor, width=2, height=1, command=lambda: self.showStations("Z"))
    buttonZ.place(x=490, y=120)

    label2 = Label(self, text='Selecteer huidige\nstation hieronder:', font=("Calibri", 14, "bold"), foreground=self.backgroundColor, background=self.tintColor, width=18, height= 2)
    label2.place(x=10, y=180)

    #stationbuttons frame
    self.frame1 = Frame(self, width=800, height=360, background=self.backgroundColor)
    self.frame1.place(x=5, y=240)

    #laad de data in
    self.loadStations()


  def loadStations(self):
    """
    Gebruik de NsRequest klasse om de stationlijst te laden.
    Todo: Toon foutmelding
    """
    request = NsRequest(url=self.api_stationlijst, filename="stationlijst.xml")
    request.start()
    # wanneer de data via request niet refreshed is wordt er een cache getoond.
    self.fillValues(filename='assets/database/stationlijst.xml')

  def fillValues(self, filename):
    """
    Vul de value lijsten met alle stations in Nederland
    :param filename: Een xml file waar de data in is opgeslagen
    """
    with open(filename, 'r') as Stations: # open filename met reading
      dictobject = xmltodict.parse(Stations.read())
      stations = dictobject['Stations'] # haal met de sleutel de data op
      for value in stations['Station']: #loop door alle stations
        if value['Land'] == 'NL':
          self.valuesLang.append(value['Namen']['Lang'])
          self.valuesMiddel.append(value['Namen']['Middel'])

  def showStations(self, letter):
      """
      Alle stations die beginnen met de meegegeven letter een knop geven en weergeven.
      Als er op een knop gedrukt wordt, verandert het huidige station op reisoverzichtPage.
      :param letter: een string van 1 letter waarop wordt gefilterd
      """
      stationList = []
      buttons = []
      counter = 0
      self.frame1.destroy() #frame leegmaken door te verwijderen en nieuwe aan te maken
      self.frame1 = Frame(self, width=800, height=360, background=self.backgroundColor)
      self.frame1.place(x=5, y=240)
      #alle stations afgaan en checken met beginletter
      for n in range(len(self.valuesLang)):
          if self.valuesLang[n].startswith(letter): #beginletter check voor volledige naam
              stationList.append(self.valuesMiddel[n])
          elif self.valuesMiddel[n].startswith(letter): #beginletter check voor middellange naam
              stationList.append(self.valuesMiddel[n])
      for i in range(int(math.ceil(len(stationList)/6))): #for loop voor aantal rows van de grid
          if len(stationList)-counter >= 6:
              for j in range(6): #aantal columns
                  buttons.append(tk.Button(self, text=stationList[counter],font=("Calibri", 10, "bold"), foreground=self.backgroundColor, background=self.tintColor, width=16, command=lambda counter=counter:self.parent.refreshData(stationList[counter])))
                  buttons[counter].grid(column=j,row=i, padx=5, pady=5, in_=self.frame1)
                  counter += 1
          elif len(stationList)-1-counter < 6:
              for k in range(int(len(stationList)%6)): # overige columns
                  buttons.append(tk.Button(self, text=stationList[counter],font=("Calibri", 10, "bold"), foreground=self.backgroundColor, background=self.tintColor, width=16))
                  buttons[counter].grid(column=k,row=i, padx=5, pady=5, in_=self.frame1)
                  counter += 1
