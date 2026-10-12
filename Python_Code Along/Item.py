import csv

class Item:
    pay_rate=0.8#discount
    all = []
    def __init__(self,name:str,price:float,quantity=0):
        #validation
        assert price>=0,f"Price {price} is not greater than or equal to 0"
        assert quantity>=0,f"Quantity {quantity} is not greater than or equal to 0"
        #assignment
        self.__name=name#makes it private
        self.__price=price
        self.quantity=quantity
        Item.all.append(self)

    @property#getter
    def name(self):
        return self.__name

    @name.setter#setter
    def name(self,value):
        self.__name=value

    @property
    def price(self):
        return self.__price
    def apply_discount(self):
        self.__price = self.__price * Item.pay_rate

    def apply_increament(self,incval):
        self.__price=self.__price+self.__price*incval
    @price.setter
    def price(self,price):
        self.__price=price
    def calculate_total_price(self):
        return self.__price*self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        '''This should also do something that has a relationship with the class,but usually,those are used to manipulate different structures of data to instantiate objects,like we have done with CSV'''
        with open('items.csv','r') as f:
            reader =csv.DictReader(f)
            items= list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )
    @staticmethod
    def is_integer(num):
        '''
            Do something that has a relationship with the class ,but not something that must be unique per instance
        '''
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}','{self.__price}','{self.quantity}')"

    def __prepare_body(self):
        return "This is an email regards"
    def send_email(self):
        self.__prepare_body()
    # @property
    # def read_only_name(self):
    #     return "ABC"