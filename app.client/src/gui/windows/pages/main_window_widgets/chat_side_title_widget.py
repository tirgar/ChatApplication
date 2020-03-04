"""
    - created at march 03/2020 by Tirgar

    -- this package is chat side title widget
"""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QScrollArea,
    QFrame, QLabel, QPushButton, QFormLayout, QHBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

from gui.styles.pages.main_window_widgets.chat_title_widgets_styles import *


class ChatTitle(QWidget):

    def __init__(self, parent=None):
        super(ChatTitle, self).__init__(parent=parent)

        # self.setAccessibleName(chat_title_widget_styles[0])
        # self.setStyleSheet(chat_title_widget_styles[1])

        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self.main_layout)

        self.__add_widget__()

    def __add_widget__(self):
        user_icon = QPushButton()
        user_icon.setAccessibleName(user_icon_styles[0])
        user_icon.setStyleSheet(user_icon_styles[1])
        icon = QIcon(
            '/home/farzad/Workspace/Python_practice/session_17/ChatApplication/app.client/src/assets/user.png'
        )
        user_icon.setIcon(icon)
        user_icon.setIconSize(QSize(60, 60))
        user_label = QLabel('username')
        user_label.setFrameShape(QFrame.NoFrame)
        user_label.setAccessibleName(user_label_styles[0])
        user_label.setStyleSheet(user_label_styles[1])

        self.main_layout.addWidget(user_icon)
        self.main_layout.addWidget(user_label)