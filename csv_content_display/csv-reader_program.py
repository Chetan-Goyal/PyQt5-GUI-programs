from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from csv-reader_GUI import *
import sys
import csv

class myForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.addcontent()
    
    def addcontent(self):
        self.data = (
            ('Name', 'Class', 'Grade'),
            ('Chetan', '12', 'A'),
            ('Harsh', '11', 'D'),
            ('Arjun', '8', 'B')
        )

        # setting no of rows and columns in QTableWidget
        nor = noc = 0
        with open('data.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                noc = len(row)
                nor += 1

            self.ui.table.setRowCount(nor)
            self.ui.table.setColumnCount(noc)
            
        
        self.csv_file = open('data.csv')
        self.csv_reader = csv.reader(self.csv_file, delimiter=',')

        for row_index, record in enumerate(self.csv_reader):
            for col_index, item in enumerate(record):
                obj = QTableWidgetItem(item)
                self.ui.table.setItem(row_index, col_index, obj)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myForm()
    w.show()
    sys.exit(app.exec_())