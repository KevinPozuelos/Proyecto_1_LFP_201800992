from tkinter import *
from tkinter import filedialog
def openFile():
    root = Tk()
    root.fileName = filedialog.askopenfilename(filetypes=(("HowCOde files", ".lfp"), ("All files", ".")))
    file = root.fileName
    data = open(file, "r",encoding='utf8')
    aux = data.read()
    data.close()
    return aux