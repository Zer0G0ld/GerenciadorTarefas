# Author: Zer0G0ld
# Divirtam-se modificando o código !!!

import tkinter as tk

class GerenciadorTarefaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Tarefas")

        # Definir tamanho da janela para ocupar a tela
        # width_window = root.winfo_screenwidth()
        # height_window = root.winfo_screenheight()
        # self.root.geometry(f"{width_window}x{height_window}")
        self.root.geometry(f"500x500")

        self.tasks = []

        self.frame_center = tk.Frame(root)
        self.frame_center.pack(expand=True, fill="both")

        self.input_tasks = tk.Entry(self.frame_center)
        self.input_tasks.pack(pady=10, padx=20, fill="both")

        self.button_add = tk.Button(
            self.frame_center, text="Adicionar Tarefa", command=self.add_task
        )
        self.button_add.pack(pady=10, fill="both")

        self.button_remove = tk.Button(
            self.frame_center, text="Remover Tarefa Selecionada", command=self.remove_task
        )
        self.button_remove.pack(pady=10, fill="both")

        self.button_clear = tk.Button(
            self.frame_center, text="Limpar Tarefas completas", command=self.clear_tasks
        )
        self.button_clear.pack(pady=10, fill="both")

        self.list_tasks = tk.Listbox(self.frame_center)
        self.list_tasks.pack(pady=10, padx=20, fill="both", expand=True)
    
    def add_task(self):
        task = self.input_tasks.get()
        if task:
            self.tasks.append(task)
            self.list_tasks.insert(tk.END, task)
            self.input_tasks.delete(0, tk.END)
    
    def remove_task(self):
        selected = self.list_tasks.curselection()
        if selected:
            index = int(selected[0])
            self.list_tasks.delete(index)
            self.tasks.pop(index)

    def clear_tasks(self):
        tasks_complete = [task for task in self.tasks if task]
        self.list_tasks.delete(0, tk.END)
        self.tasks = []
        for task in tasks_complete:
            self.list_tasks.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = GerenciadorTarefaGUI(root)
    root.mainloop()
