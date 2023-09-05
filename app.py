import tkinter as tk

class GerenciadorTarefasGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Tarefas")

        # Definir tamanho da janela para ocupar toda a tela
        largura_tela = root.winfo_screenwidth()
        altura_tela = root.winfo_screenheight()
        self.root.geometry(f"{largura_tela}x{altura_tela}")

        self.tarefas = []

        self.frame_centro = tk.Frame(root)
        self.frame_centro.pack(expand=True, fill="both")

        self.input_tarefa = tk.Entry(self.frame_centro)
        self.input_tarefa.pack(pady=10, padx=20, fill="both")

        self.botao_adicionar = tk.Button(self.frame_centro, text="Adicionar Tarefa", command=self.adicionar_tarefa)
        self.botao_adicionar.pack(pady=10, fill="both")

        self.botao_remover = tk.Button(self.frame_centro, text="Remover Tarefa Selecionada", command=self.remover_tarefa)
        self.botao_remover.pack(pady=10, fill="both")

        self.botao_limpar = tk.Button(self.frame_centro, text="Limpar Tarefas Completas", command=self.limpar_tarefas)
        self.botao_limpar.pack(pady=10, fill="both")

        self.lista_tarefas = tk.Listbox(self.frame_centro)
        self.lista_tarefas.pack(pady=10, padx=20, fill="both", expand=True)

    def adicionar_tarefa(self):
        tarefa = self.input_tarefa.get()
        if tarefa:
            self.tarefas.append(tarefa)
            self.lista_tarefas.insert(tk.END, tarefa)
            self.input_tarefa.delete(0, tk.END)

    def remover_tarefa(self):
        selecionado = self.lista_tarefas.curselection()
        if selecionado:
            indice = selecionado[0]
            self.lista_tarefas.delete(indice)
            self.tarefas.pop(indice)

    def limpar_tarefas(self):
        tarefas_completas = [tarefa for tarefa in self.tarefas if tarefa]
        self.lista_tarefas.delete(0, tk.END)
        self.tarefas = []
        for tarefa in tarefas_completas:
            self.lista_tarefas.insert(tk.END, tarefa)

if __name__ == "__main__":
    root = tk.Tk()
    app = GerenciadorTarefasGUI(root)
    root.mainloop()
