"""
    - created at march 05/2020 by Tirgar
    -- this package is chat text input widget
"""

from PyQt5.QtWidgets import (
    QWidget,QFrame, QLabel, QPushButton, QTextEdit, QHBoxLayout
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon

from gui.styles.pages.main_window_widgets.chat_text_input_widget_styles import *


class ChatTextInput(QWidget):

    def __init__(self, parent=None):
        super(ChatTextInput, self).__init__(parent=parent)
        self.setAccessibleName(chat_text_input_widget_styles[0])
        self.setStyleSheet(chat_text_input_widget_styles[1])

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

        text_input = QTextEdit()
        text_input.setPlaceholderText("Type something...")
        # text_input.setAlignment(Qt.AlignCenter)
        text_input.setAccessibleName(input_text_styles[0])
        text_input.setStyleSheet(input_text_styles[1])

        attach_icon = QPushButton()
        attach_icon.setAccessibleName(attach_icon_styles[0])
        attach_icon.setStyleSheet(attach_icon_styles[1])
        icon_attach = QIcon('./assets/clip.png')
        attach_icon.setIcon(icon_attach)
        attach_icon.setIconSize(QSize(25, 25))

        sticker_icon = QPushButton()
        sticker_icon.setAccessibleName(sticker_icon_styles[0])
        sticker_icon.setStyleSheet(sticker_icon_styles[1])
        icon_sticker = QIcon('./assets/smile.png')
        sticker_icon.setIcon(icon_sticker)
        sticker_icon.setIconSize(QSize(25, 25))

        send_icon = QPushButton()
        send_icon.setAccessibleName(send_icon_styles[0])
        send_icon.setStyleSheet(send_icon_styles[1])
        icon_send = QIcon('./assets/paper-plane.png')
        send_icon.setIcon(icon_send)
        send_icon.setIconSize(QSize(25, 25))

        frame_layout.addWidget(text_input)
        frame_layout.addWidget(attach_icon)
        frame_layout.addWidget(sticker_icon)
        frame_layout.addWidget(send_icon)
        main_frame.setLayout(frame_layout)

        return main_frame
