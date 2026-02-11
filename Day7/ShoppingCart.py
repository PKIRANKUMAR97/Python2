# Q6. Shopping Cart
# Constructor → empty cart
# Method → add_item(item, price)
# Method → remove_item(item)
# Method → total_price()

class Cart:
    def __init__(self):
        self.cart={}


    def add_item(self,item,price):
        self.cart[item]=price
        print(f"added {item} - price: {price} to cart")

    def remove_item(self,item):
        if item in self.cart:
            removed_item = self.cart.pop(item)
        else :
            print("Item not in cart")



    def total_price(self):
        total = sum(self.cart.values())
        return total


cart_obj = Cart()
cart_obj.add_item("novo1",2300)
cart_obj.add_item("novo2",2800)
cart_obj.remove_item("novo2")
print(cart_obj.total_price())




