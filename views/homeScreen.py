from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

home = tk.Tk()#initialise la fenêtre principale
home.title("Dictionaire")#titre de la fenêtre principale
home.geometry("1000x610")
imgFrame = PhotoImage(file="./frames/frame.png")#importation du frame de l'application
label1 = Label( home, image = imgFrame)
label1.place(x = 0, y = 0)#mettre à zero la place de l'image pour qu'il se positionne par défeaut
frame1 = Frame(home)#metre l'image dans la fenetre home
frame1.pack(pady = 20 )
home.resizable(0,0)#à 0,0 la taille de la fenetre ne peut plus etre modifié


def Traduction():
    messagebox.showinfo("TRADUCTION...", "Votre texte est en cours de traduction")
def Inversion():
    messagebox.showinfo("INVERSION...", "Votre traduction a bien été inversé")

texteTraduire = tk.StringVar()
texte_mot = ttk.Entry(home, textvariable=texteTraduire)
texte_mot.place(x=320, y=119, width=280, height=30)

#configuration du boutton Traduire
traduireButton = Button(home, text="Traduire", command=Traduction)
traduireButton.place(x=640, y=119, width=80, height=30)
traduireButton.configure(overrelief="flat")
traduireButton.configure(relief="flat")
traduireButton.configure(activebackground="white")
traduireButton.configure(background="#55bf76")
traduireButton.configure(foreground="white")
traduireButton.configure(cursor="hand2")
traduireButton.configure(font="-family {Poppins SemiBold} -size 10")
traduireButton.configure(borderwidth=0)

#configuration du boutton changer de langue
inversetraduireButton = Button(home, text="OK", command=Inversion)
inversetraduireButton.place(x=593, y=452, width=40, height=30)
inversetraduireButton.configure(overrelief="flat")
inversetraduireButton.configure(relief="flat")
inversetraduireButton.configure(activebackground="white")
inversetraduireButton.configure(background="#55bf76")
inversetraduireButton.configure(foreground="white")
inversetraduireButton.configure(cursor="hand2")
inversetraduireButton.configure(font="-family {Poppins SemiBold} -size 10")
inversetraduireButton.configure(borderwidth=0)

home.mainloop()
