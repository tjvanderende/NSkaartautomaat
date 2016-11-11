from tkinter import *
from pages.Page import *
from PIL import Image, ImageTk

class Start(Page):

  def __init__(self, *args, **kwargs):
    """
    :param: backgroundColor (string), achtergrond kleur
    :param: tintColor (string), titn kleur (knop kleur).
    :rtype: object
    """
    super(Start, self).__init__(*args, **kwargs)

    self.backgroundColor = kwargs.get("backgroundColor")
    self.tintColor = kwargs.get("tintColor")

    label1 = Label(self, text='Welkom bij de NS', font=("Calibri", 28, "bold"), background=self.backgroundColor)
    label1.pack(fill='both', anchor="s", expand=True)

    photo = PhotoImage(file="assets/ovchipkaart.png")
    label2 = Label(self, image=photo, background=self.backgroundColor)
    label2.image = photo
    label2.pack(fill='x', anchor="n", side=TOP, expand=True)


    self.buttonFrame = Frame(self)

    button1 = Button(self.buttonFrame,width=150, text="Ik wil naar amsterdam")
    button1.config(foreground=self.backgroundColor, bg=self.tintColor)
    self.buttonFrame.columnconfigure(0, weight=1)
    button1.grid(row=0, padx=5, column=0, sticky=N+S+W+E)

    button2 = Button(self.buttonFrame,width=150, text="Los kaartje kopen")
    button2.config(foreground=self.backgroundColor, bg=self.tintColor)
    self.buttonFrame.columnconfigure(1, weight=1)
    button2.grid(row=0,padx=5, column=1, sticky=N+S+W+E)

    button3 = Button(self.buttonFrame,width=150, text="Kopen Ov chipkaart")
    button3.config(foreground=self.backgroundColor, bg=self.tintColor)
    self.buttonFrame.columnconfigure(2, weight=1)
    button3.grid(row=0, padx=5, column=2, sticky=N + S+W+E)

    button4 = Button(self.buttonFrame,width=150, text="Ik wil naar het buitenland")
    button4.config(foreground=self.backgroundColor, bg=self.tintColor)
    self.buttonFrame.columnconfigure(3, weight=1)
    button4.grid(row=0, padx=5, column=3, sticky=N+S+W+E)

    self.buttonFrame.columnconfigure(4, weight=1)


    self.buttonFrame.rowconfigure(0, weight=1)
    self.buttonFrame.rowconfigure(1, weight=1)
    self.buttonFrame.pack(fill='both', anchor='n', side=TOP, expand=True)
    self.buttonFrame.config(background=self.backgroundColor, padx=10)






