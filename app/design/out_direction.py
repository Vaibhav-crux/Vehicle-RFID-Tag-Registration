from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QTextEdit, QFormLayout, QGroupBox, QCalendarWidget, QDateEdit, QTimeEdit

class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()

        # self.setFixedSize(800, 600)
        self.setWindowTitle("Out Dir")

        # Create a group box for the "Out Directions" section
        self.out_directions_group_box = QGroupBox("Out Directions", self)

        # Create a form layout for the "Out Directions" section
        self.out_directions_layout = QFormLayout(self.out_directions_group_box)
        self.out_directions_layout.setVerticalSpacing(5)  # Set the vertical spacing between rows

        # Add labels and text edits to the "Out Directions" layout
        self.rfid_label = QLabel("Rfid Tag")
        self.rfid = QTextEdit()
        self.vehicle_no_label = QLabel("Vehicle Number")
        self.vehicle_no = QTextEdit()
        self.status_label = QLabel("Status")
        self.status = QTextEdit()
        self.trip_label = QLabel("Trip Count")
        self.trip = QTextEdit()

        self.rfid.setFixedSize(200, 30)
        self.vehicle_no.setFixedSize(200, 30)
        self.status.setFixedSize(200, 30)
        self.trip.setFixedSize(200, 30)

        # Add rows to the "Out Directions" layout
        self.out_directions_layout.addRow(self.rfid_label, self.rfid)
        self.out_directions_layout.addRow(self.vehicle_no_label, self.vehicle_no)
        self.out_directions_layout.addRow(self.status_label, self.status)
        self.out_directions_layout.addRow(self.trip_label, self.trip)

        # Set the layout for the "Out Directions" group box
        self.out_directions_group_box.setLayout(self.out_directions_layout)

        # Create a group box for the "Challan Detail" section
        self.challan_detail_group_box = QGroupBox("Challan Detail", self)

        # Create a form layout for the "Challan Detail" section
        self.challan_detail_layout = QFormLayout(self.challan_detail_group_box)

        # Add labels and text edits to the "Challan Detail" layout
        self.weighbridge_label = QLabel("Weighbridge")
        self.weighbridge = QTextEdit()
        self.invoice_no_label = QLabel("Invoice No")
        self.invoice_no = QTextEdit()
        self.vehicle_no_label = QLabel("Vehicle No")
        self.vehicle_no = QTextEdit()
        self.do_no_label = QLabel("Do Numnber")
        self.do_no = QTextEdit()
        self.gross_label = QLabel("Gross Weight")
        self.gross = QTextEdit()
        self.tare_label = QLabel("Tare Weight")
        self.tare = QTextEdit()
        self.net_label = QLabel("Net Weight")
        self.net = QTextEdit()
        self.weightment_date_label = QLabel("Weightment Date")
        self.weightment_date = QDateEdit()
        self.weightment_time_label = QLabel("Weightment Time")
        self.weightment_time = QTimeEdit()
        
        self.weighbridge.setFixedSize(200, 30)
        self.invoice_no.setFixedSize(200, 30)
        self.vehicle_no.setFixedSize(200, 30)
        self.do_no.setFixedSize(200, 30)
        self.gross.setFixedSize(200, 30)
        self.tare.setFixedSize(200, 30)
        self.net.setFixedSize(200, 30)
        self.weightment_date.setFixedSize(200, 30)
        self.weightment_time.setFixedSize(200, 30)

        # Add rows to the "Challan Detail" layout
        self.challan_detail_layout.addRow(self.weighbridge_label, self.weighbridge)
        self.challan_detail_layout.addRow(self.invoice_no_label, self.invoice_no)
        self.challan_detail_layout.addRow(self.vehicle_no_label, self.vehicle_no)
        self.challan_detail_layout.addRow(self.do_no_label, self.do_no)
        self.challan_detail_layout.addRow(self.gross_label, self.gross)
        self.challan_detail_layout.addRow(self.tare_label, self.tare)
        self.challan_detail_layout.addRow(self.net_label, self.net)
        self.challan_detail_layout.addRow(self.weightment_date_label, self.weightment_date)
        self.challan_detail_layout.addRow(self.weightment_time_label, self.weightment_time)
        

        # Set the layout for the "Challan Detail" group box
        self.challan_detail_group_box.setLayout(self.challan_detail_layout)

        # Create a group box for the "Extra Detail" section
        self.extra_detail_group_box = QGroupBox("", self)

        # Create a form layout for the "Extra Detail" section
        self.extra_detail_layout = QFormLayout(self.extra_detail_group_box)

        # Add labels and text edits to the "Extra Detail" layout
        self.rfid_label = QLabel("Rfid_Tag")
        self.rfid = QTextEdit()
        self.type_label = QLabel("Type")
        self.type = QTextEdit()
        self.do_no_label = QLabel("DO NO")
        self.do_no = QTextEdit()
        self.transp_label = QLabel("Transp")
        self.trans = QTextEdit()
        self.driver_label = QLabel("Driver")
        self.driver = QTextEdit()
        self.wb_no_label = QLabel("WB. No.")
        self.wb_no = QTextEdit()
        self.purpose_label = QLabel("Purpose")
        self.purpose = QTextEdit()
        self.place_label = QLabel("Place")
        self.place = QTextEdit()
        self.person_label = QLabel("Person")
        self.person = QTextEdit()

        self.rfid.setFixedSize(200, 30)
        self.type.setFixedSize(200, 30)
        self.do_no.setFixedSize(200, 30)
        self.trans.setFixedSize(200, 30)
        self.driver.setFixedSize(200, 30)
        self.wb_no.setFixedSize(200, 30)
        self.purpose.setFixedSize(200, 30)
        self.place.setFixedSize(200, 30)
        self.person.setFixedSize(200, 30)

        # Add rows to the "Extra Detail" layout
        self.extra_detail_layout.addRow(self.rfid_label, self.rfid)
        self.extra_detail_layout.addRow(self.type_label, self.type)
        self.extra_detail_layout.addRow(self.do_no_label, self.do_no)
        self.extra_detail_layout.addRow(self.transp_label, self.trans)
        self.extra_detail_layout.addRow(self.wb_no_label, self.wb_no)
        self.extra_detail_layout.addRow(self.driver_label, self.driver)
        self.extra_detail_layout.addRow(self.purpose_label, self.purpose)
        self.extra_detail_layout.addRow(self.place_label, self.place)
        self.extra_detail_layout.addRow(self.person_label, self.person)

        # Set the layout for the "Extra Detail" group box
        self.extra_detail_group_box.setLayout(self.extra_detail_layout)

        # Create a vertical layout for the main window
        main_layout = QHBoxLayout(self)
        main_layout.addWidget(self.out_directions_group_box)
        main_layout.addWidget(self.challan_detail_group_box)
        main_layout.addWidget(self.extra_detail_group_box)
        self.setLayout(main_layout)