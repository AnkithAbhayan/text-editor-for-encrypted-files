import ankith
from tkinter import *
from tkinter import filedialog
import os
import sys
import json
def savetofilehistory(string):
    path = findjsonpath()
    with open(path, "r") as jsonFile:
        data = json.load(jsonFile)
    if string in data["previousfiles"]:
        data["previousfiles"].remove(string)
    data["previousfiles"].insert(0,string)
    with open(path, "w") as jsonFile:
        json.dump(data,jsonFile,indent=4)
def getpreviousfiles():
    jsonpath = findjsonpath()
    with open(jsonpath,"r") as JsonFile:
        data = json.load(JsonFile)
    array = data["previousfiles"]
    with open(jsonpath, "w") as jsonFile:
        json.dump(data,jsonFile,indent=4)
    return array 
def promptnewpass():
    def removeasterix():
        newpasswordentry.configure(show="")
        newpasswordentry.after(300,lambda:newpasswordentry.config(show="*"))
        newpasswordentry1.configure(show="")
        newpasswordentry1.after(300,lambda:newpasswordentry1.config(show="*"))
    def getinfo(password1,password2):
        if password1 != password2:
            syntaxer = Label(root,text="passwords do not match",fg="red")
            syntaxer.grid(row=3,column=0,columnspan=3)
            syntaxer.after(3000, syntaxer.destroy)    
        elif len(password1) == 0:
            syntaxer = Label(root,text="no password entered",fg="red")
            syntaxer.grid(row=3,column=0,columnspan=3)
            syntaxer.after(3000, syntaxer.destroy)
        else:
            getpath = findjsonpath()
            with open(getpath,"r") as JsonFile:
                data = json.load(JsonFile)
            data["password"] = ankith.cryptography.encrypt(password1)
            with open(getpath, "w") as jsonFile:
                json.dump(data,jsonFile,indent=4)
            syntaxer = Label(root,text="password changed!",fg="green")
            syntaxer.grid(row=3,column=0,columnspann=3)
            syntaxer.after(3000, root.destroy)            
    root = Tk()
    root.title("ate/enternewpassword")
    newpasswordl = Label(root,text="Enter new password").grid(row=0,column=0)
    newpasswordentry = Entry(root,width=30,borderwidth=3,show="*")
    newpasswordentry.grid(row=0,column=1)
    newpasswordl = Label(root,text="re-enter new password").grid(row=1,column=0)
    newpasswordentry1 = Entry(root,width=30,borderwidth=3,show="*")
    newpasswordentry1.grid(row=1,column=1)
    showbutton = Button(root,text="show",command=lambda:removeasterix()).grid(row=0,column=2,pady=3,padx=7,rowspan=2)
    submitbutton = Button(root,text="submit",width=10,pady=2,command=lambda:getinfo(newpasswordentry.get(),newpasswordentry1.get()))
    submitbutton.grid(row=2,column=0,pady=7,columnspan=2)
    root.mainloop()
def changepassword(string):
    def removeasterixo(root,passwordEntry):
        passwordEntry.configure(show="")
        passwordEntry.after(300,lambda:passwordEntry.config(show="*"))
    def sendpassword(password):
        def printandkill():
            root.destroy()
            promptnewpass()
        def printandchange():
            root.destroy()
            getpath = findjsonpath()
            with open(getpath,"r") as JsonFile:
                data = json.load(JsonFile)
            data["password"] = ankith.cryptography.encrypt("wakapie")
            with open(getpath, "w") as jsonFile:
                json.dump(data,jsonFile,indent=4)
        path = findjsonpath()
        if os.path.exists(path):
            realpassword = ankith.cryptography.decrypt(getpassword())
        else:
            realpassword = ankith.cryptography.decrypt("8Y9ngG9n9wEr8v")
        if password != realpassword:
            syntaxer = Label(root,text="wrong password",fg="red")
            syntaxer.grid(row=2,column=0,columnspan=3)
            syntaxer.after(3000, syntaxer.destroy)
        else:
            syntaxer = Label(root,text="correct password",fg="green")
            syntaxer.grid(row=2,column=0,columnspan=3)
            if string == "nil":
                syntaxer.after(3000, lambda:printandkill())
            else:
                syntaxer.after(3000, lambda:printandchange())
    root = Tk()
    root.title("ate/enter current password")
    enterlabel = Label(root,text="Enter password").grid(row=0,column=0,padx=5)
    enterpassword = Entry(root,show="*",width=30,borderwidth=3)
    enterpassword.grid(row=0,column=1)
    showbutton = Button(root,text="show",command=lambda:removeasterixo(root,enterpassword)).grid(row=0,column=2,pady=3,padx=7)
    submitbutton = Button(root,text="submit",width=10,pady=2,command=lambda:sendpassword(enterpassword.get())).grid(row=1,column=0,columnspan=3,pady=7)
    root.bind("<Return>", (lambda event: sendpassword(enterpassword.get())))
    root.mainloop()
