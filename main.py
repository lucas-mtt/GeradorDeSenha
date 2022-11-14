import random
from tkinter import *
from tkinter import messagebox
import pyperclip



# função gerar senha
def gerarSenha():
    caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '&']

    passwd=''
    for i in range(editQtdCarac1.get()):
        passwd += random.choice(caracteres)
    editSenhaGerada1.set(passwd)


# funcao copiar senha
def copiarSenha():
    pyperclip.copy(editSenhaGerada1.get())
    messagebox.showinfo("Master", "Senha copiada!")


# função sair
def sair():
    if messagebox.askokcancel('Master', 'Tem certeza que deseja sair?', icon='question'):
        master.destroy()



# configurando a janela
master = Tk()
master.geometry("400x300")
master.title("Gerador de Senha")
master.config(bg="#c0c0c0")
master.resizable(0,0)

editSenhaGerada1 = StringVar()
editQtdCarac1 = IntVar()
editQtdCarac1.set(0)


# frame titulo
frameTitulo = Frame(master, borderwidth=0.8, relief=SOLID)
frameTitulo.config(bg="black")
frameTitulo.place(x=0, y=0, width=400, height=70)

# label titulo
labTitulo = Label(frameTitulo, text="Gerador de Senha", fg="white", bg="black", relief=FLAT, font=("Calibri", 20, "bold"))
labTitulo.place(x=95, y=15)

# label pedindo quantidade de caracteres
labQtdCarac = Label(master, text="Quantidade de Caracteres*", fg="black", bg="#c0c0c0", relief=FLAT, font=("Calibri", 12, "bold"))
labQtdCarac.place(x=10, y=100)

# edit box para inserir a quantidade de caracteres
editQtdCarac1 = IntVar()
editQtdCarac = Entry(master, textvariable=editQtdCarac1, fg="black", bg="white", relief=FLAT, font=("Calibri", 11, "italic"), justify=CENTER)
editQtdCarac.place(x=210, y=100, width=170, height=25)

# label indicando onde aparecerá a senha gerada
labSenhaGerada = Label(master, text="Senha Gerada", fg="black", bg="#c0c0c0", relief=FLAT, font=("Calibri", 12, "bold"))
labSenhaGerada.place(x=10, y=160)

# edit box mostrando a senha gerada
editSenhaGerada1 = StringVar()
editSenhaGerada = Entry(master, textvariable=editSenhaGerada1, fg="black", bg="white", relief=FLAT, font=("Calibri", 11, "italic"), justify=CENTER)
editSenhaGerada.place(x=120, y=160, width=260, height=25)
editSenhaGerada["state"]="disabled"

# frame onde fica os botões
frameBotoes = Frame(master, borderwidth=0.8, relief=SOLID)
frameBotoes.config(bg="black")
frameBotoes.place(x=0, y=230, width=400, height=70)

# botão para gerar a senha
btGerarSenha = Button(frameBotoes, text="Gerar Senha", fg="black", bg="#c0c0c0", justify=CENTER, font=("Calibri", 12), relief=RAISED, command=gerarSenha)
btGerarSenha.place(x=30, y=20, width=100, height=30)

# botão para copiar a senha gerada
btCopiar = Button(frameBotoes, text="Copiar", fg="black", bg="#c0c0c0", justify=CENTER, font=("Calibri", 12), relief=RAISED, command=copiarSenha)
btCopiar.place(x=150, y=20, width=100, height=30)

# botão para sair
btSair = Button(frameBotoes, text="Sair", fg="black", bg="#c0c0c0", justify=CENTER, font=("Calibri", 12), relief=RAISED, command=sair)
btSair.place(x=270, y=20, width=100, height=30)



master.mainloop()