from PyQt5.QtWidgets import QApplication, QDialog, QInputDialog
import sys
from country_choose import *

class myForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.choosepushbutton.clicked.connect(self.country_menu)
        self.show()
    
    def country_menu(self):
        countries = ( 'India', 'Unites Nations', 'United Kingdom', 'Bangladesh',
        'Pakistan', 'Russia', 'China')
        
        country, ok = QInputDialog.getItem(self, 'Country', 'List of Countries', countries, 0, False)
        
        self.ui.countrylineedit.setText(country)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myForm()
    w.show()
    sys.exit(app.exec_())