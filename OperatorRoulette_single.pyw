from tkinter import *
from random import randint
import tkinter.simpledialog as simpledialog

tkWindow = Tk()
tkWindow.title('Operator Roulette')
tkWindow.geometry('180x140')

labelName_operator = Label(master=tkWindow, background='green')
labelName_operator.place(x=20, y=100, width=140, height=20)

class Buttons():
    def __init__(self):
        self.attack = 0
        self.defense = 0
        self.num = 0
    
    def Attack(self):
        self.attack=1
        self.defense=0
        
    def Defense(self):
        self.attack=0
        self.defense=1
        
    def GO(self):
        if self.attack==1 and self.defense==0:
            self.num=randint(1,17)
        elif self.defense==1 and self.attack==0:
            self.num=randint(18,35)
        else:
            labelName_operator.config(text="--ERROR--")
        self.Operator()

    def Operator(self):
        if self.num==1:
            labelName_operator.config(text="Rekrut")
        elif self.num==2:
            labelName_operator.config(text="Sledge")
        elif self.num==3:
            labelName_operator.config(text="Thatcher")
        elif self.num==4:
            labelName_operator.config(text="Ash")
        elif self.num==5:
            labelName_operator.config(text="Thermite")
        elif self.num==6:
            labelName_operator.config(text="Twitch")
        elif self.num==7:
            labelName_operator.config(text="Montagne")
        elif self.num==8:
            labelName_operator.config(text="Glaz")
        elif self.num==9:
            labelName_operator.config(text="Fuze")
        elif self.num==10:
            labelName_operator.config(text="Blitz")
        elif self.num==11:
            labelName_operator.config(text="IQ")
        elif self.num==12:
            labelName_operator.config(text="Buck")
        elif self.num==13:
            labelName_operator.config(text="Blackbeard")
        elif self.num==14:
            labelName_operator.config(text="Capitao")
        elif self.num==15:
            labelName_operator.config(text="Hibana")
        elif self.num==16:
            labelName_operator.config(text="Jackal")
        elif self.num==17:
            labelName_operator.config(text="Ying")
        elif self.num==18:
            labelName_operator.config(text="Rekrut")
        elif self.num==19:
            labelName_operator.config(text="Smoke")
        elif self.num==20:
            labelName_operator.config(text="Mute")
        elif self.num==21:
            labelName_operator.config(text="Castle")
        elif self.num==22:
            labelName_operator.config(text="Pulse")
        elif self.num==23:
            labelName_operator.config(text="Doc")
        elif self.num==24:
            labelName_operator.config(text="Rook")
        elif self.num==25:
            labelName_operator.config(text="Kapkan")
        elif self.num==26:
            labelName_operator.config(text="Lord Tachanka")
        elif self.num==27:
            labelName_operator.config(text="Jäger")
        elif self.num==28:
            labelName_operator.config(text="Bandit")
        elif self.num==29:
            labelName_operator.config(text="Frost")
        elif self.num==30:
            labelName_operator.config(text="Valkyrie")
        elif self.num==31:
            labelName_operator.config(text="Echo")
        elif self.num==32:
            labelName_operator.config(text="Caveira")
        elif self.num==33:
            labelName_operator.config(text="Mira")
        elif self.num==34:
            labelName_operator.config(text="Lesion")
        elif self.num==35:
            labelName_operator.config(text="Ela")
        else:
            labelName_operator.config(text="--ERROR--")

b=Buttons()

buttonATT = Button(master=tkWindow, text="Attack", command=b.Attack)
buttonATT.place(x=20, y=20, width=60, height=20)

buttonDEF = Button(master=tkWindow, text="Defense", command=b.Defense)
buttonDEF.place(x=100, y=20, width=60, height=20)

buttonGO = Button(master=tkWindow, text="Go!", command=b.GO)
buttonGO.place(x=60, y=60, width=60, height=20)

tkWindow.mainloop()
