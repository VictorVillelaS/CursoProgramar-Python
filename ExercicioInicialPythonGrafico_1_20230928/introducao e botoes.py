"""
Os aplicativos de computador modernos são fáceis de usar. A interação do usuário não se restringe a E / S baseada
em console. Eles têm uma interface gráfica de usuário (GUI) mais ergonômica, graças aos processadores de alta
velocidade e hardware gráfico poderoso. Esses aplicativos podem receber entradas por meio de cliques do mouse e
permitir que o usuário escolha alternativas com a ajuda de botões de rádio, listas suspensas e outros elementos de
GUI (ou widgets).

Esses aplicativos são desenvolvidos usando uma das várias bibliotecas gráficas disponíveis. Uma biblioteca gráfica é um
 kit de ferramentas de software que possui uma coleção de classes que definem a funcionalidade de vários elementos da
 GUI. Essas bibliotecas gráficas geralmente são escritas em C / C ++. Muitos deles foram portados para Python na forma
 de módulos importáveis. Alguns deles estão listados abaixo:

Este tutorial explica o uso do Tkinter no desenvolvimento de programas Python baseados em GUI.

WxPython é um wrapper Python em torno de WxWidgets, outra biblioteca gráfica de plataforma cruzada.

PyGTK é o módulo que transporta o Python para outro kit de ferramentas de widget GUI popular chamado GTK.

PyQtis, a interface Python para Qt, é um framework GUI multiplataforma muito popular.

Tkinter é a porta Python para o kit de ferramentas Tcl-Tk GUI desenvolvido por Fredrik Lundh. Este módulo é fornecido
com distribuições padrão de Python para todas as plataformas.

Aplicativo GUI Básico
Os elementos da GUI e sua funcionalidade são definidos no módulo Tkinter. O código a seguir demonstra as etapas na 
criação de uma IU.
"""

from tkinter import *
from tkinter import messagebox

#Define um objeto janela
FrmMensagem = Tk()
#Título da janela
FrmMensagem.title('Exercício Inicial de Mensagem')
#Tamanho da janela; f'{largura}x{altura}+{desloc_horizontal}+{desloc_vertical}' (a partir de cima esquerda)
FrmMensagem.geometry('300x200+500+300')


'''
Em primeiro lugar, importe o módulo TKinter. Após a importação, configure o objeto do aplicativo chamando a função 
Tk (). Isso criará uma janela de nível superior (raiz) com um quadro com uma barra de título, caixa de controle com 
os botões minimizar e fechar e uma área de cliente para armazenar outros widgets. O método geometry () define a 
largura, altura e coordenadas do canto superior esquerdo do quadro conforme abaixo (todos os valores estão em 
pixels): objJanela.geometry ("widthxheight + XPOS + YPOS") O objeto do aplicativo então entra em um evento de escuta 
loop chamando o método mainloop (). O aplicativo agora está constantemente esperando por qualquer evento gerado nos 
elementos nele. O evento pode ser um texto inserido em um campo de texto, uma seleção feita no menu suspenso ou botão 
de rádio, ações de clique único / duplo do mouse, etc. A funcionalidade do aplicativo envolve a execução de funções 
de retorno de chamada apropriadas em resposta a um tipo específico de evento. Discutiremos o tratamento de eventos 
posteriormente neste tutorial. O loop de eventos terminará quando o botão Fechar na barra de título for clicado.

Todas as classes de widget Tkinter são herdadas da classe Widget. Vamos adicionar os widgets mais usados.

Botão
O botão pode ser criado usando a classe Button. O construtor da classe Button requer uma referência à janela principal 
e às opções.

Assinatura: Button(janela, atributos)

Você pode definir as seguintes propriedades importantes para personalizar um botão:

text : caption of the button                    texto: legenda do botão
bg : background colour                          bg: cor de fundo
fg : foreground colour                          fg: cor de primeiro plano
font : font name and size                       fonte: nome e tamanho da fonte
image : to be displayed instead of text         imagem: a ser exibida em vez de texto
command : function to be called when clicked    comando: função a ser chamada quando clicada
'''


def Mensagem():
    if messagebox.askyesnocancel('Pergunta', 'Escolha Sim ou Não'):
        messagebox.showinfo('Sim', 'Você escolheu sim')
    else:
        messagebox.showinfo('Não', 'Você escolheu não')
    messagebox.showinfo('Mensagem', 'Parabéns, meu primeiro programa gráfico!')


#Definindo o botão, com algumas configurações iniciais
BtnMensagem = Button(FrmMensagem, text="Clique aqui para mensagem!", fg='blue', bg='yellow', width=25, height=1,
                     command=Mensagem)
#Definindo o lugar do botão
BtnMensagem.place(x=85, y=90)
#Abre a janela - tem que ser a última coisa do programa
FrmMensagem.mainloop()
'''
Label - Rótulo
Um rótulo pode ser criado na IU em Python usando a classe Label. O construtor Label requer o objeto de janela de nível 
superior e os parâmetros de opções. Os parâmetros de opção são semelhantes ao objeto Botão.

O seguinte adiciona um rótulo na janela.

Aqui, a legenda do rótulo será exibida em vermelho usando a fonte Helvetica de tamanho 16 pontos.
'''

# from tkinter import *
# objJanela=Tk()
#
# lblExemplo=Label(objJanela, text="ProgrAmar Label - Rótulo", fg='red', font=("Helvetica", 16))
# lblExemplo.place(x=25, y=50)
#
# objJanela.title('Curso ProgrAmar')
# objJanela.geometry("300x200+10+10")
# objJanela.mainloop()

'''
Entry - Entrada
Este widget renderiza uma caixa de texto de linha única para aceitar a entrada do usuário. Para entrada de texto com 
várias linhas, use o widget Texto. Além das propriedades já mencionadas, o construtor da classe Entry aceita o seguinte:

bd: tamanho da borda da caixa de texto; o padrão é 2 pixels.
show: para converter a caixa de texto em um campo de senha, defina show property para "*".
O código a seguir adiciona o campo de texto.

txtfld = Entry (objJanela, text = "Este é o widget Entry", bg = 'preto', fg = 'branco', bd = 5)

O exemplo a seguir cria uma janela com um botão, rótulo e campo de entrada.
'''

# from tkinter import *
# objJanela=Tk()
#
# btnExemplo=Button(objJanela, text="ProgrAmar Button widget", fg='blue')
# btnExemplo.place(x=80, y=100)
#
# lblExemplo=Label(objJanela, text="ProgrAmar Label widget", fg='red', font=("Helvetica", 16))
# lblExemplo.place(x=60, y=50)
#
# txtExemplo=Entry(objJanela, text="ProgrAmar Entry Widget", bd=5)
# txtExemplo.place(x=80, y=150)
#
# objJanela.title('Curso ProgrAmar Python')
# objJanela.geometry("300x200+10+10")
# objJanela.mainloop()