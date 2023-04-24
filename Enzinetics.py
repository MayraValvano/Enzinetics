# Código do Software Enzinetics

# Importação das Bibliotecas
import tkinter as tk
import numpy as np
import pandas as pd
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename  # caixa externa - explorar files no computador
import os  # divisão de strings
from tkinter.ttk import Combobox
from tkinter.filedialog import asksaveasfilename
from tkinter import colorchooser
import winsound
from tkinter import ttk
import webbrowser
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk)
from scipy.integrate import odeint #função de integração numérica
from scipy.optimize import differential_evolution #função de algoritmo genético
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.integrate import odeint
from scipy.optimize import leastsq
import scipy.stats as sc #funções estatíticas


#FUNÇÕES

#Função de Modelo Michaelis Menten Sem Inibição                                  
def modelo(s,Vmax,Km):
    return Vmax*s/(Km+s) #Retorna Velocidade (V)

def f_conversao(s0, sf):
    return (sf/s0) * 100

#Função Window Definição Inibição Enzimática
def Inib_Def():
    window_inst = tk.Toplevel()
    window_inst.title("Inibição Enzimática")
    window_inst.geometry("1000x480")
    window_inst.minsize(width=1000, height=480)
    window_inst.resizable(0, 0)
    label_inst = tk.Label(window_inst, text='Definição: Inibição Enzimática', font='Arial 16 bold',bg='grey67').pack(fill='x')
    label_sobre_texto_x = tk.Label(window_inst, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_sobre_texto_x = tk.Label(window_inst, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto = tk.Label(window_inst, width=1000, text='          Como forma de controle de reações enzimáticas podem ser introduzidas outras moléculas ao sistema, denominadas inibidores, que alteram a ', font='Arial 11',anchor='w').pack()
    label_texto_2 = tk.Label(window_inst, width=1000, text='   cinética enzimática, reduzindo a velocidade da reação, através de diferentes mecanismos (DORAN, 2013; LEHNINGER; NELSON; COX, 2012).', font='Arial 11',anchor='w').pack()     
    label_sobre_texto_x = tk.Label(window_inst, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto_3 = tk.Label(window_inst, width=1000, text='         Entre os principais modelos de inibição enzimática estabelecidos na literatura, encontram-se os modelos de inibição reversível, entre os quais', font='Arial 11',anchor='w').pack()
    label_texto_4 = tk.Label(window_inst, width=1000, text='   destacam-se a Inibição Competitiva, Inibição Não-Competitiva e a Inibição Incompetitiva.', font='Arial 11',anchor='w').pack()
    load_1 = Image.open('Inibicao_Def.png')
    load_1_resized = load_1.resize((710,220), Image.ANTIALIAS)
    render_1 = ImageTk.PhotoImage(load_1_resized)
    img_1= tk.Label(window_inst, image = render_1, border = 0, borderwidth = 2, relief="solid")
    img_1.image = render_1
    img_1.place(x = 150, y = 220)
    
#Função Window Inibição Competitiva
def Inib_1():
    window_inst = tk.Toplevel()
    window_inst.title("Inibição Competitiva")
    window_inst.geometry("1000x480")
    window_inst.minsize(width=1000, height=480)
    window_inst.resizable(0, 0)
    label_inst = tk.Label(window_inst, text='Inibição Competitiva', font='Arial 16 bold',bg='grey67').pack(fill='x')
    label_sobre_texto_x = tk.Label(window_inst, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_sobre_texto_x = tk.Label(window_inst, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto = tk.Label(window_inst, width=1000, text='           Os inibidores competitivos são aqueles que possuem semelhanças estruturais com o substrato da reação, e, dessa forma, ambos competem', font='Arial 11',anchor='w').pack()
    label_texto_2 = tk.Label(window_inst, width=1000, text='    pelo sítio ativo da enzima. Assim, são formados, também, complexos enzima-inibidor (EI). Essa competição com os inibidores, de concentração I', font='Arial 11',anchor='w').pack()
    label_texto_3 = tk.Label(window_inst, width=1000, text='    e constante Ki, dificulta a ligação do susbtrato a enzima e, consequentemente, a formação de produto (BORZANI et al, 2001).', font='Arial 11',anchor='w').pack()
    label_sobre_texto_x = tk.Label(window_inst, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto_4 = tk.Label(window_inst, width=1000, text='         A velocidade de formação de ambos os complexos, é dependente da concentração de substrato e de inibidores. A Inibição Competitiva afeta ', font='Arial 11',anchor='w').pack()
    label_texto_5 = tk.Label(window_inst, width=1000, text='    o valor da constante de Michaelis-Menten, que deve ser substituído por um Km aparente (LEHNINGER; NELSON; COX, 2012).', font='Arial 11',anchor='w').pack()
    load_1 = Image.open('Compet_1.PNG')
    load_1_resized = load_1.resize((260,140), Image.ANTIALIAS)
    render_1 = ImageTk.PhotoImage(load_1_resized)
    img_1= tk.Label(window_inst, image = render_1, border = 0, borderwidth = 2, relief="solid")
    img_1.image = render_1
    img_1.place(x = 50, y = 270)
    load_2 = Image.open('Compet_2.PNG')
    load_2_resized = load_2.resize((270,140), Image.ANTIALIAS)
    render_2 = ImageTk.PhotoImage(load_2_resized)
    img_2= tk.Label(window_inst, image = render_2, border = 0, borderwidth = 2, relief="solid")
    img_2.image = render_2
    img_2.place(x = 355, y = 270)
    load_3 = Image.open('Compet_3.PNG')
    load_3_resized = load_3.resize((270,140), Image.ANTIALIAS)
    render_3 = ImageTk.PhotoImage(load_3_resized)
    img_3= tk.Label(window_inst, image = render_3, border = 0, borderwidth = 2, relief="solid")
    img_3.image = render_3
    img_3.place(x = 670, y = 270)
                             
#Função Window Inibição Não Competitiva
def Inib_2():
    window_inst = tk.Toplevel()
    window_inst.title("Inibição Não Competitiva")
    window_inst.geometry("1000x480")
    window_inst.minsize(width=1030, height=480)
    window_inst.resizable(0, 0)
    label_inst = tk.Label(window_inst, text='Inibição Não Competitiva', font='Arial 16 bold',bg='grey67').pack(fill='x')
    label_sobre_texto_x = tk.Label(window_inst, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_sobre_texto_x = tk.Label(window_inst, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto = tk.Label(window_inst, width=1000, text='            A inibição não competitiva mista ocorre quando as moléculas inibidoras possuem afinidade com a enzima, em um sítio ativo diferente do substrato, e ', font='Arial 11',anchor='w').pack()
    label_texto_2 = tk.Label(window_inst, width=1000, text='    com o complexo enzima-substrato (BORZANI et al, 2001). Ocorre, então, a formação de um outro tipo de complexo, o enzima-substrato-inibidor (EIS), que ', font='Arial 11',anchor='w').pack()
    label_texto_3 = tk.Label(window_inst, width=1000, text='    impede a continuação da reação, diminuindo a velocidade da catálise. Em suma, pode-se afirmar que concomitantemente, na reação, ocorrem a formação', font='Arial 11',anchor='w').pack()
    label_texto_4 = tk.Label(window_inst, width=1000, text='    do complexo enzima-substrato, com formação de produto, do complexo enzima-inibidor e do complexo enzima-substrato-inibidor, que, por sua vez, pode', font='Arial 11',anchor='w').pack()
    label_texto_5 = tk.Label(window_inst, width=1000, text='    ser formado pela ligação do inibidor no complexo enzima-substrato ou do substrato ao complexo enzima-inibidor (LEHNINGER;NELSON;COX , 2012)', font='Arial 11',anchor='w').pack()
    label_sobre_texto_x = tk.Label(window_inst, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto_5 = tk.Label(window_inst, width=1000, text='         A Inibição Não Competitiva, por sua vez, não altera o valor de Km, mas afeta a velocidade máxima (Vmax), gerando uma velocidade máxima aparente.', font='Arial 11',anchor='w').pack()
    load_1 = Image.open('NCompet_1.PNG')
    load_1_resized = load_1.resize((260,180), Image.ANTIALIAS)
    render_1 = ImageTk.PhotoImage(load_1_resized)
    img_1= tk.Label(window_inst, image = render_1, border = 0, borderwidth = 2, relief="solid")
    img_1.image = render_1
    img_1.place(x = 50, y = 260)
    load_2 = Image.open('NCompet_2.PNG')
    load_2_resized = load_2.resize((270,140), Image.ANTIALIAS)
    render_2 = ImageTk.PhotoImage(load_2_resized)
    img_2= tk.Label(window_inst, image = render_2, border = 0, borderwidth = 2, relief="solid")
    img_2.image = render_2
    img_2.place(x = 355, y = 280)
    load_3 = Image.open('NCompet_3.PNG')
    load_3_resized = load_3.resize((270,140), Image.ANTIALIAS)
    render_3 = ImageTk.PhotoImage(load_3_resized)
    img_3= tk.Label(window_inst, image = render_3, border = 0, borderwidth = 2, relief="solid")
    img_3.image = render_3
    img_3.place(x = 670, y = 280)

#Função Window Inibição Incompetitiva    
def Inib_3():
    window_inst = tk.Toplevel()
    window_inst.title("Inibição Incompetitiva")
    window_inst.geometry("1000x480")
    window_inst.minsize(width=1030, height=480)
    window_inst.resizable(0, 0)
    label_inst = tk.Label(window_inst, text='Inibição Incompetitiva', font='Arial 16 bold',bg='grey67').pack(fill='x')
    label_sobre_texto_x = tk.Label(window_inst, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_sobre_texto_x = tk.Label(window_inst, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto = tk.Label(window_inst, width=1000, text='            A inibição incompetitiva é a inibição reversível que ocorre quando a molécula inibidora não possui afinidade diretamente à enzima livre, apenas ao', font='Arial 11',anchor='w').pack()
    label_texto_2 = tk.Label(window_inst, width=1000, text='    complexo enzima-substrato (ES). Essa ligação do inibidor ao complexo se dá em um sítio diferente do centro ativo ao qual se liga o substrato ', font='Arial 11',anchor='w').pack()
    label_texto_3 = tk.Label(window_inst, width=1000, text='    formando o complexo enzima-substrato-inibidor, que é inativo (DORAN, 2013).', font='Arial 11',anchor='w').pack()
    label_sobre_texto_x = tk.Label(window_inst, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto_4 = tk.Label(window_inst, width=1000, text='        A inibição incompetitiva reduz os valores da constante Km e da Velocidade Máxima (Vmax), gerando valores aparentes dos dois parâmetros cinéticos.', font='Arial 11',anchor='w').pack()
    load_1 = Image.open('Incompet_1.PNG')
    load_1_resized = load_1.resize((260,180), Image.ANTIALIAS)
    render_1 = ImageTk.PhotoImage(load_1_resized)
    img_1= tk.Label(window_inst, image = render_1, border = 0, borderwidth = 2, relief="solid")
    img_1.image = render_1
    img_1.place(x = 50, y = 260)
    load_2 = Image.open('Incompet_2.PNG')
    load_2_resized = load_2.resize((280,200), Image.ANTIALIAS)
    render_2 = ImageTk.PhotoImage(load_2_resized)
    img_2= tk.Label(window_inst, image = render_2, border = 0, borderwidth = 2, relief="solid")
    img_2.image = render_2
    img_2.place(x = 360, y = 250)
    load_3 = Image.open('Incompet_3.PNG')
    load_3_resized = load_3.resize((270,140), Image.ANTIALIAS)
    render_3 = ImageTk.PhotoImage(load_3_resized)
    img_3= tk.Label(window_inst, image = render_3, border = 0, borderwidth = 2, relief="solid")
    img_3.image = render_3
    img_3.place(x = 690, y = 280)


def Doc_Michaelis():
    window_inst = tk.Toplevel()
    window_inst.title("Michaelis-Menten")
    window_inst.geometry("1000x480")
    window_inst.minsize(width=1030, height=680)
    window_inst.resizable(0, 0)
    label_inst = tk.Label(window_inst, text='Michaelis-Menten', font='Arial 16 bold',bg='grey67').pack(fill='x')
    label_texto_x = tk.Label(window_inst, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto_x = tk.Label(window_inst, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto = tk.Label(window_inst, width=1000, text='            O modelo de cinética enzimática proposto por Michaelis-Menten (1913) é um dos mais conhecidos na enzimologia e propõe duas etapas na reação', font='Arial 11',anchor='w').pack()
    label_texto_2 = tk.Label(window_inst, width=1000, text='    catalisada. Na primeira etapa, uma enzima (E) e um substrato (S) se ligam, formando o complexo enzima-substrato (ES), em uma reação reversível. Na', font='Arial 11',anchor='w').pack()
    label_texto_3 = tk.Label(window_inst, width=1000, text='    segunda etapa, este complexo (ES) é transformado em produto (P), com a regeneração da enzima integralmente', font='Arial 11',anchor='w').pack()
    label_texto_x = tk.Label(window_inst, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto_4 = tk.Label(window_inst, width=1000, text='        A equação de Michaelis-Menten considera uma condição em que a concentração do substrato é maior que a concentração da enzima. Nessa ', font='Arial 11',anchor='w').pack()
    label_texto_5 = tk.Label(window_inst, width=1000, text='    configuração reacional, a velocidade de reação é limitada, então, pela velocidade de catálise do complexo enzima-substrato. ', font='Arial 11',anchor='w').pack()
    label_sobre_texto_x = tk.Label(window_inst, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto_6 = tk.Label(window_inst, width=1000, text='        O modelo proposto descreve, portanto, as taxas de reações enzimáticas, relacionando a taxa de reação V, que se refere a taxa de formação de produto ', font='Arial 11',anchor='w').pack()
    label_texto_7 = tk.Label(window_inst, width=1000, text='    em relação a concentração de um substrato ([S]) (MARTINS, 2015).', font='Arial 11',anchor='w').pack()
    label_texto_x = tk.Label(window_inst, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto_8 = tk.Label(window_inst, width=1000, text='        Nesse sentido, a constante de Michaelis-Menten (KM) é igual à concentração de substrato cuja taxa de reação seja metade de Vmax, sendo caracterís-', font='Arial 11',anchor='w').pack()
    label_texto_9 = tk.Label(window_inst, width=1000, text='    tico de cada enzima (MICHAELIS; MENTEN, 1913).', font='Arial 11',anchor='w').pack()
    label_texto_x = tk.Label(window_inst, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto_10 = tk.Label(window_inst, width=1000, text='       Para altas concentrações de substrato, a velocidade de reação se aproxima da velocidade máxima (Vmax) e torna-se independente da concentração de', font='Arial 11',anchor='w').pack()
    label_texto_11 = tk.Label(window_inst, width=1000, text='   substrato. Para baixas concentrações de substrato, a velocidade inicial é proporcional à concentração de substrato (LEHNINGER; NELSON; COX, 2012).', font='Arial 11',anchor='w').pack()
    load_1 = Image.open('Grafico_MM.PNG')
    load_1_resized = load_1.resize((290,210), Image.ANTIALIAS)
    render_1 = ImageTk.PhotoImage(load_1_resized)
    img_1= tk.Label(window_inst, image = render_1, border = 0, borderwidth = 2, relief="solid")
    img_1.image = render_1
    img_1.place(x = 160, y = 445)
    load_2 = Image.open('Eq_MM.PNG')
    load_2_resized = load_2.resize((280,160), Image.ANTIALIAS)
    render_2 = ImageTk.PhotoImage(load_2_resized)
    img_2= tk.Label(window_inst, image = render_2, border = 0, borderwidth = 2, relief="solid")
    img_2.image = render_2
    img_2.place(x = 550, y = 470)


def Doc_Lineweaver():
    window_inst = tk.Toplevel()
    window_inst.title("Lineweaver-Burk")
    window_inst.geometry("1030x680")
    window_inst.minsize(width=1030, height=680)
    window_inst.resizable(0, 0)
    label_inst = tk.Label(window_inst, text='Lineweaver-Burk', font='Arial 16 bold',bg='grey67').pack(fill='x')
    label_texto_x = tk.Label(window_inst, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto_x = tk.Label(window_inst, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto = tk.Label(window_inst, width=1000, text='            A fim de facilitar a compreensão gráfica do Modelo de Michaelis-Menten, sua equação pode ser submetida ao método de linearização algébrica', font='Arial 11',anchor='w').pack()
    label_texto_2 = tk.Label(window_inst, width=1000, text='    proposto por Lineweaver-Burk (1934). A Equação de Lineweaver-Burk é obtida, portanto, através da inversão da Equação de Michaelis-Menten. ', font='Arial 11',anchor='w').pack()
    label_texto_x = tk.Label(window_inst, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto_3 = tk.Label(window_inst, width=1000, text='        O modelo, conhecido como duplo recíproco, é representado por uma equação algébrica de primeiro grau, com coeficiente angular equivalente à relação ', font='Arial 11',anchor='w').pack()
    label_texto_4 = tk.Label(window_inst, width=1000, text='    entre KM e Vmax e com coeficiente angular do valor inverso de Vmax (LEHNINGER; NELSON; COX, 2012).', font='Arial 11',anchor='w').pack()
    label_texto_x = tk.Label(window_inst, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto_5 = tk.Label(window_inst, width=1000, text='        Segundo Doran (2013), no gráfico, de eixos 1/[S] e 1/V, pode-se determinar os valores de KM e Vmax, visto que a intersecção do eixo das abcissas ', font='Arial 11',anchor='w').pack()
    label_texto_6 = tk.Label(window_inst, width=1000, text='    é equivalente a -1/KM, enquanto a intersecção do eixo das ordenadas é equivalente a 1/ Vmax. ', font='Arial 11',anchor='w').pack()
    label_texto_x = tk.Label(window_inst, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto_7 = tk.Label(window_inst, width=1000, text='       Apesar de muito utilizado na diferenciação qualitativa dos mecanismos de catálise enzimática e na análise dos modelos de inibição, o modelo linearizado ', font='Arial 11',anchor='w').pack()
    label_texto_8 = tk.Label(window_inst, width=1000, text='    de Lineweaver-Burk não é considerado apropriado para a determinação dos parâmetros cinéticos, uma vez que distorce o erro experimental,', font='Arial 11',anchor='w').pack()
    label_texto_9 = tk.Label(window_inst, width=1000, text='   especialmente em baixas concentrações de substrato (LEHNINGER; NELSON; COX, 2012; PEREIRA et al, 2015).', font='Arial 11',anchor='w').pack()
    load_1 = Image.open('Grafico_LB.PNG')
    load_1_resized = load_1.resize((330,280), Image.ANTIALIAS)
    render_1 = ImageTk.PhotoImage(load_1_resized)
    img_1= tk.Label(window_inst, image = render_1, border = 0, borderwidth = 2, relief="solid")
    img_1.image = render_1
    img_1.place(x = 160, y = 370)
    load_2 = Image.open('Eq_LB.PNG')
    load_2_resized = load_2.resize((280,160), Image.ANTIALIAS)
    render_2 = ImageTk.PhotoImage(load_2_resized)
    img_2= tk.Label(window_inst, image = render_2, border = 0, borderwidth = 2, relief="solid")
    img_2.image = render_2
    img_2.place(x = 570, y = 430)

def Doc_Batelada():
    window_inst = tk.Toplevel()
    window_inst.title("Batelada")
    window_inst.geometry("1060x680")
    window_inst.minsize(width=1030, height=680)
    window_inst.resizable(0, 0)
    label_inst = tk.Label(window_inst, text='Operação em Batelada', font='Arial 16 bold',bg='grey67').pack(fill='x')
    label_texto_x = tk.Label(window_inst, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto_x = tk.Label(window_inst, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto = tk.Label(window_inst, width=1000, text='            As reações de catálise enzimática ocorrem nos chamados biorreatores, nos quais as enzimas utilizadas podem encontrar-se livres no meio reacional ou ', font='Arial 11',anchor='w').pack()
    label_texto_2 = tk.Label(window_inst, width=1000, text='   imobilizadas. Os biorreatores são sistemas onde ocorrem reações biológicas, ambiente adequado para síntese de bioprodutos e crescimento celular', font='Arial 11',anchor='w').pack()
    label_texto_2 = tk.Label(window_inst, width=1000, text='   (SCHMIDELL et al., 2001).', font='Arial 11',anchor='w').pack()    
    label_texto_x = tk.Label(window_inst, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto_3 = tk.Label(window_inst, width=1000, text='        Entre a grande variedade de biorreatores, constata-se que o mais difundido e empregado é o biorreator de mistura (STR) em modo de operação e batelada,', font='Arial 11',anchor='w').pack()
    label_texto_4 = tk.Label(window_inst, width=1000, text='   em especial em processos fermentativos e farmacêuticos laboratoriais e industriais (FOGLER, 1999).', font='Arial 11',anchor='w').pack()
    label_texto_x = tk.Label(window_inst, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto_5 = tk.Label(window_inst, width=1000, text='        Neste modo de operação, os reatores operam em sistema fechado, sem variação volumétrica (V0 = Vf). O substrato e o produto são alimentados no início ', font='Arial 11',anchor='w').pack()
    label_texto_6 = tk.Label(window_inst, width=1000, text='   da operação (T0) em suas concentrações iniciais ([S]0 e [P]0), juntamente com a enzima, que por ser apenas um biocatalisador de concentração constante, ', font='Arial 11',anchor='w').pack()
    label_texto_7 = tk.Label(window_inst, width=1000, text='   não é considerada no balanço de massa do sistema. Depois do tempo de reação, a enzima, o produto e o substrato (caso a conversão substrato-produto ', font='Arial 11',anchor='w').pack()
    label_texto_8 = tk.Label(window_inst, width=1000, text='   não seja integral) são retirados apenas ao fim da operação (Tf), não ocorrendo a entrada ou saída de matéria durante toda a reação de catálise', font='Arial 11',anchor='w').pack()
    label_texto_9 = tk.Label(window_inst, width=1000, text='   (FOGLER, 1999).', font='Arial 11',anchor='w').pack()
    load_1 = Image.open('Batelada.PNG')
    load_1_resized = load_1.resize((390,220), Image.ANTIALIAS)
    render_1 = ImageTk.PhotoImage(load_1_resized)
    img_1= tk.Label(window_inst, image = render_1, border = 0, borderwidth = 2, relief="solid")
    img_1.image = render_1
    img_1.place(x = 50, y = 390)
    load_2 = Image.open('BM.PNG')
    load_2_resized = load_2.resize((250,170), Image.ANTIALIAS)
    render_2 = ImageTk.PhotoImage(load_2_resized)
    img_2= tk.Label(window_inst, image = render_2, border = 0, borderwidth = 2, relief="solid")
    img_2.image = render_2
    img_2.place(x = 490, y = 410)
    load_3 = Image.open('Conversao.PNG')
    load_3_resized = load_3.resize((200,100), Image.ANTIALIAS)
    render_3 = ImageTk.PhotoImage(load_3_resized)
    img_3= tk.Label(window_inst, image = render_3, border = 0, borderwidth = 2, relief="solid")
    img_3.image = render_3
    img_3.place(x = 780, y = 435)
    
#Função Window Sobre
def Sobre():
    window_sobre = tk.Toplevel()
    window_sobre.title("Sobre")
    window_sobre.geometry("1010x480")
    window_sobre.minsize(width=1010, height=480)
    window_sobre.resizable(0, 0)
    label_sobre = tk.Label(window_sobre, text='Sobre', font='Arial 16 bold',bg='grey67').pack(fill='x')
    label_sobre_texto_x = tk.Label(window_sobre, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_sobre_texto_1 = tk.Label(window_sobre, width=1000, text='        Enzinetics é um software desenvolvido totalmente em linguagem python, a nível back-end e front-end com o objetivo de facilitar o estudo e ', font='Arial 11',anchor='w').pack()
    label_sobre_texto_2 = tk.Label(window_sobre, width=1000, text='  compreensão de modelos de cinéticas enzimáticas. ', font='Arial 11',anchor='w').pack()
    label_sobre_texto_x = tk.Label(window_sobre, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_sobre_texto_3 = tk.Label(window_sobre, width=1000, text='        Através da simulação e modelagem em batelada de 6 diferentes modelos cinéticos, já descritos na literatura, o programa permite  a inserção', font='Arial 11',anchor='w').pack()
    label_sobre_texto_4 = tk.Label(window_sobre, width=1000, text='  de parâmetros cinéticos para simulação, e arquivos excel para modelagem, em uma interface user-friendly e intuitiva. ', font='Arial 11',anchor='w').pack()
    label_sobre_texto_x = tk.Label(window_sobre, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_sobre_texto_5 = tk.Label(window_sobre, width=1000, text='        As documentações e referências bibliográficas utilizadas, encontram-se disponíveis na seção Documentação, facilitando ainda mais o aprendizado.', font='Arial 11',anchor='w').pack()
    label_sobre_texto_x = tk.Label(window_sobre, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_sobre_texto_6 = tk.Label(window_sobre, width=1000, text='        Desenvolvido inicialmente como Trabalho de Conclusão de Curso do Curso de Engenharia de Bioprocessos e Biotecnologia da Universidade ', font='Arial 11',anchor='w').pack()            
    label_sobre_texto_7 = tk.Label(window_sobre, width=1000, text='  Estadual Júlio de  Mesquita Filho (UNESP – Araraquara), com orientação do Prof. Dr. Marcel Cerri, teve sua versão inicial disponibilizada no ano de 2023.', font='Arial 11',anchor='w').pack()
    label_sobre_texto_x = tk.Label(window_sobre, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_sobre_texto_x = tk.Label(window_sobre, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_sobre_texto_x = tk.Label(window_sobre, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_sobre_texto_8 = tk.Label(window_sobre, width=1000, text='        Contato: mayra.valvano@unesp.br', font='Arial 11 bold',anchor='w').pack()
    label_sobre_texto_9 = tk.Label(window_sobre, width=1000, text='        Engenharia de Bioprocessos e Biotecnologia', font='Arial 11',anchor='w').pack()
    label_sobre_texto_10 = tk.Label(window_sobre, width=1000, text='        Faculdade de Ciências Farmacêuticas', font='Arial 11',anchor='w').pack()
    label_sobre_texto_11 = tk.Label(window_sobre, width=1000, text='        Universidade Estadual Paulista Júlio de Mesquita Filho (UNESP - Araraquara)', font='Arial 11',anchor='w').pack()
    label_sobre_texto_x = tk.Label(window_sobre, width=1000, text=' ', font='Arial 11',anchor='w').pack()


#Função Window Referências Bibliográficas
def Referencias():
    window_ref = tk.Toplevel()
    window_ref.title("Referências Bibliográficas")
    window_ref.geometry("1100x580")
    window_ref.minsize(width=1100, height=580)
    window_ref.resizable(0, 0)
    label_ref = tk.Label(window_ref, text='Referências Bibliográficas', font='Arial 16 bold',bg='grey67').pack(fill='x')
    label_texto_x = tk.Label(window_ref, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto_x = tk.Label(window_ref, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto_2 = tk.Label(window_ref, width=1000, text='     BORZANI, W. et al. Biotecnologia Industrial: Fundamentos. São Paulo: Edgard Blucher Ltda. vol. 1. 254 p., 2001. ', font='Arial 11',anchor='w').pack()
    label_texto_x = tk.Label(window_ref, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto_1 = tk.Label(window_ref, width=1000, text='     DORAN, P. M. Bioprocess Engineering Principles. 2. ed. United Kingdom: Elsevier, 2013.', font='Arial 11',anchor='w').pack()
    label_texto_x = tk.Label(window_ref, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto_1 = tk.Label(window_ref, width=1000, text='     FOGLER, H. S. Elements of Chemical Reaction Enineering. Chemical Engineering Guide, Michigan Engineering, 1999.', font='Arial 11',anchor='w').pack()
    label_texto_x = tk.Label(window_ref, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto_5 = tk.Label(window_ref, width=1000, text='     LEHNINGER, T. M.; NELSON, D. L.; COX, M. M. Princípios de Bioquímica. 6ª Edição. Ed. Artmed, 2012. ', font='Arial 11',anchor='w').pack()
    label_texto_x = tk.Label(window_ref, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto_5 = tk.Label(window_ref, width=1000, text='     LINEWEAVER, H; BURK, D. The determination of enzyme dissociation constantes. Journal od the American Chemical Society. vol. 56, n. 3, p. 658-666, 1934.', font='Arial 11',anchor='w').pack()
    label_texto_x = tk.Label(window_ref, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto_3 = tk.Label(window_ref, width=1000, text='     MARTINS, A. R. Represemtação do efeito de inibição enzimática reversível para o modelo cinético de Michaelis-Menten no estado transiente. Brazilian Journal of ', font='Arial 11',anchor='w').pack()
    label_texto_3 = tk.Label(window_ref, width=1000, text='     Food Technology, vol.18, n.2, p-112-120. Campinas, 2015.', font='Arial 11',anchor='w').pack()
    label_texto_x = tk.Label(window_ref, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto_4 = tk.Label(window_ref, width=1000, text='     MICHAELIS L, MENTEN ML. Die Kinetik der Invertinwirkung. Biochem, 1913. Tradução: Johnson KA, Goody RS. The Original Michaelis ', font='Arial 11',anchor='w').pack()
    label_texto_4 = tk.Label(window_ref, width=1000, text='     Constant: Translation of the 1913 Michaelis–Menten Paper. Biochemistry, 2011.', font='Arial 11',anchor='w').pack()
    label_texto_x = tk.Label(window_ref, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto_6 = tk.Label(window_ref, width=1000, text='     PEREIRA, A. S. et al. Implementação em linguagem python de métodos de estimação e comparação de parâmetros cinéticos aplicados a hidrólise catalisada por ', font='Arial 11',anchor='w').pack()
    label_texto_6 = tk.Label(window_ref, width=1000, text='     ALDC. XI Congresso Brasileiro de Engenharia Química em Iniciação Científica. Unicamp – Campinas – SP, 2015.', font='Arial 11',anchor='w').pack()
    label_texto_x = tk.Label(window_ref, width=1000, text=' ', font='Arial 11',anchor='w').pack()
    label_texto_6 = tk.Label(window_ref, width=1000, text='     SCHIMIDELL, W. et al. Biotecnologia Industrial: Engenharia Bioquímica. São Paulo: Edgard Blucher Ltda. vol. 2, 541 p., 2011.', font='Arial 11',anchor='w').pack()

#Função Window Simulação
def Window_Simulation():
    
    window_sim = tk.Toplevel()
    window_sim.title("Simulação")
    window_sim.geometry("1280x680")
    window_sim.minsize(width=1270, height=680)
    window_sim.resizable(0, 0)
    label_sim = tk.Label(window_sim, text='SIMULAÇÃO', font='Arial 16 bold', width = 500, bg='grey67').pack()
    
    #Modo Operação
    titulo_batelada = tk.Label(window_sim, text="Modo de Operação: Batelada", font ='Arial 12 bold', width = 45, height = 1, 
                               bg = "grey78").place(x = 5, y = 35)

    #Imagem Biorreator
    load = Image.open('biorreator.png')
    load_resized = load.resize((190,175), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load_resized)
    img = tk.Label(window_sim, image = render, border = 0, borderwidth = 2, relief="solid")
    img.image = render
    img.place(x = 5, y = 65)
    
    #Balanço de Massa
    balanco_massa = tk.Frame(window_sim, width = 257, height = 180, bg='grey85').place(x = 205, y = 65)
    titulo_balaco_massa = tk.Label(window_sim, bg='grey85', font="Arial 10 bold", text='Balanço de Massa').place(x = 265, y = 67)
    bm_1 = tk.Label(window_sim, text='Acúmulo = Entrada - Saída - Reação', font ='Arial 10 italic', bg='grey85').place(x = 220, y = 90)
    bm_2 = tk.Label(window_sim, text='Acúmulo = - Reação', font ='Arial 10 italic', bg='grey85').place(x = 255, y = 110)
    bm_3 = tk.Label(window_sim, text='d(V.[S]) = - (r . V)', font ='Arial 10 italic', bg='grey85').place(x = 265, y = 133)
    bm_4 = tk.Label(window_sim, text='_________________', font ='Arial 3 italic', bg='grey85').place(x = 270, y = 151)
    bm_5 = tk.Label(window_sim, text='dt', font ='Arial 10 italic', bg='grey85').place(x = 277, y = 161)
    bm_6 = tk.Label(window_sim, text='d[S] = - ( Vmax * [S] )', font ='Arial 10 italic', bg='grey85').place(x = 268, y = 185)
    bm_7 = tk.Label(window_sim, text='________               ___________________________________________', font ='Arial 3 italic', bg='grey85').place(x = 270, y = 203)
    bm_8 = tk.Label(window_sim, text='dt        Km + [S]', font ='Arial 10 italic', bg='grey85').place(x = 270, y = 213)
   
    #Parâmetros
    #Título
    frame_parametros = tk.Frame(window_sim, width = 458, height=80, bg='grey85').place(x = 5, y = 251)
    parametros_label = tk.Label(window_sim, text='Parâmetros', font = 'Arial 10 bold', bg='grey85').place(x = 180, y = 255)
    #Km
    text_km = tk.StringVar()
    km_label = tk.Label(window_sim, text='Km:', font = 'Arial 10 bold', bg='grey85').place(x = 21, y = 290)
    textbox_km = ttk.Entry(window_sim, textvariable=text_km, width = 7).place(x = 53, y = 290)
    km_unid = tk.Label(window_sim, text='mol/L', font = 'Arial 9', bg='grey85').place(x = 103, y = 290)
    #Eo -> Concentração de Enzima Inicial
    text_e0 =tk.StringVar()
    e0_label = tk.Label(window_sim, text='E0:', font = 'Arial 10 bold', bg='grey85').place(x = 165, y = 290)
    textbox_e0 = ttk.Entry(window_sim, textvariable=text_e0, width = 7).place(x = 200, y = 290)
    e0_unid = tk.Label(window_sim, text='mol/L', font = 'Arial 9', bg='grey85').place(x = 255, y = 290)
    #Kcat da enzima
    text_kcat = tk.StringVar()
    kcat_label = tk.Label(window_sim, text='Kcat:', font = 'Arial 10 bold', bg='grey85').place(x = 310, y = 290)
    textbox_kcat = ttk.Entry(window_sim, textvariable=text_kcat, width = 7).place(x = 360, y = 290)
    kcat_unid = tk.Label(window_sim, text='1/s', font = 'Arial 9', bg='grey85').place(x = 420, y = 290)
    
    #Inibição
    frame_inibition = tk.Frame(window_sim, width = 458, height=170, bg='grey85').place(x = 5, y = 338)
    inibition_label = tk.Label(window_sim, text='Tipo de Inibição: ', font = 'Arial 10 bold', bg='grey85').place( x = 40, y = 345)
    inibition_list = ttk.Combobox(window_sim, width=28)
    inibition_list['values'] = ('Sem Inibição', 'Competitiva', 'Não Competitiva', 'Incompetitiva')
    inibition_list.place(x = 210, y = 345)
    
    #Função Altera Frame da Inibição, de acordo com o valor selecionado no combobox
    def on_select(event):
        selected = event.widget.get()
        
        if selected == "Sem Inibição":
            frame_1 = tk.Label(window_sim, bg='grey85', width=25, height=7).place(x=9, y =380)
            frame_1_formulas = tk.Label(window_sim, bg='grey85', width=36, height=8).place(x=200, y =370)
            
        elif selected == "Competitiva":
            frame_2 = tk.Label(window_sim, bg='grey85', width=25, height=7).place(x=9, y =380)
            frame_2_formulas = tk.Label(window_sim, bg='gray85', width=36, height=8).place(x=200, y =370)
            label_2_formula = tk.Label(window_sim, bg = 'gray85', text=' Km_ap  =  Km * ( 1 + I )', font='Arial 10 italic').place(x= 250, y = 400)
            label_2_formula_2 = tk.Label(window_sim, bg = 'gray85', text='   ____', font='Arial 5 italic').place(x= 370, y = 420)
            label_2_formula_3 = tk.Label(window_sim, bg = 'gray85', text='              Ki', font='Arial 10 italic').place(x= 320, y = 430)
            
            global label_2_i_text
            label_2_i_text = tk.StringVar()
            label_2_i = tk.Label(window_sim, text='I:', font = 'Arial 10', bg='grey85').place(x=30, y = 400)
            textbox_2_i = ttk.Entry(window_sim, textvariable=label_2_i_text, width = 7).place(x = 65, y = 400)
            unid_2_i = tk.Label(window_sim, text='mol/L', font = 'Arial 9', bg='grey85').place(x = 115, y = 400)  
            
            global label_2_ki_text 
            label_2_ki_text = tk.StringVar()
            label_2_ki = tk.Label(window_sim, text='Ki:', font = 'Arial 10', bg='grey85').place(x=30, y =440)
            textbox_2_ki = ttk.Entry(window_sim, textvariable=label_2_ki_text, width = 7).place(x = 65, y = 440)
            unid_2_ki = tk.Label(window_sim, text='mol/L', font = 'Arial 9', bg='grey85').place(x = 115, y = 440)
            
        
        elif selected == "Não Competitiva":
            frame_3 = tk.Label(window_sim, bg='grey85', width=25, height=7).place(x=9, y =380)
            frame_3_formulas =  tk.Label(window_sim, bg='gray85', width=36, height=8).place(x=200, y =370)
            label_3_formula = tk.Label(window_sim, bg = 'gray85', text=' Vmax_ap  =         Vmax', font='Arial 10 italic').place(x= 250, y = 400)
            label_3_formula_2 = tk.Label(window_sim, bg = 'gray85', text=' __________________', font='Arial 5 italic').place(x= 335, y = 420)
            label_3_formula_3 = tk.Label(window_sim, bg = 'gray85', text='   1  +  ( I / Ki )', font='Arial 10 italic').place(x= 325, y = 430)
            
            global label_3_i_text
            label_3_i_text = tk.StringVar()
            label_3_i = tk.Label(window_sim, text='I:', font = 'Arial 10', bg='grey85').place(x=30, y = 400)
            textbox_3_i = ttk.Entry(window_sim, textvariable=label_3_i_text, width = 7).place(x = 65, y = 400)
            unid_3_i = tk.Label(window_sim, text='mol/L', font = 'Arial 9', bg='grey85').place(x = 115, y = 400)  
            
            global label_3_ki_text
            label_3_ki_text = tk.StringVar()
            label_3_ki = tk.Label(window_sim, text='Ki:', font = 'Arial 10', bg='grey85').place(x=30, y =440)
            textbox_3_ki = ttk.Entry(window_sim, textvariable=label_3_ki_text, width = 7).place(x = 65, y = 440)
            unid_3_ki = tk.Label(window_sim, text='mol/L', font = 'Arial 9', bg='grey85').place(x = 115, y = 440)
        
        else:
            frame_4 = tk.Label(window_sim, bg='grey85', width=25, height=7).place(x=9, y =380)
            frame_4_formulas =  tk.Label(window_sim, bg='gray85', width=36, height=8).place(x=200, y =370)
            label_4_formula = tk.Label(window_sim, bg = 'gray85', text=' Vmax_ap  =        Vmax', font='Arial 10 italic').place(x= 250, y = 380)
            label_4_formula_2 = tk.Label(window_sim, bg = 'gray85', text=' _________________', font='Arial 5 italic').place(x= 335, y = 400)
            label_4_formula_3 = tk.Label(window_sim, bg = 'gray85', text=' 1  +  ( I / Ki )', font='Arial 10 italic').place(x= 325, y = 410)
            label_4_formula_4 = tk.Label(window_sim, bg = 'gray85', text=' Km_ap  =             Km', font='Arial 10 italic').place(x= 250, y = 440)
            label_4_formula_5 = tk.Label(window_sim, bg = 'gray85', text=' __________________', font='Arial 5 italic').place(x= 335, y = 460)
            label_4_formula_6 = tk.Label(window_sim, bg = 'gray85', text='   1  +  ( I / Ki )', font='Arial 10 italic').place(x= 325, y = 470)
            
            global label_4_i_text
            label_4_i_text = tk.StringVar()
            label_4_i = tk.Label(window_sim, text='I:', font = 'Arial 10', bg='grey85').place(x=30, y = 400)
            textbox_4_i = ttk.Entry(window_sim, textvariable=label_4_i_text, width = 7).place(x = 65, y = 400)
            unid_4_i = tk.Label(window_sim, text='mol/L', font = 'Arial 9', bg='grey85').place(x = 115, y = 400)  
            
            global label_4_ki_text
            label_4_ki_text = tk.StringVar()
            label_4_ki = tk.Label(window_sim, text='Ki:', font = 'Arial 10', bg='grey85').place(x=30, y =440)
            textbox_4_ki = ttk.Entry(window_sim, textvariable=label_4_ki_text, width = 7).place(x = 65, y = 440)
            unid_4_ki = tk.Label(window_sim, text='mol/L', font = 'Arial 9', bg='grey85').place(x = 115, y = 440)
            
    inibition_list.bind('<<ComboboxSelected>>', on_select)
    
    #Estequeometria
    frame_esteq = tk.Frame(window_sim, width = 204, height=80, bg='grey85').place(x = 5, y = 515)
    esteq_label = tk.Label(window_sim, text='Estequiometria da Reação', font = 'Arial 10 bold', bg='grey85').place(x = 20, y = 520)
    S_label = tk.Label(window_sim, text='1 S  ---- >  ', font = 'Arial 10 bold', bg='grey85').place(x = 50, y = 560)
    P_text = tk.StringVar()
    textbox_P = ttk.Entry(window_sim, textvariable = P_text, width = 4).place(x = 125, y = 560)
    P_label = tk.Label(window_sim, text=' P', font = 'Arial 10 bold', bg='grey85').place(x = 155, y = 560)
    
    #Tempo
    frame_tempo = tk.Frame(window_sim, width = 204, height=75, bg='grey85').place(x = 5, y = 600)
    tempo_label = tk.Label(window_sim, text='Tempo de Reação', font = 'Arial 10 bold', bg='grey85').place(x = 48, y = 605)
    t_text = tk.StringVar()
    textbox_t = ttk.Entry(window_sim, textvariable = t_text, width = 6).place(x = 120, y = 642)
    t_label = tk.Label(window_sim, text='Tempo (min):', font = 'Arial 10', bg='grey85').place(x = 25, y = 640)
    
    #Concentrações Entrada
    frame_initial_cond = tk.Frame(window_sim, width = 249, height=160, bg='grey85').place(x = 213, y = 515)
    initial_cond_label = tk.Label(window_sim, text='Concentrações Iniciais', font = 'Arial 10 bold', bg='grey85').place(x = 262, y = 520)
    s0_label = tk.Label(window_sim, text='S0:', font = 'Arial 10 bold', bg='grey85').place(x = 270, y = 555)
    s0_text = tk.StringVar()
    textbox_s0 = ttk.Entry(window_sim, textvariable=s0_text, width = 7).place(x = 300, y = 555)
    s0_unid = tk.Label(window_sim, text='mol/L', font = 'Arial 10', bg='grey85').place(x = 350, y = 555)
    p0_label = tk.Label(window_sim, text='P0:', font = 'Arial 10 bold', bg='grey85').place(x = 270, y = 595)
    p0_text = tk.StringVar()
    textbox_p0 = ttk.Entry(window_sim, textvariable=p0_text, width = 7).place(x = 300, y = 595)
    p0_unid = tk.Label(window_sim, text='mol/L', font = 'Arial 10', bg='grey85').place(x = 350, y = 595)
    
    #Equação diferencial -> Balanço de Massa
    def eq_dif(C,t, km, E0, Kcat):
        s = C[0]
        p = C[1]

        dSdt = - (E0 * Kcat * s)/(km+s)
        dPdt = (E0 * Kcat * s)/(km+s)

        return [dSdt, dPdt]
    
    #Função para plotar gráficos da simulação
    def plot_sim():
       
        #Variáveis modelo
        E0 = float(text_e0.get())
        Kcat = float(text_kcat.get())
        Km = float(text_km.get())
        s0 = float(s0_text.get())
        p0 = float(p0_text.get())
        t_input = float(t_text.get())
        
        if inibition_list.get() == "Competitiva":
            
            I = float(label_2_i_text.get())
            Ki = float(label_2_ki_text.get())
                
            Km = Km * (1 + (I/Ki))
                    
        if inibition_list.get() == "Não Competitiva":
            I = float(label_3_i_text.get())
            Ki = float(label_3_ki_text.get())
            
            Vmax = (E0 * Kcat)/(1+ (I/Ki))
            
        if inibition_list.get() == "Incompetitiva":
            I = float(label_4_i_text.get())
            Ki = float(label_4_ki_text.get())
            
            Vmax = (E0 * Kcat)/(1 + (I/Ki))
            Km = Km/(1 + (I/Ki))
        
        #Variáveis Estequiometria de Reação
        esteq_s = 1    # Número de mols de S é sempre 1 para Michaelis-Menten
        esteq_p = float(P_text.get())

        # Criando o conjunto de dados artificiais -> ARRAY
        n_ptos = int(101)               #Número de pontos experimentais: 100 pontos
        s = np.linspace(0,s0, n_ptos)   #Gera um array com n_ptos de concentração de substrato (s) de 0 a s_max
        Vmax = E0 * Kcat                #Cálculo da Velocidade Máxima
        v = modelo(s,Vmax,Km)           #Calcula a velocidade para cada s (concentração) do array através da função modelo

        #Concentração por Tempo
        t = np.linspace(0,t_input, int(t_input)+1) #(0 a t_input minutos de reação, minuto a minuto)

        C0 = [s0,p0] #Concentração Inicial

        C= odeint(eq_dif, C0, t, args = (Km, E0, Kcat)) #Resolução EDO
        
        conv = f_conversao(s0, C[:,1])

        #Gráficos

        #Quadrante 1 -> Velocidade x Substrato
        fig, axs = plt.subplots(2, 2, figsize=(11.1, 8.4))
        axs[0,0].plot(s,v, ls='-', color='firebrick', markersize=3)
        axs[0,0].set_title('Velocidade x Substrato', fontsize=12, weight='bold')
        axs[0,0].set_xlabel('[S] (mol/L)', fontsize=10, weight='bold')
        axs[0,0].set_ylabel('V (-mol/(L*min))', fontsize=10, weight='bold')

        #Quadrante 2 -> 1/Velocidade x 1/Substrato
        np.seterr(divide='ignore', invalid='ignore')
        axs[0,1].plot(1/s,1/v, ls='-', color = 'darkorange', markersize=3)
        axs[0,1].set_title('1/ Velocidade x 1/ Substrato', fontsize=12, weight='bold')
        axs[0,1].set_xlabel('1/[S]', fontsize=10, weight='bold')
        axs[0,1].set_ylabel('1/V', fontsize=10, weight='bold')

        #Quadrante 3 -> Concentração (Substrato e Produto) x Tempo
        axs[1,0].plot(t,C[:,0], ls= '-', color='navy', label='Substrato')
        axs[1,0].plot(t,C[:,1], ls='-', color='dodgerblue', label ='Produto')
        axs[1,0].set_title('Concentração x Tempo', fontsize=12, weight='bold')
        axs[1,0].set_xlabel('Tempo (min)', fontsize=10, weight='bold')
        axs[1,0].set_ylabel('Concentração (mol/L)', fontsize=10, weight='bold')
        axs[1,0].legend(loc='best')

        #Quadrante 4 -> Conversão x Tempo
        axs[1,1].plot(t, conv, ls='-', color='seagreen')
        axs[1,1].set_title('Conversão x Tempo', fontsize=12, weight='bold')
        axs[1,1].set_xlabel('Tempo (min)', fontsize=10, weight='bold')
        axs[1,1].set_ylabel('Conversão (%)', fontsize=10, weight='bold')
        
        plt.style.use('ggplot')
        fig.tight_layout()
                        
        canvas = FigureCanvasTkAgg(fig, window_sim)   
        canvas.get_tk_widget().place(x = 470 , y = 35)
        
        df_saida_sim = pd.DataFrame({'Tempo (min)': t, '[S] (mol/L)': C[:,0], '[P] (mol/L)': C[:,1]})
        df_s_v = pd.DataFrame({'[S] (mol/L)': s, 'V (-mol/(L*min)': v})
        with pd.ExcelWriter('Dados_Saida_Simulacao.xlsx') as writer:
            df_saida_sim.to_excel(writer, sheet_name="Dados_S_P")
            df_s_v.to_excel(writer, sheet_name="Dados_S_V")
            writer.save()
            
    #Função Salvar Gráficos
    def salvar():
        a = asksaveasfilename(filetypes=(("PNG Image", "*.png"),("All Files", "*.*")), 
        defaultextension='.png')
        plt.savefig(a)
    
    def excel_saida_sim():
        os.system("start EXCEL Dados_Saida_Simulacao.xlsx")
    
    #Frames Gráficos e Botões
    frame_buttons = tk.Frame(window_sim, width = 800, height=34, bg='grey85').place(x = 470, y = 640)
    frame_graf_1 = tk.Frame(window_sim, width = 800, height=600, bg='white').place(x = 470, y = 35)
    
    #Botões
    button_sim = tk.Button(window_sim, font = 'Arial 10 bold', text='Simular', width = 15, command=plot_sim).place(x = 480, y = 643)
    button_export = tk.Button(window_sim, font='Arial 10 bold', text="Exportar Gráficos", width = 15, command=salvar).place(x = 620, y = 643)
    button_excel = tk. Button(window_sim, font='Arial 10 bold', text="Arquivo Excel", width = 15, command=excel_saida_sim).place(x = 760, y = 643)
    
def Window_Modelling():
    window_model = tk.Toplevel()
    window_model.title("Modelagem")
    window_model.geometry("470x680")
    window_model.minsize(width=470, height=480)
    window_model.resizable(0, 0)
    label_model = tk.Label(window_model, text='MODELAGEM', font='Arial 16 bold', width = 100, bg='grey67').pack()
    
    #Modo Operação
    titulo_batelada = tk.Label(window_model, text="Modo de Operação: Batelada", font ='Arial 12 bold', width = 45, height = 1, 
                               bg = "grey78").place(x = 5, y = 35)

    #Imagem Biorreator
    load = Image.open('biorreator.png')
    load_resized = load.resize((190,175), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load_resized)
    img = tk.Label(window_model, image = render, border = 0, borderwidth = 2, relief="solid")
    img.image = render
    img.place(x = 5, y = 65)
    
    #Balanço de Massa
    balanco_massa = tk.Frame(window_model, width = 257, height = 180, bg='grey85').place(x = 205, y = 65)
    titulo_balaco_massa = tk.Label(window_model, bg='grey85', font="Arial 10 bold", text='Balanço de Massa').place(x = 265, y = 67)
    bm_1 = tk.Label(window_model, text='Acúmulo = Entrada - Saída - Reação', font ='Arial 10 italic', bg='grey85').place(x = 220, y = 90)
    bm_2 = tk.Label(window_model, text='Acúmulo = - Reação', font ='Arial 10 italic', bg='grey85').place(x = 255, y = 110)
    bm_3 = tk.Label(window_model, text='d(V.[S]) = - (r . V)', font ='Arial 10 italic', bg='grey85').place(x = 265, y = 133)
    bm_4 = tk.Label(window_model, text='_________________', font ='Arial 3 italic', bg='grey85').place(x = 270, y = 151)
    bm_5 = tk.Label(window_model, text='dt', font ='Arial 10 italic', bg='grey85').place(x = 277, y = 161)
    bm_6 = tk.Label(window_model, text='d[S] = - ( Vmax * [S] )', font ='Arial 10 italic', bg='grey85').place(x = 268, y = 185)
    bm_7 = tk.Label(window_model, text='________               ______________________________________', font ='Arial 3 italic', bg='grey85').place(x = 270, y = 203)
    bm_8 = tk.Label(window_model, text='dt        Km + [S]', font ='Arial 10 italic', bg='grey85').place(x = 270, y = 213)
   
    #Importação Arquivo
    #Título
    frame_arquivo = tk.Frame(window_model, width = 458, height=80, bg='grey85').place(x = 5, y = 251)
    arquivo_label = tk.Label(window_model, text='Arquivo', font = 'Arial 10 bold', bg='grey85').place(x = 190, y = 255)
    #Imagem Excel
    load = Image.open('excel.png')
    load_resized = load.resize((60,60), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load_resized)
    img = tk.Label(window_model, image = render, border = 0, borderwidth = 2, relief="solid")
    img.image = render
    img.place(x = 15, y = 260)
    
    #Template EXCEL
    def excel_template():
        df_t = pd.DataFrame({'Tempo (t)':[]})
        df_S = pd.DataFrame({'[S] (mol/L)':[]})
        df_P = pd.DataFrame({'[P] (mol/L)':[]})
        df_dad_exp = pd.concat([df_t, df_S, df_P], axis=0)
        with pd.ExcelWriter('Template_Entrada_Dados.xlsx') as writer:
            df_dad_exp.to_excel(writer, sheet_name="C_t_exp", index=False)
            writer.save()
        os.system("start EXCEL Template_Entrada_Dados.xlsx")
    
    def explorer():
        explorador = askopenfilename()
        nome_arquivo = os.path.basename(explorador)
        # Captura dos dados de entrada - formato dataframe:
        excel_entrada = pd.read_excel(explorador)
        excel_entrada_np = excel_entrada.values
        
        global exp_t
        global exp_C
        
        exp_t = excel_entrada_np[:,0]
        exp_C = (excel_entrada_np[:,1:3])
        P_0 = [exp_C[0,0], exp_C[0,1]]
        
        #Equação Diferencial: Balanço de Mas
        def eq_dif(C, t, *args):
            km, Vmax = args
            S, P = C 
            dSdt = - Vmax*S/(km + S)
            dPdt = Vmax*S/(km + S)

            return [dSdt, dPdt]

        # Função objetiva para o algoritmo genético
        def func_ob_ag(parametros, *dados):
            # km e Vmax = parametros
            exp_t, exp_C = dados
            km, Vmax = parametros 
            sim_C = odeint(eq_dif, P_0, exp_t, args=(km, Vmax))
            res = sim_C - exp_C
            for i in range(0,2):
                res[:,i] = res[:,i]/dpC[i]
            res = res.flatten()
            res = sum(res**2)
            return res

        #Criação da Função Objetiva do Levemberg-Marquardt
        def func_ob_lm(p):
            p=tuple(p)
            #Calculando os valores simulados, através dos modelos matemáticos de EDOs (resolvidas por integração numérica computacional)para [S] e [P] utilizando os argumentos guardados na tupla: 
            sim_C=odeint(eq_dif,P_0,exp_t,args=p)
            #Determinado o erro entre os valores experimentais e calculados pelo método acima para os valores de [S] e [P]:
            res=sim_C-exp_C
            #Para cada uma das duas colunas da matriz contendo os valores experimentais, o erro calculado é dividido pelo peso atribuído a cada uma das concentrações
            for i in range(0,2):
                res[:,i]=res[:,i]/dpC[i]
            #O que a função retorna é uma matriz unidimensional, pelo uso da função flatten:
            return res.flatten()

        # Função objetiva, compara os pontos experimentais com o modelo
        dpC = [1, 1] # Pesos para cada concentração

        # Aplicando o algoritmo genético
        # Os limites para gerar os valores de km e Vmax
        limites = [(0, 10000), (0, 10000)]

        # Os argumentos para o algoritmo genético
        args = (exp_t, exp_C)

        # A função de algoritmo genético
        resultados_ag = differential_evolution(func_ob_ag, limites, args=args, popsize=5,  tol=0.01, mutation=(0.5, 1), recombination=0.7, updating='immediate')
        param_ajustado_ag = resultados_ag.x

        #Minimizando a função objetiva pela função leastsq:

        ##A lista 'initial guess' contém os valores de entrada:
        valor_init = [param_ajustado_ag]

        ##A função leastsq, a partir da solução da função residuals e dos valores de entrada aproximados anteriores irá definir qual o valor dessas mesmas constantes que minimiza o erro observado entre os valores simulados e modelo:
        solucao_lm=leastsq(func_ob_lm,valor_init, args=(), Dfun=None, full_output=1)

        param_ajustado_lm=solucao_lm[0]

        res_otimo =solucao_lm[2]['fvec']
        sensT_otimo =solucao_lm[2]['fjac']

        npar = len(sensT_otimo[:,1])
        ndata = len(sensT_otimo[1,:])
        invXtX=np.linalg.inv(np.matmul(sensT_otimo,sensT_otimo.transpose()))
        sig2y= sum(res_otimo**2) / (ndata-npar)
        covparamers = invXtX*sig2y
        EPpar = np.sqrt(covparamers.diagonal())
        ICpar = EPpar*sc.t.interval(.95, ndata-npar, loc=0, scale=1)[1]

        #As constantes, já com valores otimizados, são armazenadas em uma tupla (lista imutável):
        param_ajustado_lm=tuple(param_ajustado_lm)

        #Agora, a função que contém as EDOs que descrevem o comportamento, em função do tempo, de [S] e [P] é novamente integrada numericamente utilizando as constantes cinéticas (argumentos) já otimizados (convergidas):

        # Criando meu vetor tempo do modelo
        n_passo = 200
        t = np.linspace(0, exp_t[-1], n_passo)

        # Integrando com os valores dos parâmetros ajustados
        Cotim = odeint(eq_dif, P_0, t, args = (param_ajustado_lm))

        #imprimindo os valores dos parâmetros
        param = np.asarray(param_ajustado_lm)
        
        global km_ajust
        global vmax_ajust
    
        km_ajust = param[0]
        vmax_ajust = param[1]
    
    
    def plot_model():
        
        E0 = float(text_e0.get())
        Kcat = vmax_ajust/E0
        
        conv = f_conversao(exp_C[0,0], exp_C[:,1]) 
        
        #Variáveis de Resposta
        titulo_var_resp = tk.Label(window_model, text="Variáveis de Resposta", font ='Arial 12 bold', width = 45, height = 1, 
                               bg = "grey78").place(x = 5, y = 455)
        frame_var_resp = tk.Frame(window_model, width = 458, height=185, bg='white').place(x = 5, y = 485)
        
        km_resp = tk.Label(window_model, text= "Km Estimado: ", bg='white', font="Arial 14 bold",).place(x = 130, y = 510)
        km_num = tk.Label(window_model, text= round(km_ajust,2), bg='white', font="Arial 14 bold",).place(x = 300, y = 510)
        vmax_resp = tk.Label(window_model, text= "Vmax Estimado: ", bg='white', font="Arial 14 bold",).place(x = 130, y = 560)
        vmax_num = tk.Label(window_model, text= round(vmax_ajust,2), bg='white', font="Arial 14 bold",).place(x = 300, y = 560)
        kcat_resp = tk.Label(window_model, text= "Kcat Estimado: ", bg='white', font="Arial 14 bold",).place(x = 130, y = 610)
        kcat_num = tk.Label(window_model, text= round(Kcat, 2), bg='white', font="Arial 14 bold",).place(x = 300, y = 610)
        
    
    #Botões
    button_template = tk.Button(window_model, font = 'Arial 10 bold', text='Baixar Template', width = 15, command=excel_template).place(x = 120, y = 285)
    button_importar = tk.Button(window_model, font = 'Arial 10 bold', text='Importar Arquivo', width = 15, command=explorer).place(x = 280, y = 285)
    
    #Parâmetros Enzima
    frame_enzima = tk.Frame(window_model, width = 458, height=110, bg='grey85').place(x = 5, y = 338)
    enzima_label = tk.Label(window_model, text='Parâmetros da Enzima', font = 'Arial 10 bold', bg='grey85').place(x = 165, y = 345)
    text_e0 =tk.StringVar()
    e0_label = tk.Label(window_model, text='E0:', font = 'Arial 10 bold', bg='grey85').place(x = 40, y = 375)
    textbox_e0 = ttk.Entry(window_model, textvariable=text_e0, width = 7).place(x = 70, y = 375)
    e0_unid = tk.Label(window_model, text='mol/L', font = 'Arial 9', bg='grey85').place(x = 120, y = 375)
    formula_label = tk.Label(window_model, text='Considerando  Vmáx = [E0] * Kcat', font = 'Arial 10', bg='grey85').place(x = 200, y = 375)
    
    #Variáveis de Resposta
    titulo_var_resp = tk.Label(window_model, text="Variáveis de Resposta", font ='Arial 12 bold', width = 45, height = 1, 
                               bg = "grey78").place(x = 5, y = 455)
    frame_var_resp = tk.Frame(window_model, width = 458, height=185, bg='white').place(x = 5, y = 485)

    #Função Salvar Gráficos
    def salvar():
        a = asksaveasfilename(filetypes=(("PNG Image", "*.png"),("All Files", "*.*")), 
        defaultextension='.png')
        plt.savefig(a)
    
    #Botões
    button_modelar = tk.Button(window_model, font = 'Arial 10 bold', text='Modelar', width = 15, command=plot_model).place(x = 320, y = 410)
   
    
# Configurações de tela
window = tk.Tk()
window.title("Enzinetics")
window.geometry("1200x680")
window.minsize(width=1300, height=680)
window.resizable(0, 0)

#Frame Inicial
Start_frame = tk.Frame(window, bg='grey90', width=1300, height=700).pack(fill='x')

# Barra Menu
menubar = tk.Menu(window)

modemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Modo", menu=modemenu)
modemenu.add_command(label="Simulação", command=Window_Simulation)
modemenu.add_separator()
modemenu.add_command(label="Modelagem", command=Window_Modelling)

helpmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Sobre", menu=helpmenu)
helpmenu.add_command(label="Enzinetics", command=Sobre)

docmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Documentação", menu=docmenu)
docmenu.add_command(label="Michaelis-Menten", command=Doc_Michaelis)
docmenu.add_separator()
inib_menu = tk.Menu(docmenu, tearoff=0)
docmenu.add_cascade(label='Inibição Enzimática', menu=inib_menu)
docmenu.add_separator()
inib_menu.add_cascade
inib_menu.add_command(label='Definição', command=Inib_Def)
inib_menu.add_separator()
inib_menu.add_command(label='Competitiva', command=Inib_1)
inib_menu.add_separator()
inib_menu.add_command(label='Não Competitiva', command=Inib_2)
inib_menu.add_separator()
inib_menu.add_command(label='Incompetitiva', command=Inib_3)
docmenu.add_command(label="Lineweaver-Burk", command=Doc_Lineweaver)
docmenu.add_separator()
docmenu.add_command(label="Modo de Operação: Batelada", command=Doc_Batelada)
docmenu.add_separator()
docmenu.add_command(label="Referências Bibliográficas", command=Referencias)

window.config(menu=menubar)

#Main
# Título
nome_1 = tk.Label(window, text="ENZINETICS", font='Ubuntu 100 bold italic', fg="SteelBlue2", bg='grey90').place(x=240, y=210)
nome_2 = tk.Label(window, text="SIMULAÇÃO E MODELAGEM DE CINÉTICAS ENZIMÁTICAS", font='Ubuntu 18 bold', fg="grey33", bg='grey90').place(x=285, y=350)

#Versão
version = tk.Label(window, text="Versão: 1.0", font='arial 11 bold italic', fg="BLACK", bg='grey90').place(x=1213, y=0)

#Autora
author = tk.Label(window, text="Mayra Valvano", font='arial 11 bold italic', fg="BLACK", bg='grey90').place(x=1186, y=650)

# MainLoop
window.mainloop()
