'''
Created on 18/03/2011

@author: mm
'''
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
#import smtplib
from datetime import date

root = Tk()
tkinterLabel = Label(root)
date = date.today()

#lists
list_all = []
list_tcpports = []
list_udpports = []

#About functions
def about():
    tkinterLabel["text"] = "Written by Marc Munk - marc@pungloppen.dk"
    tkinterLabel.pack()

#File Menu functions
#Loads log file to be worked with
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
    errorloadfile()
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
    len_all = len(list_all)
    errorloadfile()
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
    len_all = len(list_all)
    errorloadfile()
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
    errorloadfile()
    if len_all != 0:
        while i <= len_all:
            input = list_all[i]
            Allow = input.split()
            Allow = str(Allow)
            output = Allow.find('Allow')
            if output != -1:
                Allow = list_all[i]
                tkinterLabel = Label(root)
                tkinterLabel["text"] = Allow
                tkinterLabel.pack()
            i += 1
            if i == len_all:
                break

#Show all Denied connections
def showallDeny():
    i = 0
    len_all = len(list_all)
    errorloadfile()
    if len_all != 0:
        while i <= len_all:
            input = list_all[i]
            deny = input.split()
            deny = str(deny)
            output = deny.find('Deny')
            if output != -1:
                deny = list_all[i]
                tkinterLabel = Label(root)
                tkinterLabel["text"] = deny
                tkinterLabel.pack()
            i += 1
            if i == len_all:
                break

#Show all ingress connections            
def showallIngress():
    i = 0
    len_all = len(list_all)
    errorloadfile()
    if len_all != 0:
        while i <= len_all:
            input = list_all[i]
            ingress = input.split()
            ingress = str(ingress)
            output = ingress.find('in')
            if output != -1:
                ingress = list_all[i]
                tkinterLabel = Label(root)
                tkinterLabel["text"] = ingress
                tkinterLabel.pack()
            i += 1
            if i == len_all:
                break

#show all engress connections
def showallEgress():
    i = 0
    len_all = len(list_all)
    errorloadfile()
    if len_all != 0:
        while i <= len_all:
            input = list_all[i]
            egress = str.split(input)
            egress = str(egress)
            output = egress.find('out')
            if output != -1:
                egress = list_all[i]
                tkinterLabel = Label(root)
                tkinterLabel["text"] = egress
                tkinterLabel.pack()
            i += 1
            if i == len_all:
                break

#Export menu functions
#Export Show all Lines
def exportAll():
    i = 0
    filename = filedialog.asksaveasfilename()
    len_all = len(list_all)
    while len_all != 0:
        f = open (filename, 'a')
        output = list_all[i]
        output = str(output)
        f.write (output)
        f.close
        i += 1
        if i == len_all:
            break

#Export all Allowed lines
def exportAllow():
    i = 0
    filename = filedialog.asksaveasfilename()
    len_all = len(list_all)
    while len_all == 0:
        tkinterLabel["text"] = "please open log file"
        tkinterLabel.pack()
        break
    if len_all != 0:
        while i <= len_all:
            input = list_all[i]
            Allow = input.split()
            Allow = str(Allow)
            output = Allow.find('Allow')
            if output != -1:
                Allow = list_all[i]
                f = open (filename, 'a')
                f.write (Allow)
            i += 1
            if i == len_all:
                break

#Export all denied lines
def exportDeny():
    i = 0
    filename = filedialog.asksaveasfilename()
    len_all = len(list_all)
    while len_all == 0:
        tkinterLabel["text"] = "please open log file"
        tkinterLabel.pack()
        break
    if len_all != 0:
        while i <= len_all:
            input = list_all[i]
            Deny = input.split()
            Deny = str(Deny)
            output = Deny.find('Deny')
            if output != -1:
                Deny = list_all[i]
                f = open (filename, 'a')
                f.write (Deny)
            i += 1
            if i == len_all:
                break
            
#export all Egress connections
def exportEgress():
    i = 0
    filename = filedialog.asksaveasfilename()
    egress = ""
    len_all = len(list_all)
    while len_all == 0:
        tkinterLabel = Label(root)
        tkinterLabel["text"] = "Please load log file"
        tkinterLabel.pack()
        break
    if len_all != 0:
        while i <= len_all:
            input = list_all[i]
            egress = input.split()
            egress = str(egress)
            output = egress.find('out')
            if output != -1:
                egress = list_all[i]
                f = open (filename, 'a')
                f.write (egress)
            i += 1
            if i == len_all:
                break

#export all Ingress connections
def exportIngress():
    i = 0
    filename = filedialog.asksaveasfilename()
    ingress = ""
    len_all = len(list_all)
    while len_all == 0:
        tkinterLabel = Label(root)
        tkinterLabel["text"] = "Please load log file"
        tkinterLabel.pack()
        break
    if len_all != 0:
        while i <= len_all:
            input = list_all[i]
            ingress = input.split()
            ingress = str(ingress)
            output = ingress.find('in')
            if output != -1:
                ingress = list_all[i]
                f = open (filename, 'a')
                f.write (ingress)
            i += 1
            if i == len_all:
                break

#Script wide functions
#Tells user to load log file
def errorloadfile():
    len_all = len(list_all)
    while len_all == 0:
        tkinterLabel = Label(root)
        tkinterLabel["text"] = "Please load log file"
        tkinterLabel.pack()
        break 

#Find tcpport
def tcpPORTS():
    i = 0
    len_all = len(list_all)
    errorloadfile()
    if len_all != 0:
        while i <= len_all:
            incoming = list_all[i]
            port = incoming.split()
            port = str(port)
            port = port.find('TCP')
            if port != -1:
                test = list_all[i]
                test = test.split()
                test = test[10]
                test = str(test)
                test = test.split( ':' )
                test = test[1:]
                test = ''.join(filter(lambda x: x.isdigit(),test))
                test = int(test)
                list_tcpports.insert(i, test)
                print(i, list_tcpports[i])
            i += 1
            if i == len_all:
                break

#Used for finding port numbers on incoming trafic
def udpPORTS():
    i = 0
    len_all = len(list_all)
    errorloadfile()
    if len_all != 0:
        while i <= len_all:
            incoming = list_all[i]
            port = incoming.split()
            port = str(port)
            port = port.find('udp')
            if port != -1:
                test = list_all[i]
                test = test.split()
                test = test[10]
                test = str(test)
                test = test.split( ':' )
                test = test[1:]
                test = ''.join(filter(lambda x: x.isdigit(),test))
                test = int(test)
                list_udpports.insert(i, test)
            i += 1
            if i == len_all:
                break

#Used for testing new functions without making a new menu entry
def test():
    print("Testing")

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
analysemenu.add_command(label="Show all Ingress connections", command=showallIngress)
analysemenu.add_command(label="Show all Egress connections", command=showallEgress)
analysemenu.add_command(label="Test", command=tcpPORTS)

exportemenu = Menu(menu)
menu.add_cascade(label="Export", menu=exportemenu)
exportemenu.add_command(label="Export all lines", command=exportAll)
exportemenu.add_command(label="Export all Allowed lines", command=exportAllow)
exportemenu.add_command(label="Export all Denied lines", command=exportDeny)
exportemenu.add_command(label="Export all Egress lines", command=exportEgress)
exportemenu.add_command(label="Export all Ingress lines", command=exportIngress)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about)

mainloop()