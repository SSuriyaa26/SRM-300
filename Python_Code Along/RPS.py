import random # to make random RPS choice

#function to get choices
def get_choice():
    #player_choice = "rock" # hard coding values
    
    player_choice = input("Enter a choice (Rock, Paper or Scissors):")# getting user input
    
    options = ["rock",'paper',"scissor"] # list with options
    computer_choice =random.choice(options)# random assignment
    choices = {"player":player_choice,"computer":computer_choice} # dictionary storing the values
    return choices
'''
choices=get_choice()
print (choices)
just an example done in the video for showing how functions work


food =["pizza","dosa","carrot"]
dinner = random.choice(food)
print(dinner)
example from video on how random works

a=5
b=3
if b>a:
    print("Yes")
else:
    print("No")
example of how if statemetns work   
'''
def check_win(player , computer):
    print(f"You chose {player} and computer chose {computer}")
    '''
               elif player == "rock" and computer =="scissor":
                   return "You Win"
               elif player == "rock" and computer =="paper":
                       return "You Lose"
               
               Before refactoring
        '''  
    if player == computer:
        return "Tie"
    
    elif player == "rock":
        if computer == "scissor":
            return "You Win"
        else:
            return "You Lose"
    elif player =="paper":
            if computer == "rock":
                return "You Win"
            else:
                return "You Lose"
    elif player =="scissor":
                if computer == "paper":
                    return "You Win"
                else:
                    return "You Lose"
    
choices = get_choice()

result = check_win(choices["player"],choices["computer"])

print(result)