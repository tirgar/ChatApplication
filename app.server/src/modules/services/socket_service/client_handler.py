
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
            new_message = {
                "system": json_message["option"]["sys_info"],
                "ip": self.client_address[0],
                "port": str(self.client_address[1]),
                "name": "new client"
            }                              # TODO get user name
            data = json_dumps({
                "message": new_message,
                "to": "TABLE_WIDGET",
                "type": "[ADD]"
            })
        elif (json_message["command"] == "[CLOSE]" and 
            json_message["route"]["to"] == "server"):
            data = json_dumps({
                "message": self.client_address,
                "to": "TABLE_WIDGET",
                "type": "[REMOVE]"
            })
        elif (json_message["command"] == "[REGISTER]" and 
            json_message["route"]["to"] == "server"):
            try:
                data = json_dumps({
                    "message": json_message,
                    "to": "DATABASE_ADAPTER",
                    "client_ip_port": self.client_address,
                    "type": "[ADD_USER]"
                })
            except Exception as error:
                print(error)
        elif (json_message["command"] == "[INFO]" and
              json_message["route"]["to"] == "server"):
            try:
                data = json_dumps({
                    "message": json_message,
                    "to": "TABLE_WIDGET",
                    "client_ip_port": self.client_address,
                    "type": "[USER_INFO]"
                })
            except Exception as error:
                print(error)

        self._signal.emit(data)

    def start(self):
        while True:
            incoming_data = self.client_socket.recv(8096).decode("utf-8")
            self.cataliz_data(incoming_data)
