from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from file_handling import *
import sys

class myForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionSave.triggered.connect(self.save_file)
        self.ui.actionExit.triggered.connect(self.exit_file)
        self.show()

    def open_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home', 'Text Files (*.txt)')
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.ui.textEdit.setText(data)
    
    def save_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fname = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        text = self.ui.textEdit.toPlainText()
        with open(fname[0], 'w') as f:
            f.write(text)
        

    def exit_file(self):
        sys.exit(0)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myForm()
    w.show()
    sys.exit(app.exec_())