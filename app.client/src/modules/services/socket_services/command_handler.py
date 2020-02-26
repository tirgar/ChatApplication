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
        self.client_socket = client_socket

    def start(self):
        """ start command handler service
            :params:
            :return:
        """

        name = input("Enter your name ")
        systen = input("Enter your system platform")

        self.client_socket.sendall(
            json_dumps({
                "message": {
                    "name": name,
                    "system": systen
                }
            })
        ).encode("utf-8")

        self.start()

