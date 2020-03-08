"""
    - created at march 06/2020 by Tirgar
    -- this package is server info widget
"""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLineEdit,
    QFrame, QLabel, QPushButton, QHBoxLayout
)

from gui.styles.pages.main_window_widgets.server_info_widget_styles import *
from interfaces.observer_pattern.observer import Observer
from core.inner_concentrate.concentrate import ConcentrateSubject

from json import (
    loads as json_loads,
    dumps as json_dumps
)


class ServerInfo(Observer, QWidget):
    """ this class make the server info inputs widget gui of server app """

    def __init__(self, parent=None, socket_server=None):
        super(ServerInfo, self).__init__(parent=parent)
        self.concentrate_subject = ConcentrateSubject()
        self.concentrate_subject.attach(self)

        self.socket_server = socket_server

        self.setAccessibleName(server_info_widget_styles[0])
        self.setStyleSheet(server_info_widget_styles[1])

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(self.__add_widget__())
        self.setLayout(main_layout)

    @property
    def class_name(self):
        """ this function return a class name to access in codes """

        return "SERVER_INFO"

    def __add_widget__(self):
        """ this function return a q-frame to use in main layout """

        main_frame = QFrame()
        main_frame.setContentsMargins(0, 10, 0, 0)
        main_frame.setAccessibleName(main_frame_styles[0])
        main_frame.setStyleSheet(main_frame_styles[1])

        frame_layout = QVBoxLayout()
        frame_layout.setContentsMargins(0, 0, 0, 0)
        frame_layout.setStretch(0, 0)
        frame_layout.setSpacing(0)

        self.server_ip_input = QLineEdit()
        self.server_ip_input.setPlaceholderText("Server IP")
        self.server_ip_input.setText("127.0.0.1")
        self.server_ip_input.setAccessibleName(server_ip_input_style[0])
        self.server_ip_input.setStyleSheet(server_ip_input_style[1])

        self.port_input = QLineEdit()
        self.port_input.setPlaceholderText("Port")
        self.port_input.setText("9500")
        self.port_input.setAccessibleName(port_input_style[0])
        self.port_input.setStyleSheet(port_input_style[1])

        self.server_status_label = QLabel()
        self.server_status_label.setText("Server status => not listening")
        self.server_status_label.setAccessibleName(server_status_label_styles[0])
        self.server_status_label.setStyleSheet(server_status_label_styles[1])

        self.btn_connect = QPushButton()
        self.btn_connect.setText("Connect")
        self.btn_connect.setAccessibleName(btn_connect_styles[0])
        self.btn_connect.setStyleSheet(btn_connect_styles[1])

        def on_clicked_connect():
            """ this function identify the connect btn event """

            result = self.socket_server.try_binding(
                server_ip=self.server_ip_input.text(),
                server_port=int(self.port_input.text())
            )  # return => (bool, status)
            self.server_status_label.setText("Server status => \n" + str(result[1]))

            if result[0] is True:
                # run server in background thread
                self.socket_server.start()  # when we use start method actually we call run

                _data = json_dumps({
                    "message": "Connect to server",
                    "to": "EDIT_LOGGER",
                    "type_log": "SERVER_LOG"
                })
                self.concentrate_subject.notify(message=_data, to=json_loads(_data)["to"])

                def send_data_concentrate(data):
                    self.concentrate_subject.notify(message=data, to=json_loads(data)["to"])

                self.socket_server.signal.connect(send_data_concentrate)
                
                self.server_ip_input.setReadOnly(True)
                self.port_input.setReadOnly(True)
                self.btn_connect.setEnabled(False)

        self.btn_connect.clicked.connect(on_clicked_connect)

        frame_layout.addWidget(self.server_ip_input)
        frame_layout.addWidget(self.port_input)
        frame_layout.addWidget(self.btn_connect)
        frame_layout.addWidget(self.server_status_label)

        main_frame.setLayout(frame_layout)

        return main_frame

    @property
    def signal(self):
        return self._signal
