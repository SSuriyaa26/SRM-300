from Item import Item

item1=Item("MyItem",750)

item1.send_email()

from Phone import Phone

item2=Phone("v2",100,3)
item2.apply_increament(0.2)#inheritance


#polymorphism: len function is an example of polymorphism

item1.apply_discount()#this works even if item 1 is a Phone class or Item class
# print(item1.name)
# item1.name="OtherItem"
# print(item1.name)
# print(item1.read_only_name)





# phone1=Phone("Phonev1",500,5,1)
# #phone1.broke_phones=1
# phone2=Phone("PhoneV2",7500,5)
# print(Item.all)
# print(Phone.all)
# Item.instantiate_from_csv()
#
# print(Item.all)
# print(item1.calculate_total_price())
# # print(Item.__dict__)
# # print(item1.__dict__)
# item2.pay_rate=0.7
# item1=Item("Phone",100,5)
# item2=Item("Laptop",1000,3)
# item3=Item("Cable",10,3)
# item4=Item("Mouse",50,3)
# item5=Item("Keyboard",75,3)
# print(Item.all)
# for instance in Item.all:
#     print(instance.name)
# print(item1)
# print(Item.is_integer(7.006))
