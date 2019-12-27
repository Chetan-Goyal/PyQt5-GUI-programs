import sys
from PyQt5.QtWidgets import QDialog, QApplication
from font_changer import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.font.currentFontChanged.connect(self.font_change)
    
    def font_change(self):
        my_font = QtGui.QFont(self.ui.font.itemText(self.ui.font.currentIndex()), 14)
        self.ui.output.setFont(my_font)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())