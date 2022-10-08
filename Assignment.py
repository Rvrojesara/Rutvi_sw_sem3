
#1. Triple all the numbers given in list

# nums=(1,2,3,4,5,6,7)
# result=map(lambda i:i*3,nums)
# print("\nTriple of said list numbers:")
# print(list(result))

# print("============================================================")

# 2. Separate even odd number from given list

# num=(1,2,3,4,5,6,7,8,9,11,12,13,14,15,10)
# result=map(lambda i:i%2==0,num)
# print(list(result))

# print("============================================================")

# 3. Print all string in lower case from given tuple

# def toLower(str):
#     return str.lower()
# res=map(toLower,("SOFTWARE","SEM","3"))
# print(tuple(res))    

# print("============================================================")

# 4. Print square root of numbers given in list

# x=map(lambda i:i**0.5,(4,9,16,25,36,49,64,81,100,121,144))
# print(list(x))

# print("============================================================")

# 5. Eliminate duplicate letter from given string

from collections import OrderedDict


def remove_duplicate(str1):
  return "".join(OrderedDict.fromkeys(str1))
     
print(remove_duplicate("rojesara"))

# 6. Print table of any number 

# def multiply(i):
#     return num*i
# num=int(input("Enter a number"))
# res=map(multiply,(1,2,3,4,5,6,7,8,9,10))
# print(list(res))

# print("============================================================")

# 7. Add two list

# list1=["a","b","c"]
# list2=[1,2,3]

# list1.extend(list2)
# print(list1)

# print("============================================================")

# 8. Convert all float digits into integer using built in function from given list.

# num=[1.0,2.5,3.4,5.5]
# x=map(int,num)
# print(list(x))

# print("============================================================")

# 9. Reverse given set

list=[1,2,3,'a','b','c']
list.reverse()
print(list)

# print("============================================================")

# 10. Add ‘@gmail.com’ to all the values of given dictionary and convert it to lower case.
def toLower(str):
    return str.lower()
dict_item={"1":"RUTVI","2":"RIYA"}
a=map(lambda i:(i[0],i[1]+"@gmail.com"),dict_item.items())

print(dict(a))

new_dict = dict((k.lower(), v.lower()) for k, v in dict_item .items()) 
print(new_dict)