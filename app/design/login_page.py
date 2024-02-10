from PyQt6.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QPushButton, QLabel, QMessageBox, QStackedWidget, QLineEdit
from PyQt6.QtCore import Qt
from functions.authentication_user import AuthenticationLogic
from design.menu_bars import MyWidget

class LoginCrend(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title and geometry
        self.setWindowTitle("Digital Weighing System Pvt. Ltd")

        # Create stacked widget to switch between login and menu
        self.stacked_widget = QStackedWidget(self)

        # Create layout for the main window
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.stacked_widget, alignment=Qt.AlignmentFlag.AlignTop)  # Align the stacked widget to the top

        # Create a container widget for login-related widgets
        self.login_container = QWidget(self)
        self.login_layout = QVBoxLayout(self.login_container)
        self.login_layout.setContentsMargins(0, 0, 0, 0)  # Set margins to zero
        self.login_layout.setSpacing(10)  # Set the spacing to your desired value

        # Call methods to create widgets and connect signals
        self.create_widgets()
        self.connect_signals()

        # Add the login container to the main layout
        self.layout.addWidget(self.login_container, alignment=Qt.AlignmentFlag.AlignTop)

        self.setLayout(self.layout)

    def create_widgets(self):
        # Create widgets for login
        self.username_label = QLabel("User Id")
        self.username = QLineEdit()
        self.username.setContentsMargins(0, 0, 0, 0)  # Set margins to zero

        self.password_label = QLabel("Password")
        self.password = QLineEdit()
        self.password.setContentsMargins(0, 0, 0, 0)  # Set margins to zero
        self.password.setEchoMode(QLineEdit.EchoMode.Password) 

        self.button = QPushButton("Login")

        # Set fixed sizes for labels and widgets
        self.username_label.setFixedSize(80, 20)
        self.username.setFixedSize(200, 30)
        self.password_label.setFixedSize(80, 20)
        self.password.setFixedSize(200, 30)
        self.button.setFixedWidth(100)
        self.button.setFixedHeight(40)

        # Stylesheet
        self.username_label.setStyleSheet("font-weight: bold; font-size: 16px")
        self.password_label.setStyleSheet("font-weight: bold; font-size: 16px")

        # Add widgets directly to the login container layout
        self.login_layout.addWidget(self.username_label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.login_layout.addWidget(self.username, alignment=Qt.AlignmentFlag.AlignCenter)
        self.login_layout.addWidget(self.password_label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.login_layout.addWidget(self.password, alignment=Qt.AlignmentFlag.AlignCenter)
        self.login_layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Add login widgets to stacked widget
        self.stacked_widget.addWidget(QWidget())

    def connect_signals(self):
        # Connect signals
        self.button.clicked.connect(self.check_password)

    def check_password(self):
        # Your logic for checking the password goes here
        entered_password = self.password.text()
        entered_username = self.username.text()

        if AuthenticationLogic.check_credentials(entered_username, entered_password):
            self.clear_login_fields()
            self.show_menu()
        else:
            self.show_error_message("Incorrect Username or Password")

    def clear_login_fields(self):
        # Clear the login-related fields
        self.username.clear()
        self.password.clear()

        # Optionally, you can hide or destroy the login-related widgets
        self.username_label.hide()
        self.username.hide()
        self.password_label.hide()
        self.password.hide()
        self.button.hide()

    def show_menu(self):
        # Create MyWidget instance and add it to the stacked widget
        widget_menu = MyWidget()
        self.stacked_widget.addWidget(widget_menu)

        # Switch to the menu page
        self.stacked_widget.setCurrentWidget(widget_menu)

    def show_error_message(self, message):
        error_message = QMessageBox(self)
        error_message.setIcon(QMessageBox.Icon.Warning)
        error_message.setText(message)
        error_message.setWindowTitle("Error")
        error_message.exec()
