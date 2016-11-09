from tkinter import *
from tkinter.ttk import *
import xmltodict
from Applicatie.api.nsAPI import NsRequest


class SelectStation(Toplevel):
  def __init__(self, parent, station, background, api_stationlijst):
    """

    :param parent: Reisoverzicht.py context
    :param station: Het huidige station (string)
    :param background: Achtergrond kleur (string)
    :param api_stationlijst: URI van NS API waarmee stations opgevraagd kunnen worden (string)
    """
    super(SelectStation, self).__init__()

    self.api_stationlijst = api_stationlijst
    self.listboxFilter = StringVar()  # stringvar kan gebruikt worden om data te binden (direct door geven aan UI).
    self.listboxFilter.set("All")  # standaard filter toon alles.
    self.values = []  # waarden die getoond worden in list.
    self.parent = parent
    self.station = station
    self.grab_set()  # zorg ervoor dat interactie geblokkeerd is zolang dit scherm open is.
    self.wm_title("Selecteer station")  # titel van window.
    self.wm_geometry("400x500")  # zet grootte van window.

    # listbox
    self.listbox = Listbox(self, bg=background, relief=FLAT, bd=0)
    self.listbox.pack(fill="both", expand=True)
    self.listbox.bind('<<ListboxSelect>>', self.listboxSelect)  # bind selectie event aan listbox.

    # menu balk
    menuBar = Menu(self) #toon een menu optie
    self.config(menu=menuBar, background=background)
    self.generateOptions(menuBar)

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
    self.printStations(filename='assets/database/stationlijst.xml')

  def printStations(self, filename):
    """
    Toon alle stations uit de meegegeven XML file.
    :param filename: Een xml file waar de data in is opgeslagen
    """
    with open(filename, 'r') as Stations: # open filename met reading
      dictobject = xmltodict.parse(Stations.read())
      stations = dictobject['Stations'] # haal met de sleutel de data op
      for value in stations['Station']: #loop door alle stations
        self.values.append(value['Namen']['Lang'])

    self.fillListbox() # vul de listbox

  def generateOptions(self, menuBar):
    """
    Genereer de opties voor het menu
    :param menuBar: Menuobject waar het submenu dat gegenereerd wordt in deze functie aan vastgekoppeld wordt
    """
    filterOptions = Menu(menuBar)
    menuBar.add_cascade(label="Filter", menu=filterOptions)
    options = ["All", "A", "B", "C",
               "D", "E", "F", "G", "H",
               "I", "J","K","L","M",
               "N","O","P","Q", "R",
               "S", "T", "U", "V", "W", "X", "Y", "Z"] # filter opties (alfabet)
    for filter in options: # Genereer opties
      """
      lamda wordt gebruikt om direct een referentie te kunnen genereren van filter.
      Anders wordt de verkeerder filter aan de functie meegegeven.
      """
      filterOptions.add_command(label=filter, command=lambda filter=filter: self.filterAlphabetic(filter))

  def filterAlphabetic(self, filter):
    """
    Deze functie maakt gebruik van fillListbox, alleen wordt hier de letter gezet.
    :param filter: String, de letter waarop gefilterd wordt.
    """
    self.listboxFilter.set(filter) # bind eerst het filter.
    self.fillListbox() # roep nu filllistbox aan


  def fillListbox(self):
    """
    Handel het filteren af.
    Gooit de listbox leeg en vult het daarna opnieuw afhankelijk van het filter.
    """
    filter_mode = self.listboxFilter.get() #haal filter op
    self.listbox.delete(0, END) # gooi leeg

    if (filter_mode == "All"): #toon alle stations in listbox
      for item in self.values:
        self.listbox.insert(END, item)
    else:
      for item in self.values:
        if item.startswith(filter_mode): #toon alleen stations die overeenkomen met het filter.
          self.listbox.insert(END, item)

  def listboxSelect(self, event):
    """
    Handel klik event af vanuit de listbox.
    :param event: Geselecterde element
    """
    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index) # haal juiste waarde op met de index.
    self.parent.refreshData(value) # refresh de data in ReisOverzicht.

