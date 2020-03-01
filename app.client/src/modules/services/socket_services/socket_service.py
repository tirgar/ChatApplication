"""
    created at feb 26/2020 by Tirgar
    - this package act as client socket service for
        connection to server
"""

from socket import (
    socket, AF_INET, SOL_SOCKET, SO_REUSEADDR, SOCK_STREAM
)

from utils.config_manager import ConfigManager
from .command_handler import CommandHandler
from gui.components.message_box import MessageBox


class SocketService:
    def __init__(self):
        self.config_manager = ConfigManager()

        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

        self.__connect__()

    def __connect__(self):
        """ this function try connecting to server
           :param:
           :return:
        """
        print("[+] Try connecting to server ..")

        response_code = self.sock.connect_ex((
            self.config_manager.get.socket_server.IP,
            self.config_manager.get.socket_server.PORT,
        ))

        if response_code == 0:
            print("[+] Client connect to server successfully")
            CommandHandler(client_socket=self.sock).start()

        elif response_code == 111:
            MessageBox(
                title="Error",
                message="[-] server no response maybe it is down ..."
            ).show()
            # `print("[-] server no response maybe it is down ...")