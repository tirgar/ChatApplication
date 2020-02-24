
from socket import (
    socket, AF_INET, SOCK_STREAM,
    SOL_SOCKET, SO_REUSEADDR
)

from utils.config_maneger import ConfigManager


class SocketServer:
    
    def __init__(self, server_ip: str, server_port: int):
        super().__init__()
        
        self.server_ip: str = server_ip
        self.server_port: int = server_port
        
        self.socket_server = socket(AF_INET, SOCK_STREAM)
        self.socket_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        
        self.config_manager = ConfigManager()
    
    def try_binding(self) -> tuple:
        """ trying to binding server with IP and Port inserted
            :return tuple: (bool, str) => binding status
        """

        try:
            # start listening to client from this IP and PORT
            self.socket_server.listen(self.config_manager.get.SOCKET_SERVER.CLIENT_COUNT)
            self.socket_server.bind((self.server_ip, self.server_port))
            return (True, "[+] Server binding was successfull ...")
        except Exception as error:
            return (False, error)
    
    def run(self, start: bool):
        """ run server for accepting new client
            :params start: start or stoping the server
            :return:
        """
        while start:
            client, client_address = self.socket_server.accept()
            
        
