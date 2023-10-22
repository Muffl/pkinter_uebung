import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
 
script = sys.argv[0]



_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc

_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

class Toplevel1:
    def __init__(self, top=None):
         '''This class configures and populates the toplevel window.
   33            top is the toplevel containing window.'''

    top.geometry("600x450+660+210")
    top.minsize(120, 1)
    
   37         top.maxsize(3844, 1061)
   38         top.resizable(1,  1)
   39         top.title("Toplevel 0")
   40         top.configure(background="#d9d9d9")
   41 
   42         self.top = top
   """