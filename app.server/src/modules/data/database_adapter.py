
from interfaces.observer_pattern.observer import Observer
from .data_context import User

from json import (
    loads as json_loads
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

        if incoming_message["type"] == "[ADD_USER]":
            try:
                User.create(
                    username=incoming_message["message"]["USERNAME"],
                    password=incoming_message["message"]["PASSWORD"],
                    created_time=datetime.now(),
                    is_online=True
                )
                # self.socket_server
            except Exception as error:
                print(error)
