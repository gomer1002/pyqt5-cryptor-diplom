import sys
import sqlite3
from PyQt5.QtWidgets import (
    QWidget,
    QStackedWidget,
    QHBoxLayout,
    QFormLayout,
    QLabel,
    QApplication,
    QPushButton,
    QVBoxLayout,
    QFrame,
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QSize, QRect, Qt

from login import Login
from register import Register
from poligon import Poligon
from material import Material

db = sqlite3.connect("database.db")
cursor = db.cursor()

# cursor.execute(
#     """CREATE TABLE IF NOT EXISTS users(
#     login TEXT,
#     password TEXT
# )"""
# )
# db.commit()

# for i in cursor.execute("SELECT * FROM users"):
#     print(i)


class stackedExample(QWidget):
    def __init__(self):
        super(stackedExample, self).__init__()

        self.title = "Учебное пособие - {}"

        self.stack_0 = Login().getWidget(self)
        self.stack_1 = Register().getWidget(self)
        self.stack_2 = QWidget()
        self.stack_3 = Poligon().getWidget(self)
        self.stack_4 = Material().getWidget(self)

        self.stack_2_ui()

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.stack_0)
        self.Stack.addWidget(self.stack_1)
        self.Stack.addWidget(self.stack_2)
        self.Stack.addWidget(self.stack_3)
        self.Stack.addWidget(self.stack_4)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)

        self.display(0)
        self.show()

    def stack_2_ui(self):
        self.stack_2.setObjectName("Главная")
        self.stack_2.block_size = QSize(422, 470)

        # добавляем кнопки в виджет
        button1 = QPushButton("Полигон", self, font=self.get_d_font())
        button1.clicked.connect(lambda: self.display(3))
        button1.setFixedHeight(40)
        button1.setFixedWidth(130)

        button2 = QPushButton("Материал", self, font=self.get_d_font())
        button2.clicked.connect(lambda: self.display(4))
        button2.setFixedHeight(40)
        button2.setFixedWidth(130)

        b_layout_r = QHBoxLayout()
        b_layout_r.setAlignment(Qt.AlignCenter)
        b_layout_r.addWidget(button1)
        b_layout_r.addWidget(button2)

        h_layout = QVBoxLayout()
        h_layout.addStretch()
        h_layout.addWidget(
            QLabel(
                "Добро пожаловать",
                alignment=Qt.AlignCenter,
                font=self.get_font(),
                geometry=QRect(90, 200, 251, 61),
            )
        )
        h_layout.addStretch()

        # создаем разделительную линию
        h_line = QFrame(
            self,
            frameShape=QFrame.HLine,
            frameShadow=QFrame.Sunken,
        )

        layout = QFormLayout()
        layout.addRow(b_layout_r)
        layout.addRow(h_line)
        layout.addRow(h_layout)

        self.stack_2.setLayout(layout)

    def display(self, i):
        # переключаем виджеты
        self.Stack.setCurrentIndex(i)
        self.setWindowTitle(self.title.format(self.Stack.currentWidget().objectName()))
        self.resize(self.Stack.currentWidget().block_size)

    def get_d_font(self, size=12):
        font = QFont()
        font.setPointSize(size)
        return font

    def get_font(self):
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        return font


def main():
    app = QApplication(sys.argv)
    ex = stackedExample()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
