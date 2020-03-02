"""
    created at feb 26/2020 by Tirgar
    - start app from this class
"""
from sys import (
    exit as sys_exit, argv as sys_argv
)
from PyQt5.QtWidgets import QApplication

from gui.windows.window_handler.main_window_handler.mainwindow import MainWindow


class StartUp:
    """ This is start up class for initilizing our services and other classes """

    def __init__(self):
        self.app = QApplication(sys_argv)
        self.__start_socket_service__()

    def __start_socket_service__(self):
        """ this functions start socket tcp service
            :params:
            :return:
        """
        from modules.services.socket_services.socket_service import SocketService

        self.socket_server = SocketService()

    def start(self):
        """ start main gui application and other services
            :return:
        """
        main_window = MainWindow(socket_server=self.socket_server)
        main_window.execute_app()

        sys_exit(self.app.exec_())
