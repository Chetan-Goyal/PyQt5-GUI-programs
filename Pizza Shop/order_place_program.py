import sys
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from order_place import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.regular.toggled.connect(self.dispAmount)
        self.ui.medium.toggled.connect(self.dispAmount)
        self.ui.large.toggled.connect(self.dispAmount)
        self.ui.EC.stateChanged.connect(self.dispAmount)
        self.ui.TB.stateChanged.connect(self.dispAmount)
        self.ui.CLC.stateChanged.connect(self.dispAmount)
        self.ui.HTB.stateChanged.connect(self.dispAmount)
        self.show()

    def dispAmount(self):
        amount = 0
        if self.ui.regular.isChecked() == True:
            amount += 3.99
        elif self.ui.medium.isChecked() == True:
            amount += 6.99
        elif self.ui.large.isChecked() == True:
            amount += 8.49

        if self.ui.EC.isChecked() == True:
            amount += 0.99
        if self.ui.TB.isChecked() == True:
            amount += 1.49
        if self.ui.CLC.isChecked() == True:
            amount += 2.99
        if self.ui.HTB.isChecked() == True:
            amount += 0.49
        
        self.ui.Result.setText("Total Amount to be Paid: $ {}".format(round(amount, 2)))


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())