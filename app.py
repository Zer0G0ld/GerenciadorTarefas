import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QListWidgetItem, QMessageBox
from PyQt6.QtGui import QFont

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, text):
        self.tasks.append({"text": text, "done": False})

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def mark_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True

    def remove_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = False

    def get_task_text(self, index):
        task = self.tasks[index]
        return f"{task['text']} - Concluída" if task["done"] else task["text"]

class GerenciadorTarefaGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.task_manager = TaskManager()

    def initUI(self):
        self.setWindowTitle("Gerenciador de Tarefas")
        self.setGeometry(300, 100, 500, 500)
        self.setStyleSheet("background-color: #2E2E2E;")

        layout = QVBoxLayout()

        # Entrada de tarefa
        self.input_tasks = QLineEdit(self)
        self.input_tasks.setPlaceholderText("Digite uma nova tarefa...")
        self.input_tasks.setStyleSheet("background-color: #424242; color: #FFFFFF; padding: 10px;")
        layout.addWidget(self.input_tasks)

        # Lista de tarefas
        self.list_tasks = QListWidget(self)
        self.list_tasks.setStyleSheet("background-color: #424242; color: #FFFFFF;")
        layout.addWidget(self.list_tasks)

        # Botões
        self.button_add = QPushButton("Adicionar Tarefa", self)
        self.button_add.clicked.connect(self.add_task)
        self.button_add.setStyleSheet("background-color: #4CAF50; color: #FFFFFF;")
        layout.addWidget(self.button_add)

        self.button_remove = QPushButton("Remover Tarefa Selecionada", self)
        self.button_remove.clicked.connect(self.remove_task)
        self.button_remove.setStyleSheet("background-color: #F44336; color: #FFFFFF;")
        layout.addWidget(self.button_remove)

        self.button_mark_done = QPushButton("Marcar como Concluída", self)
        self.button_mark_done.clicked.connect(self.mark_task_done)
        self.button_mark_done.setStyleSheet("background-color: #FFA000; color: #FFFFFF;")
        layout.addWidget(self.button_mark_done)

        self.button_clear = QPushButton("Limpar Tarefas", self)
        self.button_clear.clicked.connect(self.clear_tasks)
        self.button_clear.setStyleSheet("background-color: #2196F3; color: #FFFFFF;")
        layout.addWidget(self.button_clear)

        self.setLayout(layout)

    def add_task(self):
        task_text = self.input_tasks.text().strip()
        if task_text:
            self.task_manager.add_task(task_text)
            self.update_task_list()
            self.input_tasks.clear()
        else:
            QMessageBox.warning(self, "Erro", "Por favor, insira uma tarefa.")

    def remove_task(self):
        selected = self.list_tasks.currentRow()
        if selected >= 0:
            self.task_manager.remove_task(selected)
            self.update_task_list()
        else:
            QMessageBox.warning(self, "Erro", "Nenhuma tarefa selecionada para remover.")

    def clear_tasks(self):
        self.task_manager.tasks = []
        self.update_task_list()

    def mark_task_done(self):
        selected = self.list_tasks.currentRow()
        if selected >= 0:
            self.task_manager.mark_task_done(selected)
            self.update_task_list()
        else:
            QMessageBox.warning(self, "Erro", "Nenhuma tarefa selecionada para marcar como concluída.")

    def update_task_list(self):
        self.list_tasks.clear()
        for i in range(len(self.task_manager.tasks)):
            task_text = self.task_manager.get_task_text(i)
            item = QListWidgetItem(task_text)
            item.setFont(QFont("Arial", 12))
            self.list_tasks.addItem(item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    task_manager_gui = GerenciadorTarefaGUI()
    task_manager_gui.show()
    sys.exit(app.exec())
