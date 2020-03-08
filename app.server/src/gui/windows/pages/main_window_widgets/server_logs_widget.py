"""
    - created at march 06/2020 by Tirgar
    -- this package is server logs widget
"""

from PyQt5.QtWidgets import (
    QWidget, QTextEdit, QFrame, QHBoxLayout
)
from datetime import datetime

from gui.styles.pages.main_window_widgets.server_log_widget_styles import *
from interfaces.observer_pattern.observer import Observer
from core.inner_concentrate.concentrate import ConcentrateSubject


class ServerLogs(Observer, QWidget):
    """ this class make the server logs widget gui of server app """

    def __init__(self, parent=None):
        super(ServerLogs, self).__init__(parent=parent)
        self.concentrate_subject = ConcentrateSubject()
        self.concentrate_subject.attach(self)

        self.setAccessibleName(server_log_widget_styles[0])
        self.setStyleSheet(server_log_widget_styles[1])

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(self.__add_widget__())
        self.setLayout(main_layout)

    @property
    def class_name(self):
        """ this function return a class name to access in codes """

        return "EDIT_LOGGER"

    def __add_widget__(self):
        """ this function return a q-frame to use in main layout """

        main_frame = QFrame()
        main_frame.setContentsMargins(0, 0, 0, 0)
        main_frame.setAccessibleName(main_frame_styles[0])
        main_frame.setStyleSheet(main_frame_styles[1])

        frame_layout = QHBoxLayout()
        frame_layout.setContentsMargins(0, 0, 0, 0)
        frame_layout.setStretch(0, 0)
        frame_layout.setSpacing(0)

        self.q_text_edit = QTextEdit()
        self.q_text_edit.setAccessibleName(q_text_edit_styles[0])
        self.q_text_edit.setReadOnly(True)
        self.q_text_edit.setStyleSheet(q_text_edit_styles[1])

        frame_layout.addWidget(self.q_text_edit)

        main_frame.setLayout(frame_layout)

        return main_frame

    def notification(self, message):
        """ Receive update from subject
            :params message: incoming message
        """
        from json import loads as json_loads

        incoming_message = json_loads(message)

        if incoming_message["type_log"] == "CLIENT_LOG":

            last_text = self.q_text_edit.toPlainText()
            self.q_text_edit.setText(
                last_text + "\n" + str(datetime.now()).split(".")[0]
                + " " + str(incoming_message["client_address"])
                + ": " + incoming_message["message"]
            )
        elif incoming_message["type_log"] == "SERVER_LOG":
            last_text = self.q_text_edit.toPlainText()
            self.q_text_edit.setText(
                last_text + "\n" + str(datetime.now()).split(".")[0]
                + " " + incoming_message["message"]
            )
            
    @property
    def signal(self):
        return self._signal
