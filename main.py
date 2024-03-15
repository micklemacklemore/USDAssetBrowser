from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.mainwindow import Ui_MainWindow
import sys


class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui_mainwindow = Ui_MainWindow()
        self.ui_mainwindow.setupUi(self)
        self.setMinimumSize(1200, 800)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
