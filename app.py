#Udemy Course Work - Lottery App

#Import the random class
import random

def menu():
    """Controlling method that
    1. Ask players for numbers
    2. Calculate the lottery numbers
    3. Print out the winnings
    """
    players_numbers = get_players_numbers()
    lottery_numbers = create_lottery_numbers()
    if len(players_numbers.intersection(lottery_numbers)) == 1:
        print("Congratulations, you have won 10 Euro!!!")
    elif len(players_numbers.intersection(lottery_numbers)) == 2:
        print("Congratulations, you have won 20 Euro!!!")
    elif len(players_numbers.intersection(lottery_numbers)) == 3:
        print("Congratulations, you have won 30 Euro!!!")
    elif len(players_numbers.intersection(lottery_numbers)) == 4:
        print("Congratulations, you have won 40 Euro!!!")
    elif len(players_numbers.intersection(lottery_numbers)) == 5:
        print("Congratulations, you have won 50 Euro!!!")
    elif len(players_numbers.intersection(lottery_numbers)) == 6:
        print("Congratulations, you have won it all!!!")
    else:
        print("Sorry, you have won nothing!!!")






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




if __name__ == "__main__":
    menu()
