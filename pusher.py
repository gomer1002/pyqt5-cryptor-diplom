import sys
import json
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
    QTextEdit,
    QMessageBox,
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QSize, QRect, Qt
from pywebpush import webpush
from loguru import logger

VAPID_PRIVATE_KEY = "MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgupTx8wK5HzEl+pcAX/PpRAIu2Qmj0m19NGzupjcOCiKhRANCAATPCv2S4WqpcB8OdqDrsDmYsorwibuBlrqIlATcS0BWn17uD9n46eGzO/SBRxomMOSXi2W4NIUoOLjm38AzQs3L"


class stackedExample(QWidget):
    def __init__(self):
        super(stackedExample, self).__init__()

        self.title = "Учебное пособие - {}"

        self.stack_0 = QWidget()

        self.stack_0_ui()

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.stack_0)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)

        self.display(0)
        self.show()

    def stack_0_ui(self):
        self.stack_0.setObjectName("Главная")
        self.stack_0.block_size = QSize(500, 500)

        # добавляем кнопки в виджет
        button1 = QPushButton("Отправить", self, font=self.get_d_font())
        button1.clicked.connect(self.send_push)
        button1.setFixedHeight(40)
        button1.setFixedWidth(130)

        self.lbl = QLabel()
        h_layout = QVBoxLayout()
        h_layout.addStretch()
        h_layout.addWidget(button1)
        h_layout.addWidget(self.lbl)
        h_layout.addStretch()

        # создаем разделительную линию
        h_line = QFrame(
            self,
            frameShape=QFrame.HLine,
            frameShadow=QFrame.Sunken,
        )

        # Текстовое поле 1
        self.textPol_1 = QTextEdit(
            self,
            font=self.get_d_font(),
            geometry=QRect(10, 160, 301, 151),
            plainText=VAPID_PRIVATE_KEY,
        )
        # Текстовое поле 2
        self.textPol_2 = QTextEdit(
            self, font=self.get_d_font(), geometry=QRect(10, 160, 301, 151)
        )
        # Текстовое поле 3
        self.textPol_3 = QTextEdit(
            self, font=self.get_d_font(), geometry=QRect(10, 160, 301, 151)
        )

        layout = QFormLayout()
        layout.addRow("vapid", self.textPol_1)
        layout.addRow("token", self.textPol_2)
        layout.addRow("message", self.textPol_3)
        layout.addRow(h_line)
        layout.addRow(h_layout)

        self.stack_0.setLayout(layout)

    def display(self, i):
        # переключаем виджеты
        self.Stack.setCurrentIndex(i)
        self.setWindowTitle(self.title.format(self.Stack.currentWidget().objectName()))
        self.resize(self.Stack.currentWidget().block_size)

    def get_d_font(self, size=12):
        font = QFont()
        font.setPointSize(size)
        return font

    def send_push(self):
        try:
            self.lbl.setText("")
            vapid = self.textPol_1.toPlainText()
            token = self.textPol_2.toPlainText()
            message = self.textPol_3.toPlainText()
            message_data = {"message": message}
            logger.debug(f"vapid {vapid}")
            logger.debug(f"token {token}")
            logger.debug(f"message {message}")
            response = webpush(
                subscription_info=json.loads(token),
                data=json.dumps(message_data),
                vapid_private_key=vapid,
                vapid_claims={"sub": "mailto:chubaka1002@gmail.com"},
            )
            logger.debug(f"status {response.status_code}")
            self.lbl.setText(str(response.status_code))
        except Exception as e:
            QMessageBox.about(self, "Error", str(e))
            logger.error(str(e))

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
