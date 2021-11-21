from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# command installation googletrans(mila connection internet tout au long de l'application):
# pip install googletrans==4.0.0-rc1

from googletrans import Translator


# le fonction qui permet d'utiliser le mode offline
def traductionOffline(event):
##offline
##open donnees.txt
    file = open("frames/dictionnaire.txt")
    datas = file.readlines()
    for data in datas:
        dataList = data.split(' : ')
        french = dataList[0]
        english = str(dataList[1]).split('\n')[0]


        if status.get() == 1:
        ## translation in french
            if inputString.get().lower() in english.lower():
                result['text'] = french.lower()
                return True


        elif status.get() == 0:
        ## translation in english
            if inputString.get().lower() in french.lower():
                result["text"] = english.lower()
                return True

    file.close()

# espace de definition de fonction
def traductionOnline(event):
    translator = Translator()
    if status.get() == 1:
        # translation in french
        resultat = translator.translate(inputString.get(), src="en", dest="fr")

    if resultat:
        result['text'] = resultat.text

    elif status.get() == 0:
        # translation in english
        resultat = translator.translate(inputString.get(), src="fr", dest="en")
        if resultat:
            result['text'] = resultat.text


def radioBouton(master, text, variable, value):
    new = Radiobutton(master,
                      text=text,
                      variable=variable,
                      value=value,
                      activebackground="#252525",
                      background="#24242c",
                      foreground="gray",
                      activeforeground="gray",
                      highlightthickness=0,
                      borderwidth=0,
                      height=2
                      )
    return new





# fonction qui inverse la langue de traduction
def inversion():
    # messagebox.showinfo("INVERSION...", "Votre traduction a bien été inversé")
    if status.get() == 0:
        status.set(1)
    else:
        status.set(0)
def message():
    messagebox.showinfo("INVERSION...", "Votre traduction a bien été inversé")


# fonction qui inverse l'Etat de la traduction (Offline - Online)
def Line(event):
    if tradStat.get() == 0:
        traductionOffline
    else:
        traductionOnline()


# mettre les boutton en fonction pour eviter D.R.Y
def bouton(text, command=None):
    new = Button(
        text=text,
        overrelief="flat",
        relief="flat",
        activebackground="#55bf76",
        background="#55bf76",
        foreground="white",
        cursor="hand2",
        font="-family {Poppins SemiBold} -size 10",
        borderwidth=0,
        command=command,
        highlightthickness=0,
    )
    return new


# initialise la fenêtre principale
home = Tk()

# titre de la fenêtre principale
home.title("Dictionaire")
home.geometry("1000x610")
# rendre la fenetre non redimensionnable
home.resizable(0, 0)

# declaration des variables
inputString = StringVar()
status = IntVar()
tradStat = IntVar()

# importation du frame de l'application
imgFrame = PhotoImage(file="frames/frame.png")

# metre l'image dans la fenetre home
label1 = Label(home, image=imgFrame)
label1.place(x=0, y=0)

frame1 = Frame(home)
frame1.pack(pady=20)

texte_mot = ttk.Entry(home, textvariable=inputString)
texte_mot.bind('<Return>', traductionOffline)
texte_mot.place(x=320, y=119, width=280, height=30)

# configuration du boutton Traduire
traduireButton = bouton("Traduire", message)
traduireButton.bind('<Button-1>', traductionOffline)
traduireButton.place(x=640, y=119, width=80, height=30)

statusFrame = Frame(home,
                    background="#55bf76",
                    highlightthickness=0,
                    borderwidth=0
                    )
statusFrame.place(x=300, y=165)


# enfants de statusFrame
toFrench = radioBouton(statusFrame, "Français", status, 1)
toFrench.grid(row=0, column=0)

toEnglish = radioBouton(statusFrame, "Anglais", status, 0)
toEnglish.grid(row=0, column=1)

TradStatus = Frame(home,
                    background="#24242c",
                    highlightthickness=0,
                    borderwidth=0
                    )
TradStatus.place(x=65, y=40)

toOffline = radioBouton(TradStatus, "Offline", tradStat, 0)
toOffline.grid(row=1, column=1)

toOnline = radioBouton(TradStatus, "Online", tradStat, 1)
toOnline.grid(row=0, column=1)

# configuration du boutton changer de langue
inversetraduireButton = bouton("OK", inversion)
inversetraduireButton.place(x=593, y=452, width=40, height=30)

# affichage du texte une fois qu'elle a été traduit
result = Label(home,
               bg="#b0e279",
               width=50,
               height=9,
               fg="#000"
               )
result.place(x=317, y=250)

home.mainloop()


