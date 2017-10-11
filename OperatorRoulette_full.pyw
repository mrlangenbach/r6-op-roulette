from tkinter import *
from random import randint
import tkinter.simpledialog as simpledialog

#Creates Window

tkWindow = Tk()
tkWindow.title('Operator Roulette')
tkWindow.geometry('220x220')

#Creates output labels

labelName_operator1 = Label(master=tkWindow, background='green')
labelName_operator1.place(x=20, y=100, width=80, height=20)

labelName_operator2 = Label(master=tkWindow, background='green')
labelName_operator2.place(x=120, y=100, width=80, height=20)

labelName_operator3 = Label(master=tkWindow, background='green')
labelName_operator3.place(x=20, y=140, width=80, height=20)

labelName_operator4 = Label(master=tkWindow, background='green')
labelName_operator4.place(x=120, y=140, width=80, height=20)

labelName_operator5 = Label(master=tkWindow, background='green')
labelName_operator5.place(x=60, y=180, width=80, height=20)

#Main class

class Buttons():
    def __init__(self):
        self.attack = 0
        self.defense = 0
        self.num = 0
        self.plynum = 0
        self.op1 = ""
        self.op2 = ""
        self.op3 = ""
        self.op4 = ""
        self.op5 = ""

#Buttons for number of players

    def Ply_1(self):
        self.plynum = 1

    def Ply_2(self):
        self.plynum = 2

    def Ply_3(self):
        self.plynum = 3

    def Ply_4(self):
        self.plynum = 4

    def Ply_5(self):
        self.plynum = 5

#Sets Attack or Defense mode
    
    def Attack(self):
        self.attack=1
        self.defense=0
        
    def Defense(self):
        self.attack=0
        self.defense=1

#Generates number for operator depending on mode
        
    def Generator(self):
        if self.attack==1 and self.defense==0:
            return randint(1,17)
        elif self.defense==1 and self.attack==0:
            return randint(18,35)
        else:
            return 0

#Assigns number to variables and checks for doubles

    def Go(self):
        self.op1=self.Generator()
        self.op2=self.Generator()
        while self.op1 == self.op2:
            self.op2=self.Generator()
        self.op3=self.Generator()
        while self.op1 == self.op3 or self.op2 == self.op3:
            self.op3=self.Generator()
        self.op4=self.Generator()
        while self.op1 == self.op4 or self.op2 == self.op4 or self.op3 == self.op4:
            self.op4=self.Generator()
        self.op5=self.Generator()
        while self.op1 == self.op5 or self.op2 == self.op5 or self.op3 == self.op5 or self.op4 == self.op5:
            self.op5=self.Generator()
        self.Output()

#Assigns operator to number and outputs them

    def Output(self):
        if self.plynum == 1:
            labelName_operator1.config(text=self.Operator(self.op1))
            labelName_operator2.config(text="")
            labelName_operator3.config(text="")
            labelName_operator4.config(text="")
            labelName_operator5.config(text="")
        elif self.plynum == 2:            
            labelName_operator1.config(text=self.Operator(self.op1))
            labelName_operator2.config(text=self.Operator(self.op2))
            labelName_operator3.config(text="")
            labelName_operator4.config(text="")
            labelName_operator5.config(text="")
        elif self.plynum == 3:
            labelName_operator1.config(text=self.Operator(self.op1))
            labelName_operator2.config(text=self.Operator(self.op2))
            labelName_operator3.config(text=self.Operator(self.op3))
            labelName_operator4.config(text="")
            labelName_operator5.config(text="")
        elif self.plynum == 4:
            labelName_operator1.config(text=self.Operator(self.op1))
            labelName_operator2.config(text=self.Operator(self.op2))
            labelName_operator3.config(text=self.Operator(self.op3))
            labelName_operator4.config(text=self.Operator(self.op4))
            labelName_operator5.config(text="")
        elif self.plynum == 5:
            labelName_operator1.config(text=self.Operator(self.op1))
            labelName_operator2.config(text=self.Operator(self.op2))
            labelName_operator3.config(text=self.Operator(self.op3))
            labelName_operator4.config(text=self.Operator(self.op4))
            labelName_operator5.config(text=self.Operator(self.op5))
        else:
            labelName_operator1.config(text="--ERROR--")
        

#List of operators

    def Operator(self, num):
        if num==1:
            return "Rekrut"
        elif num==2:
            return "Sledge"
        elif num==3:
            return "Thatcher"
        elif num==4:
            return "Ash"
        elif num==5:
            return "Thermite"
        elif num==6:
            return "Twitch"
        elif num==7:
            return "Montagne"
        elif num==8:
            return "Glaz"
        elif num==9:
            return "Fuze"
        elif num==10:
            return "Blitz"
        elif num==11:
            return "IQ"
        elif num==12:
            return "Buck"
        elif num==13:
            return "Blackbeard"
        elif num==14:
            return "Capitao"
        elif num==15:
            return "Hibana"
        elif num==16:
            return "Jackal"
        elif num==17:
            return "Ying"
        elif num==18:
            return "Rekrut"
        elif num==19:
            return "Smoke"
        elif num==20:
            return "Mute"
        elif num==21:
            return "Castle"
        elif num==22:
            return "Pulse"
        elif num==23:
            return "Doc"
        elif num==24:
            return "Rook"
        elif num==25:
            return "Kapkan"
        elif num==26:
            return "Lord Tachanka"
        elif num==27:
            return "Jäger"
        elif num==28:
            return "Bandit"
        elif num==29:
            return "Frost"
        elif num==30:
            return "Valkyrie"
        elif num==31:
            return "Echo"
        elif num==32:
            return "Caveira"
        elif num==33:
            return "Mira"
        elif num==34:
            return "Lesion"
        elif num==35:
            return "Ela"
        else:
            return "--ERROR--"

#Buttons for Number of Players, Mode and Execute

b=Buttons()

buttonPly_1 = Button(master=tkWindow, text="1", command=b.Ply_1)
buttonPly_1.place(x=20, y=20, width=20, height=20)

buttonPly_2 = Button(master=tkWindow, text="2", command=b.Ply_2)
buttonPly_2.place(x=60, y=20, width=20, height=20)

buttonPly_3 = Button(master=tkWindow, text="3", command=b.Ply_3)
buttonPly_3.place(x=100, y=20, width=20, height=20)

buttonPly_4 = Button(master=tkWindow, text="4", command=b.Ply_4)
buttonPly_4.place(x=140, y=20, width=20, height=20)

buttonPly_5 = Button(master=tkWindow, text="5", command=b.Ply_5)
buttonPly_5.place(x=180, y=20, width=20, height=20)

buttonATT = Button(master=tkWindow, text="Attack", command=b.Attack)
buttonATT.place(x=20, y=60, width=60, height=20)

buttonDEF = Button(master=tkWindow, text="Defense", command=b.Defense)
buttonDEF.place(x=140, y=60, width=60, height=20)

buttonGO = Button(master=tkWindow, text="Go", command=b.Go)
buttonGO.place(x=100, y=60, width=20, height=20)

tkWindow.mainloop()
