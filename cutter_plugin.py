import cutter

from PySide2.QtCore import QObject, SIGNAL
#from PySide2.QtWidgets import QAction, QLabel, QPushButton, QLineEdit, QPlainTextEdit, QFileDialog
from PySide2.QtWidgets import *


class MyDockWidget(cutter.CutterDockWidget):
    def __init__(self, parent, action):
        super(MyDockWidget, self).__init__(parent, action)
        self.setObjectName("Note")
        self.setWindowTitle("Take note plugin")

        self._label = QLabel(self)
        self.setWidget(self._label)


        QObject.connect(cutter.core(), SIGNAL("seekChanged(RVA)"), self.update_contents)
        self.update_contents()

    def update_contents(self):
        self.button = QPushButton('Open a txt file', self)
        self.button.move(120,410)
        self.button.clicked.connect(self.openfile)



        self.lineEntry = QTextEdit(self)
        self.lineEntry.move(0,410)
        self.lineEntry.resize(120,30)
        self.lineEntry.insertPlainText("FILE PATH")


        self.b = QPlainTextEdit(self)
        self.b.resize(300,400)

    def openfile(self):
        dir_ = QFileDialog.getOpenFileName(self, "Select File", "", filter="*.txt")
        print(dir_[0])
        self.lineEntry.insertPlainText(dir_[0])
        data = open(dir_[0], "r")
        self.b.insertPlainText(data.read())

    




class MyCutterPlugin(cutter.CutterPlugin):
    name = "Take Note"
    description = "You can take note when you are using cutter and you can open other txt file."
    version = "1.0"
    author = "Deucalion"

    def setupPlugin(self):
        pass

    def setupInterface(self, main):
        action = QAction("My Plugin", main)
        action.setCheckable(True)
        widget = MyDockWidget(main, action)
        main.addPluginDockWidget(widget, action)

    def terminate(self):
        pass

def create_cutter_plugin():
    return MyCutterPlugin()