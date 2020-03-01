"""
    created at feb 28/2020 by Tirgar
    this class is for contact list of chat application
"""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QScrollArea, QFrame,
)
from PyQt5.QtCore import Qt

from gui.styles.windows.contact_list_widget import *


class ContactList(QWidget):
    def __init__(self, parent=None):
        super(ContactList, self).__init__(parent=parent)
        self.setContentsMargins(0, 0, 0, 0)
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addStretch(0)
        self.setAccessibleName(contact_list_styles[0])
        self.setStyleSheet(contact_list_styles[1])

        self.__widget_init__()

    def __widget_init__(self):
        v_layout = QVBoxLayout()
        v_layout.setContentsMargins(0, 0, 0, 0)

        for i in range(10):
            frame = QFrame()
            frame.setFrameShape(QFrame.StyledPanel)
            frame.setLineWidth(0.5)

            v_layout.addWidget(frame)

        scroll_layout = QScrollArea()
        scroll_layout.setAccessibleName(scroll_layout_styles[0])
        scroll_layout.setStyleSheet(scroll_layout_styles[1])
        scroll_layout.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll_layout.setLayout(v_layout)
        scroll_layout.setWidgetResizable(True)
        self.main_layout.addWidget(scroll_layout)

        self.setLayout(self.main_layout)
