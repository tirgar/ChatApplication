"""
    - created at Feb 23/2020 by Farzad-Tirgar
    -   This package start the main application and services
"""

from sys import (
    exit as sys_exit, argv as sys_argv
)
from PyQt5.QtWidgets import QApplication
from gui.windows.mainwindow import MainWindow


class StartUp:
    """ This is start up class for initilizing our services and other classes """

    def __init__(self):
        self.app = QApplication(sys_argv)
        self.init_services()
    
    def init_services(self):
        from modules.services.socket_service.socket_server import SocketServer
        self.socket_server = SocketServer()

    def start(self):
        """ start main gui application and other services
            :return:
        """
        main_window = MainWindow(socket_server=self.socket_server)
        main_window.execute_app()
        
        sys_exit(self.app.exec_())