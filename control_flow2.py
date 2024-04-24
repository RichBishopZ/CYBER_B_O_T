import random

numbers_to_guess = [random.randint(1, 10) for number in range (5)]

print("Welcome to the game ! try pick a number between 1 and 10.")  

amount_staked = int(input("Enter the amount you want to stake: "))
                    
guessed_number = []

for num in range (5):
    guessed_number.append(int(input("Enter the number between 1 and 20: ")))
    
matches =0

for guessed_number in guessed_number:
    if guessed_number in numbers_to_guess:
        matches += 1
        
if matches > 0:
    print(f"Congratulations! You Matched {matches} number (s) You win {amount_staked * matches}!")
    
else: 
    print("Sorry, you didn't match any numbers. Better luck next time!")