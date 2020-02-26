"""
    created at feb 26/2020 by Tirgar
    - start app from this class
"""


class StartUp:

    def __init__(self):
        pass

    def __start_socket_service__(self):
        """ this functions start socket tcp service
            :params:
            :return:
        """
        from modules.services.socket_services.socket_service import ClientSocketService

        ClientSocketService()

    def start(self):
        """ this function start app from this lines
            :params:
            :return:
        """

        self.__start_socket_service__()