#Udemy Course Work - Lottery App

#Get the Lottery numbers
numbers = str( raw_input("Enter the numbers separated by commas: "))
#Now split the string into a list using the string split method
numbers_in_list=numbers.split(",")
#Now get a list of numbers instead of list of string by using list comprehension
numbers_in_list=[int(x) for x in numbers_in_list]
