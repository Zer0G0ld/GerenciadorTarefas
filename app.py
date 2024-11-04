import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton,
    QListWidget, QListWidgetItem, QMessageBox, QInputDialog, QTextEdit, QDialog, QLabel, QHBoxLayout
)
from PyQt6.QtGui import QFont

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        self.tasks.append({"title": title, "description": description, "done": False})

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def mark_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True

    def unmark_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = False

    def get_task_text(self, index):
        task = self.tasks[index]
        status = "Concluída" if task["done"] else "Pendente"
        return f"{task['title']} - {status}"

class TaskDialog(QDialog):
    def __init__(self, title, description, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Visualizar Tarefa")
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()
        self.label_title = QLabel(f"Título: {title}")
        self.label_description = QLabel(f"Descrição:\n{description}")

        layout.addWidget(self.label_title)
        layout.addWidget(self.label_description)

        button_layout = QHBoxLayout()
        self.button_edit = QPushButton("Editar")
        self.button_edit.clicked.connect(self.accept)  # Retorna com "aceitar" para indicar edição
        button_layout.addWidget(self.button_edit)

        self.button_close = QPushButton("Fechar")
        self.button_close.clicked.connect(self.reject)  # Retorna com "rejeitar" para fechar sem edição
        button_layout.addWidget(self.button_close)

        layout.addLayout(button_layout)
        self.setLayout(layout)

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

        # Entrada de título e descrição
        self.input_title = QLineEdit(self)
        self.input_title.setPlaceholderText("Digite o título da tarefa...")
        self.input_title.setStyleSheet("background-color: #424242; color: #FFFFFF; padding: 10px;")
        layout.addWidget(self.input_title)

        self.input_description = QTextEdit(self)
        self.input_description.setPlaceholderText("Digite a descrição da tarefa...")
        self.input_description.setStyleSheet("background-color: #424242; color: #FFFFFF; padding: 10px;")
        layout.addWidget(self.input_description)

        # Lista de tarefas
        self.list_tasks = QListWidget(self)
        self.list_tasks.setStyleSheet("background-color: #424242; color: #FFFFFF;")
        self.list_tasks.itemDoubleClicked.connect(self.view_task)
        layout.addWidget(self.list_tasks)

        # Botões
        button_layout = QHBoxLayout()

        self.button_add = QPushButton("Adicionar Tarefa", self)
        self.button_add.clicked.connect(self.add_task)
        self.button_add.setStyleSheet("background-color: #4CAF50; color: #FFFFFF;")
        button_layout.addWidget(self.button_add)

        self.button_remove = QPushButton("Remover Tarefa Selecionada", self)
        self.button_remove.clicked.connect(self.remove_task)
        self.button_remove.setStyleSheet("background-color: #F44336; color: #FFFFFF;")
        button_layout.addWidget(self.button_remove)

        self.button_mark_done = QPushButton("Marcar/Desmarcar Concluída", self)
        self.button_mark_done.clicked.connect(self.toggle_task_done)
        self.button_mark_done.setStyleSheet("background-color: #FFA000; color: #FFFFFF;")
        button_layout.addWidget(self.button_mark_done)

        self.button_clear = QPushButton("Limpar Tarefas", self)
        self.button_clear.clicked.connect(self.clear_tasks)
        self.button_clear.setStyleSheet("background-color: #2196F3; color: #FFFFFF;")
        button_layout.addWidget(self.button_clear)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def add_task(self):
        title = self.input_title.text().strip()
        description = self.input_description.toPlainText().strip()
        if title and description:
            self.task_manager.add_task(title, description)
            self.update_task_list()
            self.input_title.clear()
            self.input_description.clear()
        else:
            QMessageBox.warning(self, "Erro", "Por favor, insira o título e a descrição da tarefa.")

    def view_task(self, item):
        selected = self.list_tasks.currentRow()
        task = self.task_manager.tasks[selected]
        dialog = TaskDialog(task["title"], task["description"], self)
        if dialog.exec() == QDialog.DialogCode.Accepted:  # Se clicou em "Editar"
            new_title, ok_title = QInputDialog.getText(self, "Editar Título", "Novo título:", QLineEdit.Normal, task["title"])
            new_description, ok_desc = QInputDialog.getText(self, "Editar Descrição", "Nova descrição:", QLineEdit.Normal, task["description"])
            if ok_title and new_title.strip() and ok_desc and new_description.strip():
                task["title"] = new_title.strip()
                task["description"] = new_description.strip()
                self.update_task_list()

    def remove_task(self):
        selected = self.list_tasks.currentRow()
        if selected >= 0:
            self.task_manager.remove_task(selected)
            self.update_task_list()
        else:
            QMessageBox.warning(self, "Erro", "Nenhuma tarefa selecionada para remover.")

    def clear_tasks(self):
        reply = QMessageBox.question(self, 'Confirmação', 'Você tem certeza que deseja limpar todas as tarefas?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.task_manager.tasks = []
            self.update_task_list()

    def toggle_task_done(self):
        selected = self.list_tasks.currentRow()
        if selected >= 0:
            if self.task_manager.tasks[selected]["done"]:
                self.task_manager.unmark_task_done(selected)
            else:
                self.task_manager.mark_task_done(selected)
            self.update_task_list()
        else:
            QMessageBox.warning(self, "Erro", "Nenhuma tarefa selecionada para marcar/desmarcar.")

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
