
from tkinter import *
from tkinter import ttk
import string
import re


class TestDrivenDevelopment:
    def funA(numList):
        if numList % 2 == 0:
            return "Even"
        else:
            return "Odd"

    def funB(strFunA):
        return strFunA.upper()[0:len(strFunA)-1][::-1]+str(strFunA[len(strFunA)-1])

    def funC(strFunB):
        if strFunB in string.digits:
            return strFunB
        else:
            return str((ord(strFunB)))

    def funD(strFunC):
        if int(strFunC) < 10:
            return strFunC
        else:
            return str((chr(int(strFunC))))

    def funE(strFunD):
        return (re.split("([0-9])", strFunD.lower()[0:len(strFunD)][-1::-1]))

    def funF(strFunE):
        return (re.findall('\d', strFunE))



def calculator(order):
    k, j = 0, 0
    convertStr = ""
    funA, funB, funC, funD, funE, funF = "", "", "", "", "", ""
    numList, resultFunA, resultFunB, resultFunC, resultFunD, resultFunE, resultFunF = list(
    ), list(), list(), list(), list(), list(), list()

    for k in range(len(order)):
        numList.append(int(order[k]))
        resultFunA.append(TestDrivenDevelopment.funA(
            numList[k]) + str(numList[k]))
        funA += resultFunA[k]

    for k in range(len(resultFunA)):
        resultFunB.append(TestDrivenDevelopment.funB(resultFunA[k]))
        funB += resultFunB[k]

    for k in range(len(numList)):
        for j in range(len(resultFunB[k])):
            resultFunC.append(TestDrivenDevelopment.funC(resultFunB[k][j]))
            funC += resultFunC[len(resultFunC)-1]

    for k in range(len(resultFunC)):
        resultFunD.append(TestDrivenDevelopment.funD(resultFunC[k]))
        funD += resultFunD[k]

    for k in resultFunD:
        convertStr += k
        resultFunE = (TestDrivenDevelopment.funE(convertStr))
        resultFunE.reverse()
    for k in range(len(resultFunE)):
        funE += resultFunE[k].capitalize()

    for k in resultFunE:
        convertStr += k
        resultFunF = (TestDrivenDevelopment.funF(convertStr))
    for k in range(len(numList)):
        funF += resultFunF[k]
    return funA, funB, funC, funD, funE, funF


class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text='Command')
        self.lbl2 = Label(win, text='Funtion A :')
        self.lbl3 = Label(win, text='Funtion B :')
        self.lbl4 = Label(win, text='Funtion C :')
        self.lbl5 = Label(win, text='Funtion D :')
        self.lbl6 = Label(win, text='Funtion E :')
        self.lbl7 = Label(win, text='Funtion F :')
        self.t1 = Entry(width=80)
        self.t2 = Entry(width=80)
        self.t3 = Entry(width=80)
        self.t4 = Entry(width=80)
        self.t5 = Entry(width=80)
        self.t6 = Entry(width=80)
        self.t7 = Entry(width=80)
        self.btn1 = Button(win, text='Generate')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.b1 = Button(win, text='Generate', command=self.generate)
        self.b1.place(x=200, y=100,)

        self.lbl2.place(x=100, y=150)
        self.t2.place(x=200, y=150)

        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)

        self.lbl4.place(x=100, y=250)
        self.t4.place(x=200, y=250)

        self.lbl5.place(x=100, y=300)
        self.t5.place(x=200, y=300)

        self.lbl6.place(x=100, y=350)
        self.t6.place(x=200, y=350)

        self.lbl7.place(x=100, y=400)
        self.t7.place(x=200, y=400)

    def generate(self):
        self.t2.delete(0, 'end')
        command = self.t1.get()
        funA, funB, funC, funD, funE, funF = calculator(command)
        self.t2.insert(END, str(funA))

        self.t3.delete(0, 'end')
        self.t3.insert(END, str(funB))

        self.t4.delete(0, 'end')
        self.t4.insert(END, str(funC))

        self.t5.delete(0, 'end')
        self.t5.insert(END, str(funD))

        self.t6.delete(0, 'end')
        self.t6.insert(END, str(funE))

        self.t7.delete(0, 'end')
        self.t7.insert(END, str(funF))


window = Tk()
mywin = MyWindow(window)
window.title('Test Driven Development')
window.geometry("800x500")
window.mainloop()
