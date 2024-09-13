import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QTextEdit, QPushButton, QListWidget, QMessageBox, QHBoxLayout, QSizePolicy, QDialog
)
from PyQt5.QtCore import Qt
from database import Database
from bson.objectid import ObjectId

class PasswordDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Admin Login")
        self.setFixedSize(300, 150)

        # Apply dark mode stylesheet
        self.setStyleSheet("""
            QDialog {
                background-color: #2b2b2b;
                color: #ffffff;
                font-family: Consolas;
                font-size: 10px;
            }
            QLineEdit {
                background-color: #3c3f41;
                color: #ffffff;
                border: 1px solid #4a4a4a;
                padding: 5px;
                font-family: Consolas;
            }
            QPushButton {
                background-color: #3c3f41;
                color: #ffffff;
                border: 1px solid #4a4a4a;
                padding: 5px;
                font-family: Consolas;
            }
            QPushButton:hover {
                background-color: #4a4a4a;
            }
            QPushButton:pressed {
                background-color: #2a2a2a;
            }
            QLabel {
                color: #ffffff;
                font-family: Consolas;
            }
        """)

        layout = QVBoxLayout()

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.password_input)

        button_layout = QHBoxLayout()
        ok_button = QPushButton("OK")
        cancel_button = QPushButton("Cancel")
        ok_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def get_password(self):
        return self.password_input.text()

class StartScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("IT Help Desk Ticketing System")
        self.setFixedSize(400, 200)

        # Apply dark mode stylesheet
        self.setStyleSheet("""
            QWidget {
                background-color: #2b2b2b;
                color: #ffffff;
                font-family: Consolas;
                font-size: 10px;
            }
            QPushButton {
                background-color: #3c3f41;
                color: #ffffff;
                border: 1px solid #4a4a4a;
                padding: 5px;
                font-family: Consolas;
            }
            QPushButton:hover {
                background-color: #4a4a4a;
            }
            QPushButton:pressed {
                background-color: #2a2a2a;
            }
            QLabel {
                color: #ffffff;
                font-family: Consolas;
            }
        """)

        layout = QVBoxLayout()

        admin_button = QPushButton("Admin")
        user_button = QPushButton("User")

        admin_button.clicked.connect(self.launch_admin_mode)
        user_button.clicked.connect(self.launch_user_mode)

        layout.addWidget(admin_button)
        layout.addWidget(user_button)

        self.setLayout(layout)

    def launch_admin_mode(self):
        password_dialog = PasswordDialog(self)
        if password_dialog.exec_() == QDialog.Accepted:
            if password_dialog.get_password() == "admin1":
                self.launch_main_app(is_admin=True)
            else:
                QMessageBox.warning(self, "Error", "Incorrect password. Access denied.")
        else:
            QMessageBox.warning(self, "Cancelled", "Admin login cancelled.")

    def launch_user_mode(self):
        self.launch_main_app(is_admin=False)

    def launch_main_app(self, is_admin):
        self.main_app = HelpDeskApp(is_admin=is_admin)
        self.main_app.show()
        self.close()

