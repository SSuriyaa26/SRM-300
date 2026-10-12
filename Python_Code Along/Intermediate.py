# # # # # # # # # # # # # # # # # # # # # # # # # # # # mylist=["banana","cherry","apple"]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # print(mylist)
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # mylist2 = [5,True]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # print(mylist2)
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #indexing , negative indexing
# # # # # # # # # # # # # # # # # # # # # # # # # # # # for i in mylist:
# # # # # # # # # # # # # # # # # # # # # # # # # # # #     print(i)
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # if "banana" in mylist:
# # # # # # # # # # # # # # # # # # # # # # # # # # # #     print("Yes")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # # # # # # # # # # # # #     print("No")
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # append , len
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # mylist.insert(1,"Blueberry")
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # mylist.pop()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # print(mylist)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #clear , remove
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #reverse,sort
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # myList =[0]*5
# # # # # # # # # # # # # # # # # # # # # # # # # # # print(myList)
# # # # # # # # # # # # # # # # # # # # # # # # # # # myList2=[1]*2
# # # # # # # # # # # # # # # # # # # # # # # # # # # new_list=myList+myList2
# # # # # # # # # # # # # # # # # # # # # # # # # # # print(new_list)
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # #slicing , steps(::1)
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # #.copy and list() and slicing to duplicate lists which doesnt share a mem
# # # # # # # # # # # # # # # # # # # # # # # # # # # a=[1,2,3,4,5,6]
# # # # # # # # # # # # # # # # # # # # # # # # # # # b=[i*i for i in a]
# # # # # # # # # # # # # # # # # # # # # # # # # # # print(b)
# # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # #Tuple #immutuable
# # # # # # # # # # # # # # # # # # # # # # # # # # mytuple =("Max",)# if , isnt there it is considered a string
# # # # # # # # # # # # # # # # # # # # # # # # # # print(type(mytuple))
# # # # # # # # # # # # # # # # # # # # # # # # # # mytuple=tuple([1,2,3])
# # # # # # # # # # # # # # # # # # # # # # # # # # print(mytuple)
# # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # item=mytuple[0]
# # # # # # # # # # # # # # # # # # # # # # # # # # print(item)
# # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # #if in and loop works the same as list
# # # # # # # # # # # # # # # # # # # # # # # # # # #count , index on a tuple
# # # # # # # # # # # # # # # # # # # # # # # # # # #conversion between list and tuple , using list() and tuple()
# # # # # # # # # # # # # # # # # # # # # # # # # # print(mytuple[:2])
# # # # # # # # # # # # # # # # # # # # # # # # # # num1,num2,num3=mytuple #u can use a * here to make a list
# # # # # # # # # # # # # # # # # # # # # # # # # # print((num1))
# # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # #dictionary
# # # # # # # # # # # # # # # # # # # # # # # # # dict={"Name":"Suriyaa","City":"Chennai"}
# # # # # # # # # # # # # # # # # # # # # # # # # value=dict["City"]
# # # # # # # # # # # # # # # # # # # # # # # # # print(value)
# # # # # # # # # # # # # # # # # # # # # # # # # dict["email"]="ab@mail.com"
# # # # # # # # # # # # # # # # # # # # # # # # # print(dict)
# # # # # # # # # # # # # # # # # # # # # # # # # dict.pop("email") # or del dict("email")
# # # # # # # # # # # # # # # # # # # # # # # # # print(dict)
# # # # # # # # # # # # # # # # # # # # # # # # # for key in dict.keys():
# # # # # # # # # # # # # # # # # # # # # # # # #     print(key)
# # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # for value in dict.values():
# # # # # # # # # # # # # # # # # # # # # # # # #     print (value)
# # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # for key,value in dict.items():
# # # # # # # # # # # # # # # # # # # # # # # # #     print(key,value)
# # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # #use dict() to copy not =
# # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # #.update can be used to update/overwrite
# # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # #tuples can also be a key in a dict
# # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # #Sets removes duplicates
# # # # # # # # # # # # # # # # # # # # # # # # #.discard removes element if exists , clean clears it and pop removes an random val and removes it
# # # # # # # # # # # # # # # # # # # # # # # # #unions , intersections and diffrences (already done in basics) .intersect , .union,.difference,.symmetric_diffrences ((A intersect B) complement)
# # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # #update , adds 2nd set onto 1st one
# # # # # # # # # # # # # # # # # # # # # # # # #intersection_updates , keeps only elements in both sets , symmetricdiffrence update
# # # # # # # # # # # # # # # # # # # # # # # # #is subset and issuperset check if condition is true
# # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # #isdisjoin checks if 2 sets are disjoint
# # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # #copying , use set() or .copy
# # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # #frozen set is an immutable version of set
# # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # a=frozenset([1,2,3,4])
# # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # print (a)
# # # # # # # # # # # # # # # # # # # # # # # # print(type(a))
# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # #strings
# # # # # # # # # # # # # # # # # # # # # # # #all the things in strings were either already done in the basics or know from DSA practice etc
# # # # # # # # # # # # # # # # # # # # # # # #use .join over +=
# # # # # # # # # # # # # # # # # # # # # # # #f strings , .format
# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # var="Tom"
# # # # # # # # # # # # # # # # # # # # # # # mystring="The variable is %s"%var #this is like printf in C
# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # mystr="the var is {}".format(var)
# # # # # # # # # # # # # # # # # # # # # # # print(mystr)
# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # newstr=f"the var is {var}"
# # # # # # # # # # # # # # # # # # # # # # # print (newstr)
# # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # #collections
# # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # #it has Counter,named tuple,OrderedDict,defaultdict ,deque
# # # # # # # # # # # # # # # # # # # # # # from collections import Counter
# # # # # # # # # # # # # # # # # # # # # # a="aaaaabbbcbbasccc"
# # # # # # # # # # # # # # # # # # # # # # my_counter=Counter(a)
# # # # # # # # # # # # # # # # # # # # # # print(my_counter)
# # # # # # # # # # # # # # # # # # # # # # print(my_counter.most_common(1)[0][1])
# # # # # # # # # # # # # # # # # # # # # # print(list(my_counter.elements()))
# # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # from collections import namedtuple, defaultdict
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # point = namedtuple('Point','x,y')
# # # # # # # # # # # # # # # # # # # # # pt=point(1,-3)
# # # # # # # # # # # # # # # # # # # # # print(pt.x,pt.y)
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # from collections import OrderedDict
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # odict=OrderedDict()
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # odict['a']=1
# # # # # # # # # # # # # # # # # # # # # odict['b']=2
# # # # # # # # # # # # # # # # # # # # # odict['c']=3
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # print(odict)
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # from collections import defaultdict
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # d=defaultdict(int)
# # # # # # # # # # # # # # # # # # # # d['a']=1
# # # # # # # # # # # # # # # # # # # # d['b']=2
# # # # # # # # # # # # # # # # # # # # print(d['c'])
# # # # # # # # # # # # # # # # # # # from collections import deque
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # d=deque()
# # # # # # # # # # # # # # # # # # # d.append(1)
# # # # # # # # # # # # # # # # # # # d.appendleft(2)
# # # # # # # # # # # # # # # # # # # d.append(3)
# # # # # # # # # # # # # # # # # # # print(d)
# # # # # # # # # # # # # # # # # # # # d.pop()
# # # # # # # # # # # # # # # # # # # # d.popleft()
# # # # # # # # # # # # # # # # # # # # print(d)
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # d.rotate(1)
# # # # # # # # # # # # # # # # # # # print(d)
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # #itertool:product,ermutations,combinations,accumulate,groupby,and infinite iterators
# # # # # # # # # # # # # # # # # # # from itertools import product, repeat
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # a=[1,2]
# # # # # # # # # # # # # # # # # # # b=[3,4]
# # # # # # # # # # # # # # # # # # # prod=product(a,b,repeat=2)
# # # # # # # # # # # # # # # # # # # print(list(prod))
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # from itertools import permutations
# # # # # # # # # # # # # # # # # # # perm =permutations(a)
# # # # # # # # # # # # # # # # # # # print(list(perm))
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # from itertools import combinations
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # combs=combinations(a)
# # # # # # # # # # # # # # # # # # # print(list(combs))
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # from itertools import accumulate
# # # # # # # # # # # # # # # # # # a=[1,2,3,4]
# # # # # # # # # # # # # # # # # # acc=accumulate(a)#func=operator.mul or func=max are additional parameters
# # # # # # # # # # # # # # # # # # print(list(acc))
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # from itertools import groupby
# # # # # # # # # # # # # # # # # # def small(x):
# # # # # # # # # # # # # # # # # #     return  x<3
# # # # # # # # # # # # # # # # # # g=groupby(a,key=lambda x:x<3)
# # # # # # # # # # # # # # # # # # for key,value in g:
# # # # # # # # # # # # # # # # # #     print(key,list(value))
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # from itertools import count,cycle,repeat
# # # # # # # # # # # # # # # # # a=[1,2,3]
# # # # # # # # # # # # # # # # # for i in count(10):
# # # # # # # # # # # # # # # # #     print(i)
# # # # # # # # # # # # # # # # #     if i==15:
# # # # # # # # # # # # # # # # #         break
# # # # # # # # # # # # # # # # # for i in cycle(a)
# # # # # # # # # # # # # # # # #     print(i)
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # for i in repeat(1,4):
# # # # # # # # # # # # # # # # #     print(i)
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # #lambda , almost same content as basics , talks about map,filter ,reduce and how it can be used in sorted
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # #exception and erros try , except ,else ,finally , raise ,assert and custom exception
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # #Logging
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # import logging
# # # # # # # # # # # # # # # # logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s-%(message)s',datefmt='%m/%d/%Y %H:%M:%S')
# # # # # # # # # # # # # # # # logging.debug("This is a debug msg")
# # # # # # # # # # # # # # # # logging.info("This is an info msg")
# # # # # # # # # # # # # # # # logging.warning("This is  a warning msg")
# # # # # # # # # # # # # # # # logging.error("This is an error msg")
# # # # # # # # # # # # # # # # logging.critical("This is a critical msg")
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # #logging from a helper uses(__name__) , log probagation to stop hierarchy
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # logger=logging.getLogger()
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # import logging
# # # # # # # # # # # # # # # try:
# # # # # # # # # # # # # # #     a=[1,2]
# # # # # # # # # # # # # # #     val=a[4]
# # # # # # # # # # # # # # # except IndexError as e:
# # # # # # # # # # # # # # #     logging.error(e)#using traceback to find where error is
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #rotating file handler
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #######
# # # # # # # # # # # # # # #JSON :javascript object notation
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # import json
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # dict={"Name":"Suriyaa","Age":"19","is18":True}
# # # # # # # # # # # # # # jdict= json.dumps(dict)
# # # # # # # # # # # # # # print(jdict)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # new_dict= json.loads(jdict)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print(new_dict)
# # # # # # # # # # # # #
# # # # # # # # # # # # # #Random
# # # # # # # # # # # # # import random
# # # # # # # # # # # # #
# # # # # # # # # # # # # a=random.random()# float from 0 to 1
# # # # # # # # # # # # # b= random.uniform(0,10) # float between range
# # # # # # # # # # # # # c= random.randint(1,10)
# # # # # # # # # # # # # d=random.randrange(1,10)#excludes last num
# # # # # # # # # # # # # e=random.normalvariate(0,1)#from a normal distribution
# # # # # # # # # # # # #
# # # # # # # # # # # # # mylist=("abced")
# # # # # # # # # # # # # f=random.choice(mylist)
# # # # # # # # # # # # # g=random.choices(mylist,k=3)#use random.sample for non repeating
# # # # # # # # # # # # # #shuffle already seen in blackjack implementation
# # # # # # # # # # # # #
# # # # # # # # # # # # # random.seed(1)
# # # # # # # # # # # # # print(random.random())
# # # # # # # # # # # # # random.seed(1)
# # # # # # # # # # # # # print(random.random())
# # # # # # # # # # # # #
# # # # # # # # # # # # # #seed determines how the randoms are made , not truly random
# # # # # # # # # # # # #
# # # # # # # # # # # # import secrets
# # # # # # # # # # # # print(secrets.randbelow(10))
# # # # # # # # # # # # print(secrets.randbits(4))
# # # # # # # # # # # # # secrets.choice(mylist)
# # # # # # # # # # #
# # # # # # # # # # # import numpy as np
# # # # # # # # # # #
# # # # # # # # # # # a=np.random.rand(3)
# # # # # # # # # # # print(a)
# # # # # # # # # # #
# # # # # # # # # # # #randint for ints , u can also determine sizes
# # # # # # # # # # # # np.random.shuffle(arr),seed works similar np.random.seed()
# # # # # # # # # #
# # # # # # # # # # #decorators : wrok with functions and classes
# # # # # # # # # # # def start_end_decorator(func):
# # # # # # # # # # #     def wrapper():
# # # # # # # # # # #         print("start")
# # # # # # # # # # #         func()
# # # # # # # # # # #         print("end")
# # # # # # # # # # #     return wrapper
# # # # # # # # # # # @start_end_decorator
# # # # # # # # # # # def print_name():
# # # # # # # # # # #     print("Alex")
# # # # # # # # # # # #print_name=start_end_decorator(print_name)
# # # # # # # # # # # print_name()
# # # # # # # # # # #
# # # # # # # # # # # def start_end_decorator(func):
# # # # # # # # # # #     def wrapper(*args, **kwargs):
# # # # # # # # # # #         print("start")
# # # # # # # # # # #         func(*args, **kwargs)
# # # # # # # # # # #         print("end")
# # # # # # # # # # #     return wrapper
# # # # # # # # # # # @start_end_decorator
# # # # # # # # # # # def print_name(name):
# # # # # # # # # # #     print(name)
# # # # # # # # # # # #print_name=start_end_decorator(print_name)
# # # # # # # # # # # # print_name("Apple")
# # # # # # # # # # # print(help(print_name))
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # # import functools
# # # # # # # # # # # def repeat(num_tries):
# # # # # # # # # # #     def decorator_repeat(func):
# # # # # # # # # # #         @functools.wraps(func)
# # # # # # # # # # #         def wrapper(*args, **kwargs):
# # # # # # # # # # #             for _ in range(num_tries):
# # # # # # # # # # #                 resut=func(*args, **kwargs)
# # # # # # # # # # #             return resut
# # # # # # # # # # #         return wrapper
# # # # # # # # # # #     return decorator_repeat
# # # # # # # # # # # @repeat(num_tries=4)
# # # # # # # # # # # def greet(name):
# # # # # # # # # # #     print("Hello "+name)
# # # # # # # # # # #
# # # # # # # # # # # greet("Suriyaa")
# # # # # # # # # # #decorators can be stacked,so they run the funcs in order
# # # # # # # # # #
# # # # # # # # # # #class decorator
# # # # # # # # # # class Countcalls:
# # # # # # # # # #     def __init__(self,func):
# # # # # # # # # #         self.func=func
# # # # # # # # # #         self.num_calls=0
# # # # # # # # # #
# # # # # # # # # #     def __call__(self, *args, **kwargs):
# # # # # # # # # #         self.num_calls+=1
# # # # # # # # # #         val=str(self.num_calls)
# # # # # # # # # #         print("This is executed "+val+" times")
# # # # # # # # # #         return self.func(*args,**kwargs)
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # # cc=Countcalls(None)
# # # # # # # # # # # cc()
# # # # # # # # # # @Countcalls
# # # # # # # # # # def say_hello():
# # # # # # # # # #     print("hello")
# # # # # # # # # #
# # # # # # # # # # say_hello()
# # # # # # # # # # say_hello()
# # # # # # # # # #
# # # # # # # # # # #use cases are timers,debuggers, checkers,register plugins,cache,update states
# # # # # # # # # import sys
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # #generators functions that return an object that allows for iteration
# # # # # # # # #
# # # # # # # # # # def mygenerator():
# # # # # # # # # #     yield  1
# # # # # # # # # #     yield 2
# # # # # # # # # #     yield 3
# # # # # # # # # #
# # # # # # # # # # g=mygenerator()
# # # # # # # # # #
# # # # # # # # # # print(g)
# # # # # # # # # #
# # # # # # # # # # # for i in g:
# # # # # # # # # # #     print(i)
# # # # # # # # # #
# # # # # # # # # # # value=next(g)
# # # # # # # # # # # print(value)
# # # # # # # # # # #
# # # # # # # # # # # value=next(g)
# # # # # # # # # # # print(value)
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # value=next(g)
# # # # # # # # # # # print(value)
# # # # # # # # # #
# # # # # # # # # # # value=next(g)
# # # # # # # # # # # print(value)
# # # # # # # # # #
# # # # # # # # # # print(sum(g))
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # # def countdown(num):
# # # # # # # # # #     while num>0:
# # # # # # # # # #         yield  num
# # # # # # # # # #         num-=1
# # # # # # # # # #
# # # # # # # # # # cd=countdown(4)
# # # # # # # # # #
# # # # # # # # # # value=next(cd)
# # # # # # # # # # print(value)
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # #the key thing to remember about generators is that they are very memory efficient
# # # # # # # # #
# # # # # # # # # # def firstn(n):
# # # # # # # # # #     mylist=[]
# # # # # # # # # #     num=0
# # # # # # # # # #     while (num<n):
# # # # # # # # # #         mylist.append(num)
# # # # # # # # # #         num+=1
# # # # # # # # # #     return mylist
# # # # # # # # # #
# # # # # # # # # # def firstn_generator(n):
# # # # # # # # # #     num=0
# # # # # # # # # #     while num<n:
# # # # # # # # # #         yield num
# # # # # # # # # #         num+=1
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # print(sys.getsizeof(firstn(1000000)))
# # # # # # # # # # print(sys.getsizeof(firstn_generator(1000000)))
# # # # # # # # # #generator uses much less memory
# # # # # # # # # # Threading and multi Threading
# # # # # # # # #
# # # # # # # # # #process is an instance of a program
# # # # # # # # # #takes adv of multiple CPU and cores, separate memory storage,new process is started indempendiently , one GIL for each process,killable
# # # # # # # # # #IPC is complex
# # # # # # # # # #thread is an entity in a thread
# # # # # # # # # #lightweight ,great for I/O bound task,
# # # # # # # # # #limited by GIL,careful with race condition
# # # # # # # # #
# # # # # # # # # #GIL
# # # # # # # # # # a lock that allows only one thread at a time to execute in python
# # # # # # # # # #needed in CPuthon because memory management is not thread safe
# # # # # # # # # #avoid:
# # # # # # # # # #use multiprocessing,use different-free threaded Python implementation (Jython,IronPython),use Python as a wrapper for thirdparty libraries (C/C++)->numpy,scipy
# # # # # # # # #
# # # # # # # # # from multiprocessing import Process
# # # # # # # # # import os
# # # # # # # # # import time
# # # # # # # # # from queue import Queue
# # # # # # # # # from threading import Thread, Lock, current_thread
# # # # # # # # #
# # # # # # # # # # def sqrnums():
# # # # # # # # # #     for i in range(100):
# # # # # # # # # #         i+=1
# # # # # # # # # #         time.sleep(0.1)
# # # # # # # # # database_value=0
# # # # # # # # # def increase(lock):
# # # # # # # # #     global database_value
# # # # # # # # #     lock.acquire()
# # # # # # # # #     local_copy= database_value
# # # # # # # # #
# # # # # # # # #     local_copy+=1
# # # # # # # # #
# # # # # # # # #     time.sleep(0.1)
# # # # # # # # #     database_value =local_copy
# # # # # # # # #     lock.release()
# # # # # # # # # def worker(q,lock):
# # # # # # # # #       while True:
# # # # # # # # #         value=q.get()
# # # # # # # # #         with lock:
# # # # # # # # #             print(f"in {current_thread().name} got {value} \n")
# # # # # # # # #         q.task_done()
# # # # # # # # # if __name__ =="__main__":
# # # # # # # # #     q=Queue()
# # # # # # # # #     lock=Lock()
# # # # # # # # #     num_threads=10
# # # # # # # # #     for i in range(num_threads):
# # # # # # # # #         thread=Thread(target=worker,args=(q,lock))
# # # # # # # # #         thread.daemon=True
# # # # # # # # #         thread.start()
# # # # # # # # #
# # # # # # # # #     for i in range(1,21):
# # # # # # # # #         q.put(i)
# # # # # # # # #     q.join()
# # # # # # # # #
# # # # # # # # #     print("end main")
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #     # print('start value',database_value)
# # # # # # # # #     # lock =Lock()#lock allows it to be 2
# # # # # # # # #     # thread1=Thread(target=increase,args=(lock,))
# # # # # # # # #     # thread2 = Thread(target=increase,args=(lock,))
# # # # # # # # #     # thread1.start()
# # # # # # # # #     # thread2.start()
# # # # # # # # #     # thread1.join()
# # # # # # # # #     # thread2.join()
# # # # # # # # #     #
# # # # # # # # #     # print('end value ',database_value)#race condition occurs and is only incremented by 1
# # # # # # # # #     # print ('end main')
# # # # # # # # #     # threads=[]
# # # # # # # # #     # num_thread=10
# # # # # # # # #     # for i in range(num_thread):
# # # # # # # # #     #     t=Thread(target=sqrnums())
# # # # # # # # #     #     threads.append(t)
# # # # # # # # #     # for t in threads:
# # # # # # # # #     #     t.start()
# # # # # # # # #     # for t in threads:
# # # # # # # # #     #     t.join()
# # # # # # # # #     #
# # # # # # # # #     # print("End main")
# # # # # # # # #
# # # # # # # # #     # processes=[]
# # # # # # # # #     # num_processes=os.cpu_count()
# # # # # # # # #     #
# # # # # # # # #     # for i in range(num_processes):
# # # # # # # # #     #     p=Process(target=sqrnums())
# # # # # # # # #     #     processes.append(p)
# # # # # # # # #     #
# # # # # # # # #     # for p in processes:
# # # # # # # # #     #     p.start()
# # # # # # # # #     #
# # # # # # # # #     # for p in processes:
# # # # # # # # #     #     p.join()
# # # # # # # # #     #
# # # # # # # # #     # print("end main")
# # # # # # # # import numbers
# # # # # # # # #multiprocessing
# # # # # # # # from multiprocessing import Process, Value, Array,Lock
# # # # # # # # import time
# # # # # # # # from multiprocessing import Queue
# # # # # # # #
# # # # # # # # # def add_100(numbers,lock):
# # # # # # # # #     for i in range(100):
# # # # # # # # #         time.sleep(0.01)
# # # # # # # # #         for i in range(len(numbers)):
# # # # # # # # #
# # # # # # # # #             # lock.acquire()
# # # # # # # # #             with lock:
# # # # # # # # #                 numbers[i]+= 1
# # # # # # # # #             # lock.release()
# # # # # # # # from  multiprocessing import Pool
# # # # # # # # from unittest import result
# # # # # # # #
# # # # # # # #
# # # # # # # # def square(numbers,queue):
# # # # # # # #     for i in numbers:
# # # # # # # #         queue.put(i*i)
# # # # # # # # def make_negative(numbers, queue):
# # # # # # # #     for i in numbers:
# # # # # # # #         queue.put(-1 * i)
# # # # # # # # def cube(number):
# # # # # # # #     return number*number*number
# # # # # # # # if __name__ == "__main__":
# # # # # # # #     numbers=range(10)
# # # # # # # #     pool=Pool()
# # # # # # # #     result = pool.map(cube,numbers)
# # # # # # # #     # pool.apply(cube,numbers[0],)
# # # # # # # #     pool.close()
# # # # # # # #     pool.join()
# # # # # # # #     print (result)
# # # # # # # #
# # # # # # # #
# # # # # # # #     #q=Queue()
# # # # # # # #     # numbers=range(1,6)
# # # # # # # #     # p1 = Process(target=square, args=(numbers, q))
# # # # # # # #     # p2 = Process(target=make_negative, args=(numbers, q))
# # # # # # # #     #
# # # # # # # #     # p1.start()
# # # # # # # #     # p2.start()
# # # # # # # #     #
# # # # # # # #     # p1.join()
# # # # # # # #     # p2.join()
# # # # # # # #     #
# # # # # # # #     # while not q.empty():
# # # # # # # #     #     print (q.get())
# # # # # # # #
# # # # # # # #
# # # # # # # #  #lock=Lock()
# # # # # # # #     # shared_array=Array('d',[0.0,100.0,200.0])
# # # # # # # #     # shared_number = Value('i', 0)
# # # # # # # #     # print('array at beginning is', shared_array[:])
# # # # # # # #     #
# # # # # # # #     # p1 = Process(target=add_100, args=(shared_array,lock))
# # # # # # # #     # p2 = Process(target=add_100, args=(shared_array,lock))
# # # # # # # #     #
# # # # # # # #     # p1.start()
# # # # # # # #     # p2.start()
# # # # # # # #     #
# # # # # # # #     # p1.join()
# # # # # # # #     # p2.join()
# # # # # # # #     #
# # # # # # # #     # print('number at end is', shared_array[:])
# # # # # # #
# # # # # # #
# # # # # # # #function arguments
# # # # # # # '''
# # # # # # # -the diffrence between arguments and parametrs
# # # # # # # -postional and keyword arguments
# # # # # # # -default arguments
# # # # # # # -variable elength arguments
# # # # # # # -container unpacking into function arguments
# # # # # # # -Local vs global arguments
# # # # # # # -parameter passing/(by value and reference)
# # # # # # # '''
# # # # # # # # def print_name(name):#parameter
# # # # # # # #     print(name)
# # # # # # # #
# # # # # # # # print_name('Suriyaa')#argument
# # # # # # #
# # # # # # # # def foo(a,b,c,d=4):# d is a default and it default parameters must be at the end
# # # # # # # #     print(a,b,c,d)
# # # # # # # #
# # # # # # # # foo(a=1,b=2,c=3)#keyword argument
# # # # # # # # foo(1,b=2,c=3)# mix of positional and keyword, positional cannot come after a keyword
# # # # # # # # foo(1,2,3)#prints 4 also by default
# # # # # # # # foo(1,2,3,7)#replaces default
# # # # # # #
# # # # # # # # def foo(a,b,*args,**kwargs):
# # # # # # # #     print(a,b)
# # # # # # # #     for arg in args:
# # # # # # # #         print(arg)
# # # # # # # #     for key in kwargs:
# # # # # # # #         print(key,kwargs[key])
# # # # # # #     #args is for postional arguemnts and kwargs are for keyword arguements
# # # # # # #
# # # # # # # # def foo(a,b,*,c,d):#everything after * must be keyword
# # # # # # # #     print (a,b,c,d)
# # # # # # # # foo(1,2,c=6,d=7)
# # # # # # #
# # # # # # # def foo(a,b,c):
# # # # # # #     print(a,b,c)
# # # # # # #
# # # # # # # mylist=[0,1,2]
# # # # # # # foo(*mylist)#unpacking, container must be same length
# # # # # # #
# # # # # # # my_dict={'a':1,'b':2,'c':3}
# # # # # # # foo(**my_dict)#unpacks dict with 2 * , only works when keys of dict are same as func and length mathc
# # # # # # #
# # # # # # import numbers
# # # # # #
# # # # # #
# # # # # # def foo():
# # # # # #     global number
# # # # # #     x= number
# # # # # #     print("number inside func:",x)
# # # # # # number =3
# # # # # # foo()
# # # # # # #parameter passing
# # # # # def foo(a_list):
# # # # #     a_list.append(4)
# # # # # var=10
# # # # # my_list=[1,2,3]
# # # # # foo(my_list)
# # # # # # foo(var)
# # # # # # print(var)
# # # # # print((my_list))
# # # #
# # # # #use of *
# # # # #multiplication , exponenet, repeat list and string,args and kwargs
# # # #
# # # # my_tuple=(1,2,3)
# # # # my_list=[4,5,6]
# # # #
# # # # new_list = [*my_tuple,*my_list]
# # # # print(new_list)
# # # # #* used for mergeing list/tuples and sets and even dicts using **
# # #
# # # # shallow and deep copy
# # # import copy
# # # # og=[1,2,3]
# # # # cpy=copy.copy(og)
# # # # cpy[0]=-5
# # # # print(cpy)
# # # # print(og) #but this only works in 1 level so if we make a list inside a list shallow copy has the same result
# # # class Person:
# # #     def __init__(self,name,age):
# # #         self.age=age
# # #         self.name=name
# # #
# # # class Company:
# # #     def __init__(self,boss,employee):
# # #         self.boss=boss
# # #         self.employee=employee
# # #
# # # p1=Person('Alex',27)
# # # p2=Person('Joe',18)
# # #
# # # company=Company(p1,p2)
# # # company_deepclone=copy.deepcopy(company)
# # # company_clone=copy.copy((company))
# # # company_clone.boss.age=55
# # # company_deepclone.boss.age=100
# # # print(company_clone.boss.age)
# # # print(company.boss.age)
# # # print(company_deepclone.boss.age)
# # from types import TracebackType
# #
# #
# # #context managers
# #
# # # with open('notes.txt','w')as file:
# # #     file.write('some todo...')
# # #
# # # file =open('notes.txt','w')
# # # try:
# # #     file.write('some todo...')
# # # finally:
# # #     file.close()
# #
# # #same with lock
# #
# # class Managed_file:
# #     def __init__(self,filename):
# #         self.filename=filename
# #
# #     def __enter__(self):
# #         print ('enter')
# #         self.file = open(self.filename,'w')
# #         return self.file
# #     def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None):
# #         if self.file:
# #             self.file.close()
# #         print('exc:',exc_type,exc_val)
# #         print('exit')
# # with Managed_file('notes.txt') as file:
# #     print('do smth')
# #     file.write('some todoo...')
# #
# # print('continue')
#
# from contextlib import  contextmanager
# @contextmanager
# def open_managed_file(filename):
#     f=open(filename,'w')
#     try:
#         yield f
#     finally:
#         f.close()
# with open_managed_file('notes.txt') as f:
#     f.write('smth to do')
#
#
