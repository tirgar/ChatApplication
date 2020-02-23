"""
    created by Farzad Tirgar at 23.feb
    this class is for main window of chat application
"""

from PyQt5.QtWidgets import (
    QMainWindow, QPushButton, QWidget, QGridLayout,
    QTableWidget, QApplication, QVBoxLayout, QGroupBox,
    QLineEdit,
)

from src.gui.styles.windows.main_window_style import *


class MainWindow(QMainWindow):
    def __init__(self , parent=None):
        super(MainWindow, self).__init__(parent=parent)

        self.setWindowTitle("main window")
        
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
        main_widget_layout = QGridLayout(main_widget)
        main_widget_layout.setContentsMargins(0, 0, 0, 0)

        self.setCentralWidget(main_widget)

    def __add__input__(self):
        """
        this function add layout with buttons widgets to grid_layout
        :return:
        """
        v_layout = QVBoxLayout()
        v_layout.setContentsMargins(0, 0, 0, 0)
        v_layout.addStretch(0)

        self.server_id_input = QLineEdit()
        self.server_id_input.setPlaceholderText("Server ID")
        self.setAccessibleName(server_id_input_style[0])
        self.setStyleSheet(server_id_input_style[1])

        self.port_input = QLineEdit()
        self.port_input.setPlaceholderText("Port")
        self.setAccessibleName(port_input_style[0])
        self.setStyleSheet(port_input_style[1])

        v_layout.addWidget(self.server_id_input)
        v_layout.addWidget(self.port_input)

        self.grid_layout.addLayout(v_layout, 0, 0)

    def execute_app(self):
        self.show()