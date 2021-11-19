from tkinter import *

## FUNCTIONS


def translate():
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
                print(result['text'])
            

        elif status.get() == 0:
            # translation in french
            if inputString.get() in english:
                result["text"] = french            
    
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
result = Label(resultFrame, text="anglais", bg="white", width=50, height=10)
result.pack()

window.mainloop()