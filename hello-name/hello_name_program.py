import sys
from PyQt5.QtWidgets import QDialog, QApplication
from hello_name import *
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.SubmitButton.clicked.connect(self.dispmessage)
        self.show()
    def dispmessage(self):
        self.ui.FinalOutput.setText("Hello " + self.ui.Response.text())


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())