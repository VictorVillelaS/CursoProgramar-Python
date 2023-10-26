'''
https://www.askpython.com/python-modules/tkinter/stringvar-with-examples
Selection Widgets - Widgets de seleção
Radiobutton - Botão de opção: Este widget exibe um botão de alternância com um estado LIGADO / DESLIGADO. Pode haver
mais de um botão, mas apenas um deles estará LIGADO em um determinado momento.

Checkbutton - Botão de verificação: Este também é um botão de alternância. Uma caixa de seleção retangular aparece antes
de sua legenda. Seu estado LIGADO é exibido pela marca de seleção na caixa que desaparece quando é clicado em DESLIGADO.

Combobox - Combobox: esta classe é definida no módulo ttk do tkinterpackage. Ele preenche dados suspensos de um tipo de
dados de coleção, como uma tupla ou uma lista como parâmetro de valores.

Listbox - Listbox: ao contrário do Combobox, este widget exibe toda a coleção de itens de string. O usuário pode
selecionar um ou vários itens.

O exemplo a seguir demonstra a janela com os widgets de seleção: Radiobutton, Checkbutton, Listbox e Combobox:
'''

from tkinter import *
from tkinter.ttk import Combobox

janela = Tk()
strVar = StringVar()
strVar.set("primeiro")
lstDdata = ("primeiro", "segundo", "terceiro", "quarto")
cmbbxPosicao = Combobox(janela, values=lstDdata)
cmbbxPosicao.place(x=60, y=150)

#Tem como adicionar aquelas barras laterais pra descer?
#Tem como executar um comando se der um clique duplo em algum item?
lstbxPosicao = Listbox(janela, height=5, selectmode='multiple')
for num in lstDdata:
    lstbxPosicao.insert(END, num)
lstbxPosicao.place(x=250, y=150)

intVarRadioButton0 = IntVar()
#Marca uma opção
intVarRadioButton0.set(1)
rdbtnSexo1 = Radiobutton(janela, text="Masculino", variable=intVarRadioButton0, value=1)
rdbtnSexo2 = Radiobutton(janela, text="Feminino", variable=intVarRadioButton0, value=2)
rdbtnSexo1.place(x=100, y=50)
rdbtnSexo2.place(x=180, y=50)

chkbxEsportesPreferidosV1 = IntVar()
chkbxEsportesPreferidosV2 = IntVar()
chkbxEsportesPreferidos1 = Checkbutton(janela, text="Natação", variable=chkbxEsportesPreferidosV1)
chkbxEsportesPreferidos2 = Checkbutton(janela, text="Futebol", variable=chkbxEsportesPreferidosV2)
chkbxEsportesPreferidos1.place(x=100, y=100)
chkbxEsportesPreferidos2.place(x=180, y=100)

janela.title('Curso ProgrAmar')
janela.geometry("400x300+10+10")
janela.mainloop()