
from threading import Thread
from socket import socket
from typing import Any
from time import sleep
from json import (dumps as json_dumps, loads as json_loads)

from core.inner_concentrate.concentrate import ConcentrateSubject


class ClientHandler:
    
    def __init__(self, client: socket, client_address: Any, signal: Any): 
        self.client_socket = client
        self.client_address = client_address
        self._signal = signal

    def cataliz_data(self, message):
        json_message = json_loads(message)
        
        if (
            json_message["command"] == "[FIRST]" and 
            json_message["route"]["to"] == "server"
        ):
            try:
                print(json_message)
                new_message = {
                    "system": json_message["option"]["sys_info"],
                    "ip": self.client_address[0],
                    "port": str(self.client_address[1]),
                    "name": "new client"
                }
                data = json_dumps({
                    "message": new_message,
                    "to": "TABLE_WIDGET"
                })
                self._signal.emit(data)

            except Exception as error:
                print(error)
    
    def start(self):
        while True:
            incoming_data = self.client_socket.recv(8096).decode("utf-8")
            self.cataliz_data(incoming_data)