def initializejson():
    path = findjsonpath()
    if os.path.exists(path) == False:
        password = getpassword()
        with open(path, "w") as jsonFile:
            json.dump({"path":"","password":ankith.cryptography.encrypt(password),"previousfiles":[]},jsonFile,indent=4)
def getpassword():
    jsonfilepath = findjsonpath()
    if os.path.exists(jsonfilepath):
        with open(jsonfilepath,"r") as JsonFile:
            data = json.load(JsonFile)
        return data["password"]
    else:
        return "wakapie"
def getaccess():
    def removeasterixo(root,passwordEntry):
        passwordEntry.configure(show="")
        passwordEntry.after(300,lambda:passwordEntry.config(show="*"))
    def sendpassword(password):
        path = findjsonpath()
        if os.path.exists(path):
            realpassword = ankith.cryptography.decrypt(getpassword())
        else:
            realpassword = ankith.cryptography.decrypt("8Y9ngG9n9wEr8v")
        if password != realpassword:
            syntaxer = Label(root,text="wrong password",fg="red")
            syntaxer.grid(row=2,column=0,columnspan=3)
            syntaxer.after(3000, syntaxer.destroy)
        else:
            syntaxer = Label(root,text="correct password",fg="green")
            syntaxer.grid(row=2,column=0,columnspan=3)
            syntaxer.after(1000, root.destroy)
            global accessqmark
            accessqmark = True
    root = Tk()
    root.title("ankith's text editor : enter password")
    enterlabel = Label(root,text="Enter password").grid(row=0,column=0,padx=5)
    enterpassword = Entry(root,show="*",width=30,borderwidth=3)
    enterpassword.grid(row=0,column=1)
    showbutton = Button(root,text="show",command=lambda:removeasterixo(root,enterpassword)).grid(row=0,column=2,pady=3,padx=7)
    submitbutton = Button(root,text="submit",width=10,pady=2,command=lambda:sendpassword(enterpassword.get())).grid(row=1,column=0,columnspan=3,pady=7)
    root.bind("<Return>", (lambda event: sendpassword(enterpassword.get())))
    root.mainloop()    
def findjsonpath():
    relative_path = sys.argv[0]
    letter_list = [x for x in relative_path]
    slashindex = []
    lix = ["\ "] 
    if lix[0][0] not in letter_list:
        return "cache.json"  
    for item in letter_list:
        if item == lix[0][0]:
            indexx = letter_list.index(lix[0][0])
            slashindex.append(indexx)
            letter_list[indexx] = "a"
    return relative_path[0:slashindex[-1]]+"\cache.json"
def getpath():
    jsonfilepath = findjsonpath()
    if os.path.exists(jsonfilepath):
        with open(jsonfilepath, "r") as jsonFile:
            data = json.load(jsonFile)
        return data["path"]
    else:
        return ""
def savepath(path):
    jsonfilepath = findjsonpath()
    password = getpassword()
    previousopenedarray = getpreviousfiles()
    with open(jsonfilepath, "w") as jsonFile:
        json.dump({"path":path,"password":password,"previousfiles":previousopenedarray},jsonFile,indent=4)
def open_file(path):
    jsonpath = findjsonpath()
    if path == "":
        path = filedialog.askopenfilename()
        if path != "":
            file = open(path,"r")
            data = file.read()
            text_field.delete('1.0', END)
            text_field.insert(0.0,ankith.cryptography.decrypt(data))
            file.close()
            savepath(path)
            root.title(path+" ["+ankith.cryptography.findsize(os.path.getsize(path))+"]")
            savetofilehistory(path)
    else:
        if os.path.exists(path):
            file = open(path,"r")
            data = file.read()
            text_field.delete('1.0', END)
            text_field.insert(0.0,ankith.cryptography.decrypt(data))
            file.close()
            savepath(path)
            root.title(path+" ["+ankith.cryptography.findsize(os.path.getsize(path))+"]")
            savetofilehistory(path)
