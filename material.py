import os
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QTreeView,
    QSplitter,
    QFileSystemModel,
)

from PyQt5.QtGui import QFont
from PyQt5.QtCore import QDir, QSize


class Material(QWidget):
    def getWidget(self, parent):

        # устанавливаем название данного объекта
        self.setObjectName("Материал")
        self.setWindowTitle("Материал")

        # запоминаем родителя (для переходов между виджетами)
        self.parent_widget = parent
        self.block_size = QSize(1000, 500)

        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.rootPath())

        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(os.path.join(os.getcwd(), "Материал")))
        self.tree.doubleClicked.connect(self._on_double_clicked)
        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)

        self.textEdit = QTextEdit()

        splitter = QSplitter()
        splitter.addWidget(self.tree)
        splitter.addWidget(self.textEdit)
        splitter.setSizes([10, 350])

        button = QPushButton("Назад", self, font=self.get_font())
        button.clicked.connect(lambda: parent.display(2))
        button.setFixedWidth(130)

        main_layout = QVBoxLayout()
        main_layout.addWidget(splitter)
        main_layout.addWidget(button)

        self.setLayout(main_layout)
        return self

    def get_font(self, size=12):
        font = QFont()
        font.setPointSize(size)
        return font

    def _on_double_clicked(self, index):
        file_name = self.model.filePath(index)

        with open(file_name, encoding="utf-8") as f:
            text = f.read()
            self.textEdit.setPlainText(text)
