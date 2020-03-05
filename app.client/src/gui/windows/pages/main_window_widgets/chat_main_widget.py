"""
    - created at march 03/2020 by Tirgar

    -- this package is chat side  widget
"""

from PyQt5.QtWidgets import QVBoxLayout, QWidget, QPushButton

from gui.styles.pages.main_window_widgets.chat_main_widget_styles import *
from .chat_side_title_widget import ChatTitle
from .chat_display_widget import ChatDisplayWidget
from .chat_text_input_widget import ChatTextInput


class ChatMainWidget(QWidget):
    def __init__(self, parent=None):
        super(ChatMainWidget, self).__init__(parent=parent)

        self.setAccessibleName(chat_main_widget_styles[0])
        self.setStyleSheet(chat_main_widget_styles[1])

        self.chat_main_layout = QVBoxLayout()
        self.chat_main_layout.setContentsMargins(10, 0, 20, 0)
        self.chat_main_layout.setStretch(0, 0)
        self.chat_main_layout.setSpacing(0)

        self.setLayout(self.chat_main_layout)
        self.__add_btn__()

    def __add_btn__(self):
        title_widget = ChatTitle(parent=self)
        chat_display_widget = ChatDisplayWidget(parent=self)
        chat_text_input_widget = ChatTextInput(parent=self)

        self.chat_main_layout.addWidget(title_widget)
        self.chat_main_layout.addWidget(chat_display_widget)
        self.chat_main_layout.addWidget(chat_text_input_widget)
