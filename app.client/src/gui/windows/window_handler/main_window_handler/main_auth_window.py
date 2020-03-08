"""
    - created at march 08/2020 by Tirgar
    -   This package create main auth window for signin and signup
"""

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QGridLayout
)
from interfaces.observer_pattern.observer import Observer
from core.inner_concentrate.concentrate import ConcentrateSubject

from gui.styles.windows.main_auth_window_styles import *


class MainAuthWindow(Observer, QMainWindow):
    """ Main window for sign-in and sign-up pages and application
    """

    def __init__(self, parent=None, socket_server=None):
        super(MainAuthWindow, self).__init__(parent=parent)
        self.concentrate_subject = ConcentrateSubject()
        self.concentrate_subject.attach(self)
        self.socket_server = socket_server

        self.setWindowTitle("Auth page")
        self.setMinimumSize(800, 600)
        self.setMaximumSize(800, 600)

        self.setContentsMargins(0, 0, 0, 0)

        self.setAccessibleName(main_window_style[0])
        self.setStyleSheet(main_window_style[1])

        self.__set_centeral_widget_config__()

    @property
    def class_name(self):
        return "MAIN_AUTH_WINDOW"

    def __set_centeral_widget_config__(self):
        """ Add centeral widget for switching between widgets in main window
        :return:
        """
        main_widget = QWidget(self)
        main_widget.setContentsMargins(0, 0, 0, 0)

        # add widget to main widget
        main_widget_layout = QGridLayout(main_widget)
        main_widget_layout.setContentsMargins(0, 0, 0, 0)

        # add another widget
        from gui.windows.pages.auth.signin import SignIn
        from gui.windows.pages.auth.signup import SignUp

        signin_page = SignIn(parent=self, socket_server=self.socket_server)
        signin_page.set_visibility(True)
        signup_page = SignUp(parent=self, socket_server=self.socket_server)
        signup_page.set_visibility(False)

        signin_page.set_sign_up_page(signup_page)
        signup_page.set_sign_in_page(signin_page)

        main_widget_layout.addWidget(signin_page)
        main_widget_layout.addWidget(signup_page)

        self.setCentralWidget(main_widget)

    def execute_app(self):
        """ show main window in application layout
        :return:
        """
        self.show()