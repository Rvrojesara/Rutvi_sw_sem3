# 1. Using filter() function filter the list so that only negative numbers are left.

nums = [-34, 0,-1, 12, -88,45,-44,32,-37,66,-90,22]
result = list(filter(lambda x: x >0, nums))
print("positive numbers list: ",result)
print("------------------------------------------------------------------------------------------------------")


# 2. Using filter function,filter the even numbers so that only odd numbers are passed to the new list.

nums=[1,2,3,4,5,6,7,8,9,10,11,22,33,44,55,66,77,88,99]
odd_nums=list(filter(lambda x:x%2!=0,nums))
print("odd numbers: ",odd_nums)
print("------------------------------------------------------------------------------------------------------")

# 3. Using filter() and list() functions and lower() method filter all the vowels in a given string. 

str="When you have a dream,you've got to grab it and never let go."
list3=list(filter(lambda x:True if x.lower() in "aeiou" else False,str))
print(list3)
print("------------------------------------------------------------------------------------------------------")


# 4. This time using filter() and list() functions filter all the positive integer in the string.

str="William Faulkner's Absalom,Absalom!(1936) contains a sentence composed of 1,288 words (in the 1951 Random House version)."
list4=list(filter(lambda x:True if x in "0123456789" else False,str))
print("positive numbers list: ",list4)
print("------------------------------------------------------------------------------------------------------")


# 5. Convert a number to positive if it's negative in the list.Only pass those that are converted from 
# negative to positive to the new list.[Try using map inside filter]  

list1=[1,-2,3,-4,5,-6,7,-8,9,-10,11,-12,13,-14,15,-16]
list2=list(filter(lambda x:True if x>0 else False,map(lambda x:x*-1,list1)))
print(list2)
print("------------------------------------------------------------------------------------------------------")