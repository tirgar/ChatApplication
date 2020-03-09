"""
    - created at Feb 23/2020 by Farzad-Tirgar
    -   This package start the main application and services
"""

from sys import (
    exit as sys_exit, argv as sys_argv
)
from PyQt5.QtWidgets import QApplication
from gui.windows.window_handlers.main_window_handler.mainwindow import MainWindow
from .inner_concentrate.concentrate import ConcentrateSubject


class StartUp:
    """ This is start up class for initilizing our services and other classes """

    def __init__(self):
        self.app = QApplication(sys_argv)
        self.init_services()
        self.__add_adapters__()
    
    def init_services(self):
        from modules.services.socket_service.socket_server import SocketServer
        self.socket_server = SocketServer()

    def __add_adapters__(self):
        from modules.data.database_adapter import DataBaseAdapter
        ConcentrateSubject().attach(DataBaseAdapter(self.socket_server))

    def start(self):
        """ start main gui application and other services
            :return:
        """
        main_window = MainWindow(socket_server=self.socket_server)
        main_window.execute_app()
        
        sys_exit(self.app.exec_())