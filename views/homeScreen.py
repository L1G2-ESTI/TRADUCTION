from tkinter import *
import tkinter as tk
from tkinter import ttk

home = tk.Tk()#initialise la fenêtre principale
home.title("Dictionaire")#titre de la fenêtre principale
home.geometry("1000x610")
imgFrame = PhotoImage(file="./frames/frame.png")#importation du frame de l'application
label1 = Label( home, image = imgFrame)
label1.place(x = 0, y = 0)#mettre à zero la place de l'image pour qu'il se positionne par défeaut
frame1 = Frame(home)#metre l'image dans la fenetre home
frame1.pack(pady = 20 )
home.resizable(0,0)#à 0,0 la fênetre ne peut pas être agrandis

#configuration du boutton Traduire
traduireButton = Button(home, text="Traduire")
traduireButton.place(x=640, y=120, width=80, height=30)
traduireButton.configure(overrelief="flat")
traduireButton.configure(relief="flat")
traduireButton.configure(activebackground="white")
traduireButton.configure(background="#55bf76")
traduireButton.configure(foreground="white")
traduireButton.configure(cursor="hand2")
traduireButton.configure(font="-family {Poppins SemiBold} -size 10")
traduireButton.configure(borderwidth=50)

home.mainloop()
