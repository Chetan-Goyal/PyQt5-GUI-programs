import sys
from PyQt5.QtWidgets import QDialog, QApplication
from placing_order import *

class myForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.add_product.clicked.connect(self.cart_add)
        # self.ui.edit.connect(self.cart_edit)
        # self.ui.delete.connect(self.cart_delete)
        # self.ui.delete_all.connect(self.cart_delete_all)
        self.show()
    
    def cart_add(self):
        product = self.ui.CB.currentText()
        qty = self.ui.SB.value()
        price = float(product.split()[-1])
        discount = round(price/10,2)
        final_price = price - discount
        self.ui.cart.addItem(product)
        self.ui.LCD_total.display( self.ui.LCD_total.value() + price)
        self.ui.LCD_discount.display(self.ui.LCD_discount.value() + discount)
        self.ui.LCD_to_pay.display(self.ui.LCD_to_pay.value() + final_price)
      
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myForm()
    w.show()
    sys.exit(app.exec_())