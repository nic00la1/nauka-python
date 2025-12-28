from cart import *

phone1 = Phone("Iphone 16 Pro", 5600, "White")
tv1 = TV("TV Y", 2000, 65)
cart1 = Cart()
cart1.addProduct(phone1)
cart1.addProduct(tv1)
cart1.addProduct(tv1)
cart1.addProduct("test")
print(cart1)