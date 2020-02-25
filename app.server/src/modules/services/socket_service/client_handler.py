
from threading import Thread
from socket import socket
from typing import Any
from time import sleep
from json import (dumps as json_dumps)


class ClientHandler(Thread):
    
    def __init__(self, client: socket, client_address: Any):
        Thread.__init__(self)
        
        self.client = client
        self.client_address = client_address
        
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
                    "message": "Welcome to WhatsUp server",
                    "command": "START",
                    "from": "server",
                    "group": "brodcast"
                })
            ).encode("utf-8"))

            sleep(.1)

            self.client.sendall(str(
                json_dumps({
                    "message": "",
                    "command": "AUTH",
                    "from": "server",
                    "group": "brodcast"
                })
            ).encode("utf-8"))
            self.first_message = True
            
            # TODO: write recv message from client and then send it to message handler system
