import sys
from PyQt5.QtWidgets import QDialog, QApplication
from GUI import *

class myForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.SB.valueChanged.connect(self.SB_nomove)
        self.ui.DSB.valueChanged.connect(self.DSB_nomove)
        self.ui.HS.actionTriggered.connect(self.HS_nomove)
        self.ui.VS.actionTriggered.connect(self.VS_nomove)
        self.ui.HSB.actionTriggered.connect(self.HSB_nomove)
        self.ui.VSB.actionTriggered.connect(self.VSB_nomove)

    def SB_nomove(self):
        value = self.ui.SB.value()
        self.ui.DSB.setValue(float(value))
        self.ui.HS.setValue(value)
        self.ui.VS.setValue(value)
        self.ui.HSB.setValue(value)
        self.ui.VSB.setValue(value)
        self.ui.Result.setText('Result: {}'.format(value))

    def DSB_nomove(self):
        value = int(self.ui.DSB.value())
        self.ui.SB.setValue(value)
        self.ui.HS.setValue(value)
        self.ui.VS.setValue(value)
        self.ui.HSB.setValue(value)
        self.ui.VSB.setValue(value)
        self.ui.Result.setText('Result: {}'.format(value))
    
    def HS_nomove(self):
        value = self.ui.HS.value()
        self.ui.SB.setValue(float(value))
        self.ui.DSB.setValue(value)
        self.ui.VS.setValue(value)
        self.ui.HSB.setValue(value)
        self.ui.VSB.setValue(value)
        self.ui.Result.setText('Result: {}'.format(value))
    
    def VS_nomove(self):
        value = self.ui.VS.value()
        self.ui.SB.setValue(float(value))
        self.ui.DSB.setValue(value)
        self.ui.HS.setValue(value)
        self.ui.HSB.setValue(value)
        self.ui.VSB.setValue(value)
        self.ui.Result.setText('Result: {}'.format(value))
    
    def HSB_nomove(self):
        value = self.ui.HSB.value()
        self.ui.SB.setValue(float(value))
        self.ui.DSB.setValue(value)
        self.ui.HS.setValue(value)
        self.ui.VS.setValue(value)
        self.ui.VSB.setValue(value)
        self.ui.Result.setText('Result: {}'.format(value))
    
    def VSB_nomove(self):
        value = self.ui.VSB.value()
        self.ui.SB.setValue(float(value))
        self.ui.DSB.setValue(value)
        self.ui.HS.setValue(value)
        self.ui.VS.setValue(value)
        self.ui.HSB.setValue(value)
        self.ui.Result.setText('Result: {}'.format(value))
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myForm()
    w.show()
    sys.exit(app.exec_())