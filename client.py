from random import choice, randint
from tkinter import *
import json


class Passwd():
    @classmethod
    def get_input(self):
        self.title = self.inp.get()
        acc = {str(self.title) : str(self.password)
            }

        with open("passwords.json") as outfile:
            file = json.load(outfile)
            temp = file['list']
            temp.append(acc)

        with open('passwords.json', 'w') as f:
            json.dump(file, f, indent=4)


    @classmethod
    def generate(self):
        widgets = window.winfo_children()
        widgets = widgets[2:]
        for widget in widgets:
            widget.destroy()

        self.password = ""
        self.chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+}{"
        self.big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.lenght = randint(13, 20)

        self.password += choice(self.big)
        for i in range(self.lenght):
            self.password += choice(self.chars)

        T = Text(background='grey', fg='purple', height=2, width=30)
        T.pack()
        T.insert(END, self.password)

        self.inp = Entry(background='#1af4df', width=40)
        self.inp.pack()

        apply = Button(text="Enter the title", command=Passwd.get_input, activebackground='#f4c11a',
                       activeforeground='black',)
        apply.pack()


    @classmethod
    def show(self):
        widgets = window.winfo_children()
        widgets = widgets[2:]
        for widget in widgets:
            widget.destroy()

        passwords = json.load(open("passwords.json"))['list']
        window.geometry("500x100")

        text = Text(bg="yellow")

        x = 100
        for i in passwords:
            window.geometry("500x"+str(x))
            text.insert(END, i)
            text.insert(END, '\n')
            x += 15

        text.pack()


if __name__ == '__main__':
    window = Tk()
    window.iconbitmap('icon.ico')
    window.title('Password Generator')
    window.geometry("275x170")
    window.config(background="grey")

    generate = Button(text="Generate new password", background='#9af41a',
                      fg='blue', activebackground='yellow', activeforeground='black',
                      command=Passwd.generate)

    showp = Button(text="Show passwords", background='purple',
                      fg='black', activebackground='red', activeforeground='blue',
                      command=Passwd.show)

    generate.pack()
    showp.pack()

    window.mainloop()