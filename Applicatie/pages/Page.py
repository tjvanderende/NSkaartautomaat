from tkinter import *

class Page (Frame):
  def __init__(self, *args, **kwargs):
    super(Page, self).__init__()
    self.configure(background=kwargs.get("backgroundColor"))
