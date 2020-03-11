"""
    created at feb 26/2020 by Tirgar
    - this package act as client socket service for
        connection to server
"""

from socket import (
    socket, AF_INET, SOL_SOCKET, SO_REUSEADDR, SOCK_STREAM
)
from PyQt5.QtCore import QThread, pyqtSignal

from utils.config_manager import ConfigManager
from .command_handler import CommandHandler


class SocketService(QThread):

    _signal = pyqtSignal(object)

    def __init__(self, parent=None):
        super(SocketService, self).__init__(parent=parent)
        self.config_manager = ConfigManager()

        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    @property
    def get_socket(self):
        return self.sock

    def __try_connecting_to_server__(self):
        """ this function try connecting to server
           :param:
           :return:
        """  
        response_code = self.sock.connect_ex((
            self.config_manager.get.socket_server.IP,
            self.config_manager.get.socket_server.PORT,
        ))
        if response_code == 0:
            print("[+] Client connect to server successfully")
            # self._signal.emit(message)
        else:
            message = "[-] Server no response maybe it is down ..."
            self._signal.emit(message)

    def run(self):
        self.__try_connecting_to_server__()
        CommandHandler(
            client_socket=self.sock, signal=self._signal
        ).start()

    @property
    def signal(self):
        return self._signal
