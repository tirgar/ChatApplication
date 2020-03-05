"""
    - created at march 05/2020 by Tirgar
    -- this package is chat display widget
"""

from PyQt5.QtWidgets import (
    QWidget,QFrame, QHBoxLayout
)


from gui.styles.pages.main_window_widgets.chat_display_widget_styles import *


class ChatDisplayWidget(QWidget):

    def __init__(self, parent=None):
        super(ChatDisplayWidget, self).__init__(parent=parent)
        self.setAccessibleName(chat_display_widget_styles[0])
        self.setStyleSheet(chat_display_widget_styles[1])

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

        main_frame.setLayout(frame_layout)

        return main_frame
