'''
Created on 18/03/2011

@author: mm
'''
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import smtplib
from datetime import date

root = Tk()
tkinterLabel = Label(root)
date = date.today()

#lists
list_all = []

#About functions
def about():
    tkinterLabel["text"] = "Written by Marc Munk - marc@pungloppen.dk"
    tkinterLabel.pack()

def version():
    tkinterLabel["text"] = "IPFW log parser version 0.5"
    tkinterLabel.pack()

def loadfile():
    i = 0
    filename = filedialog.askopenfilename()
    f = open(filename, 'r')  
    for line in (f):
        list_all.insert(i, line)
        i += 1
    f.close
    tkinterLabel = Label(root)
    tkinterLabel["text"] = "Number of lines loaded are", i
    tkinterLabel.pack() 
    
#Analyse menu functions
#Shows all entries in list_all 
def showall():
    i = 0
    len_all = len(list_all)
    while len_all == 0:
        tkinterLabel = Label(root)
        tkinterLabel["text"] = "Please load log file"
        tkinterLabel.pack() 
        break
    if i != len_all:
        while len_all >= i:
            output = list_all[i]
            tkinterLabel = Label(root)
            tkinterLabel["text"] = output
            tkinterLabel.pack()
            i += 1
            if i == len_all:
                break

#Filters out TCP connections
def showallTCP():
    i = 0
    proto = ""
    len_all = len(list_all)
    while len_all == 0:
        tkinterLabel = Label(root)
        tkinterLabel["text"] = "Please load log file"
        tkinterLabel.pack()
        break
    if len_all != 0:
        while i <= len_all:
            input = list_all[i]
            proto = input.split()
            proto = str(proto)
            output = proto.find('TCP')
            if output != -1:
                TCP = list_all[i]
                tkinterLabel = Label(root)
                tkinterLabel["text"] = TCP
                tkinterLabel.pack()
            i += 1
            if i == len_all:
                break

#Filters out UDP connections
def showallUDP():
    i = 0
    proto = ""
    len_all = len(list_all)
    while len_all == 0:
        tkinterLabel = Label(root)
        tkinterLabel["text"] = "Please load log file"
        tkinterLabel.pack()
        break
    if len_all != 0:
        while i <= len_all:
            input = list_all[i]
            proto = input.split()
            proto = str(proto)
            output = proto.find('UDP')
            if output != -1:
                UDP = list_all[i]
                tkinterLabel = Label(root)
                tkinterLabel["text"] = UDP
                tkinterLabel.pack()
            i += 1
            if i == len_all:
                break
            
#Filters out Allowed connections
def showallAllow():
    i = 0
    len_all = len(list_all)
    while len_all == 0:
        tkinterLabel = Label(root)
        tkinterLabel["text"] = "Please load log file"
        tkinterLabel.pack()
        break
    if len_all != 0:
        while i <= len_all:
            input = list_all[i]
            Allow = input.split()
            Allow = str(Allow)
            output = Allow.find('Allow')
            if output != -1:
                Deny = list_all[i]
                tkinterLabel = Label(root)
                tkinterLabel["text"] = Allow
                tkinterLabel.pack()
            i += 1
            if i == len_all:
                break

#Filters out Denied connections
def showallDeny():
    i = 0
    len_all = len(list_all)
    while len_all == 0:
        tkinterLabel = Label(root)
        tkinterLabel["text"] = "Please load log file"
        tkinterLabel.pack()
        break
    if len_all != 0:
            input = list_all[i]
            Deny = input.split()
            Deny = str(Deny)
            output = Deny.find('Deny')
    if output != -1:
            Deny = list_all[i]
            tkinterLabel = Label(root)
            tkinterLabel["text"] = Deny
            tkinterLabel.pack()
            i += 1
            if i == len_all:
                break

#Export menu functions
#Export Show all Lines
def exportall():
    i = 0
    len_all = len(list_all)
    while len_all == 0:
        tkinterLabel["text"] = "please open log file"
        tkinterLabel.pack()
        break
    while len_all != 0:
        filename = filedialog.asksaveasfilename()
        f = open (filename, 'a')
        output = list_all[i]
        output = str(output)
        f.write (output)
        i += 1
        if i == len_all:
            break

#GUI 
#Window size and name
class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
myapp = App()
myapp.master.title("Logparser")
myapp.master.maxsize(1400, 800)

#Gui menu 
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open and load log file(IPFW)", command=loadfile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit)


analysemenu = Menu(menu)
menu.add_cascade(label="Analyse", menu=analysemenu)
analysemenu.add_command(label="Show all TCP connections", command=showallTCP)
analysemenu.add_command(label="Show all UDP connections", command=showallUDP)
analysemenu.add_separator()
analysemenu.add_command(label="Show all Allowed connections", command=showallAllow)
analysemenu.add_command(label="Show all Denied connections", command=showallDeny)

exportemenu = Menu(menu)
menu.add_cascade(label="Export", menu=exportemenu)
exportemenu.add_command(label="Export all lines", command=exportall)


helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about)
helpmenu.add_command(label="Version", command=version)

mainloop()