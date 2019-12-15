import sys
from PyQt5.QtWidgets import QDialog, QApplication
from age_group import *

class myForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.kid.toggled.connect(self.dispResult)
        self.ui.teenager.toggled.connect(self.dispResult)
        self.ui.adult.toggled.connect(self.dispResult)
        self.show()

    def dispResult(self):
        age = ''
        if self.ui.kid.isChecked() :
            age = 'Kid'
        elif self.ui.teenager.isChecked() :
            age = 'Teenager'
        elif self.ui.adult.isChecked() :
            age = 'Adult'
        
        self.ui.Result.setText('You are ' + age)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myForm()
    w.show()
    sys.exit(app.exec_())