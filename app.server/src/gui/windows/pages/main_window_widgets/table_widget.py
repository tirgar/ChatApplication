"""
    - created at march 06/2020 by Tirgar
    -- this package is server table widget
"""

from PyQt5.QtWidgets import (
    QVBoxLayout, QWidget, QTableWidget, QHeaderView, QFrame, QTableWidgetItem
    )
from PyQt5.QtCore import Qt

from gui.styles.pages.main_window_widgets.table_widget_styles import *
from interfaces.observer_pattern.observer import Observer
from core.inner_concentrate.concentrate import ConcentrateSubject


class TableWidget(Observer, QWidget):
    """ this class make the server table widget gui of server app """
    
    client_sets: set = set()

    def __init__(self, parent=None, socket_server=None):
        super(TableWidget, self).__init__(parent=parent)
        self.concentrate_subject = ConcentrateSubject()
        self.concentrate_subject.attach(self)

        self.socket_server = socket_server

        self.setAccessibleName(main_table_widget_styles[0])
        self.setStyleSheet(main_table_widget_styles[1])

        table_main_layout = QVBoxLayout()
        table_main_layout.setContentsMargins(10, 0, 10, 0)
        table_main_layout.setStretch(0, 0)
        table_main_layout.setSpacing(0)

        table_main_layout.addWidget(self.__add_widget__())

        self.setLayout(table_main_layout)

    @property
    def class_name(self):
        """ this function return a class name to access in codes """
        return "TABLE_WIDGET"

    def __add_widget__(self):
        """ this function return a q-frame to use in main layout """

        main_frame = QFrame()
        main_frame.setContentsMargins(0, 10, 0, 0)
        main_frame.setAccessibleName(main_frame_styles[0])
        main_frame.setStyleSheet(main_frame_styles[1])

        frame_layout = QVBoxLayout()
        frame_layout.setContentsMargins(0, 0, 0, 0)
        frame_layout.setStretch(0, 0)
        frame_layout.setSpacing(0)

        self.table_widget = QTableWidget()
        self.table_widget.setAccessibleName(table_widget_styles[0])
        self.table_widget.setStyleSheet(table_widget_styles[1])
        self.table_widget.verticalHeader().hide()
        self.table_widget.setRowCount(0)
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["IP Client", "Name", "Port", "System"])

        header = self.table_widget.horizontalHeader()
        header.setAccessibleName(table_header_styles[0])
        header.setStyleSheet(table_header_styles[1])
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Stretch)

        frame_layout.addWidget(self.table_widget)
        main_frame.setLayout(frame_layout)

        return main_frame

    def notification(self, message):
        """ Receive update from subject
            :params message: incoming message
        """
        from json import loads as json_loads

        incoming_message = json_loads(message)

        if incoming_message["type"] == "[ADD]":
            self.row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(self.row_position)

            self.table_widget.setItem(self.row_position, 0, QTableWidgetItem(incoming_message["message"]["ip"]))
            self.table_widget.setItem(self.row_position, 1, QTableWidgetItem(incoming_message["message"]["name"]))
            self.table_widget.setItem(self.row_position, 2, QTableWidgetItem(incoming_message["message"]["port"]))
            self.table_widget.setItem(self.row_position, 3, QTableWidgetItem(incoming_message["message"]["system"]))
            
        elif incoming_message["type"] == "[REMOVE]":
            model = self.table_widget.model()
            for row in range(model.rowCount()):
                ip_column = model.index(row, 0)
                ip_column_text = str(model.data(ip_column))
                port_column = model.index(row, 2)
                port_column_text = str(model.data(port_column))

                if incoming_message["message"][0] + ":" + str(incoming_message["message"][1]) ==\
                        str(ip_column_text) + ":" + str(port_column_text):

                    self.table_widget.removeRow(row)
                    break
