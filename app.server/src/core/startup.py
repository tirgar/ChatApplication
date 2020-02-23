"""
    - created at Feb 23/2020 by Farzad-Tirgar
    -   This package start the main application and services
"""

from sys import (
    exit as sys_exit, argv as sys_argv
)
from PyQt5.QtWidgets import QApplication
from src.gui.windows.mainwindow import MainWindow


class StartUp:
    """ This is start up class for initilizing our services and other classes """

    def __init__(self):
        self.app =QApplication(sys_argv)
        self.main_window = MainWindow()

    def start(self):
        """ start main gui application and other services
            :return:
        """
        self.main_window.execute_app()
        sys_exit(self.app.exec_())