from tkinter import *
import tkinter as tk
from tkinter import ttk

home = tk.Tk()#initialise la fenêtre principale
home.title("Dictionaire")#titre de la fenêtre principale

#home.resizable(0,0)#à 0,0 la fênetre ne peut pas être agrandis
Titre = ttk.Label(home, text="DICTIONAIRE PYTHON")

Titre.grid(column=0, row=0)

home.mainloop()