def initialize():
    path = getpath()
    data = ""
    if os.path.exists(path):
        file = open(path,"r")
        data = file.read()
        file.close()
    if getpath() == "":
        root.title("ankiths text editor : untitled")
    else:
        root.title(path+" ["+ankith.cryptography.findsize(os.path.getsize(path))+"]")
    return ankith.cryptography.decrypt(data)
def new_file():
    text_field.delete("1.0",END)
    path = findjsonpath()
    with open(path, "r") as jsonFile:
        data = json.load(jsonFile)
    data["path"] = ""
    with open(path, "w") as jsonFile:
        json.dump(data,jsonFile,indent=4)
    root.title("ankiths text editor : untitled")
def save_file(string):
    if string == "same":
        path = getpath()
        if path == "":
            path = filedialog.asksaveasfilename()
            if path != "":
                savepath(path)
    elif string == "new":
        path = filedialog.asksaveasfilename()
        if path != "":
            savepath(path)
    if path != "":
        file = open(path,"w")
        file.write(ankith.cryptography.encrypt(text_field.get("1.0",END)))
        root.title(path+" ["+ankith.cryptography.findsize(os.path.getsize(path))+"]")
    jsonpath = findjsonpath()
    savetofilehistory(path)
def processcommand(string=False):
    if string != False:
        command = string
    else:
        command = command_pane.get()
        text_field.config(state="normal")
        text_field.focus()
        command_pane.delete(0, END)
        command_pane.config(state="disabled")
    if command == ":s":
        save_file("same")
    elif command == ":sa":
        save_file("new")
    elif command == ":n":
        new_file()
    elif command == ":o":
        open_file("")
def allowentrytocommandpane():
    if command_pane["state"] == "disabled":
        command_pane.config(state='normal')
        text_field.config(state='disabled')
        command_pane.focus()
    elif command_pane["state"] == "normal":
        text_field.config(state='normal')
        text_field.focus()
        processcommand(command_pane.get())
        command_pane.delete(0,END)
        command_pane.config(state='disabled')
accessqmark = False
getaccess()
if accessqmark != True:
    sys.exit()
initializejson()
root = Tk()
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
#root.resizable(0,0)
root.bind("<F2>",(lambda event: allowentrytocommandpane()))
menubar = Menu(root)
root.config(menu=menubar)
fileMenu = Menu(menubar,tearoff=0)
fileMenu.add_command(label="new",command=lambda:new_file())
fileMenu.add_command(label="open",command=lambda:open_file(""))
fileMenu.add_command(label="save",command=lambda:save_file("same"))
fileMenu.add_command(label="save as",command=lambda:save_file("new"))
fileMenu.add_separator()
filehistorysubmenu = Menu(fileMenu,tearoff=0)
previous_files = getpreviousfiles()
for item in previous_files:
    filehistorysubmenu.add_command(label=item,command=lambda:open_file(""))
fileMenu.add_cascade(label="open previous",menu=filehistorysubmenu,underline=0)
fileMenu.add_separator()
fileMenu.add_command(label="exit",command=lambda:sys.exit())
menubar.add_cascade(label="File", menu=fileMenu)

Access = Menu(menubar,tearoff=0)
Access.add_command(label="change password",command=lambda:changepassword("nil"))
Access.add_command(label="reset password",command=lambda:changepassword("original"))
menubar.add_cascade(label="Access",menu=Access)

inserttext = initialize()
text_field = Text(root,width=105,height=30,font="consolas",bd=2,wrap=WORD)
text_field.grid(row=0,column=0,columnspan=2,sticky="NSEW")
text_field.insert(0.0,inserttext)

scroll_bar = Scrollbar(root, orient="vertical", command=text_field.yview)
scroll_bar.grid(column=2, row=0,sticky="NSEW")
command_pane_label = Label(text="CommandPane",width=11).grid(row=1,column=0,sticky="SE")
command_pane = Entry(root,width=140,state='disabled')
command_pane.grid(row=1,column=1,sticky="S")
command_pane.bind("<Return>", (lambda event: processcommand()))
text_field.configure(yscrollcommand=scroll_bar.set)
root.mainloop()
