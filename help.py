import pathlib

from PyQt5.QtWidgets import QTextBrowser, QMainWindow, QShortcut
from PyQt5.QtCore import Qt, QUrl
from MenuBar import MenuBar


class HelpWindow(QMainWindow):
    def __init__(self, text=None):
        super().__init__()
        self.browser = QTextBrowser()
        if text:
            self.browser.setText(text)
        self.setCentralWidget(self.browser)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setMinimumWidth(600)
        self.setMinimumHeight(400)
        self.shortcutClose = QShortcut('Ctrl+W', self)
        self.shortcutClose.activated.connect(self.close)

    def setSource(self, file):
        self.browser.setSource(file)


class HelpManager:
    def __init__(self, menubar: MenuBar):
        self.menubar = menubar

    def register(self, name: str, content: str):
        self.menubar.addAction(name, 'Help', lambda: self.show(name, content))

    def show(self, name, content):
        import os
        _file = str(pathlib.Path(__file__).parent / content)
        if not os.path.exists(_file):
            _file = str(pathlib.Path(__file__).parent / (content + '.md'))
        if not os.path.exists(_file):
            _file = str(pathlib.Path(__file__).parent / (content + '.html'))
        if not os.path.exists(_file):
            self.menubar.win = HelpWindow(content)
        else:
            self.menubar.win = HelpWindow()
            self.menubar.win.setSource(QUrl(_file))
        self.menubar.win.setWindowTitle(name)
        self.menubar.win.show()
