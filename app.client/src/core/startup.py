"""
    created at feb 26/2020 by Tirgar
    - start app from this class
"""
from sys import (
    exit as sys_exit, argv as sys_argv
)
from PyQt5.QtWidgets import QApplication

from gui.windows.window_handler.main_window_handler.mainwindow import MainWindow
from gui.windows.window_handler.main_window_handler.main_auth_window import MainAuthWindow
from modules.data.data_context import AppContext
from .inner_concentrate.concentrate import ConcentrateSubject


class StartUp:
    """ This is start up class for initilizing our services and other classes """

    def __init__(self):
        self.concentrate_subject = ConcentrateSubject()
        self.app = QApplication(sys_argv)
        self.__start_socket_service__()

    def __start_socket_service__(self):
        """ this functions start socket tcp service
            :params:
            :return:
        """
        from modules.services.socket_services.socket_service import SocketService

        self.socket_server = SocketService()
        self.socket_server.start()

    def start(self):
        """ start main gui application and other services
            :return:
        """

        def send_data_concentrate(data):
            from json import loads as json_loads    
            print(data)
            self.concentrate_subject.notify(message=data, to=json_loads(data)["to"])
        
        self.socket_server.signal.connect(send_data_concentrate)

        AppContext()
        self.concentrate_subject.attach(MainWindow())
        
        main_window = MainAuthWindow(socket_server=self.socket_server)
        main_window.execute_app()

        sys_exit(self.app.exec_())
