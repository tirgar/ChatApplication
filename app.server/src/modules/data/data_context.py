
from peewee import (
    Model, CharField, DateTimeField,
    SqliteDatabase, BooleanField
)


class AppContext:
    data_context = SqliteDatabase("./assets/server.db")

    def __init__(self):
        self.data_context.connect(reuse_if_open="True")
        self.data_context.create_tables([User])


class BaseModel(Model):
    class Meta:
        database = AppContext.data_context


class User(BaseModel):
    username = CharField(unique=True, max_length=100)
    password = CharField(max_length=100)
    created_time = DateTimeField()
    is_online = BooleanField()
