from tkinter import *
from tkinter import filedialog
import requests

def Quit(ev):
    global root
    root.destroy()

def Russian(ev):
    textbox2.delete('1.0', END)
    text = textbox.get('1.0', END)
    trans_option = {'key': token, 'lang': 'en-ru', 'text': text}
    webRequest = requests.get(url_trans, params=trans_option)
    Rtext = webRequest.text
    Rtext = Rtext[36:(len(Rtext) - 5)]
    Rtext = Rtext.replace(r"\n", ' ')
    textbox2.insert("1.0", Rtext)

def English(ev):
    textbox2.delete('1.0', END)
    text = textbox.get('1.0', END)
    trans_option = {'key': token, 'lang': 'ru-en', 'text': text}
    webRequest = requests.get(url_trans, params=trans_option)
    Etext = webRequest.text
    Etext = Etext[36:(len(Etext) - 5)]
    Etext = Etext.replace(r"\n", ' ')
    textbox2.insert("1.0", Etext)

def LoadFile(ev):
    fn = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
    if fn == '':
        return
    textbox.delete('1.0', 'end')
    textbox.insert('1.0', open(fn, 'rt').read())


def SaveFile(ev):
    fn = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
    if fn == '':
        return
    if not fn.endswith(".txt"):
        fn += ".txt"
    open(fn, 'wt').write(textbox2.get('1.0', 'end'))


root = Tk()

token = "trnsl.1.1.20180517T163103Z.3f6e804d5a33f05c.d97b8ea8222671f1966e9b1efad3233beaa603a9"
url_trans = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
panelFrame = Frame(root, height=60, bg='gray')
textFrame = Frame(root, height=150, width=150)
text2Frame = Frame(root, height=150, width=150)

panelFrame.pack(side='top', fill='x')
textFrame.pack(side='left', fill='none', expand=0)
text2Frame.pack(side='right', fill='none', expand=0)

textbox = Text(textFrame, font='Arial 14', wrap='word')
textbox2 = Text(text2Frame, font='Arial 14', wrap='word')
scrollbar = Scrollbar(textFrame)
scrollbar2 = Scrollbar(text2Frame)
scrollbar['command'] = textbox.yview
scrollbar2['command'] = textbox2.yview
textbox['yscrollcommand'] = scrollbar.set
textbox2['yscrollcommand'] = scrollbar2.set

textbox.pack(side='left', fill='none', expand=1)
scrollbar.pack(side='right', fill='y')
textbox2.pack(side='right', fill='none', expand=1)
scrollbar2.pack(side='right', fill='y')

englishBtn = Button(panelFrame, text='English')
russianBtn = Button(panelFrame, text='Russian')
loadBtn = Button(panelFrame, text='Load')
saveBtn = Button(panelFrame, text='Save')
quitBtn = Button(panelFrame, text='Quit')

loadBtn.bind("<Button-1>", LoadFile)
saveBtn.bind("<Button-1>", SaveFile)
quitBtn.bind("<Button-1>", Quit)
englishBtn.bind("<Button-1>", English)
russianBtn.bind("<Button-1>", Russian)

russianBtn.place(x=900, y=10, width=60, height=40)
englishBtn.place(x=970, y=10, width=60, height=40)
loadBtn.place(x=10, y=10, width=40, height=40)
saveBtn.place(x=1070, y=10, width=40, height=40)
quitBtn.place(x=1140, y=10, width=40, height=40)

root.mainloop()