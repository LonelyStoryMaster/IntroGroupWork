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

class ShoppingCart:
    def __init__(self, customer_name="none", current_date='January 1, 2016'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def __get_item_names(self):
        item_names = []
        for item in self.cart_items:
            item_names.append(item.item_name)
        # print(item_names)
        return item_names

    def __check_for_item(self, item_names, search_item):
        # print("Search Item: %s, Item Names: %s" % (search_item, item_names))
        if search_item in item_names:
            return True
        return False

    def __get_index_by_name(self, item_name):
        index = None
        for item in self.cart_items:
            if item_name == item.item_name:
                index = self.cart_items.index(item)
        return index

    def __print_cart_info(self):
        print("\n%s's Shopping Cart - %s" % (self.customer_name, self.current_date))

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, search_item):
        if self.__check_for_item(self.__get_item_names(), search_item):
            self.cart_items.pop(self.__get_index_by_name(search_item))
        else:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, ItemToPurchase):
        item_names = self.__get_item_names()
        if self.__check_for_item(item_names, ItemToPurchase.item_name):
            item_index = item_names.index(ItemToPurchase.item_name)
            if ItemToPurchase.item_description != None:
                self.cart_items[item_index].item_description = ItemToPurchase.item_description
            if ItemToPurchase.item_price != 0:
                self.cart_items[item_index].item_price = ItemToPurchase.item_price
            if ItemToPurchase.item_quantity != 0:
                self.cart_items[item_index].item_quantity = ItemToPurchase.item_quantity
        else:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_items = 0
        for item in self.cart_items:
            total_items += item.item_quantity
        return total_items
    
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.cost
        return total_cost

    def print_total(self):
        self.__print_cart_info()
        print("Number of Items: %d\n" % self.get_num_items_in_cart())
        for item in self.cart_items:
            item.print_item_cost()
        print("\nTotal: $%0.2f" % self.get_cost_of_cart())

    def print_descriptions(self):
        print()
        for item in self.cart_items:
            item.print_item_description()

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