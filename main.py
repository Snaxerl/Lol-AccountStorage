from tkinter import *
from tkinter import messagebox
import tkinter.messagebox




objects = []
window = Tk()
window.withdraw()
window.title('LOL Accounts')

class popupWindow(object):

    loop = False
    attempts = 0

    def __init__(self, master):
        top = self.top = Toplevel(master)
        top.title('Input Password')
        top.geometry('{}x{}'.format(250, 100))
        top.resizable(width=False, height=False)
        self.l = Label(top, text=" Password: ", font=('Courier', 14), justify=CENTER)
        self.l.pack()
        self.e = Entry(top, show='*', width=30)
        self.e.pack(pady=7)
        self.b = Button(top, text='Submit', command=self.cleanup, font=('Courier', 14))
        self.b.pack()

    def cleanup(self):
        self.value = self.e.get()
        access = 'toor'

        if self.value == access:
            self.loop = True
            self.top.destroy()
            window.deiconify()
        else:
            self.attempts += 1
            if self.attempts == 5:
                window.quit()
            self.e .delete(0, 'end')
            messagebox.showerror('Incorrect Password', 'Incorrect password, attempts remaining: ' + str(5 - self.attempts))

class entity_add:

    def __init__(self, master, n, p, e):
        self.elo = p
        self.name = n
        self.info = e
        self.window = master

    def write(self):
        f = open('daten.txt', "a")
        n = self.name
        e = self.info
        p = self.elo

        encryptedN = ""
        encryptedE = ""
        encryptedP = ""
        for letter in n:
            if letter == ' ':
                encryptedN += ' '
            else:
                encryptedN += chr(ord(letter) + 5)

        for letter in e:
            if letter == ' ':
                encryptedE += ' '
            else:
                encryptedE += chr(ord(letter) + 5)

        for letter in p:
            if letter == ' ':
                encryptedP += ' '
            else:
                encryptedP += chr(ord(letter) + 5)

        f.write(encryptedN + ',' + encryptedE + ',' + encryptedP + ', \n')
        f.close()


class entity_display:

    def __init__(self, master, n, e, p, i):
        self.elo = p
        self.name = n
        self.info = e
        self.window = master
        self.i = i

        dencryptedN = ""
        dencryptedE = ""
        dencryptedP = ""
        for letter in self.name:
            if letter == ' ':
                dencryptedN += ' '
            else:
                dencryptedN += chr(ord(letter) - 5)

        for letter in self.info:
            if letter == ' ':
                dencryptedE += ' '
            else:
                dencryptedE += chr(ord(letter) - 5)

        for letter in self.elo:
            if letter == ' ':
                dencryptedP += ' '
            else:
                dencryptedP += chr(ord(letter) - 5)

        self.label_name = Label(self.window, text=dencryptedN, font=('Courier', 14))
        self.label_info = Label(self.window, text=dencryptedE, font=('Courier', 14))
        self.label_elo = Label(self.window, text=dencryptedP, font=('Courier', 14))
        self.deleteButton = Button(self.window, text='X', fg='red', command=self.delete)

    def display(self):
        self.label_name.grid(row=6 + self.i, sticky=W)
        self.label_info.grid(row=6 + self.i, column=1)
        self.label_elo.grid(row=6 + self.i, column=2, sticky=E)
        self.deleteButton.grid(row=6 + self.i, column=3, sticky=E)

    def delete(self):
        answer = tkinter.messagebox.askquestion('Delete', 'Are you sure you want to delete this entry?')

        if answer == 'yes':
            for i in objects:
                i.destroy()

            f = open('daten.txt', 'r')
            lines = f.readlines()
            f.close()

            f = open('daten.txt', "w")
            count = 0

            for line in lines:
                if count != self.i:
                    f.write(line)
                    count += 1

            f.close()
            readfile()

    def destroy(self):
        self.label_name.destroy()
        self.label_info.destroy()
        self.label_elo.destroy()
        self.deleteButton.destroy()





def onsubmit():
    m = info.get()
    p = elo.get()
    n = name.get()
    e = entity_add(window, n, p, m)
    e.write()
    name.delete(0, 'end')
    info.delete(0, 'end')
    elo.delete(0, 'end')
    messagebox.showinfo('Added Entity', 'Successfully Added, \n' + 'Name: ' + n + '\nInfo: ' + m + '\nElo: ' + p)
    readfile()


def clearfile():
    f = open('daten.txt', "w")
    f.close()


def readfile():
    f = open('daten.txt', 'r')
    count = 0

    for line in f:
        entityList = line.split(',')
        e = entity_display(window, entityList[0], entityList[1], entityList[2], count)
        objects.append(e)
        e.display()
        count += 1
    f.close()




m = popupWindow(window)

entity_label = Label(window, text='Add Entity', font=('Courier', 18))
name_label = Label(window, text='Name: ', font=('Courier', 14))
info_label = Label(window, text='Info: ', font=('Courier', 14))
elo_label = Label(window, text='Elo: ', font=('Courier', 14))
name = Entry(window, font=('Courier', 14))
info = Entry(window, font=('Courier', 14))
elo = Entry(window,  font=('Courier', 14))
submit = Button(window, text='Add Account', command=onsubmit, font=('Courier', 14))

entity_label.grid(columnspan=3, row=0)
name_label.grid(row=1, sticky=E, padx=3)
info_label.grid(row=2, sticky=E, padx=3)
elo_label.grid(row=3, sticky=E, padx=3)

name.grid(columnspan=3, row=1, column=1, padx=2, pady=2, sticky=W)
info.grid(columnspan=3, row=2, column=1, padx=2, pady=2, sticky=W)
elo.grid(columnspan=3, row=3, column=1, padx=2, pady=2, sticky=W)

submit.grid(columnspan=3, pady=4)

name_label2 = Label(window, text='Name: ', font=('Courier', 14))
info_label2 = Label(window, text='Info: ', font=('Courier', 14))
elo_label2 = Label(window, text='Elo: ', font=('Courier', 14))

name_label2.grid(row=5)
info_label2.grid(row=5, column=1)
elo_label2.grid(row=5, column=2)

readfile()

window.mainloop()
