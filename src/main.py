from time import sleep

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QThread, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication

from game import Game, GameStatus, WaitingStatus


class ThreadClass(QThread):
    any_signal = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super(ThreadClass, self).__init__(parent)
        self.is_running = True

    def run(self):
        while True:
            self.any_signal.emit(1)
            sleep(0.1)

    def stop(self):
        self.is_running = False
        self.terminate()


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.game = Game()
        self.thread = ThreadClass(parent=None)
        self.initRedBlinking()
        self.initGreenBlinking()
        self.initTimer()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        pixmap = QPixmap("../img/red.jpg")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("font: bold 11.5px;")
        self.centralwidget.setStyleSheet("""
            QWidget {
                font: bold 12px;
            }
            
            QPushButton {
                background-color: white;
                color: black;
                border: 0px solid #ccc;
                border-radius: 5px;
                transition: 0.3s;
            }

            QPushButton:hover {
                background-color: #f0f0f0;
                border: 2px solid #aaa;
            }

            QPushButton:pressed {
                background-color: #e0e0e0;
                border: 2px solid #888;
            }

            QPushButton:disabled {
                background-color: #ddd;
                color: #aaa;
                border: 2px solid #bbb;
            }
        """)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_init = QtWidgets.QPushButton(self.centralwidget)
        self.bt_init.setGeometry(QtCore.QRect(40, 20, 120, 40))
        self.bt_init.setObjectName("bt_init")
        self.bt_wating = QtWidgets.QPushButton(self.centralwidget)
        self.bt_wating.setGeometry(QtCore.QRect(320, 20, 120, 40))
        self.bt_wating.setObjectName("bt_wating")
        self.bt_run = QtWidgets.QPushButton(self.centralwidget)
        self.bt_run.setGeometry(QtCore.QRect(480, 20, 120, 40))
        self.bt_run.setObjectName("bt_run")
        self.bt_block = QtWidgets.QPushButton(self.centralwidget)
        self.bt_block.setGeometry(QtCore.QRect(640, 20, 120, 40))
        self.bt_block.setAutoExclusive(False)
        self.bt_block.setObjectName("bt_block")
        self.quest_status = QtWidgets.QLabel(self.centralwidget)
        self.quest_status.setGeometry(QtCore.QRect(180, 20, 120, 40))
        self.quest_status.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.quest_status.setAlignment(QtCore.Qt.AlignCenter)
        self.quest_status.setObjectName("quest_status")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 70, 761, 511))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 281, 511))
        self.frame_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setGeometry(QtCore.QRect(20, 0, 240, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(240, 30))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.sensor_door = QtWidgets.QLabel(self.frame_2)
        self.sensor_door.setGeometry(QtCore.QRect(20, 40, 240, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensor_door.sizePolicy().hasHeightForWidth())
        self.sensor_door.setSizePolicy(sizePolicy)
        self.sensor_door.setMinimumSize(QtCore.QSize(240, 30))
        self.sensor_door.setObjectName("sensor_door")
        self.sensor_door.setPixmap(pixmap)
        self.sensor_door.setScaledContents(True)
        self.sensor_door_layout = QtWidgets.QVBoxLayout(self.sensor_door)
        self.sensor_door_layout.setContentsMargins(0, 0, 0, 0)
        self.sensor_door_text = QtWidgets.QLabel(self.sensor_door)
        self.sensor_door_text.setAlignment(QtCore.Qt.AlignCenter)
        self.sensor_door_layout.addWidget(self.sensor_door_text)
        self.sensor_box = QtWidgets.QLabel(self.frame_2)
        self.sensor_box.setGeometry(QtCore.QRect(20, 80, 240, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensor_box.sizePolicy().hasHeightForWidth())
        self.sensor_box.setSizePolicy(sizePolicy)
        self.sensor_box.setMinimumSize(QtCore.QSize(240, 30))
        self.sensor_box.setObjectName("sensor_box")
        self.sensor_box.setPixmap(pixmap)
        self.sensor_box.setScaledContents(True)
        self.sensor_box_layout = QtWidgets.QVBoxLayout(self.sensor_box)
        self.sensor_box_layout.setContentsMargins(0, 0, 0, 0)
        self.sensor_box_text = QtWidgets.QLabel(self.sensor_box)
        self.sensor_box_text.setAlignment(QtCore.Qt.AlignCenter)
        self.sensor_box_layout.addWidget(self.sensor_box_text)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 130, 242, 106))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sensor_roulette = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensor_roulette.sizePolicy().hasHeightForWidth())
        self.sensor_roulette.setSizePolicy(sizePolicy)
        self.sensor_roulette.setMinimumSize(QtCore.QSize(240, 30))
        self.sensor_roulette.setObjectName("sensor_roulette")
        self.sensor_roulette.setPixmap(pixmap)
        self.sensor_roulette.setScaledContents(True)
        self.sensor_roulette_layout = QtWidgets.QVBoxLayout(self.sensor_roulette)
        self.sensor_roulette_layout.setContentsMargins(0, 0, 0, 0)
        self.sensor_roulette_text = QtWidgets.QLabel(self.sensor_roulette)
        self.sensor_roulette_text.setAlignment(QtCore.Qt.AlignCenter)
        self.sensor_roulette_layout.addWidget(self.sensor_roulette_text)
        self.verticalLayout.addWidget(self.sensor_roulette)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.sensor_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensor_13.sizePolicy().hasHeightForWidth())
        self.sensor_13.setSizePolicy(sizePolicy)
        self.sensor_13.setMinimumSize(QtCore.QSize(110, 30))
        self.sensor_13.setObjectName("sensor_13")
        self.sensor_13.setPixmap(pixmap)
        self.sensor_13.setScaledContents(True)
        self.sensor_13_layout = QtWidgets.QVBoxLayout(self.sensor_13)
        self.sensor_13_layout.setContentsMargins(0, 0, 0, 3)
        self.sensor_13_text = QtWidgets.QLabel(self.sensor_13)
        self.sensor_13_text.setAlignment(QtCore.Qt.AlignCenter)
        self.sensor_13_layout.addWidget(self.sensor_13_text)
        self.gridLayout.addWidget(self.sensor_13, 0, 1, 1, 1)
        self.sensor_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensor_3.sizePolicy().hasHeightForWidth())
        self.sensor_3.setSizePolicy(sizePolicy)
        self.sensor_3.setMinimumSize(QtCore.QSize(110, 30))
        self.sensor_3.setObjectName("sensor_3")
        self.sensor_3.setPixmap(pixmap)
        self.sensor_3.setScaledContents(True)
        self.sensor_3_layout = QtWidgets.QVBoxLayout(self.sensor_3)
        self.sensor_3_layout.setContentsMargins(0, 0, 0, 3)
        self.sensor_3_text = QtWidgets.QLabel(self.sensor_3)
        self.sensor_3_text.setAlignment(QtCore.Qt.AlignCenter)
        self.sensor_3_layout.addWidget(self.sensor_3_text)
        self.gridLayout.addWidget(self.sensor_3, 0, 0, 1, 1)
        self.sensor_21 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensor_21.sizePolicy().hasHeightForWidth())
        self.sensor_21.setSizePolicy(sizePolicy)
        self.sensor_21.setMinimumSize(QtCore.QSize(110, 30))
        self.sensor_21.setObjectName("sensor_21")
        self.sensor_21.setPixmap(pixmap)
        self.sensor_21.setScaledContents(True)
        self.sensor_21_layout = QtWidgets.QVBoxLayout(self.sensor_21)
        self.sensor_21_layout.setContentsMargins(0, 0, 0, 3)
        self.sensor_21_text = QtWidgets.QLabel(self.sensor_21)
        self.sensor_21_text.setAlignment(QtCore.Qt.AlignCenter)
        self.sensor_21_layout.addWidget(self.sensor_21_text)
        self.gridLayout.addWidget(self.sensor_21, 1, 0, 1, 1)
        self.sensor_33 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensor_33.sizePolicy().hasHeightForWidth())
        self.sensor_33.setSizePolicy(sizePolicy)
        self.sensor_33.setMinimumSize(QtCore.QSize(110, 30))
        self.sensor_33.setObjectName("sensor_33")
        self.sensor_33.setPixmap(pixmap)
        self.sensor_33.setScaledContents(True)
        self.sensor_33_layout = QtWidgets.QVBoxLayout(self.sensor_33)
        self.sensor_33_layout.setContentsMargins(0, 0, 0, 3)
        self.sensor_33_text = QtWidgets.QLabel(self.sensor_33)
        self.sensor_33_text.setAlignment(QtCore.Qt.AlignCenter)
        self.sensor_33_layout.addWidget(self.sensor_33_text)
        self.gridLayout.addWidget(self.sensor_33, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 250, 242, 106))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.sensor_map = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensor_map.sizePolicy().hasHeightForWidth())
        self.sensor_map.setSizePolicy(sizePolicy)
        self.sensor_map.setMinimumSize(QtCore.QSize(240, 30))
        self.sensor_map.setObjectName("sensor_map")
        self.sensor_map.setPixmap(pixmap)
        self.sensor_map.setScaledContents(True)
        self.sensor_map_layout = QtWidgets.QVBoxLayout(self.sensor_map)
        self.sensor_map_layout.setContentsMargins(0, 0, 0, 0)
        self.sensor_map_text = QtWidgets.QLabel(self.sensor_map)
        self.sensor_map_text.setAlignment(QtCore.Qt.AlignCenter)
        self.sensor_map_layout.addWidget(self.sensor_map_text)
        self.verticalLayout_3.addWidget(self.sensor_map)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.sensor_Paris = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensor_Paris.sizePolicy().hasHeightForWidth())
        self.sensor_Paris.setSizePolicy(sizePolicy)
        self.sensor_Paris.setMinimumSize(QtCore.QSize(110, 30))
        self.sensor_Paris.setObjectName("sensor_Paris")
        self.sensor_Paris.setPixmap(pixmap)
        self.sensor_Paris.setScaledContents(True)
        self.sensor_Paris_layout = QtWidgets.QVBoxLayout(self.sensor_Paris)
        self.sensor_Paris_layout.setContentsMargins(0, 0, 0, 3)
        self.sensor_Paris_text = QtWidgets.QLabel(self.sensor_Paris)
        self.sensor_Paris_text.setAlignment(QtCore.Qt.AlignCenter)
        self.sensor_Paris_layout.addWidget(self.sensor_Paris_text)
        self.gridLayout_2.addWidget(self.sensor_Paris, 0, 1, 1, 1)
        self.sensor_LA = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensor_LA.sizePolicy().hasHeightForWidth())
        self.sensor_LA.setSizePolicy(sizePolicy)
        self.sensor_LA.setMinimumSize(QtCore.QSize(110, 30))
        self.sensor_LA.setObjectName("sensor_LA")
        self.sensor_LA.setPixmap(pixmap)
        self.sensor_LA.setScaledContents(True)
        self.sensor_LA_layout = QtWidgets.QVBoxLayout(self.sensor_LA)
        self.sensor_LA_layout.setContentsMargins(0, 0, 0, 3)
        self.sensor_LA_text = QtWidgets.QLabel(self.sensor_LA)
        self.sensor_LA_text.setAlignment(QtCore.Qt.AlignCenter)
        self.sensor_LA_layout.addWidget(self.sensor_LA_text)
        self.gridLayout_2.addWidget(self.sensor_LA, 0, 0, 1, 1)
        self.sensor_Egypt = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensor_Egypt.sizePolicy().hasHeightForWidth())
        self.sensor_Egypt.setSizePolicy(sizePolicy)
        self.sensor_Egypt.setMinimumSize(QtCore.QSize(110, 30))
        self.sensor_Egypt.setObjectName("sensor_Egypt")
        self.sensor_Egypt.setPixmap(pixmap)
        self.sensor_Egypt.setScaledContents(True)
        self.sensor_Egypt_layout = QtWidgets.QVBoxLayout(self.sensor_Egypt)
        self.sensor_Egypt_layout.setContentsMargins(0, 0, 0, 3)
        self.sensor_Egypt_text = QtWidgets.QLabel(self.sensor_Egypt)
        self.sensor_Egypt_text.setAlignment(QtCore.Qt.AlignCenter)
        self.sensor_Egypt_layout.addWidget(self.sensor_Egypt_text)
        self.gridLayout_2.addWidget(self.sensor_Egypt, 1, 0, 1, 1)
        self.sensor_Japan = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensor_Japan.sizePolicy().hasHeightForWidth())
        self.sensor_Japan.setSizePolicy(sizePolicy)
        self.sensor_Japan.setMinimumSize(QtCore.QSize(110, 30))
        self.sensor_Japan.setObjectName("sensor_Japan")
        self.sensor_Japan.setPixmap(pixmap)
        self.sensor_Japan.setScaledContents(True)
        self.sensor_Japan_layout = QtWidgets.QVBoxLayout(self.sensor_Japan)
        self.sensor_Japan_layout.setContentsMargins(0, 0, 0, 3)
        self.sensor_Japan_text = QtWidgets.QLabel(self.sensor_Japan)
        self.sensor_Japan_text.setAlignment(QtCore.Qt.AlignCenter)
        self.sensor_Japan_layout.addWidget(self.sensor_Japan_text)
        self.gridLayout_2.addWidget(self.sensor_Japan, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.sensor_bottle = QtWidgets.QLabel(self.frame_2)
        self.sensor_bottle.setGeometry(QtCore.QRect(20, 370, 240, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensor_bottle.sizePolicy().hasHeightForWidth())
        self.sensor_bottle.setSizePolicy(sizePolicy)
        self.sensor_bottle.setMinimumSize(QtCore.QSize(240, 30))
        self.sensor_bottle.setObjectName("sensor_bottle")
        self.sensor_bottle.setPixmap(pixmap)
        self.sensor_bottle.setScaledContents(True)
        self.sensor_bottle_layout = QtWidgets.QVBoxLayout(self.sensor_bottle)
        self.sensor_bottle_layout.setContentsMargins(0, 0, 0, 0)
        self.sensor_bottle_text = QtWidgets.QLabel(self.sensor_bottle)
        self.sensor_bottle_text.setAlignment(QtCore.Qt.AlignCenter)
        self.sensor_bottle_layout.addWidget(self.sensor_bottle_text)
        self.sensor_phone = QtWidgets.QLabel(self.frame_2)
        self.sensor_phone.setGeometry(QtCore.QRect(20, 410, 240, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensor_phone.sizePolicy().hasHeightForWidth())
        self.sensor_phone.setSizePolicy(sizePolicy)
        self.sensor_phone.setMinimumSize(QtCore.QSize(240, 30))
        self.sensor_phone.setObjectName("sensor_phone")
        self.sensor_phone.setPixmap(pixmap)
        self.sensor_phone.setScaledContents(True)
        self.sensor_phone_layout = QtWidgets.QVBoxLayout(self.sensor_phone)
        self.sensor_phone_layout.setContentsMargins(0, 0, 0, 0)
        self.sensor_phone_text = QtWidgets.QLabel(self.sensor_phone)
        self.sensor_phone_text.setAlignment(QtCore.Qt.AlignCenter)
        self.sensor_phone_layout.addWidget(self.sensor_phone_text)
        self.sensor_bt_door = QtWidgets.QLabel(self.frame_2)
        self.sensor_bt_door.setGeometry(QtCore.QRect(20, 450, 240, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensor_bt_door.sizePolicy().hasHeightForWidth())
        self.sensor_bt_door.setSizePolicy(sizePolicy)
        self.sensor_bt_door.setMinimumSize(QtCore.QSize(240, 30))
        self.sensor_bt_door.setObjectName("sensor_bt_door")
        self.sensor_bt_door.setPixmap(pixmap)
        self.sensor_bt_door.setScaledContents(True)
        self.sensor_bt_door_layout = QtWidgets.QVBoxLayout(self.sensor_bt_door)
        self.sensor_bt_door_layout.setContentsMargins(0, 0, 0, 0)
        self.sensor_bt_door_text = QtWidgets.QLabel(self.sensor_bt_door)
        self.sensor_bt_door_text.setAlignment(QtCore.Qt.AlignCenter)
        self.sensor_bt_door_layout.addWidget(self.sensor_bt_door_text)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("QLabel { color: rgb(255, 255, 255); }")
        self.frame_3.setGeometry(QtCore.QRect(280, 0, 311, 341))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 311, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(240, 30))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setGeometry(QtCore.QRect(160, 30, 150, 51))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_10 = QtWidgets.QLabel(self.frame_6)
        self.label_10.setGeometry(QtCore.QRect(0, 0, 150, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(0, 0))
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.lazer_on = QtWidgets.QPushButton(self.frame_6)
        self.lazer_on.setGeometry(QtCore.QRect(10, 20, 65, 30))
        self.lazer_on.setObjectName("lazer_on")
        self.lazer_off = QtWidgets.QPushButton(self.frame_6)
        self.lazer_off.setGeometry(QtCore.QRect(75, 20, 65, 30))
        self.lazer_off.setObjectName("lazer_off")
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setGeometry(QtCore.QRect(0, 30, 150, 51))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_11 = QtWidgets.QLabel(self.frame_7)
        self.label_11.setGeometry(QtCore.QRect(0, 0, 150, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(0, 0))
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.light_on = QtWidgets.QPushButton(self.frame_7)
        self.light_on.setGeometry(QtCore.QRect(10, 20, 65, 30))
        self.light_on.setObjectName("light_on")
        self.light_off = QtWidgets.QPushButton(self.frame_7)
        self.light_off.setGeometry(QtCore.QRect(75, 20, 65, 30))
        self.light_off.setObjectName("light_off")
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        self.frame_8.setGeometry(QtCore.QRect(0, 80, 150, 51))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.label_12 = QtWidgets.QLabel(self.frame_8)
        self.label_12.setGeometry(QtCore.QRect(0, 0, 150, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(0, 0))
        self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.roulette_on = QtWidgets.QPushButton(self.frame_8)
        self.roulette_on.setGeometry(QtCore.QRect(10, 20, 65, 30))
        self.roulette_on.setObjectName("roulette_on")
        self.roulette_off = QtWidgets.QPushButton(self.frame_8)
        self.roulette_off.setGeometry(QtCore.QRect(75, 20, 65, 30))
        self.roulette_off.setObjectName("roulette_off")
        self.frame_9 = QtWidgets.QFrame(self.frame_3)
        self.frame_9.setGeometry(QtCore.QRect(0, 130, 150, 51))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_13 = QtWidgets.QLabel(self.frame_9)
        self.label_13.setGeometry(QtCore.QRect(0, 0, 150, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QtCore.QSize(0, 0))
        self.label_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.map_on = QtWidgets.QPushButton(self.frame_9)
        self.map_on.setGeometry(QtCore.QRect(10, 20, 65, 30))
        self.map_on.setObjectName("map_on")
        self.map_off = QtWidgets.QPushButton(self.frame_9)
        self.map_off.setGeometry(QtCore.QRect(75, 20, 65, 30))
        self.map_off.setObjectName("map_off")
        self.frame_10 = QtWidgets.QFrame(self.frame_3)
        self.frame_10.setGeometry(QtCore.QRect(0, 180, 150, 51))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_14 = QtWidgets.QLabel(self.frame_10)
        self.label_14.setGeometry(QtCore.QRect(0, 0, 150, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QtCore.QSize(0, 0))
        self.label_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.bottle_on = QtWidgets.QPushButton(self.frame_10)
        self.bottle_on.setGeometry(QtCore.QRect(10, 20, 65, 30))
        self.bottle_on.setObjectName("bottle_on")
        self.bottle_off = QtWidgets.QPushButton(self.frame_10)
        self.bottle_off.setGeometry(QtCore.QRect(75, 20, 65, 30))
        self.bottle_off.setObjectName("bottle_off")
        self.frame_11 = QtWidgets.QFrame(self.frame_3)
        self.frame_11.setGeometry(QtCore.QRect(0, 230, 150, 51))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.label_25 = QtWidgets.QLabel(self.frame_11)
        self.label_25.setGeometry(QtCore.QRect(0, 0, 150, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setMinimumSize(QtCore.QSize(0, 0))
        self.label_25.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.phone_on = QtWidgets.QPushButton(self.frame_11)
        self.phone_on.setGeometry(QtCore.QRect(10, 20, 65, 30))
        self.phone_on.setObjectName("phone_on")
        self.phone_off = QtWidgets.QPushButton(self.frame_11)
        self.phone_off.setGeometry(QtCore.QRect(75, 20, 65, 30))
        self.phone_off.setObjectName("phone_off")
        self.frame_12 = QtWidgets.QFrame(self.frame_3)
        self.frame_12.setGeometry(QtCore.QRect(0, 280, 150, 51))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.label_26 = QtWidgets.QLabel(self.frame_12)
        self.label_26.setGeometry(QtCore.QRect(0, 0, 150, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setMinimumSize(QtCore.QSize(0, 0))
        self.label_26.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.safe_on = QtWidgets.QPushButton(self.frame_12)
        self.safe_on.setGeometry(QtCore.QRect(10, 20, 65, 30))
        self.safe_on.setObjectName("safe_on")
        self.safe_off = QtWidgets.QPushButton(self.frame_12)
        self.safe_off.setGeometry(QtCore.QRect(75, 20, 65, 30))
        self.safe_off.setObjectName("safe_off")
        self.frame_13 = QtWidgets.QFrame(self.frame_3)
        self.frame_13.setGeometry(QtCore.QRect(160, 80, 150, 51))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.label_27 = QtWidgets.QLabel(self.frame_13)
        self.label_27.setGeometry(QtCore.QRect(0, 0, 150, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setMinimumSize(QtCore.QSize(0, 0))
        self.label_27.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.smoke_on = QtWidgets.QPushButton(self.frame_13)
        self.smoke_on.setGeometry(QtCore.QRect(10, 20, 65, 30))
        self.smoke_on.setObjectName("smoke_on")
        self.smoke_off = QtWidgets.QPushButton(self.frame_13)
        self.smoke_off.setGeometry(QtCore.QRect(75, 20, 65, 30))
        self.smoke_off.setObjectName("smoke_off")
        self.frame_14 = QtWidgets.QFrame(self.frame_3)
        self.frame_14.setGeometry(QtCore.QRect(160, 130, 150, 51))
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.label_28 = QtWidgets.QLabel(self.frame_14)
        self.label_28.setGeometry(QtCore.QRect(0, 0, 150, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setMinimumSize(QtCore.QSize(0, 0))
        self.label_28.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.lighthouse_on = QtWidgets.QPushButton(self.frame_14)
        self.lighthouse_on.setGeometry(QtCore.QRect(10, 20, 65, 30))
        self.lighthouse_on.setObjectName("lighthouse_on")
        self.lighthouse_off = QtWidgets.QPushButton(self.frame_14)
        self.lighthouse_off.setGeometry(QtCore.QRect(75, 20, 65, 30))
        self.lighthouse_off.setObjectName("lighthouse_off")
        self.frame_15 = QtWidgets.QFrame(self.frame_3)
        self.frame_15.setGeometry(QtCore.QRect(160, 180, 150, 51))
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.label_29 = QtWidgets.QLabel(self.frame_15)
        self.label_29.setGeometry(QtCore.QRect(0, 0, 150, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setMinimumSize(QtCore.QSize(0, 0))
        self.label_29.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.logo_on = QtWidgets.QPushButton(self.frame_15)
        self.logo_on.setGeometry(QtCore.QRect(10, 20, 65, 30))
        self.logo_on.setObjectName("logo_on")
        self.logo_off = QtWidgets.QPushButton(self.frame_15)
        self.logo_off.setGeometry(QtCore.QRect(75, 20, 65, 30))
        self.logo_off.setObjectName("logo_off")
        self.frame_16 = QtWidgets.QFrame(self.frame_3)
        self.frame_16.setGeometry(QtCore.QRect(160, 230, 150, 51))
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.label_30 = QtWidgets.QLabel(self.frame_16)
        self.label_30.setGeometry(QtCore.QRect(0, 0, 150, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        self.label_30.setMinimumSize(QtCore.QSize(0, 0))
        self.label_30.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.reset_on = QtWidgets.QPushButton(self.frame_16)
        self.reset_on.setGeometry(QtCore.QRect(10, 20, 65, 30))
        self.reset_on.setObjectName("reset_on")
        self.reset_off = QtWidgets.QPushButton(self.frame_16)
        self.reset_off.setGeometry(QtCore.QRect(75, 20, 65, 30))
        self.reset_off.setObjectName("reset_on_2")
        self.frame_17 = QtWidgets.QFrame(self.frame_3)
        self.frame_17.setGeometry(QtCore.QRect(160, 280, 150, 51))
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.label_31 = QtWidgets.QLabel(self.frame_17)
        self.label_31.setGeometry(QtCore.QRect(0, 0, 150, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setMinimumSize(QtCore.QSize(0, 0))
        self.label_31.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.spot_on = QtWidgets.QPushButton(self.frame_17)
        self.spot_on.setGeometry(QtCore.QRect(10, 20, 65, 30))
        self.spot_on.setObjectName("spot_on")
        self.spot_off = QtWidgets.QPushButton(self.frame_17)
        self.spot_off.setGeometry(QtCore.QRect(75, 20, 65, 30))
        self.spot_off.setObjectName("spot_off")
        self.music_box = QtWidgets.QComboBox(self.frame)
        self.music_box.setGeometry(QtCore.QRect(280, 360, 290, 41))
        self.music_box.setObjectName("music_box")
        self.music_box.addItem("")
        self.music_box.addItem("")
        self.music_box.addItem("")
        self.music_box.addItem("")
        self.music_box.addItem("")
        self.music_box.addItem("")
        self.music_box.addItem("")
        self.bt_play = QtWidgets.QPushButton(self.frame)
        self.bt_play.setGeometry(QtCore.QRect(280, 410, 90, 30))
        self.bt_play.setObjectName("bt_play")
        self.bt_pause = QtWidgets.QPushButton(self.frame)
        self.bt_pause.setGeometry(QtCore.QRect(380, 410, 90, 30))
        self.bt_pause.setObjectName("bt_pause")
        self.bt_stop = QtWidgets.QPushButton(self.frame)
        self.bt_stop.setGeometry(QtCore.QRect(480, 410, 90, 30))
        self.bt_stop.setObjectName("bt_stop")
        self.timer_bar = QtWidgets.QProgressBar(self.frame)
        self.timer_bar.setStyleSheet("""
    QProgressBar {
        border: 2px solid #ccc;
        border-radius: 10px;
        background-color: #f0f0f0;
        height: 20px;
        text-align: right;
        padding-right: 5px;
        font-size: 14px;
        font-weight: bold;
        color: black;
        padding: 0px; /* убираем padding, чтобы не ломал ширину */
        text-align: center;
    }

    /* Градиентная заполняющая полоса */
    QProgressBar::chunk {
        background: qlineargradient(
            spread:pad, x1:0, y1:0, x2:1, y2:0,
            stop:0 #4CAF50,   /* Начальный зелёный */
            stop:0.5 #66BB6A, /* Светло-зелёный центр */
            stop:1 #4CAF50    /* Возврат к тёмно-зелёному */
        );
        border-radius: 8px;
    }

    /* Для отключенного состояния */
    QProgressBar:disabled {
        background-color: #ddd;
        color: #aaa;
        border: 2px solid #bbb;
    }
""")
        self.timer_bar.setGeometry(QtCore.QRect(280, 479, 291, 31))
        self.timer_bar.setProperty("value", 0)
        self.timer_bar.setObjectName("timer_bar")
        self.timer_bar.setTextVisible(False)
        self.timer = QtWidgets.QLabel(self.frame)
        self.timer.setGeometry(QtCore.QRect(270, 450, 310, 40))
        self.timer.setStyleSheet("color: rgb(255, 255, 255);")
        self.timer.setTextFormat(QtCore.Qt.PlainText)
        self.timer.setAlignment(QtCore.Qt.AlignCenter)
        self.timer.setObjectName("timer")
        self.bt_alarm = QtWidgets.QPushButton(self.frame)
        self.bt_alarm.setGeometry(QtCore.QRect(610, 360, 110, 80))
        self.bt_alarm.setObjectName("bt_alarm")
        self.slider = QtWidgets.QSlider(self.frame)
        self.slider.setStyleSheet("""
            QSlider {
                min-height: 20px;
            }

            /* Горизонтальный слайдер (основная полоса) */
            QSlider::groove:horizontal {
                background: #ccc;
                height: 6px;
                border-radius: 3px;
            }

            /* Полоса при движении ползунка */
            QSlider::sub-page:horizontal {
                background: #aaa;
                border-radius: 3px;
            }

            /* Ползунок */
            QSlider::handle:horizontal {
                background: white;
                border: 2px solid #888;
                width: 18px;
                height: 18px;
                margin: -6px 0;
                border-radius: 9px;
            }

            /* Эффект при наведении */
            QSlider::handle:horizontal:hover {
                background: #f0f0f0;
                border: 2px solid #666;
            }

            /* Отключенный слайдер */
            QSlider:disabled {
                background: #ddd;
            }

            /* Вертикальный слайдер (по аналогии с горизонтальным) */
            QSlider::groove:vertical {
                background: #ccc;
                width: 6px;
                border-radius: 3px;
            }

            QSlider::handle:vertical {
                background: white;
                border: 2px solid #888;
                width: 18px;
                height: 18px;
                margin: 0 -6px;
                border-radius: 9px;
            }

            QSlider::handle:vertical:hover {
                background: #f0f0f0;
                border: 2px solid #666;
            }
        """)
        self.slider.setGeometry(QtCore.QRect(740, 360, 20, 80))
        self.slider.setProperty("value", 99)
        self.slider.setOrientation(QtCore.Qt.Vertical)
        self.slider.setObjectName("slider")
        self.bt_3min = QtWidgets.QPushButton(self.frame)
        self.bt_3min.setGeometry(QtCore.QRect(670, 480, 60, 30))
        self.bt_3min.setObjectName("bt_3min")
        self.bt_m3min = QtWidgets.QPushButton(self.frame)
        self.bt_m3min.setGeometry(QtCore.QRect(610, 480, 60, 31))
        self.bt_m3min.setObjectName("bt_m3min")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(590, 0, 171, 341))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setStyleSheet("QLabel { color: rgb(255, 255, 255); }")
        self.label_9.setGeometry(QtCore.QRect(0, 0, 170, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(0, 0))
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.bt_box = QtWidgets.QPushButton(self.frame_4)
        self.bt_box.setGeometry(QtCore.QRect(30, 50, 120, 30))
        self.bt_box.setObjectName("bt_box")
        self.bt_roulette = QtWidgets.QPushButton(self.frame_4)
        self.bt_roulette.setGeometry(QtCore.QRect(30, 100, 120, 30))
        self.bt_roulette.setObjectName("bt_roulette")
        self.bt_map = QtWidgets.QPushButton(self.frame_4)
        self.bt_map.setGeometry(QtCore.QRect(30, 150, 120, 30))
        self.bt_map.setObjectName("bt_map")
        self.bt_bottle = QtWidgets.QPushButton(self.frame_4)
        self.bt_bottle.setGeometry(QtCore.QRect(30, 200, 120, 30))
        self.bt_bottle.setObjectName("bt_bottle")
        self.bt_phone = QtWidgets.QPushButton(self.frame_4)
        self.bt_phone.setGeometry(QtCore.QRect(30, 250, 120, 30))
        self.bt_phone.setObjectName("bt_phone")
        self.bt_door = QtWidgets.QPushButton(self.frame_4)
        self.bt_door.setGeometry(QtCore.QRect(30, 300, 120, 30))
        self.bt_door.setObjectName("bt_door")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.startWorker()
        self.connectEvents()
        self.setOuts()
        self.setInputs()
        self.setStages()

    def setInputs(self):
        self.inputs = {
            "x1": self.sensor_door,
            "x2": self.sensor_box,
            "x3": self.sensor_3,
            "x4": self.sensor_13,
            "x5": self.sensor_21,
            "x6": self.sensor_33,
            "x8": self.sensor_Paris,
            "x7": self.sensor_LA,
            "x9": self.sensor_Egypt,
            "x10": self.sensor_Japan,
            "x11": self.sensor_bottle,
            "x12": self.sensor_phone,
            "x13": self.sensor_bt_door,
            "roulette": self.sensor_roulette,
            "map": self.sensor_map
        }

    def setOuts(self):
        self.outs = {
            "y1": self.light_on,
            "y2": self.roulette_on,
            "y3": self.map_on,
            "y4": self.bottle_on,
            "y5": self.phone_on,
            "y6": self.safe_on,
            "y7": self.lazer_on,
            "y8": self.smoke_on,
            "y9": self.lighthouse_on,
            "y10": self.logo_on,
            "y11": self.reset_on,
            "y12": self.spot_on,
        }

    def setStages(self):
        self.stages = {
            "box": self.bt_box,
            "roulette": self.bt_roulette,
            "map": self.bt_map,
            "bottle": self.bt_bottle,
            "phone": self.bt_phone,
            "door": self.bt_door,
        }

    def checkStages(self):
        for stageName in self.stages:
            if self.game.stages[stageName]:
                self.setGreenButton(self.stages[stageName])
            else:
                self.setWhiteButton(self.stages[stageName])

    def checkInputs(self, init=False):
        for inputName in self.inputs:
            if self.game.inputs[inputName]:
                self.setGreenSensor(self.inputs[inputName])
            else:
                if inputName[0] != "x" or not init:
                    continue
                self.setRedSensor(self.inputs[inputName])

    def checkOuts(self):
        for out in self.outs:
            if out in ("y2", "y3", "y4", "y5", "y6"):
                if self.game.outs[out]:
                    self.setWhiteButton(self.outs[out])
                else:
                    self.setGreenButton(self.outs[out])
            else:
                if self.game.outs[out]:
                    self.setGreenButton(self.outs[out])
                else:
                    self.setWhiteButton(self.outs[out])

    def checkState(self):
        if self.game.settings["gameStatus"] == GameStatus.READY:
            self.greenQuest()
            self.startGreenBlinking()
        else:
            self.redQuest()
            self.stopGreenBlinking()

    def setTime(self):
        self.timer.setText(
            f"Прошло времени от квеста: {self.game.timeSettings.getTimeStr()} / {self.game.timeSettings.getTimeLimitStr()}")
        self.timer_bar.setValue(self.game.timeSettings.getProgress())
        self.timer_bar.repaint()

    def redQuest(self):
        self.quest_status.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.quest_status.setText("Квест не собран")

    def greenQuest(self):
        self.quest_status.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.quest_status.setText("Квест собран")

    def yellowQuest(self):
        self.quest_status.setStyleSheet("background-color: rgb(255, 255, 0);}")
        self.quest_status.setText("Квест запущен")

    def blueQuest(self):
        self.quest_status.setStyleSheet("background-color: rgb(66, 170, 255);")
        self.quest_status.setText("Квест окончен")

    def setGreenButton(self, button: QtWidgets.QPushButton):
        button.setStyleSheet(button.styleSheet() + "background-color: rgb(0, 255, 0);")

    def setRedButton(self, button: QtWidgets.QPushButton):
        button.setStyleSheet(button.styleSheet() + "background-color: rgb(255, 0, 0);")

    def setYellowButton(self, button: QtWidgets.QPushButton):
        button.setStyleSheet("background-color: rgb(255, 255, 0);}")

    def setWhiteButton(self, button: QtWidgets.QPushButton):
        button.setStyleSheet("")

    def setRedSensor(self, sensor: QtWidgets.QLabel):
        pixmap = QPixmap("../img/red.jpg")
        sensor.setPixmap(pixmap)

    def setGreenSensor(self, sensor: QtWidgets.QLabel):
        pixmap = QPixmap("../img/green.jpg")
        sensor.setPixmap(pixmap)

    def btInitClick(self):
        self.stopTimer()
        self.stopGreenBlinking()
        self.stopRedBlinking()
        self.checkInputs(init=True)

        self.game.initGame()
        self.setTime()
        self.checkState()

    def btWaitingClick(self):
        if self.game.settings["gameStatus"] != GameStatus.LAUNCHED:
            self.game.settings["waitingStatus"] = WaitingStatus.READY
            self.stopGreenBlinking()
            self.setYellowButton(self.bt_wating)

    def btRunClick(self):
        if self.game.settings["waitingStatus"] == WaitingStatus.READY:
            self.game.settings["startEvent"] = True

    def btBlockClick(self):
        self.game.lockDoor()
        if self.game.settings["doorLock"]:
            self.setRedButton(self.bt_block)
            self.startRedBlinking()
        else:
            self.stopRedBlinking()

    def btOnClick(self, out: str):
        if out in ("y2", "y3", "y4", "y5", "y6"):
            self.game.deactivateOut(out)
        else:
            self.game.activateOut(out)

    def btOffClick(self, out: str):
        if out in ("y2", "y3", "y4", "y5", "y6"):
            self.game.activateOut(out)
        elif out in ("y8", "y11"):
            return
        else:
            self.game.deactivateOut(out)

    def btSkipClick(self, stage: str):
        self.game.activateStage(stage)

    def btPlayClick(self):
        self.game.playMusic(self.music_box.currentText())

    def btPauseClick(self):
        self.game.pauseMusic(self.music_box.currentText())

    def btStopClick(self):
        self.game.stopMusic(self.music_box.currentText())

    def btAlarmClick(self):
        self.game.alarm()

    def btPlusClick(self):
        self.game.timeSettings.addTimeLimit()
        self.setTime()

    def btMinusClick(self):
        self.game.timeSettings.removeTimeLimit()
        self.setTime()

    def changeVolume(self):
        self.game.changeVolume(self.slider.value())

    def connectEvents(self):
        self.bt_init.clicked.connect(self.btInitClick)
        self.bt_wating.clicked.connect(self.btWaitingClick)
        self.bt_run.clicked.connect(self.btRunClick)
        self.bt_block.clicked.connect(self.btBlockClick)

        self.light_on.clicked.connect(lambda: self.btOnClick("y1"))
        self.roulette_on.clicked.connect(lambda: self.btOnClick("y2"))
        self.map_on.clicked.connect(lambda: self.btOnClick("y3"))
        self.bottle_on.clicked.connect(lambda: self.btOnClick("y4"))
        self.phone_on.clicked.connect(lambda: self.btOnClick("y5"))
        self.safe_on.clicked.connect(lambda: self.btOnClick("y6"))
        self.lazer_on.clicked.connect(lambda: self.btOnClick("y7"))
        self.smoke_on.clicked.connect(lambda: self.btOnClick("y8"))
        self.lighthouse_on.clicked.connect(lambda: self.btOnClick("y9"))
        self.logo_on.clicked.connect(lambda: self.btOnClick("y10"))
        self.reset_on.clicked.connect(lambda: self.btOnClick("y11"))
        self.spot_on.clicked.connect(lambda: self.btOnClick("y12"))

        self.light_off.clicked.connect(lambda: self.btOffClick("y1"))
        self.roulette_off.clicked.connect(lambda: self.btOffClick("y2"))
        self.map_off.clicked.connect(lambda: self.btOffClick("y3"))
        self.bottle_off.clicked.connect(lambda: self.btOffClick("y4"))
        self.phone_off.clicked.connect(lambda: self.btOffClick("y5"))
        self.safe_off.clicked.connect(lambda: self.btOffClick("y6"))
        self.lazer_off.clicked.connect(lambda: self.btOffClick("y7"))
        self.smoke_off.clicked.connect(lambda: self.btOffClick("y8"))
        self.lighthouse_off.clicked.connect(lambda: self.btOffClick("y9"))
        self.logo_off.clicked.connect(lambda: self.btOffClick("y10"))
        self.reset_off.clicked.connect(lambda: self.btOffClick("y11"))
        self.spot_off.clicked.connect(lambda: self.btOffClick("y12"))

        self.bt_box.clicked.connect(lambda: self.btSkipClick("box"))
        self.bt_roulette.clicked.connect(lambda: self.btSkipClick("roulette"))
        self.bt_map.clicked.connect(lambda: self.btSkipClick("map"))
        self.bt_bottle.clicked.connect(lambda: self.btSkipClick("bottle"))
        self.bt_phone.clicked.connect(lambda: self.btSkipClick("phone"))
        self.bt_door.clicked.connect(lambda: self.btSkipClick("door"))

        self.bt_play.clicked.connect(self.btPlayClick)
        self.bt_pause.clicked.connect(self.btPauseClick)
        self.bt_stop.clicked.connect(self.btStopClick)
        self.bt_alarm.clicked.connect(self.btAlarmClick)
        self.slider.valueChanged.connect(self.changeVolume)

        self.bt_m3min.clicked.connect(self.btMinusClick)
        self.bt_3min.clicked.connect(self.btPlusClick)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_init.setText(_translate("MainWindow", "Init quest"))
        self.bt_wating.setText(_translate("MainWindow", "Ожидание запуска"))
        self.bt_run.setText(_translate("MainWindow", "Run quest"))
        self.bt_block.setText(_translate("MainWindow", "Блокировка\n"
                                                       "сигнала двери"))
        self.quest_status.setText(_translate("MainWindow", "Квест собран"))
        self.label_2.setText(_translate("MainWindow", "Входные сигналы"))
        self.sensor_door_text.setText(_translate("MainWindow", "Геркон двери (online)"))
        self.sensor_box_text.setText(_translate("MainWindow", "Шкатулка (offline)"))
        self.sensor_roulette_text.setText(_translate("MainWindow", "Рулетка (offline)"))
        self.sensor_13_text.setText(_translate("MainWindow", "13\n"
                                                             "(online)"))
        self.sensor_3_text.setText(_translate("MainWindow", "3\n"
                                                            "(online)"))
        self.sensor_21_text.setText(_translate("MainWindow", "21\n"
                                                             "(online)"))
        self.sensor_33_text.setText(_translate("MainWindow", "33\n"
                                                             "(online)"))
        self.sensor_map_text.setText(_translate("MainWindow", "Карта (offline)"))
        self.sensor_Paris_text.setText(_translate("MainWindow", "Париж\n"
                                                                "(online)"))
        self.sensor_LA_text.setText(_translate("MainWindow", "Л-Анджелес\n"
                                                             "(online)"))
        self.sensor_Egypt_text.setText(_translate("MainWindow", "Египет\n"
                                                                "(online)"))
        self.sensor_Japan_text.setText(_translate("MainWindow", "Япония\n"
                                                                "(online)"))
        self.sensor_bottle_text.setText(_translate("MainWindow", "Бутылки (offline)"))
        self.sensor_phone_text.setText(_translate("MainWindow", "Телефон (offline)"))
        self.sensor_bt_door_text.setText(_translate("MainWindow", "Кнопка у входа (offline)"))
        self.label_3.setText(_translate("MainWindow", "Ручное управление"))
        self.label_10.setText(_translate("MainWindow", "Лазеры"))
        self.lazer_on.setText(_translate("MainWindow", "On"))
        self.lazer_off.setText(_translate("MainWindow", "Off"))
        self.label_11.setText(_translate("MainWindow", "Освещение"))
        self.light_on.setText(_translate("MainWindow", "On"))
        self.light_off.setText(_translate("MainWindow", "Off"))
        self.label_12.setText(_translate("MainWindow", "Светодиод / Рулетка"))
        self.roulette_on.setText(_translate("MainWindow", "On"))
        self.roulette_off.setText(_translate("MainWindow", "Off"))
        self.label_13.setText(_translate("MainWindow", "Светодиод / Карта"))
        self.map_on.setText(_translate("MainWindow", "On"))
        self.map_off.setText(_translate("MainWindow", "Off"))
        self.label_14.setText(_translate("MainWindow", "Светодиод / Бутылки"))
        self.bottle_on.setText(_translate("MainWindow", "On"))
        self.bottle_off.setText(_translate("MainWindow", "Off"))
        self.label_25.setText(_translate("MainWindow", "Светодиод / Телефон"))
        self.phone_on.setText(_translate("MainWindow", "On"))
        self.phone_off.setText(_translate("MainWindow", "Off"))
        self.label_26.setText(_translate("MainWindow", "ЭМ сейфовой"))
        self.safe_on.setText(_translate("MainWindow", "On"))
        self.safe_off.setText(_translate("MainWindow", "Off"))
        self.label_27.setText(_translate("MainWindow", "Дым-машина (2 сек)"))
        self.smoke_on.setText(_translate("MainWindow", "On"))
        self.smoke_off.setText(_translate("MainWindow", "Off"))
        self.label_28.setText(_translate("MainWindow", "Проблесковый маяк"))
        self.lighthouse_on.setText(_translate("MainWindow", "On"))
        self.lighthouse_off.setText(_translate("MainWindow", "Off"))
        self.label_29.setText(_translate("MainWindow", "Подсветка логотипа"))
        self.logo_on.setText(_translate("MainWindow", "On"))
        self.logo_off.setText(_translate("MainWindow", "Off"))
        self.label_30.setText(_translate("MainWindow", "Сброс (5 сек)"))
        self.reset_on.setText(_translate("MainWindow", "On"))
        self.reset_off.setText(_translate("MainWindow", "Off"))
        self.label_31.setText(_translate("MainWindow", "Спот"))
        self.spot_on.setText(_translate("MainWindow", "On"))
        self.spot_off.setText(_translate("MainWindow", "Off"))
        self.music_box.setItemText(0, _translate("MainWindow", "Трек №1  «Проникновение»"))
        self.music_box.setItemText(1, _translate("MainWindow", "Трек №2  «Фон»"))
        self.music_box.setItemText(2, _translate("MainWindow", "Трек №3  «Замок»"))
        self.music_box.setItemText(3, _translate("MainWindow", "Трек №4  «Сирена»"))
        self.music_box.setItemText(4, _translate("MainWindow", "Трек №5  «Победа»"))
        self.music_box.setItemText(5, _translate("MainWindow", "Трек №6  «Поражение»"))
        self.music_box.setItemText(6, _translate("MainWindow", "Трек №7  «Alarm»"))
        self.bt_play.setText(_translate("MainWindow", "Play"))
        self.bt_pause.setText(_translate("MainWindow", "Pause"))
        self.bt_stop.setText(_translate("MainWindow", "Stop"))
        self.timer.setText(_translate("MainWindow", "Прошло времени от квеста: 00:00:00 / 01:00:00"))
        self.bt_alarm.setText(_translate("MainWindow", "ALARM"))
        self.bt_3min.setText(_translate("MainWindow", "+ 3 мин"))
        self.bt_m3min.setText(_translate("MainWindow", "- 3 мин"))
        self.label_9.setText(_translate("MainWindow", "Пропуск загадок"))
        self.bt_box.setText(_translate("MainWindow", "Шкатулка"))
        self.bt_roulette.setText(_translate("MainWindow", "Рулетка"))
        self.bt_map.setText(_translate("MainWindow", "Карта"))
        self.bt_bottle.setText(_translate("MainWindow", "Бутылки"))
        self.bt_phone.setText(_translate("MainWindow", "Телефон"))
        self.bt_door.setText(_translate("MainWindow", "Кнопка у двери"))

    def initTimer(self):
        self.tTimer = QTimer()
        self.tTimer.timeout.connect(self.addTime)

    def startTimer(self):
        self.tTimer.start(1000)

    def stopTimer(self):
        self.tTimer.stop()
        self.game.timeSettings.initTime()

    def addTime(self):
        self.game.timeSettings.time += 1
        self.setTime()
        if self.game.timeSettings.time == self.game.timeSettings.timeLimit:
            self.game.settings["defeatEvent"] = True

    def initRedBlinking(self):
        self.redBlinkTimer = QTimer()
        self.redBlinkTimer.timeout.connect(self.redBlink)
        self.isRed = False

    def startRedBlinking(self):
        self.redBlinkTimer.start(1000)
        self.isRed = True

    def stopRedBlinking(self):
        self.redBlinkTimer.stop()
        self.setWhiteButton(self.bt_block)

    def redBlink(self):
        if self.isRed:
            self.setRedButton(self.bt_block)
        else:
            self.setWhiteButton(self.bt_block)

        self.isRed = not self.isRed

    def initGreenBlinking(self):
        self.greenBlinkTimer = QTimer()
        self.greenBlinkTimer.timeout.connect(self.greenBlink)
        self.isGreen = False

    def startGreenBlinking(self):
        self.greenBlinkTimer.start(1000)
        self.isGreen = True

    def stopGreenBlinking(self):
        self.greenBlinkTimer.stop()
        self.setWhiteButton(self.bt_block)

    def greenBlink(self):
        if self.isGreen:
            self.setGreenButton(self.bt_wating)
        else:
            self.setWhiteButton(self.bt_wating)

        self.isGreen = not self.isGreen

    def startWorker(self):
        self.thread.start()
        self.thread.any_signal.connect(self.mainLoop)

    def startGame(self):
        self.startTimer()
        self.setWhiteButton(self.bt_wating)
        self.yellowQuest()

    def stopGame(self):
        self.stopTimer()
        self.blueQuest()

    def mainLoop(self):
        self.checkOuts()
        self.checkInputs()
        self.checkStages()

        if self.game.settings["startEvent"]:
            self.game.startGame()
            self.startGame()

        elif self.game.settings["winEvent"]:
            self.game.winScript()
            self.stopGame()

        elif self.game.settings["defeatEvent"]:
            self.game.defeatScript()
            self.stopGame()


stylesheet = """
    QMainWindow {
        background-image: url("../img/background.png");
        background-repeat: no-repeat;
        background-position: center;
        background-attachment: fixed;
        background-size: cover;
    }
"""

if __name__ == "__main__":
    import sys

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
