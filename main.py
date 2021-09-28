# prining the treasure island logo
print(''' _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
''')

# printing the treasure logo
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
''')

# printing the print function in output "Welcome to the treasure island"
print("Welcome to the Treasure Island.")

# printing the print function "your mission is to find the treasure island"
print("Your mission is to find the treasure.")

# Taking the first input from user to continue the game, here is two option to choose 'left' or 'right' .
user_input = input("you are at a cross road. Where do you want to go? Type 'left' or 'right' \n").lower()

# if user input == right than user loose and output will be the print function ("you fall in the hole. Game over")
if user_input == "right":
    print(" you fall in the hole. Game Over")

# if user input == left than user continue to next challenge , again with option "swim" or "wait"
    user_input2 = input("you have another challenge choose 'swim' or 'wait' \n").lower() 
   
    #if user input == swim than user loose and output will be the print function ("you became shark dinner. Game over")
    if user_input2 == "swim":
        print("you became the shark dinner. Game Over")

    #if user input == wait than user face another challenge to choose, with three option "red", "blue" or "yellow"    
    elif user_input2 == "wait":
        user_input3 = input("you have face another challenge, which door you open 'red' , 'blue' or 'yellow'\n").lower() 
        
        #if user input == blue than user lost the game and output will be the print function "you have enter int lion den.Game over"
        if user_input3 == "blue":
            print("you have enter in Lion den. Game Over")  
        
        # if user input == red than user lost the game and output will be the print function "you have enter in Ghost room. Game over"    
        elif user_input3 == "red":
            print("you have enter in Ghost room. Game Over") 
        
        # if user input == yellow than user lost the game and output wil be the print function "you reach the treasure island"       
        elif user_input3 == "yellow":
            print("you Reach the Treasure Island")  
            
            # last output after winning the game
            print("you Won the Game") 
          
