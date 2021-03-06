from interfaces.observer_pattern.observer import Observer
from .data_context import User

from time import sleep
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
                username = incoming_message["message"]["message"]["USERNAME"]
                client_socket.sendall(json_dumps({
                    "message": "User created successfully",
                    "option": {
                        "username": username
                    },
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
                username = incoming_message["message"]["message"]["username"]
                user_id = authenticated[0].id

                query_online = User.update(is_online=True).where(User.id == user_id)
                query_online.execute()

                online_users_query = User.select().where(
                    User.is_online == True
                )

                online_users = list()
                for item in online_users_query:
                    online_users.append({
                        "username": item.username,
                        "id": item.id
                    })

                client_socket.sendall(json_dumps({
                    "message": "Authenticated",
                    "option": {
                        "username": username,
                        "online_users": online_users
                    },
                    "command": "[LOGIN]",
                    "code": 200  # this code means ok result
                }).encode("utf-8"))

            else:
                client_socket.sendall(json_dumps({
                    "message": "Not Authorized",
                    "command": "[LOGIN]",
                    "code": 401  # this code means ok result
                }).encode("utf-8"))
                self.socket_server.delete_client_from_cliets_set(
                    str(
                        incoming_message["client_ip_port"][0] + ":"
                        + str(incoming_message["client_ip_port"][1])
                    )
                )
