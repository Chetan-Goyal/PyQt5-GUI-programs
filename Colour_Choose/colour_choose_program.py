from PyQt5.QtWidgets import QApplication, QDialog, QColorDialog
from PyQt5.QtGui import QColor
import sys
from colour_choose import *

class myForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        col = QColor(0, 0, 0)
        mystr = 'QWidget { background-color: ' + col.name() + ' }'
        self.ui.frame.setStyleSheet(mystr)
        self.ui.label_2.setText(f'Code: {col.name()}')
        self.ui.colourpushbutton.clicked.connect(self.dispcolor)
        self.show()

    def dispcolor(self):
        col = QColorDialog.getColor()
        if col.isValid():
            mystr = 'QWidget { background-color: ' + col.name() + ' }'
            self.ui.frame.setStyleSheet(mystr)
            self.ui.label_2.setText(f'Code: {col.name()}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myForm()
    w.show()
    sys.exit(app.exec_())