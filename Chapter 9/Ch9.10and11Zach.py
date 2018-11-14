#9.10
class ItemToPurchase:
    def __init__ (self, name='none', price=0, quantity=0, total=0, description = 'none'):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_total = total
        #9.11
        self.item_description = description
    #9.10
    def print_item_cost(self):
        self.total = self.item_quantity * self.item_price
        print('%s %d @ $%d = $%d' % (self.item_name, self.item_quantity, self.item_price, self.total))


    #9.11
    def print_item_description(self):
        print('%s: %s' % (self.item_name, self.item_description))

#9.11
class ShoppingCart:
    def __init__(self, name='none', date='January 1,2016'):
        self.customer_name = name
        self.current_date = date
        self.cart_items = []

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self):
        for x in self.cart_items
            if self.name == x:
                self.cart_items.remove(self.name)
            else:
                continue

    def modify_items(self):
        pass
        
    def get_num_items_in_cart(self):
        num_items = len(self.cart_items)
        print('Number of Items: %d' % num_items)

    def cost_of_cart(self):
        
if __name__ == "__main__":

    item_cart = ShoppingCart(name, date)
    
    print('Item 1')
    name = input('Enter the item name:\n')
    price = float(input('Enter the item price:\n'))
    quantity = int(input('Enter the item quantity:\n'))
    description = input('Enter item description\n')
    date = input('Enter item date\n')
    price = int(price)
    total = price * quantity
    total1 = price * quantity
    item1 = ItemToPurchase(name, price, quantity, total)
    item_cart.add_item(item1)
    print()
    
    
    print('Item 2')
    name = input('Enter the item name:\n')
    price = float(input('Enter the item price:\n'))
    quantity = int(input('Enter the item quantity:\n'))
    description = input('Enter item description\n')
    price = int(price)
    total = price * quantity
    total2 = price * quantity
    item2 = ItemToPurchase(name, price, quantity, total, description)
    
    
    print()
    print('TOTAL COST')   
    item1.print_item_cost()
    item1.print_item_description()
    item2.print_item_cost()
    item2.print_item_description()
    
    print()
    print('Total: $%d' % (total1 + total2))
    
