
from socket import (
    socket, AF_INET, SOCK_STREAM,
    SOL_SOCKET, SO_REUSEADDR
)

from utils.config_manager import ConfigManager
from .client_handler import ClientHandler


class SocketServer:
    
    def __init__(self):
        super().__init__()

        self.socket_server = socket(AF_INET, SOCK_STREAM)
        self.socket_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        
        self.config_manager = ConfigManager()
        print(self.config_manager.get.SOCKET_SERVER.CLIENT_COUNT)
    
    def try_binding(self, server_ip: str, server_port: int) -> tuple:
        """ trying to binding server with IP and Port inserted
            :return tuple: (bool, str) => binding status
        """
        try:
            # start listening to client from this IP and PORT
            self.socket_server.bind((server_ip, server_port))
            self.socket_server.listen(self.config_manager.get.SOCKET_SERVER.CLIENT_COUNT)
            return (True, "[+] Server binding was successfull ...")
        except Exception as error:
            print(error)
            return (False, error)
    
    def run(self, start: bool):
        """ run server for accepting new client
            :params start: start or stoping the server
            :return:
        """
        while start:
            client, client_address = self.socket_server.accept()
            ClientHandler(client=client, client_address=client_address).start()
        
