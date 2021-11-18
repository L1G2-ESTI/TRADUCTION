from tkinter import *

## FUNCTIONS


def translate():
    # open donnees.txt

    file = open("donnees.txt")
    datas = file.readlines()
    
    if status.get() == 1:
        # translation in english
        for data in datas:
            dataList = data.split('=') 
            english = dataList[0]
            french = dataList[1]
            if inputString.get() == french:
                result["text"] = english
            else:
                result["text"] = "non trouvé"


    else:
        # translation in french
        for data in datas:   
            dataList = data.split('=') 
            english = dataList[0]
            french = dataList[1]
            if inputString.get() == english:
                result["text"] = french
            else:
                result["text"] = "non trouvé"
    
    file.close()


window = Tk()
window.geometry("400x375")
window.resizable("false","false") # unable resizable

# Entry with Button submiting translate
inputFrame = Frame(window)
inputFrame.place(x=125,y=50)

inputString = StringVar()

input = Entry(inputFrame, textvariable=inputString, bg="white")
input.pack(ipady=5)

submit = Button(inputFrame, text="traduire", command=translate)
submit.pack(pady=10)


choiceFrame = Frame(window)
choiceFrame.place(x=120, y=150)

status = IntVar()

# Radiobutton 
toFrench = Radiobutton(choiceFrame, text="Français", value=0, variable=status)
toFrench.grid(row=0, column=0)

toEnglish = Radiobutton(choiceFrame, text="Anglais",value=1, variable=status)
toEnglish.grid(row=0, column=1)


resultFrame = Frame(window)
resultFrame.place(x=0, y=200)
result = Label(resultFrame, bg="white", width=50, height=10)
result.pack()

window.mainloop()