from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import xmltodict
from Applicatie.pages.SelectStation import *
from Applicatie.pages.Page import *
from Applicatie.api.nsAPI import NsRequest

'''
Deze klasse is overgenomen vanuit:
http://stackoverflow.com/questions/5286093/display-listbox-with-columns-using-tkinter
'''
class MultiColumnListbox (ttk.Treeview):
    """use a ttk.TreeView as a multicolumn ListBox"""

    def __init__(self, parent, headers, data):
        super(MultiColumnListbox, self).__init__(parent)
        self.headers = headers
        self.data = data
        self._setup_widgets()
        self._build_tree()

    def _setup_widgets(self):

        self.config(columns=self.headers, show="headings")


    def refresh(self, data):

      for i in self.get_children():
        self.delete(i)
      for item in data:

        self.insert('', 'end', values=item)
        # adjust column's width if necessary to fit each value
        for ix, val in enumerate(item):
          col_w = tkFont.Font().measure(val)

          if self.column(self.headers[ix], width=None) < col_w:
            self.column(self.headers[ix], width=col_w)

      self.config(height=len(data))

    def _build_tree(self):
        for col in self.headers:

            self.heading(col, text=col.title(), command=lambda c=col: self.sortby(c, 0))

            # adjust the column's width to the header string
            self.column(col, width=tkFont.Font().measure(col.title()))


        self.refresh(self.data)

    def sortby(self, col, descending):
      """sort tree contents when a column header is clicked on"""
      # grab values to sort
      data = [(self.set(child, col), child) \
              for child in self.get_children('')]
      # if the data to be sorted is numeric change to float
      # data =  change_numeric(data)
      # now sort the data in place
      data.sort(reverse=descending)
      for ix, item in enumerate(data):
        self.move(item[1], '', ix)
      # switch the heading so it will sort in the opposite direction
      self.heading(col, command=lambda col=col: self.sortby(col, \
                                                       int(not descending)))

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



    self.currentStation.set(kwargs.get('startStation'))  # bind variabele met start station
    #self.loadReisinfo()  # toon reisinformatie de eerste keer.'''
    #w = Canvas(self, width=800, height=600, bg="black")
    #w.pack()
    self.headers = ['Tijd', 'Naar', 'Vervoerder', 'Spoor']





    self.listbox = MultiColumnListbox(self, self.headers, [])
    vsb = ttk.Scrollbar(command=self.listbox.yview)
    self.listbox.configure(yscrollcommand=vsb.set)

    ttk.Style().configure("Treeview", background=self.backgroundColor,
                          foreground="black")
    ttk.Style().configure("Treeview.Heading",
                          background="white",
                          padding=12)

    title = Frame(self)
    label1 = Label(title, text='Huidige station:', font=("Calibri", 24, "bold"), background=self.backgroundColor)
    label1.pack(side="left", anchor="nw")
    title.pack(side="top", anchor="w")

    self.openMenu = Label(title, textvariable=self.currentStation, font=("Calibri", 24, "bold"),
                          background=self.backgroundColor)
    self.openMenu.pack(side="left", anchor="n")
    self.listbox.pack(fill='both', expand=True)

    self.pack(fill='both', expand=True)

    self.loadReisinfo()

  def loadReisinfo(self):
    """
    laad reisinformatie in.
    """
    request = NsRequest(url=self.api_vetrek + self.currentStation.get(), filename="vetrektijden.xml")
    request.start()
    request.join() # blok met reisinformatie tonen totdat de data er is.
    self.printReisinfo(filename='assets/database/vetrektijden.xml', key="VertrekTijd") #laad sowieso in (anders van cache).


  def printReisinfo(self, filename, key):
    list = []
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
          total = [vertrekkendeTrein['VertrekTijd']]
          total.append(vertrekkendeTrein['EindBestemming'])
          total.append(vertrekkendeTrein['Vervoerder'])
          total.append(vertrekkendeTrein['VertrekSpoor']['#text'])
          list.append(total)


        self.listbox.refresh(list)
    except FileNotFoundError:
      print("File could not be loaded")
    except KeyError:
      print("A Key Error has occurred")

  def refreshData(self, station):
    """
    Opgeroepen vanuit SelectStation

    :param station: String, station waarvan de actuele reisdata van getoond moet worden.
    """
    self.currentStation.set(station)  # update station
    self.loadReisinfo()  # laad reisinfo opnieuw
