from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import xmltodict
from Applicatie.pages.SelectStation import *
from Applicatie.pages.Page import *
from Applicatie.api.nsAPI import NsRequest
'''  titlePrefix = Label(self, text="Huidige station:", font=48, background=self.backgroundColor)
    titlePrefix.grid(row=0, column=0, padx=2, pady=2, sticky=N + S + W)

    # knop om menu mee te openen.
    self.openMenu = Label(self, textvariable=self.currentStation, font=48, background=self.backgroundColor)
    self.openMenu.bind('<Button-1>', self.openSelection)
    self.openMenu.grid(row=0, column=1, padx=2, pady=2, sticky=N + S + E)'''

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


    self.currentStation.set(kwargs.get('startStation'))  # bind variabele met start station
    self.loadReisinfo()  # toon reisinformatie de eerste keer.'''
    w = Canvas(self, width=800, height=600, bg="black")
    w.pack()

    w.create_rectangle(5, 5, 795, 595, fill="#FFCF1A")
    w.create_rectangle(0, 70, 800, 120, fill="black")
    w.create_rectangle(5, 75, 795, 115, fill="white")
    w.create_rectangle(140, 75, 145, 800, fill="black")
    w.create_rectangle(360, 75, 365, 800, fill="black")
    w.create_rectangle(640, 75, 645, 800, fill="black")
    self.openMenu = Label(self, textvariable=self.currentStation, font=("Calibri", 28, "bold"), background=self.backgroundColor)
    self.openMenu.bind('<Button-1>', self.openSelection)

    label1 = Label(self, text='Huidige station:', font=("Calibri", 28, "bold"), background=self.backgroundColor)
    label1.place(x=20, y=10)
    self.openMenu.place(x=270, y=10)

    label2 = Label(self, text="Tijd", bg="white", font=("Calibri", 11, "bold",))
    label2.place(x=15, y=80)
    label3 = Label(self, text="Naar", bg="white", font=("Calibri", 11, "bold",))
    label3.place(x=150, y=80)
    label4 = Label(self, text="Vervoerder", bg="white", font=("Calibri", 11, "bold",))
    label4.place(x=370, y=80)
    label5 = Label(self, text="Spoor", bg="white", font=("Calibri", 11, "bold",))
    label5.place(x=650, y=80)

    tijd1 = Label(self, text="Tijd1", bg="#FFCF1A", font=("Calibri", 10))
    tijd1.place(x=15, y=130)
    tijd2 = Label(self, text="Tijd2", bg="#FFCF1A", font=("Calibri", 10))
    tijd2.place(x=15, y=150)
    tijd3 = Label(self, text="Tijd3", bg="#FFCF1A", font=("Calibri", 10))
    tijd3.place(x=15, y=170)
    tijd4 = Label(self, text="Tijd4", bg="#FFCF1A", font=("Calibri", 10))
    tijd4.place(x=15, y=190)
    tijd5 = Label(self, text="Tijd5", bg="#FFCF1A", font=("Calibri", 10))
    tijd5.place(x=15, y=210)

    naar1 = Label(self, text="Naar1", bg="#FFCF1A", font=("Calibri", 10))
    naar1.place(x=150, y=130)
    naar2 = Label(self, text="Naar2", bg="#FFCF1A", font=("Calibri", 10))
    naar2.place(x=150, y=150)
    naar3 = Label(self, text="Naar3", bg="#FFCF1A", font=("Calibri", 10))
    naar3.place(x=150, y=170)
    naar4 = Label(self, text="Naar4", bg="#FFCF1A", font=("Calibri", 10))
    naar4.place(x=150, y=190)
    naar5 = Label(self, text="Naar5", bg="#FFCF1A", font=("Calibri", 10))
    naar5.place(x=150, y=210)

    # even een loop geknald
    c = 1
    Ycord = 130
    v = 1
    while v < 11:
      C = str(c)
      Xcord = 370
      v1 = Label(self, text="Vervoerder" + C, bg="#FFCF1A", font=("Calibri", 10))
      v1.place(x=Xcord, y=Ycord)
      c = c + 1
      Ycord = Ycord + 20
      v = v + 1

    '''a = 1
    Ycord = 130
    v = 1
    while v < 11:
      A = str(a)
      Xcord = 650
      v1 = Label(self, text="Spoor " + A, bg="#FFCF1A", font=("Calibri", 10))
      v1.place(x=Xcord, y=Ycord)
      a = a + 1
      Ycord = Ycord + 20
      v = v + 1 '''

    self.loadReisinfo()

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
    request.join() # blok met reisinformatie tonen totdat de data er is.
    self.printReisinfo(filename='assets/database/vetrektijden.xml', xcord=650, key="VertrekTijd") #laad sowieso in (anders van cache).
    #self.printReisinfo(filename='assets/database/vetrektijden.xml', xcord=650, key="VertrekTijd") #laad sowieso in (anders van cache).

   # if (not request.run()):  # anders dan code 200 (success)
    #  print("error")


  def printReisinfo(self, filename, xcord, key):
    ycord = 130

    v1 = Label(self, text="test", bg="blue", font=("Calibri", 10))
    v1.place(x=650, y=130)
    """
    Haal de data op uit de database (file).
    :param filename: .xml file die gebruikt wordt om de data uit te lezen.
    """
    try:
      with open(filename, 'r') as Vetrektijden:
        vetrektijden = xmltodict.parse(Vetrektijden.read())
        tijden = vetrektijden['ActueleVertrekTijden']
        vertrekkendeTreinen = tijden['VertrekkendeTrein']

        for vertrekkendeTrein in vertrekkendeTreinen:
          print(vetrre)
          v1 = Label(self, text=vertrekkendeTrein[key], bg=self.backgroundColor, font=("Calibri", 10))
          v1.place(x=xcord, y=ycord)
          ycord += 20



    except FileNotFoundError:
      print("File could not be loaded")
    except KeyError:
      print("Error")

  def refreshData(self, station):
    """
    Opgeroepen vanuit SelectStation

    :param station: String, station waarvan de actuele reisdata van getoond moet worden.
    """
    self.currentStation.set(station)  # update station
    self.loadReisinfo()  # laad reisinfo opnieuw
