"""
    created at feb 28/2020 by Tirgar
    this class is for client main window of chat application
"""

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, 
    QGroupBox, QGridLayout
)
from PyQt5.QtCore import Qt

from gui.styles.windows.main_window_style import *
from interfaces.observer_pattern.observer import Observer
from core.inner_concentrate.concentrate import ConcentrateSubject
from gui.components.message_box import MessageBox


class MainWindow(Observer, QMainWindow):
    def __init__(self, parent=None, socket_server=None):
        super(MainWindow, self).__init__(parent=parent)
        self.concentrate_subject = ConcentrateSubject()
        self.concentrate_subject.attach(self)
        self.setLayoutDirection(Qt.RightToLeft)
        self.socket_server = socket_server

        self.setWindowTitle("main window")
        self.setAccessibleName(main_window_styles[0])
        self.setStyleSheet(main_window_styles[1])
                
        self.__set_main_widget__()
        self.__signal_to_socket__()

    @property
    def class_name(self):
        return "MAIN_WINDOW"

    def __signal_to_socket__(self):
        self.socket_server.start()
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

        self.main_widget_layout = QHBoxLayout()
        self.main_widget_layout.setStretch(0, 0)
        self.main_widget_layout.setContentsMargins(0, 0, 0, 0)

        from ...pages.main_window_widgets.users_list_widgets import UserListWidget
        user_widget_main = UserListWidget(parent=self)
        self.main_widget_layout.addWidget(user_widget_main)

    def execute_app(self):
        self.show()