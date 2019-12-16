import sys
from PyQt5.QtWidgets import QDialog, QApplication
from user_data import *

class myForm(QDialog):
    # *          Name, Gender, Age
    result_data = ['',   ''  , ''] 
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.Submit.clicked.connect(self.dispmessage)
        self.ui.Male.toggled.connect(self.dispmessage)
        self.ui.Female.toggled.connect(self.dispmessage)
        self.ui.kid.toggled.connect(self.dispmessage)
        self.ui.teenager.toggled.connect(self.dispmessage)
        self.ui.adult.toggled.connect(self.dispmessage)
        self.show()
    
    def dispmessage(self):
        myForm.result_data[0] = self.ui.Name.text()

        if self.ui.Male.isChecked() :
            myForm.result_data[1] = 'Male'
        if self.ui.Female.isChecked() :
            myForm.result_data[1] = 'Female'
    
        if self.ui.kid.isChecked() :
            myForm.result_data[2] = 'Kid'
        if self.ui.teenager.isChecked() :
            myForm.result_data[2] = 'Teenager'
        if self.ui.adult.isChecked() :
            myForm.result_data[2] = 'adult'
    
        res = 'Name: ' + myForm.result_data[0] + '\nGender: ' + myForm.result_data[1] + '\nAge Group: ' + myForm.result_data[2]
        self.ui.Result.setText(res)
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = myForm()
    w.show()
    sys.exit(app.exec_())