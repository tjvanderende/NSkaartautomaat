from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
from pages.Page import *


class ReisOverzicht(Page):
  def __init__(self, *args, **kwargs):
    super(ReisOverzicht, self).__init__(*args, **kwargs)
    self.currentStation = StringVar()
    self.backgroundColor = kwargs.get("backgroundColor")
    self.tintColor = kwargs.get("tintColor")

    #knop om menu mee te openen.
    self.openMenu = Label(self, textvariable=self.currentStation)
    self.openMenu.bind('<Button-1>', self.openSelection)
    self.currentStation.set(kwargs.get('startStation')) # bind variabele
    self.openMenu.pack(side="top")

  def openSelection(self, event=None):
    selection = SelectStation(self, self.currentStation, self.backgroundColor)


  def loadStations(self):
    pass

  def loadReisinfo(self):
    pass

  def refreshData(self, station):
    self.currentStation.set(station)

class SelectStation(Toplevel):
  def __init__(self, parent, station, background):
    super(SelectStation, self).__init__()

    self.listboxFilter = StringVar()
    self.listboxFilter.set("All")


    self.listbox = Listbox(self, bg=background, relief=FLAT, bd=0)
    self.listbox.pack(fill="both", expand=True)
    self.fillListbox()

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

  def generateOptions(self, menuBar):

    filterOptions = Menu(menuBar)
    menuBar.add_cascade(label="Filter", menu=filterOptions)
    options = ["A", "B", "C","D", "E"]
    for filter in options:
      filterOptions.add_command(label = filter, command=lambda filter = filter: self.filterAlphabetic(filter))

  def filterAlphabetic(self, filter):
    self.listboxFilter.set(filter)
    self.fillListbox()

  def fillListbox(self):
    filter_mode = self.listboxFilter.get()
    values = ["One", "Two", "Three", "Adddo"]
    self.listbox.delete(0, END)

    if (filter_mode == "All"):
      for item in values:
        self.listbox.insert(END, item)
    else:
      for item in values:
        if item.startswith(filter_mode):
          self.listbox.insert(END, item)


  def submit(self):
    self.parent.refreshData("Amsterdam")

