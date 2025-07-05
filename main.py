import sys
from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QLineEdit, QTextEdit, QPushButton,
    QWidget, QVBoxLayout, QHBoxLayout, QCheckBox,
    QLabel, QListWidget, QListWidgetItem, QFileDialog
)
import json
from detailWindow import Ui_DetailWindow
from editTaskWindow import Ui_EditTaskWindow


class ToDoApp(QMainWindow):
    def __init__(self):
        super(ToDoApp, self).__init__()

        # Load The UI File
        uic.loadUi("to_do_list.ui", self)
        # Set the app's title
        self.setWindowTitle("To-Do List")

        # Define Our Widgets
        self.title_lineEdit = self.findChild(QLineEdit, "title_lineEdit")
        self.desc_textEdit = self.findChild(QTextEdit, "desc_textEdit")
        self.add_task_button = self.findChild(QPushButton, "add_task_button")
        self.list_widget = self.findChild(QListWidget, "listWidget")

        # Make an object from FileManager class
        self.file_manager = FileManager(self.list_widget)

        # Set default text in lineEdit and textEdit
        self.title_lineEdit.setPlaceholderText("Title:")
        self.desc_textEdit.setPlaceholderText("Description:")

        # Connect function to the button
        self.add_task_button.clicked.connect(self.add_task)

        # Connect functions for buttons in menuBar
        self.actionSave.triggered.connect(self.file_manager.save_file)
        self.actionOpen.triggered.connect(self.file_manager.load_file)

        # Show The App
        self.show()

    # Function for add tasks to the lists in main window
    def add_task(self):
        # Get the title and description
        title = self.title_lineEdit.text()
        description = self.desc_textEdit.toPlainText()

        # Return and don't add any task when there is no title
        if title.strip() == "":
            return

        # Make an object from TaskWidget class
        task_widget = TaskWidget(title, description, self.list_widget)

        list_item = QListWidgetItem(self.list_widget)
        task_widget.list_item = list_item
        self.list_widget.addItem(list_item)
        self.list_widget.setItemWidget(list_item, task_widget)
        task_widget.updateGeometry()
        list_item.setSizeHint(task_widget.sizeHint())

        # Clear them to be ready for next text
        self.title_lineEdit.clear()
        self.desc_textEdit.clear()


