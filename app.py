#Udemy Course Work - Lottery App

#Get the Lottery numbers
def get_players_numbers():
    numbers = str( raw_input("Enter the numbers separated by commas: "))
    #Now split the string into a list using the string split method
    numbers_in_list=numbers.split(",")
    #Now get a set of numbers instead of list of string by using set comprehension, same as list just returns a set.
    numbers_in_set={int(x) for x in numbers_in_list}
    #Now return a set from the invoking call
    return numbers_in_set
