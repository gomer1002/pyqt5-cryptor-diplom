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


class Register(QWidget):
    def getWidget(self, parent):
        # рисуем интерфейс
        self.setObjectName("Регистрация")
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
        button1 = QPushButton("Зарегистрироваться", self, font=self.get_font())
        button1.clicked.connect(self.register)
        button2 = QPushButton("Вход", self, font=self.get_font())
        button2.clicked.connect(lambda: parent.display(0))

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

    def register(self):
        user_login = self.qle_name.text()
        user_password = self.qle_pass.text()

        if len(user_login) == 0:
            return

        if len(user_password) == 0:
            return

        db = sqlite3.connect("database.db")
        cursor = db.cursor()
        cursor.execute(f'SELECT login FROM users WHERE login="{user_login}"')
        if cursor.fetchone() is None:
            cursor.execute(
                f'INSERT INTO users VALUES ("{user_login}", "{user_password}")'
            )
            QMessageBox.about(
                self, "Message", f"Аккаунт {user_login} успешно зарегистрирован!"
            )
            db.commit()
        else:
            QMessageBox.about(self, "Message", "Такая записать уже имеется!")
