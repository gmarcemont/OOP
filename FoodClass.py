# create customer class
class Customer:
    def __init__(self, id, name, address, email, phone, member_status):
        self.__id = id
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__member_status = member_status

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_phone_number(self):
        return self.__phone

    def get_member_status(self):
        return self.__member_status


# create transaction class
class Transaction:
    def __init__(self, date, item_name, cost, customer_id):
        self.__date = date
        self.__item_name = item_name
        self.__cost = cost
        self.__customer_id = customer_id

    def get_date(self):
        return self.__date

    def get_item_name(self):
        return self.__item_name

    def get_cost(self):
        return self.__cost

    def get_customer_id(self):
        return self.__customer_id
