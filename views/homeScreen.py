from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# function definitions zone

def Traduction():
    messagebox.showinfo("TRADUCTION...", "Votre texte est en cours de traduction")
def Inversion():
    messagebox.showinfo("INVERSION...", "Votre traduction a bien été inversé")


def bouton(text, command=None):
    new = Button(
            text=text,
            overrelief="flat",
            relief="flat",
            activebackground= "white",
            background="#55bf76",
            foreground="white",
            cursor="hand2",
            font="-family {Poppins SemiBold} -size 10",
            borderwidth= 0,
            command=command
            )
    return new


home = Tk()#initialise la fenêtre principale
home.title("Dictionaire")#titre de la fenêtre principale
home.geometry("1000x610")
imgFrame = PhotoImage(file="frames/frame.png") #importation du frame de l'application
label1 = Label( home, image = imgFrame)
label1.place(x = 0, y = 0)#mettre à zero la place de l'image pour qu'il se positionne par défeaut
frame1 = Frame(home)#metre l'image dans la fenetre home
frame1.pack(pady = 20 )
home.resizable(0,0)#à 0,0 la taille de la fenetre ne peut plus etre modifié



texteTraduire = StringVar()
texte_mot = ttk.Entry(home, textvariable=texteTraduire)
texte_mot.place(x=320, y=119, width=280, height=30)

#configuration du boutton Traduire
traduireButton = bouton("Traduire", Traduction)
traduireButton.place(x=640, y=119, width=80, height=30)

#configuration du boutton changer de langue
inversetraduireButton = bouton("OK", Inversion)
inversetraduireButton.place(x=593, y=452, width=40, height=30)


home.mainloop()
