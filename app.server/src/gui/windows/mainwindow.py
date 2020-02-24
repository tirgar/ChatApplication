"""
    created by Farzad Tirgar at 23.feb
    this class is for main window of chat application
"""

from PyQt5.QtWidgets import (
    QMainWindow, QPushButton, QWidget, QGridLayout,
    QTableWidget, QApplication, QVBoxLayout, QLabel,
    QLineEdit, QTableWidgetItem
)

from gui.styles.windows.main_window_style import *
from gui.components.message_box import MessageBox


class MainWindow(QMainWindow):
    def __init__(self , parent=None, socket_server=None):
        super(MainWindow, self).__init__(parent=parent)

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
        self.server_ip_input.setAccessibleName(server_id_input_style[0])
        self.server_ip_input.setStyleSheet(server_id_input_style[1])

        self.port_input = QLineEdit()
        self.port_input.setPlaceholderText("Port")
        self.port_input.setAccessibleName(port_input_style[0])
        self.port_input.setStyleSheet(port_input_style[1])

        self.label = QLabel("Status")
        self.label.setAccessibleName(label_styles[0])
        self.label.setStyleSheet(label_styles[1])

        self.btn_connect = QPushButton()
        self.btn_connect.setText("Connect")
        self.btn_connect.setAccessibleName(btn_connect_styles[0])
        self.btn_connect.setStyleSheet(btn_connect_styles[1])

        def on_clicked_connect():
            # self.table_widget.setItem(0, 0, QTableWidgetItem(self.server_id_input.text()))
            # self.table_widget.setItem(0, 1, QTableWidgetItem("Name"))
            # self.table_widget.setItem(0, 2, QTableWidgetItem(self.port_input.text()))
            # self.table_widget.setItem(0, 3, QTableWidgetItem("System"))
            result = self.socket_server.try_binding(
                server_ip=self.server_ip_input.text(),
                server_port=int(self.port_input.text())
            )  # return => (bool, status)

            self.label.setText(str(result[1]))
            
            if result[0] == True:
                print("Connect Success for runing")
                # TODO: make new thread for socket service on background
                # self.socket_server.run(start=True)

        self.btn_connect.clicked.connect(on_clicked_connect)

        v_layout.addWidget(self.server_ip_input)
        v_layout.addWidget(self.port_input)
        v_layout.addWidget(self.label)
        v_layout.addWidget(self.btn_connect)

        self.main_widget_layout.addLayout(v_layout, 0, 0)

    def __add_table__(self):
        """
        this function add layout with table widgets to grid_layout
        :return:
        """
        v_layout = QVBoxLayout()
        v_layout.setContentsMargins(0, 0, 0, 0)

        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(1)
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["IP Client", "Name", "Port", "System"])

        v_layout.addWidget(self.table_widget)
        self.main_widget_layout.addLayout(v_layout, 0, 1)

    def execute_app(self):
        self.show()