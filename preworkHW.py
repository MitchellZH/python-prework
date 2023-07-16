# Question 1
# Write a function to print “hello_USERNAME!” USERNAME is the input of the function. The first line of the code has been defined as below.
def hello_name(user_name):
  print("hello_" + user_name + "!")

hello_name("mitchell")


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
  oddNumbers = list(range(1,100))
  for oddNumber in oddNumbers:
    if oddNumber % 2 == 0:
      continue
    else:
      print(oddNumber)

first_odds()


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. def max_num_in_list(a_list):
def max_num_in_list(a_list):
  return max(a_list)

maxNumber = max_num_in_list([1,5,3,10,4,-1])

print(maxNumber)


# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, 
# unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
  if a_year % 4 == 0 and a_year % 100 != 0:
    return True
  elif a_year % 4 == 0 and a_year % 100 == 0 and a_year % 400 == 0:
    return True
  else:
    return False
  
result = str(is_leap_year(2014))
print(result)


# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

# def is_consecutive(a_list):
#   a_list.sort()
#   generatedList = list(range[min(a_list),max(a_list)])
  
#   if generatedList == a_list:
#     return True
#   else: 
#     return False 


# is_consecutive([3,1,26,15])

a_list = [3,1,26,15]
a_list.sort()
print(a_list)
print(type(max(a_list)))
range