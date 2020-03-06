"""
    - created at march 06/2020 by Tirgar

    -- this package is main server widget
"""

from PyQt5.QtWidgets import QVBoxLayout, QWidget

from gui.styles.pages.main_window_widgets.main_server_widget_styles import *
from .server_info_widget import ServerInfo
from .server_logs_widget import ServerLogs


class ServerMainWidget(QWidget):
    """ this class make main server widget to add another widgets on it """

    def __init__(self, parent=None, socket_server=None):
        super(ServerMainWidget, self).__init__(parent=parent)
        self.socket_server = socket_server

        self.setAccessibleName(main_server_widget_styles[0])
        self.setStyleSheet(main_server_widget_styles[1])

        self.server_main_layout = QVBoxLayout()
        self.server_main_layout.setContentsMargins(0, 0, 0, 0)
        self.server_main_layout.setStretch(0, 0)
        self.server_main_layout.setSpacing(0)

        self.setLayout(self.server_main_layout)
        self.__add_widgets__()

    def __add_widgets__(self):
        """ this function add imported widget on main layout """

        server_info = ServerInfo(parent=self, socket_server=self.socket_server)
        server_logs = ServerLogs(parent=self)

        self.server_main_layout.addWidget(server_info)
        self.server_main_layout.addWidget(server_logs)
