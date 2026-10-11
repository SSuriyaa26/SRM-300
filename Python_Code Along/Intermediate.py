# # # # # # # # # # # # # # mylist=["banana","cherry","apple"]
# # # # # # # # # # # # # # print(mylist)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # mylist2 = [5,True]
# # # # # # # # # # # # # # print(mylist2)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # #indexing , negative indexing
# # # # # # # # # # # # # # for i in mylist:
# # # # # # # # # # # # # #     print(i)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # if "banana" in mylist:
# # # # # # # # # # # # # #     print("Yes")
# # # # # # # # # # # # # # else:
# # # # # # # # # # # # # #     print("No")
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # # append , len
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # mylist.insert(1,"Blueberry")
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # mylist.pop()
# # # # # # # # # # # # # # print(mylist)
# # # # # # # # # # # # # # #clear , remove
# # # # # # # # # # # # # # #reverse,sort
# # # # # # # # # # # # #
# # # # # # # # # # # # # myList =[0]*5
# # # # # # # # # # # # # print(myList)
# # # # # # # # # # # # # myList2=[1]*2
# # # # # # # # # # # # # new_list=myList+myList2
# # # # # # # # # # # # # print(new_list)
# # # # # # # # # # # # #
# # # # # # # # # # # # # #slicing , steps(::1)
# # # # # # # # # # # # #
# # # # # # # # # # # # # #.copy and list() and slicing to duplicate lists which doesnt share a mem
# # # # # # # # # # # # # a=[1,2,3,4,5,6]
# # # # # # # # # # # # # b=[i*i for i in a]
# # # # # # # # # # # # # print(b)
# # # # # # # # # # # #
# # # # # # # # # # # # #Tuple #immutuable
# # # # # # # # # # # # mytuple =("Max",)# if , isnt there it is considered a string
# # # # # # # # # # # # print(type(mytuple))
# # # # # # # # # # # # mytuple=tuple([1,2,3])
# # # # # # # # # # # # print(mytuple)
# # # # # # # # # # # #
# # # # # # # # # # # # item=mytuple[0]
# # # # # # # # # # # # print(item)
# # # # # # # # # # # #
# # # # # # # # # # # # #if in and loop works the same as list
# # # # # # # # # # # # #count , index on a tuple
# # # # # # # # # # # # #conversion between list and tuple , using list() and tuple()
# # # # # # # # # # # # print(mytuple[:2])
# # # # # # # # # # # # num1,num2,num3=mytuple #u can use a * here to make a list
# # # # # # # # # # # # print((num1))
# # # # # # # # # # #
# # # # # # # # # # # #dictionary
# # # # # # # # # # # dict={"Name":"Suriyaa","City":"Chennai"}
# # # # # # # # # # # value=dict["City"]
# # # # # # # # # # # print(value)
# # # # # # # # # # # dict["email"]="ab@mail.com"
# # # # # # # # # # # print(dict)
# # # # # # # # # # # dict.pop("email") # or del dict("email")
# # # # # # # # # # # print(dict)
# # # # # # # # # # # for key in dict.keys():
# # # # # # # # # # #     print(key)
# # # # # # # # # # #
# # # # # # # # # # # for value in dict.values():
# # # # # # # # # # #     print (value)
# # # # # # # # # # #
# # # # # # # # # # # for key,value in dict.items():
# # # # # # # # # # #     print(key,value)
# # # # # # # # # # #
# # # # # # # # # # # #use dict() to copy not =
# # # # # # # # # # #
# # # # # # # # # # # #.update can be used to update/overwrite
# # # # # # # # # # #
# # # # # # # # # # # #tuples can also be a key in a dict
# # # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # #Sets removes duplicates
# # # # # # # # # # #.discard removes element if exists , clean clears it and pop removes an random val and removes it
# # # # # # # # # # #unions , intersections and diffrences (already done in basics) .intersect , .union,.difference,.symmetric_diffrences ((A intersect B) complement)
# # # # # # # # # #
# # # # # # # # # # #update , adds 2nd set onto 1st one
# # # # # # # # # # #intersection_updates , keeps only elements in both sets , symmetricdiffrence update
# # # # # # # # # # #is subset and issuperset check if condition is true
# # # # # # # # # #
# # # # # # # # # # #isdisjoin checks if 2 sets are disjoint
# # # # # # # # # #
# # # # # # # # # # #copying , use set() or .copy
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # #frozen set is an immutable version of set
# # # # # # # # # #
# # # # # # # # # # a=frozenset([1,2,3,4])
# # # # # # # # # #
# # # # # # # # # # print (a)
# # # # # # # # # # print(type(a))
# # # # # # # # #
# # # # # # # # # #strings
# # # # # # # # # #all the things in strings were either already done in the basics or know from DSA practice etc
# # # # # # # # # #use .join over +=
# # # # # # # # # #f strings , .format
# # # # # # # # #
# # # # # # # # # var="Tom"
# # # # # # # # # mystring="The variable is %s"%var #this is like printf in C
# # # # # # # # #
# # # # # # # # # mystr="the var is {}".format(var)
# # # # # # # # # print(mystr)
# # # # # # # # #
# # # # # # # # # newstr=f"the var is {var}"
# # # # # # # # # print (newstr)
# # # # # # # #
# # # # # # # # #collections
# # # # # # # #
# # # # # # # # #it has Counter,named tuple,OrderedDict,defaultdict ,deque
# # # # # # # # from collections import Counter
# # # # # # # # a="aaaaabbbcbbasccc"
# # # # # # # # my_counter=Counter(a)
# # # # # # # # print(my_counter)
# # # # # # # # print(my_counter.most_common(1)[0][1])
# # # # # # # # print(list(my_counter.elements()))
# # # # # # # #
# # # # # # # #
# # # # # # #
# # # # # # # from collections import namedtuple, defaultdict
# # # # # # #
# # # # # # # point = namedtuple('Point','x,y')
# # # # # # # pt=point(1,-3)
# # # # # # # print(pt.x,pt.y)
# # # # # # #
# # # # # # # from collections import OrderedDict
# # # # # # #
# # # # # # # odict=OrderedDict()
# # # # # # #
# # # # # # # odict['a']=1
# # # # # # # odict['b']=2
# # # # # # # odict['c']=3
# # # # # # #
# # # # # # # print(odict)
# # # # # # #
# # # # # # #
# # # # # # from collections import defaultdict
# # # # # #
# # # # # # d=defaultdict(int)
# # # # # # d['a']=1
# # # # # # d['b']=2
# # # # # # print(d['c'])
# # # # # from collections import deque
# # # # #
# # # # # d=deque()
# # # # # d.append(1)
# # # # # d.appendleft(2)
# # # # # d.append(3)
# # # # # print(d)
# # # # # # d.pop()
# # # # # # d.popleft()
# # # # # # print(d)
# # # # #
# # # # # d.rotate(1)
# # # # # print(d)
# # # #
# # # # #itertool:product,ermutations,combinations,accumulate,groupby,and infinite iterators
# # # # # from itertools import product, repeat
# # # # #
# # # # # a=[1,2]
# # # # # b=[3,4]
# # # # # prod=product(a,b,repeat=2)
# # # # # print(list(prod))
# # # # #
# # # # #
# # # # # from itertools import permutations
# # # # # perm =permutations(a)
# # # # # print(list(perm))
# # # # #
# # # # # from itertools import combinations
# # # # #
# # # # # combs=combinations(a)
# # # # # print(list(combs))
# # # # #
# # # # from itertools import accumulate
# # # # a=[1,2,3,4]
# # # # acc=accumulate(a)#func=operator.mul or func=max are additional parameters
# # # # print(list(acc))
# # # #
# # # # from itertools import groupby
# # # # def small(x):
# # # #     return  x<3
# # # # g=groupby(a,key=lambda x:x<3)
# # # # for key,value in g:
# # # #     print(key,list(value))
# # # #
# # #
# # # from itertools import count,cycle,repeat
# # # a=[1,2,3]
# # # for i in count(10):
# # #     print(i)
# # #     if i==15:
# # #         break
# # # for i in cycle(a)
# # #     print(i)
# # #
# # # for i in repeat(1,4):
# # #     print(i)
# # #
# #
# # #lambda , almost same content as basics , talks about map,filter ,reduce and how it can be used in sorted
# #
# # #exception and erros try , except ,else ,finally , raise ,assert and custom exception
# #
# # #Logging
# #
# # import logging
# # logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s-%(message)s',datefmt='%m/%d/%Y %H:%M:%S')
# # logging.debug("This is a debug msg")
# # logging.info("This is an info msg")
# # logging.warning("This is  a warning msg")
# # logging.error("This is an error msg")
# # logging.critical("This is a critical msg")
# #
# # #logging from a helper uses(__name__) , log probagation to stop hierarchy
# #
# # logger=logging.getLogger()
# #
# import logging
# try:
#     a=[1,2]
#     val=a[4]
# except IndexError as e:
#     logging.error(e)#using traceback to find where error is
#
# #rotating file handler
#
#######
#JSON :javascript object notation

import json

dict={"Name":"Suriyaa","Age":"19","is18":True}
jdict= json.dumps(dict)
print(jdict)


new_dict= json.loads(jdict)

print(new_dict)