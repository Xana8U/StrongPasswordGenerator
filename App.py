from tkinter import *
from tkinter import ttk
import random
import pyautogui as pyag
import re
import time

# global generation progress
prog = 0
seed = ""

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master

        self.run_window()

    def run_window(self):
        global prog
        self.master.title("Password Generator")
        self.pack(fill=BOTH, expand=1)

        self.showtext()
        self.tickboxes()
        self.pwlen()
        self.seedbuttn()
        self.progressbar()
        self.passbutt()

# GUI TEXT
    def showtext(self):
        welcome_text = Label(self, text="\n Welcome to Strong Password Generator by Markus Kaleton \n"
                                        "----------------------------------------------------------------\n\n"
                                        "Please select password properties below\n", font=("Arial", 9, "bold"))
        welcome_text.pack()

# Text for password lenght area
        lentext = Label(self, text="Length:")
        lentext.pack()
        lentext.place(x=100, y=100)
        lenrecomm = Label(self, text="(6-24 recommended for the best compatibility)*", font=('Arial', 7, 'italic'))
        lenrecomm.pack()
        lenrecomm.place(x=225, y=102)

# Text for Seed generator
        seedtext = Label(self, text="After pressing generate, move your mouse randomly around your screen.\n"
                                    "Seed for the password will be ready after the process meter is full!")
        seedtext.pack()
        seedtext.place(x=3, y=200)

# Selections for lower, upper, digits, specials, underlines, spaces
    def tickboxes(self):
        lower = Checkbutton(self, text="Lowecase (a-z)")
        lower.pack()
        lower.place(x=20, y=140)
        uppercase = Checkbutton(self, text="Uppercase (A-Z)")
        uppercase.pack()
        uppercase.place(x=180, y=140)
        digits = Checkbutton(self, text="Digits (0-9)")
        digits.pack()
        digits.place(x=340, y=140)
        lower = Checkbutton(self, text="Specials (€$%!?..)")
        lower.pack()
        lower.place(x=20, y=165)
        uppercase = Checkbutton(self, text="Underlines (_)")
        uppercase.pack()
        uppercase.place(x=180, y=165)
        digits = Checkbutton(self, text="Spaces ( )")
        digits.pack()
        digits.place(x=340, y=165)

# Length selector
    def pwlen(self):
        length = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
                  22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

        _variable = IntVar(self)
        _variable.set(length[0])
        dropdown = OptionMenu(self, _variable, *length)
        dropdown.pack()
        dropdown.place(x=157, y=95)

# seed generator and process, buttons/meter
    def seedbuttn(self):
        global prog
        generate = Button(self, text="Generate\n Seed", command=self.seed)
        generate.pack()
        generate.place(x=140, y=400)

    def progressbar(self):
        global prog
        progress = ttk.Progressbar(self, orient=HORIZONTAL, length=300, mode="determinate", maximum=500, value=prog)
        progress.pack()
        progress.place(x=100, y=350)

# seed generator
    def seed(self):
        seedbase = []
        lastcoord = list()
        global prog, seed
        while len(seedbase) < 500:
            pos = list(pyag.position())
            if [pos] == lastcoord[-1::1]:
                continue
            else:
                lastcoord = list()
                lastcoord.append(list(pyag.position()))
                seedbase.append(list(pyag.position()))
                print(seedbase)
                print(len(seedbase))
                time.sleep(0.02)
                prog += 1
        seedstr = str(seedbase)
        seed = re.sub('[\(\)\[\]\,\ ]', '', seedstr)
        print(seed)
        self.passbutt()

# seed calculations and pass generation
    def passbutt(self):
        global prog
        generate = Button(self, text="Generate\n Password", state='disabled', command=self.password)
        generate.pack()
        generate.place(x=280, y=400)
        if prog >= 499:
            generate.config(state='normal')

    def password(self):
        global seed
        random.seed(seed)


base = Tk()
base.geometry("500x500")
base.resizable(False, False)

app = App(base)

base.mainloop()
