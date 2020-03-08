"""
    created at feb 28/2020 by Tirgar
    this class is for client main window of chat application
"""

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, 
    QGroupBox, QGridLayout, QVBoxLayout
)
from PyQt5.QtGui import QCloseEvent

from gui.styles.windows.main_window_style import *
from interfaces.observer_pattern.observer import Observer
from core.inner_concentrate.concentrate import ConcentrateSubject
from gui.components.message_box import MessageBox
from modules.services.socket_services.socket_service import SocketService


class MainWindow(Observer, QMainWindow):
    def __init__(self, parent=None, socket_server=None):
        super(MainWindow, self).__init__(parent=parent)
        self.concentrate_subject = ConcentrateSubject()
        self.concentrate_subject.attach(self)
        self.parent = parent
        self.socket_server = SocketService()

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
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        self.main_widget_layout = QHBoxLayout()
        self.main_widget_layout.setStretch(0, 0)
        self.main_widget_layout.setContentsMargins(0, 0, 0, 0)

        self.__create_grid_layout__()

        self.main_widget_layout.addWidget(self.horizontalGroupBox)
        main_widget.setLayout(self.main_widget_layout)

    def __create_grid_layout__(self):
        self.horizontalGroupBox = QGroupBox()
        self.horizontalGroupBox.setContentsMargins(0, 0, 0, 0)
 
        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        from ...pages.main_window_widgets.users_list_widgets import UserListWidget
        from ...pages.main_window_widgets.chat_main_widget import ChatMainWidget
        user_widget_main = UserListWidget(parent=self)
        chat_main_widget = ChatMainWidget(parent=self)

        layout.addWidget(user_widget_main, 0, 0)
        layout.addWidget(chat_main_widget, 0, 1)

        self.horizontalGroupBox.setLayout(layout)

    def execute_app(self):
        self.show()
        
    def closeEvent(self, a0: QCloseEvent) -> None:
        from json import dumps as json_dumps
        self.socket_server.get_socket.sendall(json_dumps({
            "message": None,
            "params": None,
            "command": "[CLOSE]",
            "session": None,
            "route": {
                "group": "",
                "to": "server"
            },
            "option": None
        }).encode("utf-8"))
        