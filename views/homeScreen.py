from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# espace de definition de fonction

def translate(event):
    # open donnees.txt
    file = open("donnees.txt")
    datas = file.readlines()
    for data in datas:
        dataList = data.split('=')
        english = dataList[0]
        french = str(dataList[1]).split('\n')[0] 
    
    
        if status.get() == 1:
            # translation in english
            if inputString.get() in french:
                result['text'] = english
                return True
            
            

        elif status.get() == 0:
            # translation in french
            if inputString.get() in english:
                result["text"] = french      
                return True      
    
    file.close()

def radioBouton(master, text, variable, value):
    new = Radiobutton(master, 
                      text=text,
                      variable=variable,
                      value=value,
                      activebackground="#252525",
                      background="#252525",
                      foreground="grey",
                      activeforeground="grey",
                      highlightthickness=0,
                      borderwidth=0,
                      height=2
                    )
    return new


def traduction():
    #messagebox.showinfo("TRADUCTION...", "Votre texte est en cours de traduction")
    pass

def inversion():
    #messagebox.showinfo("INVERSION...", "Votre traduction a bien été inversé")
    if status.get() == 0:
        status.set(1)
    else:
        status.set(0)

def bouton(text, command=None):
    new = Button(
            text=text,
            overrelief="flat",
            relief="flat",
            activebackground= "#55bf76",
            background="#55bf76",
            foreground="white",
            cursor="hand2",
            font="-family {Poppins SemiBold} -size 10",
            borderwidth= 0,
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
home.resizable(0,0)
 
 # declaration des variables
inputString = StringVar()
status = IntVar()
inputString = StringVar()

#importation du frame de l'application
imgFrame = PhotoImage(file="frames/frame.png")

# metre l'image dans la fenetre home
label1 = Label( home, image = imgFrame)
label1.place(x = 0, y = 0)

frame1 = Frame(home)
frame1.pack(pady = 20)

texte_mot = ttk.Entry(home, textvariable=inputString)
texte_mot.bind('<Return>', translate)
texte_mot.place(x=320, y=119, width=280, height=30)

#configuration du boutton Traduire
traduireButton = bouton("Traduire", traduction)
traduireButton.bind('<Button-1>', translate)
traduireButton.place(x=640, y=119, width=80, height=30)

statusFrame = Frame(home, 
                    background="#55bf76", 
                    highlightthickness=0,
                    borderwidth=0
                    )
statusFrame.place(x=300, y=165)

# enfants de statusFrame
toFrench = radioBouton(statusFrame, "Français", status, 0)
toFrench.grid(row=0, column=0)

toEnglish = radioBouton(statusFrame, "Anglais", status, 1)
toEnglish.grid(row=0, column=1)


#configuration du boutton changer de langue
inversetraduireButton = bouton("OK", inversion)
inversetraduireButton.place(x=593, y=452, width=40, height=30)

result = Label(home, 
               bg="white", 
               width=50, 
               height=10
               )
result.place(x=317, y=250)

home.mainloop()
