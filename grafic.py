import os
import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QLineEdit, QFileDialog, QMessageBox
from new import report
import argparse


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.edit = QLineEdit('Dima were here', self)
        self.edit.setGeometry(10, 10, 470, 30)
        self.btn_open = QPushButton('Открыть', self)
        self.btn_open.move(490, 10)
        self.btn_open.clicked.connect(self.buttonClicked)
        self.btn_graf = QPushButton('График', self)
        self.btn_graf.move(490, 50)
        self.btn_graf.clicked.connect(self.graf_click)
        self.btn_close = QPushButton('Close', self)
        self.btn_close.move(10, 50)
        self.btn_close.clicked.connect(self.close)
        self.setGeometry(300, 300, 600, 100)
        self.setWindowTitle('Event sender')
        self.status = self.statusBar()
        self.show()

    def buttonClicked(self):
        text = QFileDialog.getOpenFileName(self, 'Open file', '')
        self.edit.clear()
        self.edit.insert(text[0])
        self.status.showMessage(f'File: {text[0]}')

    def graf_click(self):
        self.status.showMessage('Создание графика на следующий месяц')
        result = report(self.edit.text(), self.status)
        if result:
            QMessageBox.information(self, 'График', 'Файл был создан', QMessageBox.Ok)


if __name__ == '__main__':
    grafic = argparse.ArgumentParser()
    grafic.add_argument('-link', help='Enter link to file from list families', type=str)
    arg = grafic.parse_args()
    link = arg.link
    if link:
        report(link)
    else:
        app = QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec_())