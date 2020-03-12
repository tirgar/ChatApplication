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
    
    def __init__(self, parent=None):
        super(UserListWidget, self).__init__(parent=parent)
        self.concentrate_subject = ConcentrateSubject()
        self.concentrate_subject.attach(self)
        self.users_list: List = list()

        self.setAccessibleName(main_widget_styles[0])
        self.setStyleSheet(main_widget_styles[1])
    
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setStretch(0, 0)

        self.setLayout(self.main_layout)


        self.__add_scroll_area__()

    @property
    def class_name(self):
        return "USER_LIST"
    
    def __add_scroll_area__(self):
        main_frame = QFrame()
        main_frame.setContentsMargins(10, 10, 10, 10)
        main_frame.setAccessibleName(main_scroll_holder_frame[0])
        main_frame.setStyleSheet(main_scroll_holder_frame[1])
        form_layout = QFormLayout()
        form_layout.setContentsMargins(0, 0, 0, 0)

        # for i in range(len(users)):
        for user in self.users_list:
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

            self.username_label = QLabel(user)
            self.username_label.setContentsMargins(0, 0, 0, 0)
            self.username_label.setAccessibleName(username_label_styles[0])
            self.username_label.setStyleSheet(username_label_styles[1])

            user_profile_layout.addWidget(self.username_icon)
            user_profile_layout.addWidget(self.username_label)

            sub_frame.setLayout(user_profile_layout)

            form_layout.addRow(sub_frame)

        main_frame.setLayout(form_layout)
        
        scroll = QScrollArea()
        scroll.setAccessibleName(scroll_layout_styles[0])
        scroll.setStyleSheet(scroll_layout_styles[1])
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidget(main_frame)
        scroll.setWidgetResizable(True)
        
        self.main_layout.addWidget(scroll)

    def notification(self, message):
        incoming_message = json_loads(message)
        self.users_list.append(incoming_message["message"]["option"]["username"])
        print(self.users_list)
        # return self.users_list


