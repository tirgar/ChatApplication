"""
    created at feb 06/2020 by topcodermc
    - this package act as client socket command
"""

from socket import socket
from json import (
    loads as json_loads,
    dumps as json_dumps
)
from datetime import datetime


class CommandHandler:
    def __init__(self, client_socket: socket):
        self.client_socket: socket = client_socket
        self.start_tx_rc: bool = True

    def start(self):
        """ start command handler service
            :params:
            :return:
        """        
        
        while self.start_tx_rc:
            welcome_message = self.client_socket.recv(8096)
            message_loads = json_loads(welcome_message.decode("utf-8"))
            print(message_loads)