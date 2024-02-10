from PyQt6.QtWidgets import QGroupBox, QTextEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QTableWidget, QHeaderView, QSplitter, QFrame, QTableWidgetItem, QFormLayout
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QTextCursor, QTextCharFormat, QTextOption, QAction

class LeftContainer(QGroupBox):
    def __init__(self, parent=None):
        super().__init__("Register Tag", parent)

        self.container_left = QGroupBox("Register Tag", self)

        # container_left.setStyleSheet("background-color: #303030;")
        
        self.rfid_tag_label = QLabel("RFID Tag")
        self.rfid_tag = QTextEdit()
        self.vehicle_type_label = QLabel("Type of vehicle")
        self.vehicle_type = QTextEdit()
        self.vehicle_no_label = QLabel("Vehicle No")
        self.vehicle_no = QTextEdit()
        self.do_no_label = QLabel("DO Number")
        self.do_no = QTextEdit()
        self.transporter_label = QLabel("Transporter")
        self.transporter = QTextEdit()
        self.driver_label = QLabel("Driver/Owner")
        self.driver = QTextEdit()
        self.Weighbridge_label = QLabel("Weighbridge No")
        self.Weighbridge = QTextEdit()
        self.purpose_label = QLabel("Visit Purpose")
        self.purpose = QTextEdit()
        self.place_visit_label = QLabel("Place to Visit")
        self.place_visit = QTextEdit()
        self.person_visit_label = QLabel("Person Visit")
        self.person_visit = QTextEdit()
        self.validity_label = QLabel("Validity Till")
        self.validity = QTextEdit()
        self.registered_label = QLabel("Tag Already Registered")
        self.space1 = QLabel(" ")
        self.space2 = QLabel(" ")

        self.new_button = QPushButton("New")
        self.edit_button = QPushButton("Edit")
        self.save_button = QPushButton("Save")
        self.delete_button = QPushButton("Delete")
        self.close_button = QPushButton("Close")

        self.vehicle_search_label = QLabel("Vehicle No Search")
        self.vehicle_search = QTextEdit()
        self.login_label = QLabel("Your Login Password")
        self.login = QTextEdit()

        self.rfid_tag.setFixedSize(200, 30)
        self.vehicle_type.setFixedSize(200, 30)
        self.vehicle_no.setFixedSize(200, 30)
        self.do_no.setFixedSize(200, 30)
        self.transporter.setFixedSize(200, 30)
        self.driver.setFixedSize(200, 30)
        self.Weighbridge.setFixedSize(200, 30)
        self.purpose.setFixedSize(200, 30)
        self.place_visit.setFixedSize(200, 30)
        self.person_visit.setFixedSize(200, 30)
        self.validity.setFixedSize(200, 30)
        self.vehicle_search.setFixedSize(200, 30)
        self.login.setFixedSize(200, 30)

        # Set the fixed size for each button
        button_size = QSize(60, 30)
        self.new_button.setFixedSize(button_size)
        self.edit_button.setFixedSize(button_size)
        self.save_button.setFixedSize(button_size)
        self.delete_button.setFixedSize(button_size)
        self.close_button.setFixedSize(button_size)

        self.setup_ui()

    def setup_ui(self):
        # Create a form layout for organizing labels and corresponding entry boxes
        form_layout = QFormLayout(self.container_left)
        form_layout.addRow(self.rfid_tag_label, self.rfid_tag)
        form_layout.addRow(self.vehicle_type_label, self.vehicle_type)
        form_layout.addRow(self.vehicle_no_label, self.vehicle_no)
        form_layout.addRow(self.do_no_label, self.do_no)
        form_layout.addRow(self.transporter_label, self.transporter)
        form_layout.addRow(self.driver_label, self.driver)
        form_layout.addRow(self.Weighbridge_label, self.Weighbridge)
        form_layout.addRow(self.purpose_label, self.purpose)
        form_layout.addRow(self.place_visit_label, self.place_visit)
        form_layout.addRow(self.person_visit_label, self.person_visit)
        form_layout.addRow(self.validity_label, self.validity)
        form_layout.addRow(self.space1)
        form_layout.addRow(self.registered_label)
        form_layout.addRow(self.space2)
        

        # Create a horizontal layout for buttons and add spacing
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.new_button)
        button_layout.addWidget(self.edit_button)
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.close_button)

        # Add the button_layout as a row in form_layout
        form_layout.addRow(button_layout)

        # Add the remaining rows
        form_layout.addRow(self.vehicle_search_label, self.vehicle_search)
        form_layout.addRow(self.login_label, self.login)

        self.registered_label.setStyleSheet("font-weight: bold; font-size: 28px; color: #89CFF0")


class RightContainer(QGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.container_right = QFrame(self)
        self.table = QTableWidget(self)

        self.setup_ui()

    def setup_ui(self):
        table = self.table
        table.setColumnCount(7)
        table.setHorizontalHeaderLabels(["RFID TAG", "TYPE", "VEHICLE NO", "DO NO", "TRANSPORTER", "DRIVER", "WB NO"])

        table.setRowCount(19)
        for i in range(10):
            for j in range(7):
                item = QTableWidgetItem(f"First Value {i+1}, Second Value {j+1}")
                item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
                table.setItem(i, j, item)

        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

        container_right_layout = QVBoxLayout(self)
        container_right_layout.addWidget(table)

