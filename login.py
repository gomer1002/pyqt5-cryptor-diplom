import sqlite3
from PyQt5.QtWidgets import (
    QWidget,
    QFormLayout,
    QMessageBox,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont


class Login(QWidget):
    def getWidget(self, parent):
        # рисуем интерфейс
        self.setObjectName("Авторизация")
        self.block_size = QSize(422, 250)
        self.parent_widget = parent

        self.qle_name = QLineEdit()
        self.qle_name.setFocus()
        self.qle_name.setFont(self.get_font())
        self.qle_name.setPlaceholderText("Имя")

        self.qle_pass = QLineEdit()
        self.qle_pass.setFont(self.get_font())
        self.qle_pass.setEchoMode(QLineEdit.Password)
        self.qle_pass.setPlaceholderText("Пароль")

        # кнопки для перекоючения виджетов
        button1 = QPushButton("Войти", self, font=self.get_font())
        button1.clicked.connect(self.login)
        button2 = QPushButton("Регистрация", self, font=self.get_font())
        button2.clicked.connect(lambda: parent.display(1))

        f_layout = QFormLayout()
        f_layout.addRow(self.qle_name)
        f_layout.addRow(self.qle_pass)
        f_layout.addRow(button1)
        f_layout.addRow(button2)

        layout = QVBoxLayout()
        layout.addStretch()
        layout.addLayout(f_layout)
        layout.addStretch()
        self.setLayout(layout)
        return self

    def get_font(self, size=12):
        font = QFont()
        font.setPointSize(size)
        return font

    def login(self):
        user_login = self.qle_name.text()
        user_password = self.qle_pass.text()

        if len(user_login) == 0:
            return

        if len(user_password) == 0:
            return

        db = sqlite3.connect("database.db")
        cursor = db.cursor()
        cursor.execute(f'SELECT password FROM users WHERE login="{user_login}"')
        check_pass = cursor.fetchall()

        cursor.execute(f'SELECT login FROM users WHERE login="{user_login}"')
        check_login = cursor.fetchall()

        if check_pass[0][0] == user_password and check_login[0][0] == user_login:
            QMessageBox.about(self, "Message", "Успешная авторизация!")
            self.parent_widget.display(2)
        else:
            QMessageBox.about(self, "Message", "Ошибка авторизации!")
