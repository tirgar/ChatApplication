
from threading import Thread
from socket import socket
from typing import Any
from time import sleep
from json import (dumps as json_dumps)

from core.inner_concentrate.concentrate import ConcentrateSubject


class ClientHandler(Thread):
    
    def __init__(self, client: socket, client_address: Any):
        Thread.__init__(self)
        
        self.client = client
        self.client_address = client_address
        self.concentrate = ConcentrateSubject()
        
        self.first_message: bool = False
        
    def run(self):
        """ run new client thread from this function 
            :params:
            :return:
        """
        if self.first_message is False:
            # send welcome message to server
            self.client.sendall(str(
                json_dumps({
                    "message": "Welcome to server",
                    "command": "START",
                    "from": "server",
                    "group": "broadcast"
                })
            ).encode("utf-8"))

            sleep(.1)

            self.client.sendall(str(
                json_dumps({
                    "message": "",
                    "command": "AUTH",
                    "from": "server",
                    "group": "broadcast"
                })
            ).encode("utf-8"))
            self.first_message = True
            
            self.concentrate.notify(message="New client add to system", to="MAIN_WINDOW")
            # TODO: write recv message from client and then send it to message handler system
