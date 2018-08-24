#Udemy Course Work - Lottery App

#Import the random class
import random
#Get the Lottery numbers
def get_players_numbers():
    numbers = str( raw_input("Enter the numbers separated by commas: "))
    #Now split the string into a list using the string split method
    numbers_in_list=numbers.split(",")
    #Now get a set of numbers instead of list of string by using set comprehension, same as list just returns a set.
    numbers_in_set={int(x) for x in numbers_in_list}
    #Now return a set from the invoking call
    return numbers_in_set

#Lottery calaculates 6 random nubers
def create_lottery_numbers():
    lottery_num=set()
    for x in range(6):
        lottery_num.add(random.randint(1,100)) #Prints a random number between 1 and 100
    return lottery_num



print(get_players_numbers())
print(create_lottery_numbers())
