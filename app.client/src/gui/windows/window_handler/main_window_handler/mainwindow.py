"""
    created at feb 28/2020 by Tirgar
    this class is for client main window of chat application
"""

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QGridLayout, QVBoxLayout,QGroupBox
)
from PyQt5.QtCore import Qt

from gui.styles.windows.main_window_style import *
from .contact_list_widget import ContactList


class MainWindow(QMainWindow):
    def __init__(self, parent=None, socket_server=None):
        super(MainWindow, self).__init__(parent=parent, )

        self.socket_server = socket_server

        self.setWindowTitle("main window")
        self.setContentsMargins(0, 0, 0, 0)
        self.setLayoutDirection(Qt.RightToLeft)
        self.setAccessibleName(main_window_styles[0])
        self.setStyleSheet(main_window_styles[1])

        self.__set_main_widget__()

    def __set_main_widget__(self):
        """ Add centeral widget for switching between widgets in main window
            :return:
        """
        main_widget = QWidget(self)
        main_widget.setContentsMargins(0, 0, 0, 0)
        # add widget to main widget
        self.main_widget_layout = QGridLayout(main_widget)
        self.main_widget_layout.setContentsMargins(0, 0, 0, 0)
        contact_list_widget = ContactList()
        self.main_widget_layout.addWidget(contact_list_widget)

        self.setCentralWidget(main_widget)

    def execute_app(self):
        self.show()