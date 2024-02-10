from PyQt6.QtWidgets import QWidget, QVBoxLayout, QMenuBar ,QApplication ,QLabel, QTextEdit, QHBoxLayout, QFormLayout, QPushButton, QFrame, QTableWidget, QTableWidgetItem, QHeaderView, QSplitter, QGroupBox, QDateEdit, QComboBox
from PyQt6.QtGui import QIcon, QAction, QPixmap
from PyQt6.QtCore import QSize, Qt
from design.out_direction import SettingsWindow
from functions.read_from_file import read_rfid_from_file
from functions.fetch_do_no import fetch_do_numbers
from functions.fetch_wb import fetch_wb_code

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Digital Weighing System Pvt. Ltd")

        menubar = QMenuBar(self)
        menubar.setFixedHeight(40)

        # Create File menu
        file_menu = menubar.addMenu("Registration")
        icon = QIcon('app/static/icons/driving-test.png')
        icon.addPixmap(QPixmap(icon.pixmap(QSize(32, 32))))  # Set the desired icon size
        file_menu.setIcon(icon)
        

        new_action = QAction("New", self)
        file_menu.addAction(new_action)

        file_menu.addSeparator()  # Separator line between items

        # Create Configure menu
        configure_menu = menubar.addMenu("Out Dir")
        icon = QIcon('app/static/icons/edit.png')
        icon.addPixmap(QPixmap(icon.pixmap(QSize(32, 32))))  # Set the desired icon size
        configure_menu.setIcon(icon)

        settings_action = QAction("Open", self)
        configure_menu.addAction(settings_action)

        # Left side container
        self.container_left = QGroupBox("Register Tag", self)

        # container_left.setStyleSheet("background-color: #303030;")
        
        self.rfid_tag_label = QLabel("RFID Tag")
        self.rfid_tag = QTextEdit()
        self.vehicle_type_label = QLabel("Type of vehicle")
        self.vehicle_type = QComboBox()
        self.vehicle_no_label = QLabel("Vehicle No")
        self.vehicle_no = QTextEdit()
        self.do_no_label = QLabel("DO Number")
        self.do_no = QComboBox()
        self.transporter_label = QLabel("Transporter")
        self.transporter = QComboBox()
        self.driver_label = QLabel("Driver/Owner")
        self.driver = QTextEdit()
        self.weighbridge_label = QLabel("Weighbridge No")
        self.weighbridge = QComboBox()
        self.purpose_label = QLabel("Visit Purpose")
        self.purpose = QTextEdit()
        self.place_visit_label = QLabel("Place to Visit")
        self.place_visit = QTextEdit()
        self.person_visit_label = QLabel("Person Visit")
        self.person_visit = QTextEdit()
        self.validity_label = QLabel("Validity Till")
        self.validity = QDateEdit()
        self.registered_label = QLabel("Tag Already Registered")
        self.space1 = QLabel(" ")
        self.space2 = QLabel(" ")

        self.new_button = QPushButton("New")
        self.edit_button = QPushButton("Edit")
        self.save_button = QPushButton("Save")
        self.delete_button = QPushButton("Delete")
        self.close_button = QPushButton("Close")

        # Connections
        self.new_button.clicked.connect(self.read_rfid_and_display)
        self.do_no.currentIndexChanged.connect(self.populate_wb_code)
        self.populate_do_numbers()

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
        self.weighbridge.setFixedSize(200, 30)
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

        # Create a form layout for organizing labels and corresponding entry boxes
        form_layout = QFormLayout(self.container_left)
        form_layout.addRow(self.rfid_tag_label, self.rfid_tag)
        form_layout.addRow(self.vehicle_type_label, self.vehicle_type)
        form_layout.addRow(self.vehicle_no_label, self.vehicle_no)
        form_layout.addRow(self.do_no_label, self.do_no)
        form_layout.addRow(self.transporter_label, self.transporter)
        form_layout.addRow(self.driver_label, self.driver)
        form_layout.addRow(self.weighbridge_label, self.weighbridge)
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

        # Right side container with a table
        self.container_right = QFrame(self)

        table = QTableWidget(self)
        table.setColumnCount(7)  # Number of columns
        table.setHorizontalHeaderLabels(["RFID TAG", "TYPE", "VEHICLE NO", "DO NO", "TRANSPORTER", "DRIVER", "WB NO"])

        # Set up your table with data if needed
        
        table.setRowCount(19)  # Number of rows
        for i in range(10):
            for j in range(7):
                item = QTableWidgetItem(f"First Value {i+1}, Second Value {j+1}")
                item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
                table.setItem(i, j, item)

        # Adjust column widths
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

        container_right_layout = QVBoxLayout(self.container_right)
        container_right_layout.addWidget(table)
        
         # Create a splitter to add a vertical separator
        splitter = QSplitter(Qt.Orientation.Vertical)
        splitter.addWidget(self.container_left)
        splitter.addWidget(self.container_right)

        # Set the main layout of the widget to a horizontal layout containing the splitter
        main_layout = QHBoxLayout(self)
        main_layout.setMenuBar(menubar)
        main_layout.addWidget(splitter)
        main_layout.addWidget(self.container_right)
        self.setLayout(main_layout)

        self.container_left.setVisible(False)
        self.container_right.setVisible(False)
        
        # Connect the menu action to a slot that shows or hides containers
        file_menu.triggered.connect(self.toggle_containers)
        
        # Connect the "New" action to show the containers
        new_action.triggered.connect(self.show_containers)

        # Create the SettingsWindow as a member variable
        self.settings_window = SettingsWindow()

        # Connect the "Settings" action to show the settings window
        settings_action.triggered.connect(self.show_settings_window)

        

    def toggle_containers(self, action):
        # Show or hide containers based on the selected menu action
        if action.text().lower() == "registration":
            self.container_left.setVisible(True)
            self.container_right.setVisible(True)
        else:
            self.container_left.setVisible(False)
            self.container_right.setVisible(False)

    def show_containers(self):
        # Show the containers when "Registration -> New" is clicked
        self.container_left.setVisible(True)
        self.container_right.setVisible(True)

    def show_settings_window(self):
        # Set the geometry (optional)
        self.settings_window.setGeometry(100, 100, 400, 200)

        self.settings_window.show()

        # Launch as a modal dialog
        # result = self.settings_window.exec()


        # # Process any results from the dialog, if applicable
        # if result == QDialog.Accepted:
        #     # Handle dialog acceptance
        # elif result == QDialog.Rejected:
        #     # Handle dialog rejection
        # else:
        #     # Handle other possible results


    def read_rfid_and_display(self):
        print("Button Clicked")
        result, rfid_tag_value = read_rfid_from_file()

        print("DB:", rfid_tag_value)

        if result is not None:
            if result:
                # RFID tag is present in the database
                self.rfid_tag.setPlainText(rfid_tag_value)

                # Update vehicle_no and vehicle_type based on the database result
                self.vehicle_no.setPlainText(result.vehicle_no)

                # Clear the existing items in the combo box
                self.vehicle_type.clear()

                # Add the new item to the combo box
                self.vehicle_type.addItem(result.vehicle_type)

                # Set the current text of the combo box
                self.vehicle_type.setEditText(result.vehicle_type)

                # Force layout update
                self.layout().update()
                QApplication.processEvents()  # Ensure GUI updates
            else:
                print(f"RFID tag '{rfid_tag_value}' not found in the database.")
        else:
            print("Error fetching data from the file.")

        
    def populate_do_numbers(self):
        # Clear existing items in the ComboBox
        self.do_no.clear()

        # Optionally, add an empty item as the default (you can skip this line if you don't want an empty default)
        self.do_no.addItem("")

        # Populate the QComboBox with DO Numbers from the database
        do_numbers = fetch_do_numbers()

        # Add each DO Number to the QComboBox
        for do_number in do_numbers:
            self.do_no.addItem(do_number)

    def populate_wb_code(self, index):
        # Clear existing items in the Weighbridge ComboBox
        self.weighbridge.clear()

        # Fetch the selected DO Number from the do_no ComboBox
        selected_do_no = self.do_no.currentText()

        if selected_do_no:
            # Fetch the corresponding wb_code based on the selected DO Number
            wb_code = fetch_wb_code(selected_do_no)

            # Add the fetched wb_code to the Weighbridge ComboBox
            self.weighbridge.addItem(wb_code)

            # Optionally, set the initial selection
            self.weighbridge.setCurrentIndex(0)


