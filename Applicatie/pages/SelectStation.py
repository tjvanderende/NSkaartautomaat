from tkinter import *
import xmltodict
from Applicatie.api.nsAPI import NsRequest


class SelectStation(Toplevel):
  def __init__(self, parent, station, background, api_stationlijst):
    super(SelectStation, self).__init__()
    self.api_stationlijst = api_stationlijst
    self.listboxFilter = StringVar()
    self.listboxFilter.set("All")

    self.values = []
    self.listbox = Listbox(self, bg=background, relief=FLAT, bd=0)
    self.listbox.pack(fill="both", expand=True)
    self.listbox.bind('<<ListboxSelect>>', self.listboxSelect)
    self.parent = parent
    self.station = station
    self.grab_set() # zorg ervoor dat interactie geblokkeerd is zolang dit scherm open is.
    self.wm_title("Selecteer station")

    submit = Button(self, command=self.submit)
    #submit.pack(side="top", fill="both", expand=True)

    '''
    Voeg menu opties toe
    '''
    menuBar = Menu(self)
    self.config(menu=menuBar, background=background, width=300)
    self.generateOptions(menuBar)
    self.loadStations()

    self.wm_geometry("400x500")

  def loadStations(self):
    request = NsRequest(url=self.api_stationlijst, filename="stationlijst.xml")
    if(request.run()): #succesvol data opgehaald
      self.printStations(filename='stationlijst.xml')
    else:
      print("halloooo")

  def printStations(self, filename):
    with open(filename, 'r') as Stations:
      dictobject = xmltodict.parse(Stations.read())
      stations = dictobject['Stations']
      for value in stations['Station']:
        self.values.append(value['Namen']['Lang'])

    self.fillListbox()

  def generateOptions(self, menuBar):

    filterOptions = Menu(menuBar)
    menuBar.add_cascade(label="Filter", menu=filterOptions)
    options = ["All", "A", "B", "C","D", "E"]
    for filter in options:
      filterOptions.add_command(label = filter, command=lambda filter = filter: self.filterAlphabetic(filter))

  def filterAlphabetic(self, filter):
    self.listboxFilter.set(filter)
    self.fillListbox()

  def fillListbox(self):
    filter_mode = self.listboxFilter.get()
    self.listbox.delete(0, END)

    if (filter_mode == "All"):
      for item in self.values:
        self.listbox.insert(END, item)
    else:
      for item in self.values:
        if item.startswith(filter_mode):
          self.listbox.insert(END, item)

  def listboxSelect(self, event):
    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    self.parent.refreshData(value)

  def submit(self):
    self.parent.refreshData()

