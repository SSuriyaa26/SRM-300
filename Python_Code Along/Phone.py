from Item import Item


class Phone(Item):
    def __init__(self,name:str,price:float,quantity=0,broken_phones=0):
        super().__init__(
            name,price,quantity
       )

        #validation
        # assert price>=0,f"Price {price} is not greater than or equal to 0"
        # assert quantity>=0,f"Quantity {quantity} is not greater than or equal to 0"
        assert broken_phones>=0,"Broken_phone must be greater than zero"
        #assignment
        # self.name=name
        # self.price=price
        # self.quantity=quantity
        self.broken_phone=broken_phones
