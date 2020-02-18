from selenium import webdriver
from tkinter import *

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')


def Atacar():
    acao['text'] = 'Ataque iniciado'
    nome1 = nome.get()
    msg1 =  msg.get()
    count1 = int(count.get())
       
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(nome1))
    user.click()

    msg_box = driver.find_element_by_class_name('_13mgZ')

    for i in range(count1):
        msg_box.send_keys(msg1)
        button = driver.find_element_by_class_name('_3M-N-')
        button.click()

janela = Tk()
janela.title("SpamWhats v1.0 ")
janela.geometry("390x260") #Largura x Altura
janela.resizable(False, False) #Não redimensinar
janela.configure(background='black')

Label(janela, text="SPAM WHATSAPP \nby kiqx", bg="black", fg="green", font = "Consolas", padx=70).grid(row=0, column=0, columnspan=2)

Label(janela, text="Nome \nGrupo ou Contato: ", font = "Consolas", bg="black", fg="green").grid(row=1, column=0)
nome = Entry(janela, bg="black", fg="red")
nome.grid(row=1, column=1)

Label(janela, text="Mensagem: ", font = "Consolas", bg="black", fg="green").grid(row=2, column=0)
msg = Entry(janela, bg="black", fg="white")
msg.grid(row=2, column=1)

Label(janela, text="Quantidade a enviar: ", font = "Consolas", bg="black", fg="green").grid(row=3, column=0)
count = Entry(janela, bg="black", fg="white")
count.grid(row=3, column=1)

Button(janela, text="Atacar", font = "Consolas", height=1, width=15,bg="black", fg="green", command=Atacar ).grid(row=4, column=0)
acao = Label(janela, text="Ataque não iniciado", font = "Consolas", bg="black", fg="green" )
acao.grid(row=4, column=1)

Label(janela, text='"Com grandes poderes, \nvêm grandes responsabilidades." \nTio Ben', font = "Consolas", padx=50, bg="black", fg="green").grid(row=5, column=0, columnspan=2)
janela.mainloop()
