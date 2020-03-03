"""
    - created at march 02/2020 by mjghasempour (topcoder-mc)
    
    -- this package is user list side bar widget
"""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QScrollArea, QGridLayout,
    QFrame, QLabel, QPushButton, QFormLayout, QHBoxLayout
)
from PyQt5.QtCore import Qt

from gui.styles.pages.main_window_widgets.users_list_widgets_styles import *


class UserListWidget(QWidget):
    
    def __init__(self, parent=None):
        super(UserListWidget, self).__init__(parent=parent)

        self.setAccessibleName(main_widget_styles[0])
        self.setStyleSheet(main_widget_styles[1])
    
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self.main_layout)
        
        self.__add_scroll_area__()
    
    def __add_scroll_area__(self):
        main_frame = QFrame()
        form_layout = QFormLayout()

        for i in  range(100):
            sub_frame = QFrame()
            sub_frame.setContentsMargins(0, 0, 0, 0)
            
            user_profile_layout = QHBoxLayout()
            user_profile_layout.setContentsMargins(0, 0, 0, 0)
            user_profile_layout.setStretch(0, 0)

            username_label = QLabel("User" + str(i))
            username_icon = QPushButton("1")
            
            user_profile_layout.addWidget(username_label)
            user_profile_layout.addWidget(username_icon)

            sub_frame.setLayout(user_profile_layout)

            form_layout.addRow(sub_frame)    

        main_frame.setLayout(form_layout)
        
        scroll = QScrollArea()
        scroll.setAccessibleName(scroll_layout_styles[0])
        scroll.setStyleSheet(scroll_layout_styles[1])
        scroll.setWidget(main_frame)
        scroll.setWidgetResizable(True)
        
        self.main_layout.addWidget(scroll)