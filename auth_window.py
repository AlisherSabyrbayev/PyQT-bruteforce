# from PyQt5 import QtCore, QtWidgets, QtGui
#
#
# class AuthWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Authorization")
#         self.setFixedSize(300, 200)
#         self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
#         self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
#
#         self.setStyleSheet("""
#             QMainWindow {
#                 background-color: rgba(57, 67, 65, 0.9);
#                 border-radius: 15px;
#             }
#             QLabel {
#                 color: white;
#                 font-weight: bold;
#             }
#             QLineEdit {
#                 background-color: #2d3534;
#                 color: white;
#                 border-radius: 10px;
#                 padding: 8px;
#                 border: 1px solid #3db39e;
#             }
#             QPushButton {
#                 background-color: #3db39e;
#                 color: white;
#                 border-radius: 10px;
#                 padding: 8px;
#                 font-weight: bold;
#             }
#             QPushButton:hover {
#                 background-color: #3ca492;
#             }
#         """)
#
#         # Центральный виджет
#         central_widget = QtWidgets.QWidget()
#         self.setCentralWidget(central_widget)
#
#         # Layout
#         layout = QtWidgets.QVBoxLayout()
#         central_widget.setLayout(layout)
#
#         # Заголовок
#         title = QtWidgets.QLabel("ExcelRecover Auth")
#         title.setAlignment(QtCore.Qt.AlignCenter)
#         title.setStyleSheet("font-size: 16px;")
#         layout.addWidget(title)
#
#         # Поля ввода
#         self.login_input = QtWidgets.QLineEdit()
#         self.login_input.setPlaceholderText("Login")
#         layout.addWidget(self.login_input)
#
#         self.password_input = QtWidgets.QLineEdit()
#         self.password_input.setPlaceholderText("Password")
#         self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
#         layout.addWidget(self.password_input)
#
#         # Кнопка входа
#         login_btn = QtWidgets.QPushButton("Enter")
#         login_btn.clicked.connect(self.check_credentials)
#         layout.addWidget(login_btn)
#
#         # Кнопка закрытия
#         close_btn = QtWidgets.QPushButton("X")
#         close_btn.setFixedSize(30, 30)
#         close_btn.clicked.connect(self.close)
#         close_btn.move(self.width() - 40, 10)
#
#         # Учетные данные (временное решение)
#         self.valid_credentials = {
#             "admin": "admin123",
#             "user": "password123"
#         }
#
#     def mousePressEvent(self, event):
#         self.oldPos = event.globalPos()
#
#     def mouseMoveEvent(self, event):
#         delta = QtCore.QPoint(event.globalPos() - self.oldPos)
#         self.move(self.x() + delta.x(), self.y() + delta.y())
#         self.oldPos = event.globalPos()
#
#     def check_credentials(self):
#         login = self.login