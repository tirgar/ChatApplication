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
from interfaces.observer_pattern.observer import Observer
from core.inner_concentrate.concentrate import ConcentrateSubject
from gui.components.message_box import MessageBox


class MainWindow(Observer, QMainWindow):
    def __init__(self, parent=None, socket_server=None):
        super(MainWindow, self).__init__(parent=parent, )
        self.concentrate_subject = ConcentrateSubject()
        self.concentrate_subject.attach(self)

        self.socket_server = socket_server

        self.setWindowTitle("main window")
        self.setContentsMargins(0, 0, 0, 0)
        self.setLayoutDirection(Qt.RightToLeft)
        self.setAccessibleName(main_window_styles[0])
        self.setStyleSheet(main_window_styles[1])

        self.__set_main_widget__()
        self.__signal__()

    @property
    def class_name(self):
        return "MAIN_WINDOW"

    def __signal__(self):
        response = self.socket_server.__try_connect__()
        if response is True:
            def send_data_concentrate(data):
                self.socket_server.start()
                self.concentrate_subject.notify(message=data, to="MAIN_WINDOW")

            self.socket_server.signal.connect(send_data_concentrate)

        else:
            def send_data_concentrate(data):
                self.concentrate_subject.notify(message=data, to="MAIN_WINDOW")

            self.socket_server.signal.connect(send_data_concentrate)

    def notification(self, message):
        """ Receive update from subject
            :params message: incoming message
        """

        MessageBox(
            title="Error",
            message=str(message)
        ).show()

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