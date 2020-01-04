from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from login import *
import hashlib

def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.md5(password.encode())
    return salt.hexdigest()


# Sample Email and Password
_email = 'Sample@email.com'
_password = hash_password('v"N94Wk>m;HcQ')


class myForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.loginPushButton.clicked.connect(self.login_check)
        self.show()

    def login_check(self):
        email = self.ui.emailLineEdit.text()
        password = self.ui.passwordLineEdit.text()
        password_hashed = hash_password(password)

        if email == _email and password_hashed == _password:
            self.ui.resultLabel.setText('Login Successful')
        else:
            self.ui.resultLabel.setText('Invalid Email or password')
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myForm()
    w.show()
    sys.exit(app.exec_())        
