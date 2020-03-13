"""
    - created at march 08/2020 by Tirgar
    -   This package create signin page
"""

from PyQt5.QtWidgets import (
    QWidget, QLineEdit, QVBoxLayout, QPushButton,
    QFrame
)
from PyQt5.QtCore import Qt

from gui.styles.pages.auth.signin_styles import *
from modules.data.data_context import User
from gui.components.message_box import MessageBox
from interfaces.observer_pattern.observer import Observer
from core.inner_concentrate.concentrate import ConcentrateSubject

from json import (dumps as json_dumps, loads as json_loads)
from platform import uname


class SignIn(Observer, QWidget):

    def __init__(self, parent=None, socket_server=None):
        super(SignIn, self).__init__(parent=parent)
        self.concentrate_subject = ConcentrateSubject()
        self.concentrate_subject.attach(self)
        self.socket_server = socket_server

        self.check_user_pass()

        self.setContentsMargins(0, 0, 0, 0)

        self.parent = parent

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setStretch(0, 0)
        self.main_layout.setAlignment(Qt.AlignHCenter)

        self.__init_ui__()

        self.main_layout.addWidget(self.main_frame)
        self.setLayout(self.main_layout)

    def check_user_pass(self):
        last_user = User.select()
        if len(last_user) > 0:
            last_user = last_user[len(last_user) - 1]
            if last_user is not None:
                data = json_dumps({
                    "message": {
                        "username": last_user.username,
                        "password": last_user.password
                    },
                    "command": "[LOGIN]",
                    "session": None,
                    "option": None,
                    "route": {
                        "group": "",
                        "to": "server"
                    },
                })

                self.socket_server.get_socket.sendall(data.encode("utf-8"))

    @property
    def class_name(self):
        return "SIGN_IN"

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
        self._add_forgot_password_()
        self._add_btn_login_()
        self._add_btn_create_account_()

        self.main_frame.setLayout(self.frame_layout)

    def _add_textboxs_(self):

        self.username_edit_text = QLineEdit()
        self.username_edit_text.setPlaceholderText("Enter UserName")
        self.username_edit_text.setAccessibleName(q_edit_text_style[0])
        self.username_edit_text.setStyleSheet(q_edit_text_style[1])

        self.frame_layout.addWidget(self.username_edit_text)

        self.password_edit_text = QLineEdit()
        self.password_edit_text.setPlaceholderText("Enter Password")
        self.password_edit_text.setAccessibleName(q_edit_text_style[0])
        self.password_edit_text.setStyleSheet(q_edit_text_style[1])

        self.frame_layout.addWidget(self.password_edit_text)

    def _add_forgot_password_(self):
        btn_forgot_password = QPushButton("Forgot password?")
        btn_forgot_password.setAccessibleName(btn_forgot_password_style[0])
        btn_forgot_password.setStyleSheet(btn_forgot_password_style[1])

        # self.main_layout.addWidget(btn_forgot_password)
        self.frame_layout.addWidget(btn_forgot_password)

    def _add_btn_login_(self):
        btn_login = QPushButton("SingIn")
        btn_login.setAccessibleName(btn_login_style[0])
        btn_login.setStyleSheet(btn_login_style[1])

        def btn_login_clicked():
            username: str = self.username_edit_text.text()
            password: str = self.password_edit_text.text()

            try:
                if username != "" and password != "":
                    user = User.select().where(
                        (User.username == username) & (User.password == password)
                    )
                    if len(user) > 0:
                        data = json_dumps({
                            "message": "",
                            "command": "[LOGIN_INF]",
                            "session": "",
                            "option": {
                                "sys_info": str(uname().system),
                                "username": username
                            },
                            "route": {
                                "group": "",
                                "to": "server"
                            },
                        })

                        self.socket_server.get_socket.sendall(data.encode("utf-8"))

                        from gui.windows.window_handler.main_window_handler.mainwindow import MainWindow
                        main_window = MainWindow(self.parent, self.socket_server)
                        self.parent.hide()
                        main_window.execute_app()
                    else:
                        MessageBox(
                            title="Not Success",
                            message="UnAuthorized"
                        ).show()
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

        btn_login.clicked.connect(btn_login_clicked)

        self.frame_layout.addWidget(btn_login)

    def _add_btn_create_account_(self):
        btn_create_account = QPushButton("Create new account ?")
        btn_create_account.setAccessibleName(btn_create_account_style[0])
        btn_create_account.setStyleSheet(btn_create_account_style[1])
        btn_create_account.setContentsMargins(0, 0, 0, 0)

        def clicked_create_account():
            self.set_visibility(False)
            self.signup_page.set_visibility(True)

        btn_create_account.clicked.connect(clicked_create_account)

        # self.main_layout.addWidget(btn_create_account)
        self.frame_layout.addWidget(btn_create_account)

    def set_visibility(self, visible: bool):
        if visible:
            self.show()
        else:
            self.hide()

    def set_sign_up_page(self, signup: object):
        self.signup_page = signup

    def notification(self, message):
        incoming_message = json_loads(message)
        last_user = User.select()
        last_user = last_user[len(last_user) - 1]
        if incoming_message["message"]["code"] == 200:
            data = json_dumps({
                "message": "",
                "command": "[LOGIN_INF]",
                "session": "",
                "option": {
                    "sys_info": str(uname().system),
                    "username": last_user.username
                },
                "route": {
                    "group": "",
                    "to": "server"
                },
            })
            self.socket_server.get_socket.sendall(data.encode("utf-8"))

            self.concentrate_subject.notify(incoming_message, to="USER_LIST")

            from gui.windows.window_handler.main_window_handler.mainwindow import MainWindow
            main_window = MainWindow(self.parent, socket_server=self.socket_server)
            self.parent.hide()
            main_window.execute_app()
        else:
            return

    @property
    def signal(self):
        return self._signal
