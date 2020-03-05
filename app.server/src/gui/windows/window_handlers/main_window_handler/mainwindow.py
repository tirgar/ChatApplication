"""
    created by Farzad Tirgar at 23.feb
    this class is for main window of chat application
"""

from PyQt5.QtWidgets import (
    QMainWindow, QPushButton, QWidget, QGridLayout,
    QTableWidget, QVBoxLayout, QLabel,
    QLineEdit, QTableWidgetItem, QHeaderView, QTextEdit
)

from gui.styles.windows.main_window_style import *
from gui.components.message_box import MessageBox
from interfaces.observer_pattern.observer import Observer
from core.inner_concentrate.concentrate import ConcentrateSubject

from datetime import datetime


class MainWindow(Observer, QMainWindow):
    def __init__(self, parent=None, socket_server=None):
        super(MainWindow, self).__init__(parent=parent)
        self.concentrate_subject = ConcentrateSubject()
        self.concentrate_subject.attach(self)

        self.socket_server = socket_server

        self.setWindowTitle("main window")
        self.setContentsMargins(0, 0, 0, 0)
        
        self.setAccessibleName(main_window_styles[0])
        self.setStyleSheet(main_window_styles[1])

        self.__set_main_widget__()
        
    @property
    def class_name(self):
        return "MAIN_WINDOW"

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
        self.__add__widget__()
        self.__add_table__()

    def __add__widget__(self):
        """
        this function add layout with buttons widgets to grid_layout
        :return:
        """
        v_layout = QVBoxLayout()
        v_layout.setContentsMargins(0, 0, 0, 0)
        v_layout.addStretch(0)

        self.server_ip_input = QLineEdit()
        self.server_ip_input.setPlaceholderText("Server IP")
        self.server_ip_input.setText("127.0.0.1")
        self.server_ip_input.setAccessibleName(server_ip_input_style[0])
        self.server_ip_input.setStyleSheet(server_ip_input_style[1])

        self.port_input = QLineEdit()
        self.port_input.setPlaceholderText("Port")
        self.port_input.setText("9500")
        self.port_input.setAccessibleName(port_input_style[0])
        self.port_input.setStyleSheet(port_input_style[1])

        self.server_status_label = QLabel()
        self.server_status_label.setText("Server status => not listening")
        self.server_status_label.setAccessibleName(server_status_label_styles[0])
        self.server_status_label.setStyleSheet(server_status_label_styles[1])

        self.btn_connect = QPushButton()
        self.btn_connect.setText("Connect")
        self.btn_connect.setAccessibleName(btn_connect_styles[0])
        self.btn_connect.setStyleSheet(btn_connect_styles[1])

        def on_clicked_connect():
            
            result = self.socket_server.try_binding(
                server_ip=self.server_ip_input.text(),
                server_port=int(self.port_input.text())
            )  # return => (bool, status)
            self.server_status_label.setText("Server status => \n" + str(result[1]))

            if result[0] is True:
                # run server in background thread
                self.socket_server.start()  # when we use start method actually we call run

                def send_data_concentrate(data):
                    self.concentrate_subject.notify(message=data, to="MAIN_WINDOW")

                self.socket_server.signal.connect(send_data_concentrate)
                
                print("Connect Success for running")

        self.btn_connect.clicked.connect(on_clicked_connect)

        self.q_text_edit = QTextEdit()
        self.q_text_edit.setAccessibleName(q_text_edit_styles[0])
        self.q_text_edit.setReadOnly(True)
        self.q_text_edit.setStyleSheet(q_text_edit_styles[1])
        
        v_layout.addWidget(self.server_ip_input)
        v_layout.addWidget(self.port_input)
        v_layout.addWidget(self.btn_connect)
        v_layout.addWidget(self.server_status_label)
        v_layout.addWidget(self.q_text_edit)

        self.main_widget_layout.addLayout(v_layout, 0, 0)

    def __add_table__(self):
        """
        this function add layout with table widgets to grid_layout
        :return:
        """
        v_layout = QVBoxLayout()
        v_layout.setContentsMargins(0, 0, 0, 0)

        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(0)
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["IP Client", "Name", "Port", "System"])
        
        header = self.table_widget.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Stretch)

        v_layout.addWidget(self.table_widget)
        self.main_widget_layout.addLayout(v_layout, 0, 1)

    def notification(self, message):
        """ Receive update from subject
            :params message: incoming message
        """
        from json import loads as json_loads
        
        incoming_message = json_loads(message)
        
        if incoming_message["to"] == "editlog":
            
            last_text = self.q_text_edit.toPlainText()
            self.q_text_edit.setText(
                last_text + "\n" + str(datetime.now()).split(".")[0] 
                + " " + str(incoming_message["client_address"])
                + ": " + incoming_message["message"]
            )
        elif incoming_message["to"] == "table_widget":
            print(message)

    def execute_app(self):
        self.show()