# Class for an item that going to add to the list
class TaskWidget(QWidget):
    def __init__(self, title, description, list_widget):
        super().__init__()
        self.list_widget = list_widget

        # Put User's task in label
        self.title_label = QLabel(title)
        # Customize the font for title of the item
        title_font = QFont()
        title_font.setFamily("Segoe UI Variable Text Semibold")
        title_font.setPointSize(14)
        self.title_label.setFont(title_font)
        self.title_label.setStyleSheet("color: #A8D5BA;")

        self.desc_label = QLabel(description)
        # Customize the font for description of the item
        desc_font = QFont()
        desc_font.setFamily("Segoe UI Variable Text Semibold")
        desc_font.setPointSize(12)
        self.desc_label.setFont(desc_font)
        self.desc_label.setWordWrap(True)
        self.desc_label.setStyleSheet("color: #A8D5BA;")

        # Make a vertical layout to put the title and description in that
        self.text_layout = QVBoxLayout()

        # add the widgets to layout
        self.text_layout.addWidget(self.title_label)
        self.text_layout.addWidget(self.desc_label)

        # Add edit and delete button for the task
        self.edit_button = QPushButton("Edit")
        self.delete_button = QPushButton("Delete")
        self.detail_button = QPushButton("Detail")

        # Connect the buttons functions
        self.edit_button.clicked.connect(self.edit)
        self.delete_button.clicked.connect(self.delete)
        self.detail_button.clicked.connect(self.detail)

        # CheckBox for task Status
        self.checkBox = QCheckBox()

        # Make horizontal layout for task to put the buttons and others in that
        self.main_layout = QHBoxLayout()

        # add the widgets to layout
        self.main_layout.addWidget(self.checkBox)
        self.main_layout.addLayout(self.text_layout)
        # Make some space between the text and buttons
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.edit_button)
        self.main_layout.addWidget(self.delete_button)
        self.main_layout.addWidget(self.detail_button)

        # Add layout for the object of the class
        self.setLayout(self.main_layout)

    # Function for edit an item
    def edit(self):
        # Open the edit window
        self.open_edit_window()
        # Forward the task's text into new window for edit
        self.edit_Ui.titleEdit_lineEdit.setText(self.title_label.text())
        self.edit_Ui.descEdit_textEdit.setText(self.desc_label.text())

    # Function for delete an item
    def delete(self):
        index = self.list_widget.indexFromItem(self.list_item)
        self.list_widget.takeItem(index.row())

    # Open edit window
    def open_edit_window(self):
        self.edit_window = QMainWindow()
        self.edit_Ui = Ui_EditTaskWindow()
        self.edit_Ui.setupUi(self.edit_window)
        # Show the window
        self.edit_window.show()

        # Connect functions to buttons
        self.edit_Ui.save_button.clicked.connect(self.save)
        self.edit_Ui.cancel_button.clicked.connect(self.cancel)

    # Function for the save button in edit window
    def save(self):
        # Get the new title and description from edit window
        new_title = self.edit_Ui.titleEdit_lineEdit.text()
        new_desc = self.edit_Ui.descEdit_textEdit.toPlainText()

        # if there is no title for the task, The task going to remove
        if new_title == "":
            self.delete()
            return

        if new_title != self.title_label.text():
            self.title_label.setText(new_title)

        if new_desc != self.desc_label.text():
            self.desc_label.setText(new_desc)

        self.list_item.setSizeHint(self.sizeHint())

        # Close the edit window after it's work done
        self.edit_window.close()

    def cancel(self):
        # Just close the window after the button press
        self.edit_window.close()

    def detail(self):
        # Open the detail window
        self.open_detail_window()

        # Forward the task's text into new page to show them better
        self.detail_Ui.detail_title_label.setText(self.title_label.text())
        self.detail_Ui.detail_desc_label.setText(self.desc_label.text())

    def open_detail_window(self):
        self.detail_window = QMainWindow()
        self.detail_Ui = Ui_DetailWindow()
        self.detail_Ui.setupUi(self.detail_window)
        # Show the window
        self.detail_window.show()


# Class for control data
class FileManager:
    def __init__(self, list_widget):
        self.list_widget = list_widget

    # Save the data in json file
    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(None, "Save Tasks", "", "JSON Files (*.json)")
        # If the user click the cancel button the function return
        if not file_name:
            return

        # Make an empty list to put the data in that
        data = []

        # get the data from the app
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            task_widget = self.list_widget.itemWidget(item)

            task_data = {
                "title": task_widget.title_label.text(),
                "description": task_widget.desc_label.text(),
                "checked": task_widget.checkBox.isChecked()
            }

            # add data to that empty list
            data.append(task_data)

        # open file in write mode and insert the data
        with open(file_name, "w") as f:
            json.dump(data, f, indent=4)

    # load the data from json file
    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Open Task File", "", "JSON Files (*.json);;All Files (*)")
        # If the user click the cancel button the function return
        if not file_path:
            return

        try:
            # Open the file in read mode and import through that
            with open(file_path, "r") as file:
                tasks = json.load(file)

            # clear the list for the new data
            self.list_widget.clear()

            # Add new data to the app
            for task in tasks:
                title = task.get("title", "")
                desc = task.get("description", "")
                checked = task.get("checked", False)

                task_widget = TaskWidget(title, desc, self.list_widget)
                task_widget.checkBox.setChecked(checked)

                list_item = QListWidgetItem(self.list_widget)
                list_item.setSizeHint(task_widget.sizeHint())
                task_widget.list_item = list_item

                self.list_widget.addItem(list_item)
                self.list_widget.setItemWidget(list_item, task_widget)

        except Exception as e:
            print("Error loading file:", e)


# Initialize The App
app = QApplication(sys.argv)
UIWindow = ToDoApp()
app.exec_()
