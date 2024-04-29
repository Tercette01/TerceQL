import tkinter as tk
from tkinter import messagebox

def exibir_mensagem():
    messagebox.showinfo('Mensagem', 'Você clicou no botão!')

# Cria a janela principal
root = tk.Tk()
root.title('Exemplo de Botão')

# Cria um botão e o adiciona à janela principal
botao = tk.Button(root, text='Clique aqui', command=exibir_mensagem)
botao.pack()

# Inicia o loop principal da interface gráfica
root.mainloop()