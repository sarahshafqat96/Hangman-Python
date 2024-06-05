import Hangmanart
import Hangmanwordbank
import random

User_name = input("Please enter your name: ") #Ask the user to enter their name
print(f"Welcome {User_name}. Lets start!\n") #Welome the user

Comp_choice = list(random.choice(Hangmanwordbank.word_list)) #Computer chooses a random word from Hangmanwrdbank and converts it to a list
User_Guess = ["_"] * len(Comp_choice) #Make an array filled with "_" of Computer's chosen word's length
letter_guessed = [] #Initialize an empty array to append the letters that User has guessed already 
Game_Lives = 0 #Initialize the Game_Lives variable to zero

while (Game_Lives <= 6): #Hangman stick has 7 stages thsu the while loop starting with 6
        if("_" not in User_Guess): #If there is no "_" in the User_Guess list, that means User has guessed the entire word
            print("\nCongratulations, you guessed the word correctly")
            break
        else:    
            User_input = input("Enter any character from a to z: ").lower() #Otherwise ask the user to enter any character of their choice
            if(User_input in letter_guessed): #If that letter is in the letter_guessed array than inform the User that he has guessed it already
                print("You have already guessed this letter")
                continue
            elif (User_input not in Comp_choice): #Otherwise check if User's input character is not present in the word chosen by the Computer
                    print(f"Oops you have lost a life {Hangmanart.Stages[Game_Lives]}") #Then user looses a life and depending on the Game_Life, the Hangman stick is shown
                    Game_Lives += 1
                    if(Game_Lives == 7): #If Game_Lives have exceeded 6
                            print(Hangmanart.logo) #Then print the hangman logo and game ends
                            print(f"THE WORD WAS {(''.join(Comp_choice)).upper()}. BETTER LUCK NEXT TIME") #Computer's chosen word is displayed which the User was unable to guess
            else:
                for i in range(len(Comp_choice)): #Otherwise loops over the Comp_choice list
                    if(User_input == Comp_choice[i]): #And if User's input charater matches any of the Comp_choice's word
                            User_Guess[i] = User_input #Then add that character in the same position as that of Comp_choice list
            letter_guessed.append(User_input) #Append User's input in the letter_guessed array
            print(User_Guess) #Keep printing User_Guess array after every turn

