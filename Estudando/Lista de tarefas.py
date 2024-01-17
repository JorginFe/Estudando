import tkinter as tk
from tkinter import messagebox

def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa:
        lista_tarefas.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Digite uma tarefa.")

def remover_tarefa():
    try:
        selecionado = lista_tarefas.curselection()
        lista_tarefas.delete(selecionado)
    except:
        messagebox.showwarning("Selecione uma tarefa para remover.")

def limpar_tarefas():
    lista_tarefas.delete(0, tk.END)


janela = tk.Tk()
janela.title("Tarefas")


janela.configure(bg='#000000')


entrada_tarefa = tk.Entry(janela, width=30, bg='white')  
botao_adicionar = tk.Button(janela, text="Adicionar Tarefa", command=adicionar_tarefa, bg='#4CAF50', fg='white') 
botao_remover = tk.Button(janela, text="Remover Tarefa", command=remover_tarefa, bg='#FF5733', fg='white')  
botao_limpar = tk.Button(janela, text="Limpar Tarefas", command=limpar_tarefas, bg='#3498DB', fg='white')  
lista_tarefas = tk.Listbox(janela, selectmode=tk.SINGLE, width=40, height=10, bg='white') 


entrada_tarefa.grid(row=0, column=0, padx=10, pady=10)
botao_adicionar.grid(row=0, column=1, padx=10, pady=10)
botao_remover.grid(row=1, column=1, padx=10, pady=10)
botao_limpar.grid(row=2, column=1, padx=10, pady=10)
lista_tarefas.grid(row=1, column=0, padx=10, pady=10)


janela.mainloop()