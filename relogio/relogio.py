import tkinter as tk # tkinter para interfaces gráficas, das mais simples às mais complexas
from tkinter import * # outra forma de importar o tk
import os # biblioteca para interagir com o sistema operacional (obter info do sistema, criar diretórios)
from time import strftime # para pegar os dados do tempo atual, strftime é a função usada

# Variáveis para customizar a interface do relógio
root = tk.Tk() # Cria a janela principal da interface gráfica
root.title('Relógio') # Define o título da janela
root.geometry("600x320") # Define o tamanho inicial da janela
root.maxsize(600, 320) # Define o tamanho máximo da janela
root.minsize(600, 320) # Define o tamanho mínimo da janela
root.configure(background='#1d1d1d') # Define a cor de fundo da janela

# Carrega as imagens para os modos claro e escuro
light = PhotoImage(file='relogio/images/brightness.png') # Modo claro
dark = PhotoImage(file='relogio/images/dark.png') # Modo noturno

def toggle_dark_mode():
    """
    Alterna entre o modo escuro e o modo claro.
    """
    if root['bg'] == '#1d1d1d':
        # Modo claro
        root['bg'] = 'white'
        tela['bg'] = 'white'
        saudacao['bg'] = 'white'
        data['bg'] = 'white'
        horas['bg'] = 'white'
        dark_mode_button['image'] = light
        dark_mode_button['bg'] = 'white'
    else:
        # Modo escuro
        root['bg'] = '#1d1d1d'
        tela['bg'] = '#1d1d1d'
        saudacao['bg'] = '#1d1d1d'
        data['bg'] = '#1d1d1d'
        horas['bg'] = '#1d1d1d'
        dark_mode_button['image'] = dark
        dark_mode_button['bg'] = '#1d1d1d'

def get_saudacao():
    """
    Obtém o nome do usuário do sistema e exibe uma saudação personalizada.
    """
    nome_usuario = os.getlogin() # Obtém o nome do usuário atual
    saudacao.config(text='Olá, ' + nome_usuario) # Atualiza o rótulo com a saudação

def get_data():
    """
    Obtém a data atual e atualiza o rótulo de data.
    """
    data_atual = strftime('%a, %d %b %Y') # Formata a data atual
    data.config(text=data_atual) # Atualiza o rótulo com a data atual

def get_horas():
    """
    Obtém a hora atual e atualiza o rótulo de horas. Atualiza a cada segundo.
    """
    hora_atual = strftime('%H:%M:%S') # Formata a hora atual
    horas.config(text=hora_atual) # Atualiza o rótulo com a hora atual
    horas.after(1000, get_horas) # Chama a função novamente após 1000 milissegundos (1 segundo)

# Cria o botão para alternar o modo escuro/claro
dark_mode_button = Button(root, command=toggle_dark_mode)
dark_mode_button.config(image=dark, bd=0, bg='#1d1d1d') # Configura o botão
dark_mode_button.pack(pady=10) # Adiciona o botão à interface com espaçamento vertical

# Cria o canvas para exibir um espaço no topo
tela = tk.Canvas(root, width=600, height=20, bg='#1d1d1d', bd=0, highlightthickness=0, relief='ridge')
tela.pack()

# Cria e adiciona os rótulos para a saudação, data e hora
saudacao = Label(root, bg='#1d1d1d', fg='#8e27ea', font=('Montserrat', 16))
saudacao.pack() # Adiciona o rótulo à interface
data = Label(root, bg='#1d1d1d', fg='#8e27ea', font=('Montserrat', 14))
data.pack(pady=2) # Adiciona o rótulo de data à interface com um pequeno espaçamento
horas = Label(root, bg='#1d1d1d', fg='#8e27ea', font=('Montserrat', 64, 'bold'))
horas.pack(pady=2) # Adiciona o rótulo de hora à interface com um pequeno espaçamento

# Chama as funções para exibir as informações iniciais
get_saudacao()
get_data()
get_horas()

root.mainloop() # Inicia o loop principal da interface gráfica
