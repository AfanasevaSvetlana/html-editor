import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QLineEdit, QTextBrowser, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt


class EditorHTML(QWidget):
    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        self.lineedit = QLineEdit()
        self.lineedit.returnPressed.connect(self.click)

        self.qtb = QTextBrowser()
        self.qtb.setAcceptRichText(True)
        self.qtb.setOpenExternalLinks(True)

        self.clear_btn = QPushButton('Clear')
        self.clear_btn.pressed.connect(self.textClear)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lineedit, 0)
        vbox.addWidget(self.qtb, 1)
        vbox.addWidget(self.clear_btn, 2)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('HTML-Editor')
        self.show()

    def click(self):
        text = self.lineedit.text()
        self.qtb.append(text)
        self.lineedit.clear()

    def textClear(self):
        self.qtb.clear()

    def keyPressEvent(self, event):
        line = self.qtb.toPlainText().split('\n')
        if event.key() == Qt.Key_Up:
            self.le.setText(str(line[0]))
        elif event.key() == Qt.Key_Down:
            self.lineedit.setText(str(line[len(line) - 1]))

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            'Exit',
            "Are you sure to quit?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No)
        if reply == QMessageBox.Yes:
            app.exec_()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EditorHTML()
    sys.exit(app.exec_())

