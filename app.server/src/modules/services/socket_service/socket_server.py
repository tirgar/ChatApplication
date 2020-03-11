
from socket import (
    socket, AF_INET, SOCK_STREAM,
    SOL_SOCKET, SO_REUSEADDR
)
from concurrent.futures import ThreadPoolExecutor
from json import (dumps as json_dumps)

from utils.config_manager import ConfigManager
from .client_handler import ClientHandler

from PyQt5.QtCore import QThread, pyqtSignal


class SocketServer(QThread):
    
    clients_set: set = set()
    
    _signal = pyqtSignal(object)
    
    def __init__(self, parent=None):
        super(SocketServer, self).__init__(parent=parent)

        self.socket_server = socket(AF_INET, SOCK_STREAM)
        self.socket_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        
        self.config_manager = ConfigManager()
    
    def get_client(self, client_ip_port: str):
        for client_object in self.clients_set:
            if client_ip_port == client_object[1]:
                return client_object[0]  # return client object socket
    
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
        with ThreadPoolExecutor(500) as thr_pool:
            while True:
                client_socket, client_address = self.socket_server.accept()
                # client_address => ('ip', int(port))
                
                self.clients_set.add((
                    client_socket, str(client_address[0] + ":" + str(client_address[1]))
                ))

                data_transfer = json_dumps({
                    "client_address": client_address,
                    "message": "Connect to server",
                    "to": "EDIT_LOGGER",
                    "type_log": "CLIENT_LOG"
                })

                self._signal.emit(data_transfer)

                thr_pool.submit(self.serve_connections, client_socket, client_address)

    def serve_connections(self, client_socket, client_address):
        ClientHandler(
            client=client_socket, client_address=client_address, 
            signal=self._signal
        ).start()  # on blocking code
        # threading.current_thread().join()
    
    @property
    def signal(self):
        return self._signal
