import random
import csv
import os.path
import pandas as pd


Player_details =[] # list to save players data.
print("\n---------WELCOME TO [Guess The Number] GAME----------")
print("\nHello! What is your name ?")
name = input()
Player_details.append(name) # name of the player will be add to Player_details.
print("\nWelcome Mr "+ name,".\n")


class Guessing:
    
    def __init__(self, given_range): # the initializer method that is first run as soon as the object is created.
        self.result = random.randint(1,given_range)
    
    def guess(self,number_of_guesses):
        self.number_of_guesses = number_of_guesses # for picking number_of_guesses according to levels.
        guess_count = 0
        while(guess_count < number_of_guesses):
            print("\nGuess a number between 1 and 12 :")
            guess_count = guess_count + 1
            guess = int(input())
            if guess < self.result :# checking whether the random number is greater than the guessed number.
                print("Wrong, Your guess is lessthan the number.")
            if guess > self.result :# checking whether the random number is less than the guessed number.
                print("Wrong, Your guess is greater than the number.")
            if guess == self.result :# checking whether the random number is equal to the guessed number.
                break;

        def Result():# checking whether the player won or lost the game.
            if guess == self.result:
                    print("\nCorrect! Yaaaay good job,! you guessed my number in ", guess_count, " guesses!")
                    k = "Won"
                    Player_details.append(k)
            if guess != self.result:
                    print("\nSorry the number i was thinking was ",self.result)
                    print("Better luck next time.")
                    k = "Lost"
                    Player_details.append(k)
        Result()


    
    
if __name__ == '__main__':# Here __name__ was indeed set to "__main__" so that above functions will be executed when we call.


   

    while(True):
        print("Here as this is a game ")
        print("Enter 1 for is a Easy level game play,")
        print("Enter 2 for is a Medium level game play,")
        print("Enter 3 for is a Hard level game play,")
        print("Enter 4 to check previous player's data,")
        print("Enter 5 for exiting the game.")
        
        print("\n************* [Main Menu] ***************")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("4. Player's Details")
        print("5. Exit")
        print("Select any one  of the above choices: ")
        user_choice = int(input())

        if user_choice == 1:
            print("\n\n***[Easy]***")
            choice = "Easy"
            Player_details.append(choice)
            print("\nSee I will think of a number between 1 and 12 and you have to guess that number in less than 4 guesses!\n")
            number_of_guesses = 4
            play=Guessing(12) # intializing the class before trying to acess any of the class methods.
            play.guess(number_of_guesses)

        elif user_choice == 2:
            print("\n\n***[Medium]***")
            choice = "Medium"
            Player_details.append(choice)
            print("\nSee I will think of a number between 1 and 12 and you have to guess that number in less than 3 guesses!\n")
            number_of_guesses = 3
            play=Guessing(12)# intializing the class before trying to acess any of the class methods.
            play.guess(number_of_guesses)

        elif user_choice == 3:
            print("\n\n***[Hard]***")
            choice = "Hard"
            Player_details.append(choice)
            print("\nSee I will think of a number between 1 and 12 and you have to guess that number in less than 2 guesses!\n")
            number_of_guesses = 2
            play=Guessing(12)# intializing the class before trying to acess any of the class methods.
            play.guess(number_of_guesses)
            
        elif user_choice == 4:
            print("\n\n**********[Player's Details]*************\n")
            choice = "Player's Details"
            Player_details.append(choice)
            df = pd.read_csv("players.csv")# players.csv file is being read by the pandas module.
            print(df.head(20))
            k = "Checked"
            Player_details.append(k)    
        
            

        elif user_choice == 5:
            print("\nThank You!")
            choice = "Exit"
            Player_details.append(choice)
            k = "Aborted"
            Player_details.append(k)


            
        else:
            print("Please enter a valid option")
            break;
        break;
        
        
        
        
# Below code is to store player data in a csv file.
# This file will be created as soon as the program execution is completed. So that you can delete the file and it will not
# cause any error.
        
with open('players.csv', 'a', newline='') as file:           #Here the file will be created and players data will be appended to that file.
    
            writer = csv.writer(file)                        # player data will be entered in to the csv file.
    
    
            if os.stat('players.csv').st_size == 0:          #checking whether the file is present in your device.
                writer.writerow(["Name", "Choice", "Result"])# if present this line will not be executed.
            writer.writerow(Player_details)                  # here i am going to append Player_details list in to csv in to 
                                                             # new row for one time execution of the code
