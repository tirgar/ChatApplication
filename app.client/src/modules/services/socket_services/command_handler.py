"""
    created at feb 06/2020 by topcodermc
    - this package act as client socket command
"""

from socket import socket
from json import (
    loads as json_loads,
    dumps as json_dumps
)
from platform import uname


class CommandHandler:
    def __init__(self, client_socket: socket, signal):
        self.client_socket = client_socket
        self.signal = signal
        
    def __send_hi_message__(self) -> str:        
        return json_dumps({
            "message": "",
            "params": "",
            "command": "[FIRST]",
            "session": "",
            "route": {
                "group": "",
                "to": "server"
            },
            "option": {
                "sys_info": str(uname().system)
            }
        })
        
    def start(self):
        self.client_socket.sendall(self.__send_hi_message__().encode("utf-8"))
        while True:
            incoming_message = json_loads(
                self.client_socket.recv(8096).decode("utf-8")
            )
            
            print(incoming_message)
            
            if incoming_message["command"] == "[REGISTER]":
                data = json_dumps({
                    "message": incoming_message,
                    "to": "SIGN_UP"
                })
                self.signal.emit(data)
            elif incoming_message["command"] == "[LOGIN]":
                data = json_dumps({
                    "message": incoming_message,
                    "to": "SIGN_IN"
                })
                self.signal.emit(data)