class HelpDeskApp(QWidget):
    def __init__(self, is_admin):
        super().__init__()
        self.is_admin = is_admin
        self.db = Database()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("IT Help Desk Ticketing System - Admin" if self.is_admin else "IT Help Desk Ticketing System - User")
        self.setFixedSize(800, 600)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)

        self.setStyleSheet("""
            QWidget {
                background-color: #2b2b2b;
                color: #ffffff;
                font-family: Consolas;
                font-size: 10px;
            }
            QLineEdit, QTextEdit, QListWidget {
                background-color: #3c3f41;
                color: #ffffff;
                border: 1px solid #4a4a4a;
                padding: 5px;
                font-family: Consolas;
            }
            QPushButton {
                background-color: #3c3f41;
                color: #ffffff;
                border: 1px solid #4a4a4a;
                padding: 5px;
                font-family: Consolas;
            }
            QPushButton:hover {
                background-color: #4a4a4a;
            }
            QPushButton:pressed {
                background-color: #2a2a2a;
            }
            QLabel {
                color: #ffffff;
                font-family: Consolas;
            }
        """)

        main_layout = QHBoxLayout()

        # Left side: Ticket Form
        form_layout = QVBoxLayout()
        form_layout.setAlignment(Qt.AlignTop)

        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Enter title")
        self.title_input.setToolTip("Enter the title of the ticket")
        self.title_input.setFixedHeight(30)
        form_layout.addWidget(self.title_input)

        self.description_input = QTextEdit()
        self.description_input.setPlaceholderText("Enter description")
        self.description_input.setToolTip("Describe the issue in detail")
        self.description_input.setFixedHeight(150)
        form_layout.addWidget(self.description_input)

        create_button = QPushButton("Create Ticket")
        create_button.setToolTip("Click to create a new ticket")
        create_button.setFixedWidth(251)
        create_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        form_layout.addWidget(create_button, alignment=Qt.AlignBottom)
        create_button.clicked.connect(self.create_ticket)

        if self.is_admin:
            delete_button = QPushButton("Delete Selected Ticket")
            delete_button.setToolTip("Click to delete the selected ticket")
            delete_button.setFixedWidth(251)
            delete_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            delete_button.clicked.connect(self.delete_ticket)
            form_layout.addWidget(delete_button, alignment=Qt.AlignBottom)

        # Right side: Ticket List and Details
        list_layout = QVBoxLayout()

        list_layout.addWidget(QLabel("Tickets"))

        self.ticket_list = QListWidget()
        self.ticket_list.itemClicked.connect(self.display_ticket)
        list_layout.addWidget(self.ticket_list)

        self.detail_label = QLabel("Select a ticket to view details.")
        self.detail_label.setAlignment(Qt.AlignTop)
        list_layout.addWidget(self.detail_label)

        main_layout.addLayout(form_layout, 1)
        main_layout.addSpacing(20)
        main_layout.addLayout(list_layout, 2)

        self.setLayout(main_layout)

        self.load_tickets()

    def create_ticket(self):
        title = self.title_input.text().strip()
        description = self.description_input.toPlainText().strip()

        if not title or not description:
            QMessageBox.warning(self, "Input Error", "Please provide both title and description.")
            return

        ticket_id = self.db.create_ticket(title, description)
        QMessageBox.information(self, "Success", f"Ticket created with ID: {ticket_id}")
        self.title_input.clear()
        self.description_input.clear()
        self.load_tickets()

    def delete_ticket(self):
        selected_item = self.ticket_list.currentItem()
        if not selected_item:
            QMessageBox.warning(self, "Selection Error", "Please select a ticket to delete.")
            return

        ticket_id, _ = selected_item.text().split('|', 1)
        self.db.delete_ticket(ticket_id)
        QMessageBox.information(self, "Success", "Ticket deleted successfully.")
        self.load_tickets()

    def load_tickets(self):
        self.ticket_list.clear()
        tickets = self.db.get_all_tickets()
        for ticket in tickets:
            item_text = f"{ticket['title']} - {ticket['status']}"
            self.ticket_list.addItem(f"{ticket['_id']}|{item_text}")

    def display_ticket(self, item):
        ticket_id, item_text = item.text().split('|', 1)
        ticket = self.db.get_ticket(ticket_id)
        if ticket:
            details = f"Title: {ticket['title']}\n\nDescription: {ticket['description']}\n\nStatus: {ticket['status']}"
            self.detail_label.setText(details)
            self.current_ticket_id = ticket_id
        else:
            self.detail_label.setText("Ticket not found.")
            self.current_ticket_id = None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    start_screen = StartScreen()
    start_screen.show()
    sys.exit(app.exec_())
