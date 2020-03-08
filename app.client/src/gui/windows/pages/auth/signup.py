"""
    - created at march 08/2020 by Tirgar
    -   This package create signup page
"""

from PyQt5.QtWidgets import (
    QWidget, QLineEdit, QVBoxLayout, QPushButton,
    QFrame
)
from PyQt5.QtCore import Qt

from gui.styles.pages.auth.signup_styles import *
from gui.components.message_box import MessageBox
from interfaces.observer_pattern.observer import Observer
from core.inner_concentrate.concentrate import ConcentrateSubject


class SignUp(Observer, QWidget):

    def __init__(self, parent=None, socket_server=None):
        super(SignUp, self).__init__(parent=parent)
        self.concentrate_subject = ConcentrateSubject()
        self.concentrate_subject.attach(self)
        self.socket_server = socket_server

        self.parent = parent

        self.setContentsMargins(0, 0, 0, 0)

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setStretch(0, 0)
        self.main_layout.setAlignment(Qt.AlignHCenter)

        self.__init_ui__()

        self.main_layout.addWidget(self.main_frame)
        self.setLayout(self.main_layout)

    @property
    def class_name(self):
        return "SIGN_UP"

    def __init_ui__(self):
        self.main_frame = QFrame()
        self.main_frame.setContentsMargins(0, 0, 0, 0)
        self.main_frame.setAccessibleName(main_frame_styles[0])
        self.main_frame.setStyleSheet(main_frame_styles[1])

        self.frame_layout = QVBoxLayout()
        self.frame_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_layout.setStretch(0, 0)
        self.frame_layout.setSpacing(0)

        self._add_textboxs_()
        self._add_btn_signup_()
        self._add_btn_register_account_()

        self.main_frame.setLayout(self.frame_layout)

    def _add_textboxs_(self):
        self.username_edit_text = QLineEdit()
        self.username_edit_text.setPlaceholderText("UserName")
        self.username_edit_text.setAccessibleName(q_edit_text_style[0])
        self.username_edit_text.setStyleSheet(q_edit_text_style[1])

        self.frame_layout.addWidget(self.username_edit_text)

        self.password_edit_text = QLineEdit()
        self.password_edit_text.setPlaceholderText("Password")
        self.password_edit_text.setAccessibleName(q_edit_text_style[0])
        self.password_edit_text.setStyleSheet(q_edit_text_style[1])

        self.frame_layout.addWidget(self.password_edit_text)

    def _add_btn_signup_(self):
        btn_signup = QPushButton("SignUp")
        btn_signup.setAccessibleName(btn_signup_style[0])
        btn_signup.setStyleSheet(btn_signup_style[1])

        def btn_register_clicked():
            username: str = self.username_edit_text.text()
            password: str = self.password_edit_text.text()

            from modules.data.data_context import User
            from datetime import datetime

            try:
                if username != "" and password != "":                    
                    from json import dumps as json_dumps
                    
                    self.socket_server.get_socket.sendall(json_dumps({
                        "message": {
                            "USERNAME": username,
                            "PASSWORD": password
                        },
                        "params": {
                            "USERNAME": username
                        },
                        "command": "[REGISTER]",
                        "session": None,
                        "route": {
                            "group": "",
                            "to": "server"
                        },
                        "option": None
                    }).encode("utf-8"))
                    
                    # TODO: get response from server then do your reaction
                    
                    User.create(
                        username=username,
                        password=password
                    )

                    from gui.windows.window_handler.main_window_handler.mainwindow import MainWindow
                    main_window = MainWindow(self.parent, self.socket_server)
                    self.parent.hide()
                    main_window.execute_app()

                else:
                    MessageBox(
                        title="Error",
                        message=str("Please fill both of password and username")
                    ).show()
            except Exception as error:
                MessageBox(
                    title="Error",
                    message=str(error)
                ).show()

        btn_signup.clicked.connect(btn_register_clicked)

        self.frame_layout.addWidget(btn_signup)

    def _add_btn_register_account_(self):
        btn_goto_register_page = QPushButton("SignIn?")
        btn_goto_register_page.setAccessibleName(btn_goto_register_page_style[0])
        btn_goto_register_page.setStyleSheet(btn_goto_register_page_style[1])
        btn_goto_register_page.setContentsMargins(0, 0, 0, 0)

        def change_page_to_register():
            self.set_visibility(False)
            self.signin_page.set_visibility(True)

        btn_goto_register_page.clicked.connect(change_page_to_register)

        self.frame_layout.addWidget(btn_goto_register_page)

    def set_visibility(self, visible: bool):
        if visible:
            self.show()
        else:
            self.hide()

    def set_sign_in_page(self, signin: object):
        self.signin_page = signin
