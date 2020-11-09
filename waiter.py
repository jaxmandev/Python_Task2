# import the parent class
from menu import Menu

# inititate child class
# import from parent
class Waiter(Menu):
        def __init__(self):
            super().__init__()
            self.order = [] # variable unique to this child
            self.bill = [] # to accumulate the price of each selection

        # ask customer his desire: 1-see menu, 2-order, 3-review order, and 4-validate order
        def ordering(self):
            while True:
                choice = int(input("\n 1 --> Show menu\n 2 --> Add to order\n 3 --> Show order\n 4 --> Satisfied with order\n --> "))
                
                # print the menu from parent class
                if choice == 1:
                    for dish, price in self.menu.items():
                        print(f'The {dish} for £ {price}.')

                # add the input to order list while checking it exists
                # add the item's price to the bill list
                elif choice == 2:
                    add_to_menu = input("--> ").title()
                    if add_to_menu in self.menu.items():
                        self.order.append(add_to_menu)
                        for i in self.order:
                            for j in self.menu:
                                if i == j:
                                    self.bill.append(self.menu[j])
                                else:
                                    continue
                        bill = sum(bill)
                    else:
                        print("Your order is not in menu, have another look at the menu if necessary.")
                
                # view the items ordered so far
                elif choice == 3:
                    print("\n So far you have ordered: ")
                    print(self.order)
                
                # view the order total price
                elif choice == 4:
                    print("Thank you for ordering and enjoy the food! ")
                    print(f"Current order adds up to £ {bill}" )

# create an instance of the Waiter class
test1 = Waiter()

# start the ordering function which will ask user for input 
print(test1.ordering())

