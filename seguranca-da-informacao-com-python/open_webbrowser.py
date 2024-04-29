import webbrowser
from tkinter import *

root = Tk( ) # quando vazio = None

root.title('Abrir Browser')
root.geometry('300x200') # tamanho da janela em px

def google():
    webbrowser.open('www.google.com')

# cria o botão para abrir o google
my_google = Button(root, text='Abrir Google', command=google).pack(pady=20)
root.mainloop()