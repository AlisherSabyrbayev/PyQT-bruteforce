from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):  #метод принимает главный объект окна (MainWindow) и добавляет в него виджеты
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 240)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 491, 221))
        self.frame.setStyleSheet("""
            QFrame {
                border-radius: 15px;
                background-color: #394341;
            }
        """)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 131, 141))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("data/excel.png"))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.frame) #создаем пуш внутри фрейма.
        self.pushButton.setGeometry(QtCore.QRect(160, 50, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)) #динамичный курсор, меняет на палец
        button_style = """
            /* Основной стиль кнопки */
            QPushButton {
                border-radius: 10px;
                background-color: #3db39e;
                color: white;
            }

            /* Стиль при наведении */
            QPushButton:hover {
                border-radius: 10px;
                background-color: #3ca492;
                color: white;
            }

            /* Стиль при нажатии */
            QPushButton:pressed {
                border-radius: 10px;
                background-color: #3d9888;
                color: white;
            }
        """
        self.pushButton.setStyleSheet(button_style)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 100, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        button_style = """
            QPushButton {
                border-radius: 10px;
                background-color: #3db39e;
                color: white;
            }
            QPushButton:hover {
                background-color: #3ca492;
            }
            QPushButton:pressed {
                background-color: #3d9888;
            }
        """
        self.pushButton_2.setStyleSheet(button_style)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 160, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(140, 160, 441, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 10, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("""
            QPushButton {
                border-radius: 10px;
                background-color: #3db39e;
                color: white;
            }
            QPushButton:hover {
                background-color: #3ca492;
            }
            QPushButton:pressed {
                background-color: #3d9888;
            }
        """)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(300, 15, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel { color: white; }")
        self.label_5.setObjectName("label_5")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(20, 190, 71, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox.setStyleSheet("QCheckBox { color: white; }")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_2.setGeometry(QtCore.QRect(120, 190, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_2.setStyleSheet("QCheckBox { color: white; }")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_3.setGeometry(QtCore.QRect(270, 190, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_3.setStyleSheet("QCheckBox { color: white; }")
        self.checkBox_3.setObjectName("checkBox_3")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(330, 50, 151, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAcceptDrops(False)  #не принимать перетаскиваемые объект
        self.label_3.setStyleSheet("""
            QLabel {
                color: white;
                border: 3px solid #3db39e;
            }
        """)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(160, 10, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("""
            QPushButton {
                border-radius: 10px;
                background-color: #3db39e;
                color: white;
            }
            QPushButton:hover {
                background-color: #3ca492;
            }
            QPushButton:pressed {
                background-color: #3d9888;
            }
        """)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame) #отсутствие рамки вокруг QLabel
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setLineWidth(1)
        self.label_3.setMidLineWidth(0)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)  #выравнивание по (AlignCenter — по центру по вертикали и горизонтали)
        self.label_3.setWordWrap(False)
        self.label_3.setOpenExternalLinks(False)
        self.label_3.setObjectName("label_3")
        # Добавляем кнопку Credit
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(380, 190, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("""
            QPushButton {
                border-radius: 10px;
                background-color: #3db39e;
                color: white;
            }
            QPushButton:hover {
                background-color: #3ca492;
            }
            QPushButton:pressed {
                background-color: #3d9888;
            }
        """)
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        #спарсим сигналы и слоты по именам
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Choose file"))
        self.pushButton_4.setText(_translate("MainWindow", "Credit"))
        self.pushButton_5.setText(_translate("MainWindow", "Pause Music"))
        self.pushButton_2.setText(_translate("MainWindow", "Find password"))
        self.label.setText(_translate("MainWindow", "Current file:"))
        self.label_4.setText(_translate("MainWindow", "None"))
        self.pushButton_3.setText(_translate("MainWindow", "X"))
        self.label_5.setText(_translate("MainWindow", "ExcelRecover"))
        self.checkBox.setText(_translate("MainWindow", "Digits"))
        self.checkBox_2.setText(_translate("MainWindow", "Special symbols"))
        self.checkBox_3.setText(_translate("MainWindow", "Latin"))
        self.label_3.setText(_translate("MainWindow", "None"))
