from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# function definitions zone



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

def Traduction():
    messagebox.showinfo("TRADUCTION...", "Votre texte est en cours de traduction")
def Inversion():
    messagebox.showinfo("INVERSION...", "Votre traduction a bien été inversé")


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



home = Tk()#initialise la fenêtre principale
home.title("Dictionaire")#titre de la fenêtre principale
home.geometry("1000x610")
inputString = StringVar()
status = IntVar()
imgFrame = PhotoImage(file="frames/frame.png") #importation du frame de l'application
label1 = Label( home, image = imgFrame)
label1.place(x = 0, y = 0)#mettre à zero la place de l'image pour qu'il se positionne par défeaut
frame1 = Frame(home)#metre l'image dans la fenetre home
frame1.pack(pady = 20 )
home.resizable(0,0)#à 0,0 la taille de la fenetre ne peut plus etre modifié

inputString = StringVar()
texte_mot = ttk.Entry(home, textvariable=inputString)
texte_mot.place(x=320, y=119, width=280, height=30)

#configuration du boutton Traduire
traduireButton = bouton("Traduire", Traduction)
traduireButton.bind('<Button-1>', translate)
traduireButton.place(x=640, y=119, width=80, height=30)

statusFrame = Label(home, background="#55bf76", highlightthickness=0, borderwidth=0)
toFrench = Radiobutton(statusFrame,
                       text="Français",
                       value=0,
                       variable=status,
                       activebackground="#55bf76",
                       background="#55bf76",
                       activeforeground="black",
                       highlightthickness=0,
                       borderwidth=0,
                       height=2
                       )
toFrench.grid(row=0, column=0)

toEnglish = Radiobutton(statusFrame,
                        text="Anglais",
                        value=1,
                        variable=status,
                        activebackground="#55bf76",
                        background="#55bf76",
                        activeforeground="black",
                        highlightthickness=0, 
                        borderwidth=0,
                        height=2
                       )

toEnglish.grid(row=0, column=1)

statusFrame.place(x=300, y=165)



#configuration du boutton changer de langue
inversetraduireButton = bouton("OK", Inversion)
inversetraduireButton.place(x=593, y=452, width=40, height=30)

result = Label(home, bg="white", width=50, height=10)
result.place(x=317, y=250)

home.mainloop()
