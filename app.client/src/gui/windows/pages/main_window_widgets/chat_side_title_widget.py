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
        self.setAccessibleName(chat_title_widget_styles[0])
        self.setStyleSheet(chat_title_widget_styles[1])

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(self.__add_widget__())
        self.setLayout(main_layout)

    def __add_widget__(self):
        main_frame = QFrame()
        main_frame.setContentsMargins(0, 0, 0, 0)
        main_frame.setAccessibleName(main_frame_styles[0])
        main_frame.setStyleSheet(main_frame_styles[1])
        
        frame_layout = QHBoxLayout()
        frame_layout.setContentsMargins(0, 0, 0, 0)
        frame_layout.setStretch(0, 0)
        frame_layout.setSpacing(0)
        
        user_icon = QPushButton()
        user_icon.setAccessibleName(user_icon_styles[0])
        user_icon.setStyleSheet(user_icon_styles[1])
        icon = QIcon('./assets/user.png')
        user_icon.setIcon(icon)
        user_icon.setIconSize(QSize(60, 60))
        user_label = QLabel('username')
        user_label.setFrameShape(QFrame.NoFrame)
        user_label.setAccessibleName(user_label_styles[0])
        user_label.setStyleSheet(user_label_styles[1])
        
        frame_layout.addWidget(user_icon)
        frame_layout.addWidget(user_label)        

        main_frame.setLayout(frame_layout)
        
        return main_frame
