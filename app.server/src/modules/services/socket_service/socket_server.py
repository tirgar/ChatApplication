
from socket import (
    socket, AF_INET, SOCK_STREAM,
    SOL_SOCKET, SO_REUSEADDR
)

from utils.config_manager import ConfigManager
from .client_handler import ClientHandler

from PyQt5.QtCore import QThread


class SocketServer(QThread):
    
    def __init__(self, parent=None):
        super(SocketServer, self).__init__(parent=parent)

        self.socket_server = socket(AF_INET, SOCK_STREAM)
        self.socket_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        
        self.config_manager = ConfigManager()
    
    def try_binding(self, server_ip: str, server_port: int) -> tuple:
        """ trying to binding server with IP and Port inserted
            :return tuple: (bool, str) => binding status
        """
        try:
            # start listening to client from this IP and PORT
            self.socket_server.bind((server_ip, server_port))
            self.socket_server.listen(self.config_manager.get.SOCKET_SERVER.CLIENT_COUNT)
            return True, "[+] binding was success"
        except Exception as error:
            # TODO: set this action to log service
            return False, "An error happened"
    
    def run(self):
        """ run server for accepting new client
            :params start: start or stoping the server
            :return:
        """

        while True:
            client, client_address = self.socket_server.accept()
            ClientHandler(client=client, client_address=client_address).start()
        
