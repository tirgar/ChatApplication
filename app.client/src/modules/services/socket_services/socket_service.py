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

    def __try_connect__(self):
        """ this function try connecting to server
           :param:
           :return:
        """
        print("[+] Try connecting to server ..")
        while True:
            response_code = self.sock.connect_ex((
                self.config_manager.get.socket_server.IP,
                self.config_manager.get.socket_server.PORT,
            ))

            if response_code == 0:
                message = "[+] Client connect to server successfully"
                # CommandHandler(client_socket=self.sock).start()
                self._signal.emit(message)
                return True

            elif response_code == 111:
                message = "[-] server no response maybe it is down ..."
                self._signal.emit(message)
                return False
            # threading.current_thread().join()

    @property
    def signal(self):
        return self._signal
