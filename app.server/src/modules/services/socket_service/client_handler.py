
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
            json_message["command"] == "[LOGIN_INF]" and 
            json_message["route"]["to"] == "server"
        ):            
            self._signal.emit(json_dumps({
                "message": {
                    "system": json_message["option"]["sys_info"],
                    "ip": self.client_address[0],
                    "port": str(self.client_address[1]),
                    "name": json_message["option"]["username"]
                },
                "to": "TABLE_WIDGET",
                "type": "[ADD]"
            }))
        
        elif (json_message["command"] == "[CLOSE]" and 
            json_message["route"]["to"] == "server"):
            
            self._signal.emit(json_dumps({
                "message": self.client_address,
                "to": "TABLE_WIDGET",
                "type": "[REMOVE]"
            }))
        
        elif (json_message["command"] == "[REGISTER]" and 
            json_message["route"]["to"] == "server"):
            self._signal.emit(json_dumps({
                "message": json_message,
                "to": "DATABASE_ADAPTER",
                "client_ip_port": self.client_address,
                "type": "[ADD_USER]"
            }))
            
        elif (json_message["command"] == "[LOGIN]" and
            json_message["route"]["to"] == "server"):
            
            self._signal.emit(json_dumps({
                "message": json_message,
                "client_ip_port": self.client_address,
                "to": "DATABASE_ADAPTER",
                "type": "[LOGIN]"
            }))

    def start(self):
        while True:
            incoming_data = self.client_socket.recv(8096).decode("utf-8")
            self.cataliz_data(incoming_data)
