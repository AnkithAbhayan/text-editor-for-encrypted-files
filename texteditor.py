import ankith
from tkinter import *
from tkinter import filedialog
import os
import sys
import json
def findjsonpath():
    relative_path = sys.argv[0]
    letter_list = [x for x in relative_path]
    slashindex = []
    lix = ["\ "]
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
    with open(jsonfilepath, "w") as jsonFile:
        json.dump({"path":path},jsonFile,indent=4)
def open_file():
    path = filedialog.askopenfilename()
    if path != "":
        file = open(path,"r")
        data = file.read()
        text_field.delete('1.0', END)
        text_field.insert(0.0,ankith.cryptography.decrypt(data))
        file.close()
        savepath(path)
        root.title(path)
def initialize():
    path = getpath()
    print(path)
    data = ""
    if os.path.exists(path):
        file = open(path,"r")
        data = file.read()
        file.close()
    if getpath() == "":
        root.title("ankiths text editor : untitled")
    else:
        root.title(getpath())
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
        root.title(path)
root = Tk()
root.resizable(0,0)
menubar = Menu(root)
root.config(menu=menubar)
fileMenu = Menu(menubar)
fileMenu.add_command(label="open",command=lambda:open_file())
fileMenu.add_command(label="save",command=lambda:save_file("same"))
fileMenu.add_command(label="save as",command=lambda:save_file("new"))
fileMenu.add_command(label="new",command=lambda:new_file())
menubar.add_cascade(label="File", menu=fileMenu)
inserttext = initialize()
text_field = Text(root,width=105,height=30,font="consolas",bd=2,wrap=WORD)
text_field.grid(row=0,column=0,columnspan=2)
text_field.insert(0.0,inserttext)
scroll_bar = Scrollbar(root, orient="vertical", command=text_field.yview)
scroll_bar.grid(column=2, row=0,sticky=N+S+W)
text_field.configure(yscrollcommand=scroll_bar.set)
root.mainloop()