from tkinter import *
from tkinter import ttk
import random
import pyautogui as pyag
import re
import time
import _thread
import string

# global generation progress
prog = 0
seed = ""

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        # Initialize progress bar
        self.progress = ttk.Progressbar(orient=HORIZONTAL, length=300, mode="determinate", maximum=500)
        self.progress.pack()
        self.progress.place(x=100, y=350)

        self.textbox = Text()
        self.textbox.pack()
        self.textbox.place(x=100, y=270, width=300, height=50)
        self.textbox.insert(END, "-[Password will appear here]-")
        self.textbox.config(state=DISABLED)


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

# place checkboxes around
    def tickboxes(self):
        # Initialize checkboxes
        self.lowercase = Checkbutton(self, text="Lowercase (a-z)", command=self.lowercase)
        self.uppercase = Checkbutton(self, text="Uppercase (A-Z)", command=self.uppercase)
        self.digits = Checkbutton(self, text="Digits (0-9)", command=self.digits)
        self.special = Checkbutton(self, text="Specials (€$%!?..)", command=self.special)
        self.underline = Checkbutton(self, text="Underlines (_)", command=self.underline)
        self.space = Checkbutton(self, text="Spaces ( )", command=self.space)
        self.lowercase.pack()
        self.lowercase.place(x=20, y=140)
        self.uppercase.pack()
        self.uppercase.place(x=180, y=140)
        self.digits.pack()
        self.digits.place(x=340, y=140)
        self.special.pack()
        self.special.place(x=20, y=165)
        self.underline.pack()
        self.underline.place(x=180, y=165)
        self.space.pack()
        self.space.place(x=340, y=165)

    # Get correct tick box off values
    def lowercase(self):
        if self.lowercase["offvalue"] == 1:
            self.lowercase["offvalue"] = 0
        else:
            self.lowercase["offvalue"] = 1

    def uppercase(self):
        if self.uppercase["offvalue"] == 1:
            self.uppercase["offvalue"] = 0
        else:
            self.uppercase["offvalue"] = 1

    def digits(self):
        if self.digits["offvalue"] == 1:
            self.digits["offvalue"] = 0
        else:
            self.digits["offvalue"] = 1

    def special(self):
        if self.special["offvalue"] == 1:
            self.special["offvalue"] = 0
        else:
            self.special["offvalue"] = 1

    def underline(self):
        if self.underline["offvalue"] == 1:
            self.underline["offvalue"] = 0
        else:
            self.underline["offvalue"] = 1

    def space(self):
        if self.space["offvalue"] == 1:
            self.space["offvalue"] = 0
        else:
            self.space["offvalue"] = 1


# Length selector
    def pwlen(self):
        length = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
                  22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

        self._variable = IntVar(self)
        self._variable.set(length[0])
        self.dropdown = OptionMenu(self, self._variable, *length)
        self.dropdown.pack()
        self.dropdown.place(x=157, y=95)

# seed generator button and allocating a new thread for the seed generation.
    def seedbuttn(self):
        global prog
        def startseed():
            _thread.start_new(self.seed, tuple())
        generate = Button(self, text="Generate\n Seed", command=startseed)
        generate.pack()
        generate.place(x=140, y=400)
# progress ba

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
                self.progress["value"] = prog
                time.sleep(0.02)
                prog += 1
        seedstr = str(seedbase)
        seed = re.sub('[\(\)\[\]\,\ ]', '', seedstr)
        self.passbutt()

# seed calculations and pass generation
    def passbutt(self):
        global prog
        generate = Button(self, text="Generate\n Password", state='disabled', command=self.password)
        generate.pack()
        generate.place(x=280, y=400)
        if prog >= 500:
            generate.config(state='normal')

    def password(self):
        global seed
        random.seed(seed)
        # lower, aupper, digit, special, underline, space, length:
        lower = self.lowercase["offvalue"]
        upper = self.uppercase["offvalue"]
        digit = self.digits["offvalue"]
        special = self.special["offvalue"]
        underline = self.underline["offvalue"]
        space = self.space["offvalue"]
        length = self._variable.get()

        # characters
        low = string.ascii_lowercase
        up = string.ascii_uppercase
        dig = string.digits
        spec = """!@#$€&´`¨^',.-|<>{}[]()"""
        under = "_"
        spac = " "

        #selections and password bank
        loopnum = 0
        selections = ""
        password = ""
        # Check all "tickbox" selections.
        for n in lower, upper, digit, special, underline, space:
            if loopnum == 0 and type(n) == int:  # if value is not set it will be "0" and set will be 1 (str/int)
                selections += low
                loopnum += 1
            elif loopnum == 1 and type(n) == int:
                selections += up
                loopnum += 1
            elif loopnum == 2 and type(n) == int:
                selections += dig
                loopnum += 1
            elif loopnum == 3 and type(n) == int:
                selections += spec
                loopnum += 1
            elif loopnum == 4 and type(n) == int:
                selections += under
                loopnum += 1
            elif loopnum == 5 and type(n) == int:
                selections += spac
            else:
                loopnum += 1

        # generate random password with selected properties and length
        for n in range(length):
            password += random.choice(selections)

        # Give user the password
        self.textbox.config(state=NORMAL)
        self.textbox.delete(1.0, END)
        self.textbox.insert(END, password)
        self.textbox.config(state=DISABLED)



base = Tk()
base.geometry("500x500")
base.resizable(False, False)

app = App(base)

base.mainloop()
