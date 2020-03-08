"""
    created  at march 06/2020 by Tirgar
    this class is for main window of server gui
"""
from PyQt5.QtWidgets import (
    QMainWindow, QGroupBox, QWidget, QGridLayout, QHBoxLayout
    )

from gui.styles.windows.main_window_style import *
from interfaces.observer_pattern.observer import Observer
from core.inner_concentrate.concentrate import ConcentrateSubject


class MainWindow(Observer, QMainWindow):
    """ this class make the main window gui of server app """

    def __init__(self, parent=None, socket_server=None):
        super(MainWindow, self).__init__(parent=parent)
        self.concentrate_subject = ConcentrateSubject()
        self.concentrate_subject.attach(self)

        self.socket_server = socket_server

        self.setWindowTitle("main window")
        self.setContentsMargins(0, 0, 0, 0)

        self.setAccessibleName(main_window_styles[0])
        self.setStyleSheet(main_window_styles[1])

        self.__set_main_widget__()

    @property
    def class_name(self):
        """ this function return a class name to access in codes """

        return "MAIN_WINDOW"

    def __set_main_widget__(self):
        """ Add centeral widget for switching between widgets in main window
            :return:
        """
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        self.main_widget_layout = QHBoxLayout()
        self.main_widget_layout.setStretch(0, 0)
        self.main_widget_layout.setContentsMargins(0, 0, 0, 0)

        self.__create_grid_layout__()

        self.main_widget_layout.addWidget(self.horizontalGroupBox)
        main_widget.setLayout(self.main_widget_layout)

    def __create_grid_layout__(self):
        """ this function create a grid layout to add widgets on it """

        self.horizontalGroupBox = QGroupBox()
        self.horizontalGroupBox.setContentsMargins(0, 0, 0, 0)

        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        from ...pages.main_window_widgets.main_server_widget import ServerMainWidget
        from ...pages.main_window_widgets.table_widget import TableWidget

        server_widget = ServerMainWidget(parent=self, socket_server=self.socket_server)
        table_widget = TableWidget(parent=self, socket_server=self.socket_server)

        layout.addWidget(server_widget, 0, 0)
        layout.addWidget(table_widget, 0, 1)

        self.horizontalGroupBox.setLayout(layout)

    def execute_app(self):
        """ this function show up the window """

        self.show()
