import FoodClass as fc

customer_id = int(input('Enter your customer ID: '))

customer1 = fc.Customer(570, 'Danni Sellyar', '97 Mitchell Way Hewitt Texas 76712',
                        'dsellyarft@gmpg.org', '254-555-9362', False)
customer2 = fc.Customer(569, 'Aubree Himsworth', '1172 Moulton Hill Waco Texas 76710',
                        'ahimsworthfs@list-manage.com', '254-555-2273', True)

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {'trans1': ['2/15/2023', 'The Lone Patty', 17, 569],
        'trans2': ['2/15/2023', 'The Octobreakfast', 18, 569],
        'trans3': ['2/15/2023', 'The Octoveg', 16, 570],
        'trans4': ['2/15/2023', 'The Octoburger', 20, 570],
        }

# all transaction from dictionary
trans1 = fc.Transaction(dict['trans1'], 'The Lone Patty', 17, 569)
trans2 = fc.Transaction(dict['trans2'], 'The Octobreakfast', 18, 569)
trans3 = fc.Transaction(dict['trans3'], 'The Octoveg', 16, 570)
trans4 = fc.Transaction(dict['trans4'], 'The Octoburger', 20, 570)

order_total = 0

# displaying first part of customer
if customer1.get_id() == customer_id:
    print('Customer Name: ', customer1.get_name())
    print('Phone: ', customer1.get_phone_number())
    if customer1.get_member_status == True:
        cost1 = trans3.get_cost()
        discount1 = float(cost1 * 0.2)
        new_cost1 = float(cost1 - discount1)
        cost2 = trans4.get_cost()
        discount2 = float(cost2 * 0.2)
        new_cost2 = float(cost2 - discount2)
        total_cost = new_cost1 + new_cost2
        print('Order Item: ', trans3.get_item_name(), "Price: $", new_cost1)
        print('Order Item: ', trans4.get_item_name(), "Price: $", new_cost2)
        print('Total Cost: ', total_cost)
    else:
        print('Order Item: ', trans3.get_item_name(),
              'Price: ', trans3.get_cost())
        print('Order Item: ', trans4.get_item_name(),
              'Price: ', trans4.get_cost())
        total_cost = trans3.get_cost() + trans4.get_cost()
        print('Total Cost: ', total_cost)

if customer2.get_id() == customer_id:
    print('Customer Name: ', customer2.get_name())
    print('Phone: ', customer2.get_phone_number())
    if customer2.get_member_status == True:
        cost3 = trans1.get_cost()
        discount3 = float(cost3 * 0.2)
        new_cost3 = float(cost3 - discount1)
        cost4 = trans2.get_cost()
        discount4 = float(cost4 * 0.2)
        new_cost4 = float(cost4 - discount4)
        total_cost = new_cost3 + new_cost4
        print('Order Item: ', trans1.get_item_name(), "Price: $", new_cost3)
        print('Order Item: ', trans2.get_item_name(), "Price: $", new_cost4)
        print('Total Cost: ', total_cost)
    else:
        print('Order Item: ', trans1.get_item_name(),
              'Price: ', trans1.get_cost())
        print('Order Item: ', trans2.get_item_name(),
              'Price: ', trans2.get_cost())
        total_cost = trans1.get_cost() + trans2.get_cost()
        print('Total Cost: ', total_cost)
