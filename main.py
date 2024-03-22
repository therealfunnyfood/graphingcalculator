import tkinter as tk
import keyboard
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from graph import graphit
window = tk.Tk()
print("Press G to switch between graph and calculator mode.")
class click:
    def __init__(self):
        self.frame1 = tk.Frame(master = window, width = 400, height = 250)
        self.frame1.pack(side=tk.TOP)
        self.frame = tk.Frame(master = window, width = 400, height= 600)
        self.frame.pack(side=tk.BOTTOM)
        self.b = ""
        self.e = []
        self.secondnum = False
        self.fnl = []
        self.snl = []
        self.op = ""
        self.fn = 0
        self.fnb = ""
        self.sn = 0
        self.snb = ""
        self.out = 0.0
        self.done = 0.0
        self.previous = 0
        self.labelf1 = tk.Label(master= self.frame1,text = str(self.done), height= 3)
        self.labelf1.pack(fill=tk.BOTH)
        self.going = ""
        self.next = False
        self.there = False
        self.lbl = tk.Label(master = window, text = "f(x) =")
        self.txtbx = tk.Entry(master = window)
        self.graphbutton = tk.Button(master = window, text = "graph", command= lambda: self.gonow())
    def update(self, output):
        if output == "+-":
            if self.next == True:
                self.going = ""
                self.next = False
            if len(self.going) == 0:
                self.going += "-"
            else:
                goinglist = []
                for i in self.going:
                    goinglist.append(i)
                if goinglist[0] == "-":
                    goinglist.remove("-")
                else:
                    goinglist.insert(0,"-")
                self.going = ""
                for i in goinglist:
                    self.going += i
        elif output == "+" or output == "-" or output == "x" or output == "/":
            self.next = True
        elif self.next == True:
            self.going = ""
            self.going += output
            self.next = False
        else:
            self.going += output
        window.update_idletasks()
        self.labelf1.destroy()
        self.labelf1 = tk.Label(master= self.frame1,text = str(self.going), height= 3)
        self.labelf1.pack(fill=tk.BOTH)
    def solve(self):
        for value in range(len(self.e)):
            if self.e[value] != "+" and self.e[value] != "-" and self.e[value] != "x" and self.e[value] != "/" and self.e[value] != "f" and self.e[value] != "clear" and self.e[value] != "+-":
                if self.secondnum == False:
                    self.fnl.append(self.e[value])
                    print(self.fnl, "f")
                if self.secondnum == True:
                    self.snl.append(self.e[value])
                    print(self.snl, "s")
            else:
                if value == 0:
                    if self.e[value] != "f" and self.e[value] != "clear":
                        self.fnl.append(str(self.previous))
                match self.e[value]:
                    case "+":
                        self.op = "a"
                    case "-":
                        self.op = "s"
                    case "x":
                        self.op = "m"
                    case "/":
                        self.op = "d"
                    case "f":
                        continue
                    case "clear":
                        self.clear()
                        continue
                    case "+-":
                        if self.secondnum == False:
                            if self.fnl[0] == "-":
                                self.fnl.remove("-")
                            else:
                                self.fnl.insert(0,"-")
                        if self.secondnum == True:
                            if len(self.snl) == 0:
                                self.snl.append("-")
                            elif self.snl[0] == "-":
                                self.snl.remove("-")
                            else:
                                self.snl.insert(0,"-")
                print(self.op)
                self.secondnum = True
            if value == len(self.e)-1:
                for i in self.fnl:
                    self.fnb += i
                    print(self.fnb)
                for i in self.snl:
                    self.snb += i
                    print(self.snb)
                self.fn = float(self.fnb)
                print(self.fn)
                self.sn = float(self.snb)
                print(self.sn)
                match self.op:
                    case "a":
                        self.out = self.fn + self.sn
                    case "s":
                        self.out = self.fn - self.sn
                    case "m":
                        self.out = self.fn * self.sn
                    case "d":
                        self.out = self.fn / self.sn
                print(self.out)
        return self.out
    def clear(self):
        self.b = ""
        self.e = []
        self.secondnum = False
        self.fnl = []
        self.snl = []
        self.op = ""
        self.fn = 0
        self.fnb = ""
        self.sn = 0
        self.snb = ""
        self.out = 0.0
        self.going = ""
    def handle_click(self, bp: str):
        if self.there == False:
            self.b = bp
            print(self.b)
            print(self.e)
            match self.b:
                case "1":
                    self.e.append(self.b)
                    self.update(self.b)
                case "2":
                    self.e.append(self.b)
                    self.update(self.b)
                case "3":
                    self.e.append(self.b)
                    self.update(self.b)
                case "+":
                    self.e.append(self.b)
                    self.update(self.b)
                case "4":
                    self.e.append(self.b)
                    self.update(self.b)
                case "5":
                    self.e.append(self.b)
                    self.update(self.b)
                case "6":
                    self.e.append(self.b)
                    self.update(self.b)
                case "-":
                    self.e.append(self.b)
                    self.update(self.b)
                case "7":
                    self.e.append(self.b)
                    self.update(self.b)
                case "8":
                    self.e.append(self.b)
                    self.update(self.b)
                case "9":
                    self.e.append(self.b)
                    self.update(self.b)
                case "x":
                    self.e.append(self.b)
                    self.update(self.b)
                case "+-":
                    self.e.append(self.b)
                    self.update(self.b)
                case "0":
                    self.e.append(self.b)
                    self.update(self.b)
                case ".":
                    self.e.append(self.b)
                    self.update(self.b)
                case "/":
                    self.e.append(self.b)
                    self.update(self.b)
                case "f":
                    self.e.append(self.b)
                case "clear":
                    self.clear()
                    window.update_idletasks()
                    self.labelf1.destroy()
                    self.labelf1 = tk.Label(master= self.frame1,text = str(self.b), height= 3)
                    self.labelf1.pack(fill=tk.BOTH)
                case "=":
                    self.done = self.solve()
                    self.previous = self.done
                    window.update_idletasks()
                    self.clear()
                    print(self.done)
                    self.labelf1.destroy()
                    self.labelf1 = tk.Label(master= self.frame1,text = str(self.done), height= 3)
                    self.labelf1.pack(fill=tk.BOTH)
    def gonow(self):
        val = self.txtbx.get()
        graphit(val)
    def graphtime(self):
        self.frame.pack_forget()
        self.frame1.pack_forget()
        
        
        if self.there == True:
            self.lbl.pack_forget()
            self.txtbx.pack_forget()
            self.graphbutton.pack_forget()
            self.lbl.pack_forget()
            self.txtbx.pack_forget()
            self.graphbutton.pack_forget()
            self.frame.pack()
            self.frame1.pack(side=tk.TOP)
            self.frame.pack(side=tk.BOTTOM)
            self.there = False
        else:
            self.there = True
            self.lbl.pack()
            self.txtbx.pack()
            self.graphbutton.pack()

