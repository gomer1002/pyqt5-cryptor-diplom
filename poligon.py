from PyQt5.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QFormLayout,
    QRadioButton,
    QLabel,
    QPushButton,
    QTextEdit,
    QFrame,
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRect, Qt, QSize

from cryptor import Cryptor


class Poligon(QWidget):
    def getWidget(self, parent):

        # устанавливаем название данного объекта
        self.setObjectName("Полигон")
        self.block_size = QSize(422, 470)

        # запоминаем родителя (для переходов между виджетами)
        self.parent_widget = parent

        # создаем словарь с радиокнопками
        self.radios = {
            "cyrillic": {
                "radio": QRadioButton("Кириллица", font=self.get_font(), checked=True),
                "index": 2,
            },
            "morze": {"radio": QRadioButton("Морзе", font=self.get_font()), "index": 0},
            "braile": {
                "radio": QRadioButton("Брайль", font=self.get_font()),
                "index": 1,
            },
        }

        # добавляем радиокнопки в виджет
        b_layout_r = QHBoxLayout()
        b_layout_r.setAlignment(Qt.AlignCenter)
        b_layout_r.addWidget(self.radios["cyrillic"]["radio"])
        b_layout_r.addWidget(self.radios["morze"]["radio"])
        b_layout_r.addWidget(self.radios["braile"]["radio"])

        # кнопки для перекоючения виджетов
        button1 = QPushButton("Пуск", self, font=self.get_font())
        button1.clicked.connect(self.encode)
        button2 = QPushButton("Очистить", self, font=self.get_font())
        button2.clicked.connect(self.clear)
        button3 = QPushButton("Перекинуть", self, font=self.get_font())
        button3.clicked.connect(self.move)
        button4 = QPushButton("Назад", self, font=self.get_font())
        button4.clicked.connect(lambda: parent.display(2))

        # добавляем кнопки в виджет
        b_layout_b = QHBoxLayout()
        b_layout_b.addWidget(button1)
        b_layout_b.addWidget(button2)
        b_layout_b.addWidget(button3)

        # Текстовое поле 1
        self.textPol_1 = QTextEdit(
            self, font=self.get_font(), geometry=QRect(10, 160, 301, 151)
        )
        # Текстовое поле 2
        self.textPol_2 = QTextEdit(
            self, font=self.get_font(), geometry=QRect(10, 160, 301, 151)
        )

        # создаем заголовок виджета
        poly_label = QLabel("Полигон", font=self.get_font(18), alignment=Qt.AlignCenter)

        # создаем разделительную линию
        h_line = QFrame(
            self,
            frameShape=QFrame.HLine,
            frameShadow=QFrame.Sunken,
        )

        # добавляем все что насоздавали в интерфейс
        layout = QFormLayout()
        layout.addRow(poly_label)
        layout.addRow(h_line)
        layout.addRow(b_layout_r)
        layout.addRow(b_layout_b)
        layout.addRow(self.textPol_1)
        layout.addRow(self.textPol_2)
        layout.addRow(button4)

        self.setLayout(layout)
        # возвращаем собранный виджет
        return self

    def get_font(self, size=12):
        font = QFont()
        font.setPointSize(size)
        return font

    def encode(self):
        # определяем выбранный режим кодирования
        mode = 0
        for key in self.radios.keys():
            if self.radios[key]["radio"].isChecked():
                mode = self.radios[key]["index"]
        # записываем исходный текст в переменную удаляя все переносы на новую строку
        # и переводя символы в нижний регистр
        textPol_1_data = self.textPol_1.toPlainText()
        s = textPol_1_data.replace("\n", "").lower()
        # осуществляем кодировку-перевод текста согласно выбранной кодировке

        ans = Cryptor.encode(s, mode)
        # очищаем и заполняем второе текстовое поле
        self.textPol_2.setPlainText(ans)

    def clear(self):
        self.textPol_1.clear()
        self.textPol_2.clear()

    def move(self):
        textPol_2_data = self.textPol_2.toPlainText()
        self.textPol_1.setPlainText(textPol_2_data)
        self.textPol_2.setPlainText("")
