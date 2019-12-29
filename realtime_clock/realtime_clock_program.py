from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QTimer, QTime
from realtime_clock import *
import sys

class myForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        timer = QTimer(self)
        timer.timeout.connect(self.clock_update)
        timer.start(1000)
        self.clock_update()
    
    def clock_update(self):
        time = QTime.currentTime()
        time = time.toString('hh:mm:ss')
        self.ui.clock.display(time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myForm()
    w.show()
    sys.exit(app.exec_())