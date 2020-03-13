"""
    - created at march 02/2020 by mjghasempour (topcoder-mc)
    
    -- this package is user list side bar widget
"""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QScrollArea,
    QFrame, QLabel, QPushButton, QFormLayout, QHBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from typing import List

from gui.styles.pages.main_window_widgets.users_list_widgets_styles import *
from interfaces.observer_pattern.observer import Observer
from core.inner_concentrate.concentrate import ConcentrateSubject

from json import (dumps as json_dumps, loads as json_loads)


class UserListWidget(Observer, QWidget):
    
    def __init__(self):
        super(UserListWidget, self).__init__()
        self.concentrate_subject = ConcentrateSubject()
        self.concentrate_subject.attach(self)

        self.setAccessibleName(main_widget_styles[0])
        self.setStyleSheet(main_widget_styles[1])
        self.__init_ui__()

    def __init_ui__(self):
        self.scroll_layout = QFormLayout()
        self.scroll_layout.setContentsMargins(10, 10, 10, 10)
        self.scroll_layout.setSpacing(0)

        self.scroll_widget = QWidget()
        self.scroll_widget.setAccessibleName(main_scroll_holder_frame[0])
        self.scroll_widget.setStyleSheet(main_scroll_holder_frame[1])
        self.scroll_widget.setLayout(self.scroll_layout)

        self.scroll_area = QScrollArea()
        self.scroll_area.setAccessibleName(scroll_layout_styles[0])
        self.scroll_area.setStyleSheet(scroll_layout_styles[1])
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.scroll_widget)

    def get_scroll_widget(self):
        return self.scroll_area

    @property
    def class_name(self):
        return "USER_LIST"
    
    def __add_scroll_area__(self, username):
        sub_frame = QFrame()
        sub_frame.setContentsMargins(0, 0, 0, 0)

        sub_frame.setAccessibleName(sub_qframe_styles[0])
        sub_frame.setStyleSheet(sub_qframe_styles[1])

        user_profile_layout = QHBoxLayout()
        user_profile_layout.setContentsMargins(0, 0, 0, 0)

        self.username_icon = QPushButton()
        self.username_icon.setContentsMargins(0, 0, 0, 0)
        self.username_icon.setAccessibleName(username_icon_styles[0])
        self.username_icon.setStyleSheet(username_icon_styles[1])
        icon = QIcon('./assets/user.png')
        self.username_icon.setIcon(icon)
        self.username_icon.setIconSize(QSize(40, 40))

        self.username_label = QLabel(username)
        self.username_label.setContentsMargins(0, 0, 0, 0)
        self.username_label.setAccessibleName(username_label_styles[0])
        self.username_label.setStyleSheet(username_label_styles[1])

        user_profile_layout.addWidget(self.username_icon)
        user_profile_layout.addWidget(self.username_label)

        sub_frame.setLayout(user_profile_layout)

        self.scroll_layout.addRow(sub_frame)

    def notification(self, message):
        for item in message["message"]["option"]["online_users"]:
            self.__add_scroll_area__(item["username"])


