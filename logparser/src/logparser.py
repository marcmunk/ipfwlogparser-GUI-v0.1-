'''
Created on 18/03/2011

@author: mm
'''
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from datetime import date

root = Tk()
tkinterLabel = Label(root)

#lists
list_all = []
licens = []
#About functions
#About function
def about():
    tkinterLabel["text"] = "Written by Marc Munk - marc@pungloppen.dk"
    tkinterLabel.pack()

#Version number     
def version():
    tkinterLabel["text"] = "Version 0.1"
    tkinterLabel.pack()
#Licens function
def licens():
        tkinterLabel["text"] = "This script is licensed under the beerware licens."
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

#Find all trafic on TCP/80
def showHTTPTRAFIC():
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
                if test == 80:
                    tkinterLabel = Label(root)
                    tkinterLabel["text"] = list_all[i]
                    tkinterLabel.pack()
            i += 1
            if i == len_all:
                break

#Show all SSH trafic
def showSSHTRAFIC():
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
                if test == 22:
                    tkinterLabel = Label(root)
                    tkinterLabel["text"] = list_all[i]
                    tkinterLabel.pack()
            i += 1
            if i == len_all:
                break

#Find all trafic on TCP/80
def showHTTPSTRAFIC():
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
                if test == 443:
                    tkinterLabel = Label(root)
                    tkinterLabel["text"] = list_all[i]
                    tkinterLabel.pack()
            i += 1
            if i == len_all:
                break

#Show all SMTP trafic
def showSMTPTRAFIC():
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
                if test == 25:
                    tkinterLabel = Label(root)
                    tkinterLabel["text"] = list_all[i]
                    tkinterLabel.pack()
            i += 1
            if i == len_all:
                break

#show all ftp trafic
def showFTPTRAFIC():
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
                if test == 23:
                    tkinterLabel = Label(root)
                    tkinterLabel["text"] = list_all[i]
                    tkinterLabel.pack()
            i += 1
            if i == len_all:
                break

#Used for finding all UDP/53 trafic
def allDNSTRAFIC():
    i = 0
    len_all = len(list_all)
    errorloadfile()
    if len_all != 0:
        while i <= len_all:
            incoming = list_all[i]
            port = incoming.split()
            port = str(port)
            port = port.find('UDP')
            if port != -1:
                test = list_all[i]
                test = test.split()
                test = test[10]
                test = str(test)
                test = test.split( ':' )
                test = test[1:]
                test = ''.join(filter(lambda x: x.isdigit(),test))
                test = int(test)
                if test == 53:
                    tkinterLabel = Label(root)
                    tkinterLabel["text"] = list_all[i]
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
    errorloadfile()
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

#Export TCP/80 trafic
def exportHTTPTRAFIC():
    i = 0
    filename = filedialog.asksaveasfilename()
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
                if test == 80:
                    output = list_all[i]
                    f = open (filename, 'a')
                    f.write (output)
            i += 1
            if i == len_all:
                break
            
def exportSSHTRAFIC():
    i = 0
    filename = filedialog.asksaveasfilename()
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
                if test == 22:
                    output = list_all[i]
                    f = open (filename, 'a')
                    f.write (output)
            i += 1
            if i == len_all:
                break

def exportHTTPSTRAFIC():
    i = 0
    filename = filedialog.asksaveasfilename()
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
                if test == 443:
                    output = list_all[i]
                    f = open (filename, 'a')
                    f.write (output)
            i += 1
            if i == len_all:
                break

#Export SMTP trafic
def exportSMTPTRAFIC():
    i = 0
    len_all = len(list_all)
    filename = filedialog.asksaveasfilename()
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
                if test == 25:
                    output = list_all[i]
                    f = open (filename, 'a')
                    f.write (output)
            i += 1
            if i == len_all:
                break

def exportFTPTRAFIC():
    i = 0
    len_all = len(list_all)
    filename = filedialog.asksaveasfilename()
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
                if test == 23:
                    output = list_all[i]
                    f = open (filename, 'a')
                    f.write (output)
            i += 1
            if i == len_all:
                break

#Used for finding all UDP/53 trafic
def exportallDNSTRAFIC():
    i = 0
    len_all = len(list_all)
    filename = filedialog.asksaveasfilename()
    if len_all != 0:
        while i <= len_all:
            incoming = list_all[i]
            port = incoming.split()
            port = str(port)
            port = port.find('UDP')
            if port != -1:
                test = list_all[i]
                test = test.split()
                test = test[10]
                test = str(test)
                test = test.split( ':' )
                test = test[1:]
                test = ''.join(filter(lambda x: x.isdigit(),test))
                test = int(test)
                if test == 53:
                    output = list_all[i]
                    f = open (filename, 'a')
                    f.write (output)
            i += 1
            if i == len_all:
                break

#Script wide functions
#Tells user to load log file
def errorloadfile():
    len_all = len(list_all)
    while len_all == 0:
        tkinterLabel["text"] = "Please load log file"
        tkinterLabel.pack()
        break 



#Used for testing new functions without making a new menu entry
def test():
    print("Testing menu entry for new functions")

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
analysemenu.add_command(label="Show all connections", command=showall)
analysemenu.add_separator()
analysemenu.add_command(label="Show all TCP connections", command=showallTCP)
analysemenu.add_command(label="Show all UDP connections", command=showallUDP)
analysemenu.add_separator()
analysemenu.add_command(label="Show all Allowed connections", command=showallAllow)
analysemenu.add_command(label="Show all Denied connections", command=showallDeny)
analysemenu.add_command(label="Show all Ingress connections", command=showallIngress)
analysemenu.add_command(label="Show all Egress connections", command=showallEgress)
analysemenu.add_separator()
analysemenu.add_command(label="Show all http trafic", command=showHTTPTRAFIC)
analysemenu.add_command(label="Show all https trafic", command=showHTTPSTRAFIC)
analysemenu.add_command(label="Show all DNS trafic", command=allDNSTRAFIC)
analysemenu.add_command(label="Show all SSH trafic", command=showSSHTRAFIC)
analysemenu.add_command(label="Show all SMTP trafic", command=showSMTPTRAFIC)
analysemenu.add_command(label="Show all FTP trafic", command=showFTPTRAFIC)
analysemenu.add_separator()  
analysemenu.add_command(label="Test", command=test) 

exportemenu = Menu(menu)
menu.add_cascade(label="Export", menu=exportemenu)
exportemenu.add_command(label="Export all lines", command=exportAll)
exportemenu.add_command(label="Export all Allowed lines", command=exportAllow)
exportemenu.add_command(label="Export all Denied lines", command=exportDeny)
exportemenu.add_command(label="Export all Egress lines", command=exportEgress)
exportemenu.add_command(label="Export all Ingress lines", command=exportIngress) 
exportemenu.add_command(label="Export all HTTP lines", command=exportHTTPTRAFIC)
exportemenu.add_command(label="Export all SSH lines", command=exportSSHTRAFIC)
exportemenu.add_command(label="Export all HTTPS lines", command=exportHTTPSTRAFIC)
exportemenu.add_command(label="Export all DNS lines", command=exportallDNSTRAFIC)
exportemenu.add_command(label="Export all FTP lines", command= exportFTPTRAFIC)
exportemenu.add_command(label="Export all SMTP lines", command= exportSMTPTRAFIC)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about)
helpmenu.add_command(label="Version", command=version) 
helpmenu.add_command(label="Licens", command=licens)

mainloop()