Click = click()

keyboard.on_press_key("1",lambda _: Click.handle_click("1"))
keyboard.on_press_key("2",lambda _:Click.handle_click("2"))
keyboard.on_press_key("3",lambda _:Click.handle_click("3"))
keyboard.on_press_key("+",lambda _:Click.handle_click("+"))
keyboard.on_press_key("4",lambda _:Click.handle_click("4"))
keyboard.on_press_key("5",lambda _:Click.handle_click("5"))
keyboard.on_press_key("6",lambda _:Click.handle_click("6"))
keyboard.on_press_key("-",lambda _:Click.handle_click("-"))
keyboard.on_press_key("7",lambda _:Click.handle_click("7"))
keyboard.on_press_key("8",lambda _:Click.handle_click("8"))
keyboard.on_press_key("9",lambda _:Click.handle_click("9"))
keyboard.on_press_key("*",lambda _:Click.handle_click("x"))
keyboard.on_press_key("n",lambda _:Click.handle_click("+-"))
keyboard.on_press_key("0",lambda _:Click.handle_click("0"))
keyboard.on_press_key("decimal",lambda _:Click.handle_click("."))
keyboard.on_press_key("/",lambda _:Click.handle_click("/"))
keyboard.on_press_key("f",lambda _:Click.handle_click("f"))
keyboard.on_press_key("c",lambda _:Click.handle_click("clear"))
keyboard.on_press_key("enter",lambda _:Click.handle_click("="))
keyboard.on_press_key("g",lambda _:Click.graphtime())

button1 = tk.Button(master= Click.frame, text = "1", command= lambda t = "1": Click.handle_click(t))
button1.grid(row=0, column=0)
button2 = tk.Button(master= Click.frame, text = "2", command= lambda t = "2": Click.handle_click(t))
button2.grid(row=0, column=1)
button3 = tk.Button(master= Click.frame, text = "3", command= lambda t = "3": Click.handle_click(t))
button3.grid(row=0, column=2)
button4 = tk.Button(master= Click.frame, text = "+", command= lambda t = "+": Click.handle_click(t))
button4.grid(row=0, column=3)
button5 = tk.Button(master= Click.frame, text = "4", command= lambda t = "4": Click.handle_click(t))
button5.grid(row=1, column=0)
button6 = tk.Button(master= Click.frame, text = "5", command= lambda t = "5": Click.handle_click(t))
button6.grid(row=1, column=1)
button7 = tk.Button(master= Click.frame, text = "6", command= lambda t = "6": Click.handle_click(t))
button7.grid(row=1, column=2)
button8 = tk.Button(master= Click.frame, text = "-", command= lambda t = "-": Click.handle_click(t))
button8.grid(row=1, column=3)
button9 = tk.Button(master= Click.frame, text = "7", command= lambda t = "7": Click.handle_click(t))
button9.grid(row=2, column=0)
button10 = tk.Button(master= Click.frame, text = "8", command= lambda t = "8": Click.handle_click(t))
button10.grid(row=2, column=1)
button11 = tk.Button(master= Click.frame, text = "9", command= lambda t = "9": Click.handle_click(t))
button11.grid(row=2, column=2)
button12 = tk.Button(master= Click.frame, text = "x", command= lambda t = "x": Click.handle_click(t))
button12.grid(row=2, column=3)
button13 = tk.Button(master= Click.frame, text = "+-", command= lambda t = "+-": Click.handle_click(t))
button13.grid(row=3, column=0)
button14 = tk.Button(master= Click.frame, text = "0", command= lambda t = "0": Click.handle_click(t))
button14.grid(row=3, column=1)
button15 = tk.Button(master= Click.frame, text = ".", command= lambda t = ".": Click.handle_click(t))
button15.grid(row=3, column=2)
button16 = tk.Button(master= Click.frame, text = "/", command= lambda t = "/": Click.handle_click(t))
button16.grid(row=3, column=3)
button17 = tk.Button(master= Click.frame, text = "f", command= lambda t = "f": Click.handle_click(t))
button17.grid(row=4, column=0)
button18 = tk.Button(master= Click.frame, text = "clear", command= lambda t = "clear": Click.handle_click(t))
button18.grid(row=4, column=1)
button19 = tk.Button(master= Click.frame, text = "=", command= lambda t = "=": Click.handle_click(t))
button19.grid(row=4, column=2)

window.mainloop()
