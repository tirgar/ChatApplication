"""
    created at feb 28/2020 by Tirgar
    this class is for client main window of chat application
"""

from PyQt5.QtWidgets import (
    QMainWindow, QPushButton, QWidget, QGridLayout,
    QHBoxLayout, QVBoxLayout, QLabel, QListWidget,
    QListWidgetItem,
    QLineEdit, QTableWidgetItem, QHeaderView, QTextEdit
)
from PyQt5.QtGui import QIcon, QPixmap

from gui.styles.windows.main_window_style import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None, socket_server=None):
        super(MainWindow, self).__init__(parent=parent, )

        self.socket_server = socket_server

        self.setWindowTitle("main window")
        self.setContentsMargins(0, 0, 0, 0)

        self.setAccessibleName(main_window_styles[0])
        self.setStyleSheet(main_window_styles[1])

        self.__set_main_widget__()

    def __set_main_widget__(self):
        """ Add centeral widget for switching between widgets in main window
            :return:
        """
        main_widget = QWidget(self)
        main_widget.setContentsMargins(0, 0, 0, 0)

        # add widget to main widget
        self.main_widget_layout = QGridLayout(main_widget)
        self.main_widget_layout.setContentsMargins(0, 0, 0, 0)

        self.setCentralWidget(main_widget)
        self.__add_widget_list()
        self.__add_main_chat_layout__()

    def __add_widget_list(self):
        g_layout = QGridLayout()
        g_layout.setContentsMargins(0,0,0,0)

        self.setLayout(g_layout)
        self.list_widget = QListWidget()

        item_1 = QListWidgetItem("name_1")
        item_1.setIcon(QIcon("assets/tick.png"))

        item_2 = QListWidgetItem("name_2")
        item_2.setIcon(QIcon("assets/tick.png"))

        self.list_widget.addItem(item_1)
        self.list_widget.addItem(item_2)

        # self.list_widget.insertItem(0, "Red")
        # self.list_widget.insertItem(1, "Orange")
        # self.list_widget.insertItem(2, "Blue")
        # self.list_widget.insertItem(3, "White")
        # self.list_widget.insertItem(4, "Green")

        def clicked():
            _item = self.list_widget.currentItem()
            print(_item.text())

        self.list_widget.clicked.connect(clicked)

        g_layout.addWidget(self.list_widget)

        self.main_widget_layout.addLayout(g_layout, 0, 0)

    def __add_main_chat_layout__(self):
        self.v_main_chat_layout = QVBoxLayout()
        self.v_main_chat_layout.setContentsMargins(0, 0, 0, 0)
        self.v_main_chat_layout.stretch(0)

        self.__add_layout_title__()
        self.__add_layout_chat_input_btn__()

        self.main_widget_layout.addLayout(self.v_main_chat_layout, 0, 1)

    def __add_layout_title__(self):
        h_title_layout = QHBoxLayout()
        h_title_layout.setContentsMargins(0, 0, 0, 0)
        h_title_layout.stretch(0)

        self.label_icon = QLabel()
        pix = QPixmap("assets/tick.png")
        self.label_icon.setPixmap(pix)
        self.label_icon.setAccessibleName(label_icon_styles[0])
        self.label_icon.setStyleSheet(label_icon_styles[1])

        self.label_username = QLabel()
        self.label_username.setText("username")
        self.label_username.setAccessibleName(label_username_styles[0])
        self.label_username.setStyleSheet(label_username_styles[1])

        h_title_layout.addWidget(self.label_icon)
        h_title_layout.addWidget(self.label_username)

        self.v_main_chat_layout.addLayout(h_title_layout)

    def __add_layout_chat_input_btn__(self):
        v_layout = QVBoxLayout()
        v_layout.setContentsMargins(0, 0, 0, 0)
        v_layout.stretch(0)

        h_layout = QHBoxLayout()
        h_layout.setContentsMargins(0, 0, 0, 0)
        h_layout.stretch(0)

        self.msg_text_input = QTextEdit()
        self.msg_text_input.setPlaceholderText("Message text :: ")
        self.msg_text_input.setAccessibleName(msg_text_input_styles[0])
        self.msg_text_input.setStyleSheet(msg_text_input_styles[1])
        self.msg_text_input.setReadOnly(True)

        self.send_btn = QPushButton()
        self.send_btn.setText("Send")
        self.send_btn.setAccessibleName(btn_send_styles[0])
        self.send_btn.setStyleSheet(btn_send_styles[1])

        h_layout.addWidget(self.msg_text_input)
        h_layout.addWidget(self.send_btn)
        v_layout.addLayout(h_layout)

        self.v_main_chat_layout.addLayout(v_layout)

    def execute_app(self):
        self.show()