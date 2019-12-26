import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import Qt
from placing_order import *

class myForm(QDialog):
    cart_elements = {
        'Pasta Sauce            ':0,
        '2 x Oranges            ':0,
        'Lays Chips (Spicy)     ':0,
        'Coconut Biscuits       ':0
    }

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.add_product.clicked.connect(self.cart_add)
        self.ui.edit.clicked.connect(self.cart_edit)
        self.ui.Del.clicked.connect(self.cart_delete)
        self.ui.Del_all.clicked.connect(self.cart_delete_all)
        self.show()
    
    def cart_add(self):
        product_details = self.ui.CB.currentText().partition('-> $ ')
        qty = self.ui.SB.value()

        if not qty:        # checking if no item has to be added in list(when quantity = 0)
            return None

        price = float(product_details[-1])
        cost = price*qty
        discount = round((price/10)*qty,2)
        final_price = cost - discount
        product_name = product_details[0]
        myForm.cart_elements[product_name] += qty
        new_qty = myForm.cart_elements[product_name]
        
        # Deletes old record if same item is added again
        if myForm.cart_elements[product_name] > new_qty-qty:
            old_list_record = f'{product_name}{price}   {new_qty-qty}      {(new_qty-qty)*price}'
            for i in range(self.ui.cart.count()): # finding index of old record in list
                if self.ui.cart.item(i).text() == old_list_record:
                    self.ui.cart.takeItem(i)  # deleting old list item at found position
                    break
        
        # List with updated details
        list_record = f'{product_name}{price}   {myForm.cart_elements[product_name]}      {price*myForm.cart_elements[product_name]}'

        # Adding Item in list and updating total,display and pay lcd counter 
        self.ui.cart.addItem(list_record)
        self.ui.LCD_total.display( self.ui.LCD_total.value() + cost)
        self.ui.LCD_discount.display(self.ui.LCD_discount.value() + discount)
        self.ui.LCD_to_pay.display(self.ui.LCD_to_pay.value() + final_price)


    def cart_edit(self):
        cart_item = self.ui.cart.currentItem().text()

        self.ui.SB.setValue(int(cart_item.split()[-2]))

        item = cart_item[:23] + '-> $ ' + cart_item.split()[-3]
        index = self.ui.CB.findText(item, Qt.MatchFixedString)
        if index >= 0:
            self.ui.CB.setCurrentIndex(index)

        self.cart_delete()


    def cart_delete(self):
        cart_item = self.ui.cart.currentItem().text().split()
        total_price = float(cart_item[-1])

        total = round( self.ui.LCD_total.value() - total_price, 2)
        discount = round(self.ui.LCD_discount.value() - total_price*0.1, 2)
        to_pay = round(self.ui.LCD_to_pay.value() - total_price*0.9, 2)

        # setting quantity of current item in our dictionary to zero
        myForm.cart_elements[self.ui.cart.currentItem().text()[0:23]] = 0
        
        # deleting current item from list
        self.ui.cart.takeItem( self.ui.cart.currentRow() )

        # Updating values in all LCD
        if self.ui.cart.count() == 0:
            total = discount = to_pay = 0
        self.ui.LCD_total.display(total)
        self.ui.LCD_discount.display(discount)
        self.ui.LCD_to_pay.display(to_pay)


    def cart_delete_all(self):
        self.ui.cart.clear()
        self.ui.LCD_total.display(0)
        self.ui.LCD_discount.display(0)
        self.ui.LCD_to_pay.display(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myForm()
    w.show()
    sys.exit(app.exec_())