import sys
from PyQt5.QtWidgets import QDialog, QApplication
from basic_calculator import *

class myForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.plus.clicked.connect(self.add)
        self.ui.minus.clicked.connect(self.minus)
        self.ui.mul.clicked.connect(self.mul)
        self.ui.div.clicked.connect(self.div)
        self.show()

    def add(self):
        text = ''
        
        if  self.ui.num1.text() == '' or self.ui.num2.text() == '':
            text = 'Values Not Found'
        else:
            text = str( int(self.ui.num1.text()) + int(self.ui.num2.text()) )
            text = 'Result: {}'.format(text)
        self.ui.Result.setText(text)

    def minus(self):
        text = ''
        if  self.ui.num1.text() == '' or self.ui.num2.text() == '':
            text = 'Values Not Found'
        else:
            text = str( int(self.ui.num1.text()) - int(self.ui.num2.text()) )
            text = 'Result: {}'.format(text)
        self.ui.Result.setText(text)

    def mul(self):
        text = ''
        if  self.ui.num1.text() == '' or self.ui.num2.text() == '':
            text = 'Values Not Found'
        else:
            text = str( int(self.ui.num1.text()) * int(self.ui.num2.text()) )
            text = 'Result: {}'.format(text)
        self.ui.Result.setText(text)

    def div(self):
        text = ''
        if  self.ui.num1.text() == '' or self.ui.num2.text() == '':
            text = 'Values Not Found'
        else:
            if not int(self.ui.num2.text()):
                text = ''' Divisor shouldn't be zero'''
            else:
                text = str( int(self.ui.num1.text()) / int(self.ui.num2.text()) )
                text = 'Result: {}'.format(text)
        self.ui.Result.setText(text)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myForm()
    w.show()
    sys.exit(app.exec_())