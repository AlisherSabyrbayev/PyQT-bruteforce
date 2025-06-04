import os
import subprocess
import sys
import hashlib
from PyQt5 import QtCore, QtGui, QtWidgets
from handler import ThreadHandler
from des import *
from database import Database
from audio import AudioPlayer


os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"
os.environ["QT_SCALE_FACTOR"] = "1"
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"


class AuthWindow(QtWidgets.QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Authorization")
        self.setFixedSize(400, 350)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint) # Удалеям стандартную и уродливую рамку окна (свернуть, развернуть, закрыть)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # Делаем фон окна прозрачным.
        self.center()

        # Стили
        self.central_widget = QtWidgets.QWidget(self)  #основной контейнер для всех элементов
        self.central_widget.setObjectName("AuthWidget")
        self.setCentralWidget(self.central_widget)
        self.setStyleSheet("""
            #AuthWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #1a1a1a, stop:0.5 #0d3b2a, stop:1 #1a1a1a);
                border-radius: 15px;
                border: 1px solid #3db39e;
            }

            QLabel {
                color: white;
                font-weight: bold;
                border: none;
                background: transparent;
                text-align: center;
            }

            QLineEdit {
                background: rgba(30, 30, 30, 160);
                color: white;
                border-radius: 10px;
                padding: 8px;
                border: 1px solid #3db39e;
                margin: 5px 30px;
                text-align: center;
            }

            QPushButton {
                background: #3db39e;
                color: white;
                border-radius: 10px;
                padding: 10px;
                min-width: 100px;
                border: none;
                margin: 5px 50px;
            }
            QPushButton:hover {
                background: #4ac7b0;
            }

            QTabWidget::pane {
                border: none;
                background: transparent;
            }
            QTabBar::tab {
                background: transparent;
                color: #aaaaaa;
                padding: 8px;
                border: none;
            }
            QTabBar::tab:selected {
                color: #3db39e;
                border-bottom: 2px solid #3db39e;
            }
        """)

        # Создаем вкладки
        self.tabs = QtWidgets.QTabWidget()
        self.tab_login = QtWidgets.QWidget()
        self.tab_register = QtWidgets.QWidget()

        #Оборачиваем
        self.tabs.addTab(self.tab_login, "Log-in")
        self.tabs.addTab(self.tab_register, "Registration")

        # Основной layout
        layout = QtWidgets.QVBoxLayout(self.central_widget)
        layout.addWidget(self.tabs)

        # Настраиваем вкладки (наполняем элементами)
        self.setup_login_tab()
        self.setup_register_tab()

        close_btn = QtWidgets.QPushButton("✕")
        close_btn.setFixedSize(30, 30)
        close_btn.setStyleSheet("""
            background: transparent;
            border: none;
            color: #3db39e;
            font-size: 18px;
        """)
        close_btn.move(self.width() - 40, 10)
        close_btn.clicked.connect(self.close)

    def setup_login_tab(self):
        layout = QtWidgets.QVBoxLayout(self.tab_login)
        layout.setContentsMargins(20, 20, 20, 20)

        self.login_input = QtWidgets.QLineEdit()
        self.login_input.setPlaceholderText("Login")

        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)

        login_btn = QtWidgets.QPushButton("Entry")
        login_btn.clicked.connect(self.handle_login)

        layout.addWidget(QtWidgets.QLabel("ExcelRecover Auth"))
        layout.addWidget(self.login_input)
        layout.addWidget(self.password_input)
        layout.addWidget(login_btn)

    def setup_register_tab(self):
        layout = QtWidgets.QVBoxLayout(self.tab_register)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setAlignment(QtCore.Qt.AlignCenter)

        self.reg_username = QtWidgets.QLineEdit()
        self.reg_username.setPlaceholderText("Login")

        self.reg_password = QtWidgets.QLineEdit()
        self.reg_password.setPlaceholderText("Password")
        self.reg_password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.reg_confirm = QtWidgets.QLineEdit()
        self.reg_confirm.setPlaceholderText("Repeat password")
        self.reg_confirm.setEchoMode(QtWidgets.QLineEdit.Password)

        register_btn = QtWidgets.QPushButton("Sign-up")
        register_btn.clicked.connect(self.handle_register)

        layout.addWidget(QtWidgets.QLabel("Create Account"))
        layout.addWidget(self.reg_username)
        layout.addWidget(self.reg_password)
        layout.addWidget(self.reg_confirm)
        layout.addWidget(register_btn)

    # --- ОБРАБОТЧИКИ ---
    def handle_login(self):
        username = self.login_input.text().strip()
        password = self.password_input.text().strip()

        if not username or not password:
            self.show_error("Fill in all the fields!")
            return

        if self.db.authenticate_user(username, password):
            self.main_window = MainWindow(self.db)
            self.main_window.show()
            self.close()
        else:
            self.show_error("Invalid login or password")

    def handle_register(self):
        username = self.reg_username.text().strip()
        password = self.reg_password.text().strip()
        confirm = self.reg_confirm.text().strip()

        if not username or not password or not confirm:
            self.show_error("Fill all fields!")
            return

        if password != confirm:
            self.show_error("Passwords don't match!")
            return

        if len(password) < 6:
            self.show_error("Password must be 6 characters or more")
            return

        if self.db.create_user(username, password):
            self.show_success("Registration successful! Now log in")
            self.tabs.setCurrentIndex(0)  # Переключаем на вкладку входа
            self.login_input.setText(username)  # удобная авто.подстановка логина
            self.password_input.clear()
        else:
            self.show_error("Login's already taken")

    def show_error(self, message):
        error_box = QtWidgets.QMessageBox()
        error_box.setIcon(QtWidgets.QMessageBox.Warning) # Иконка желтого треугольника
        error_box.setText(message)
        error_box.setWindowTitle("Error")
        error_box.exec_()  # Warning окно

    def show_success(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information) # Иконка синего круга
        msg.setText(message)
        msg.setWindowTitle("Success")
        msg.exec_()

    def center(self):
        qr = self.frameGeometry()  # Получаем геометрию окна (размеры и положение)
        cp = QtWidgets.QDesktopWidget().availableGeometry().center() # Центрируем
        qr.moveCenter(cp)  # Перенос центр окна в центр экрана
        self.move(qr.topLeft()) #   Перемещаем окно в новую позицию

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()  # Запоминаем позицию курсора при нажатии

    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint(event.globalPos() - self.oldPos) # Смещение курсора
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Инициализация аудиоплеера
        self.audio_player = AudioPlayer()
        self.audio_player.add_music("data/menu_music.mp3")
        self.audio_player.set_volume(50)
        self.audio_player.play()

        self.ui.pushButton_5.clicked.connect(self.toggle_pause)
        self.is_paused = False

        # размер главного меню
        self.setFixedSize(510, 240)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()

        # Css для гоавного меню
        self.ui.frame.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #1a1a1a, stop:0.5 #0d3b2a, stop:1 #1a1a1a);
                border-radius: 15px;
                border: 1px solid #3db39e;
            }
            QLabel {
                color: white;
                background: transparent;
                border: none;
            }
            QCheckBox {
                color: white;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #2d3534, stop:0.5 #3db39e, stop:1 #2d3534);
                color: white;
                border-radius: 10px;
                border: 1px solid #3db39e;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #3a4a45, stop:0.5 #4ac7b0, stop:1 #3a4a45);
            }
        """)

        # Инициализация Excel данных
        self.excel_file = None



        self.ui.pushButton_4.clicked.connect(self.show_credits)
        self.ui.pushButton_3.clicked.connect(self.close)
        self.ui.pushButton.clicked.connect(self.choose_file)
        self.ui.pushButton_2.clicked.connect(self.start_process)

        # Обработчик потока
        self.handler = ThreadHandler()
        self.handler.signal.connect(self.signal_handler)

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        # Минус музыка при закрытии окна
        self.audio_player.stop()
        event.accept()

    def toggle_pause(self):
        if self.is_paused:
            self.audio_player.player.play()
            self.ui.pushButton_5.setText("Pause Music")
        else:
            self.audio_player.player.pause()
            self.ui.pushButton_5.setText("Resume Music")
        self.is_paused = not self.is_paused

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def choose_file(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self)[0]  #берем только путь к файлу
        if file:
            self.excel_file = file
            self.ui.label_4.setText(os.path.basename(self.excel_file))

    def start_process(self):
        conf_list = [
            self.ui.checkBox.isChecked(),
            self.ui.checkBox_2.isChecked(),
            self.ui.checkBox_3.isChecked(),
        ]

        if self.excel_file:
            self.handler.filepath = self.excel_file
            self.handler.config = conf_list

            if any(conf_list):
                self.handler.start()
                self.ui.pushButton.setDisabled(True)
                self.ui.pushButton_2.setDisabled(True)
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Configuration must be set up")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "You must select a file")

    def signal_handler(self, value):
        if value[0] == "result":
            self.ui.label_3.setText(value[1])
            QtWidgets.QMessageBox.about(self, "Success",
                                        f"Password recovered: {value[1]}\nFile created: decrypted.xlsx")
            self.ui.pushButton.setDisabled(False)
            self.ui.pushButton_2.setDisabled(False)
        elif value[0] == "fail":
            self.ui.label_3.setText(value[1])

    def show_credits(self):
        credit_path = r"C:\Users\Alisher\Desktop\Project ExcelRecover\credit.txt"
        try:
            if os.path.exists(credit_path):
                if sys.platform == "win32":
                    os.startfile(credit_path)
                    # dariwn: для пользователей эйр мак супер мега макс ххд (Mac)
                    # xdg-opee - линукс
                else:
                    opener = "open" if sys.platform == "darwin" else "xdg-open"
                    subprocess.call([opener, credit_path])
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "credit.txt is not found. ")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", f"Failed to open file: {str(e)}")

#блок запуска
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    # Настройки HighDPI
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app.setStyle('Fusion')
    db = Database()
    if not db.conn:
        print("PostgreSQL 17 connection error!")
        sys.exit(1)

    font = QtGui.QFont()
    font.setFamily("Segoe UI")
    font.setPointSize(10)
    app.setFont(font)

    # Создаем и показываем окно авторизации
    auth_window = AuthWindow(db)
    auth_window.show()

    # Запуск Qt-приложения:
    sys.exit(app.exec_())