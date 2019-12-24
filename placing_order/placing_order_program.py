import sys
from PyQt5.QtWidgets import QDialog, QApplication
from placing_order import *

# ** Main Tasks 
# TODO: 1. Updating all three LCD at time of deletion of one product
# TODO: 2. Testing
# TODO: 3. 0 qty list add should be 0 but it is for 1

class myForm(QDialog):
    cart_elements = {
        'Pasta Sauce':0,
        '2 x Oranges':0,
        'Lays Chips (Spicy)':0,
        'Coconut Biscuits':0
    }

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.add_product.clicked.connect(self.cart_add)
        # self.ui.edit.connect(self.cart_edit)
        self.ui.Del.clicked.connect(self.cart_delete)
        # self.ui.delete_all.connect(self.cart_delete_all)
        self.show()
    
    def cart_add(self):
        product_details = self.ui.CB.currentText()
        qty = self.ui.SB.value()
        price = float(product_details.split()[-1])
        cost = price*qty
        discount = round(price/10,2)*qty
        final_price = price - discount
        product_name = product_details.split('->')[0].strip()
        myForm.cart_elements[product_name] += qty
        qty = myForm.cart_elements[product_name]
        
        # if myForm.cart_elements[product_name] > 1:
        #     self.ui.cart.takeItem(self.ui.cart.item(0))
        list_record = f'{product_name}      {price}   {myForm.cart_elements[product_name]}    {price*myForm.cart_elements[product_name]}'
        self.cart_update(product_name, list_record)

        self.ui.cart.addItem(list_record)
        self.ui.LCD_total.display( self.ui.LCD_total.value() + cost)
        self.ui.LCD_discount.display(self.ui.LCD_discount.value() + discount)
        self.ui.LCD_to_pay.display(self.ui.LCD_to_pay.value() + final_price)

    def cart_update(self, product_name, record):
        product_names = myForm.cart_elements.keys()
        for index in range(self.ui.cart.count()):
            if self.ui.cart.item(index).text().split()[0] in product_name:
                self.ui.cart.setCurrentItem(record) # self.ui.cart.item(index).text())
                break
    
    def cart_delete(self):
        myForm.cart_elements[self.ui.cart.currentItem().text().split('  ')[0].strip()] = 0

        print(myForm.cart_elements)
        self.ui.cart.takeItem( self.ui.cart.currentRow() )
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myForm()
    w.show()
    sys.exit(app.exec_())