
from interfaces.observer_pattern.observer import Observer
from .data_context import User

from json import (
    loads as json_loads,
    dumps as json_dumps
)
from datetime import datetime


class DataBaseAdapter(Observer):
    
    def __init__(self, socket_server=None):
        super(DataBaseAdapter, self).__init__()
        self.socket_server = socket_server

    @property
    def class_name(self):
        return "DATABASE_ADAPTER"
    
    def notification(self, message):
        incoming_message = json_loads(message)
        client_socket = self.socket_server.get_client(
            str(
                incoming_message["client_ip_port"][0] + ":" 
                + str(incoming_message["client_ip_port"][1])
            )
        )
        if incoming_message["type"] == "[ADD_USER]":
            try:
                User.create(
                    username=incoming_message["message"]["message"]["USERNAME"],
                    password=incoming_message["message"]["message"]["PASSWORD"],
                    created_time=datetime.now(),
                    is_online=True
                )
                client_socket.sendall(json_dumps({
                    "message": "User created successfully",
                    "command": "[REGISTER]",
                    "code": 200  # this code means ok result
                }).encode("utf-8"))
            except Exception as error:
                client_socket.sendall(json_dumps({
                    "message": "Please change your username",
                    "command": "[REGISTER]",
                    "code": 404
                }).encode("utf-8"))
        elif incoming_message["type"] == "[LOGIN]":
            authenticated = User.select().where(
                (User.username == incoming_message["message"]["message"]["username"]) & 
                (User.password == incoming_message["message"]["message"]["password"])
            )
            
            if authenticated.exists():
                client_socket.sendall(json_dumps({
                    "message": "Authenticated",
                    "command": "[LOGIN]",
                    "code": 200  # this code means ok result
                }).encode("utf-8"))
            else:
                client_socket.sendall(json_dumps({
                    "message": "Not Authorized",
                    "command": "[LOGIN]",
                    "code": 401  # this code means ok result
                }).encode("utf-8"))
