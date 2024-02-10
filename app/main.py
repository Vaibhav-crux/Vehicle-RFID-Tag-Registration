import sys
from PySide6 import QtWidgets
import qdarkstyle
from design.login_page import LoginCrend
from design.menu_bars import MyWidget

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    app.setStyleSheet(qdarkstyle.load_stylesheet())

    widget = LoginCrend()

    # widget.resize(800, 600)
    widget.showMaximized()
    widget.show()

    sys.exit(app.exec())
