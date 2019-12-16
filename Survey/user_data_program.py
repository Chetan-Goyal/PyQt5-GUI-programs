+|from PyQt5.QtWidgets import QDialog, QApplication
from user_data import *

class myForm(QDialog):
    # *                   Name  Gender  Age
    result_data = [None, None  , None] 
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
        self.dispmessage()
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
    
        print((myForm.result_data[0]))

        if myForm.result_data[0]:
            if ( not myForm.result_data[1] and not myForm.result_data[2] ):
                self.ui.Result.setText('Hi ' + myForm.result_data[0])
            elif ( myForm.result_data[1] and not myForm.result_data[2] ):
                self.ui.Result.setText('Hi ' + myForm.result_data[0] + ',\n' + 'You are ' + myForm.result_data[1])
            elif ( not myForm.result_data[1] and  myForm.result_data[2] ):
                self.ui.Result.setText('Hi ' + myForm.result_data[0] + ',\n' + 'You are ' + myForm.result_data[2])
            elif (  myForm.result_data[1] and  myForm.result_data[2] ):
                self.ui.Result.setText('Hi ' + myForm.result_data[0] + ',\n' +\
                     'You are ' + myForm.result_data[1] +\
                         ' and ' + myForm.result_data[2] )
        if not myForm.result_data[0]:
            if ( myForm.result_data[1] and not myForm.result_data[2] ):
                self.ui.Result.setText('You are ' + myForm.result_data[1])
            elif ( not myForm.result_data[1] and  myForm.result_data[2] ):
                self.ui.Result.setText('You are ' + myForm.result_data[2])
            elif (  myForm.result_data[1] and  myForm.result_data[2] ):
                self.ui.Result.setText('You are ' + myForm.result_data[1] + ' and ' + myForm.result_data[2] )

        if myForm.result_data[1]:
            self.ui.Result.setText('Hi ' + myForm.result_data[0])
        
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = myForm()
    w.show()
    sys.exit(app.exec_())