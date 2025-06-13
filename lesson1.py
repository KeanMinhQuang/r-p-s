import random
breakLoop = False

print("Welcome to rock, paper, scissors!")

while breakLoop == False: ##The loop will continue until the user decides to stop playing
    username = input("Enter your username: ") ##Username
    botWins = 0 ##Bot wins counter
    userWins = 0 ##User wins counter
    
    while username == "": ##If the username input is empty, the system will ask for a name again
        username = input("Username invalid. Enter your username: ")
    
    maxWins = int(input("Enter the maximum number of wins to end the game (default is 3): ") or 3) ##Maximum wins to end the game, default is 3
    
    while maxWins < 1: ##If the input is less than 1, the system will ask for a number again
        maxWins = int(input("Invalid number. Enter a number greater than 0: "))
    
    while botWins < maxWins and userWins < maxWins: ##Run until either the bot or the user has 3 wins
        result = input("Enter your choice (rock, paper, scissors): ").lower() ##Input user's choice
    
        while result not in ["rock", "paper", "scissors"]: ##If the input is invalid, the system will ask again for a choice
            result = input("Invalid choice. Enter rock, paper, or scissors: ").lower()
        
        random_choice = random.choice(["rock", "paper", "scissors"]) ##Bot's choice
        
        if random_choice == result: ##If the bot's choice is the same as the user's
            print("Tied. You both chose "+ result +". No one gets a point")
        elif (random_choice == "rock" and result == "scissors") or \
            (random_choice == "paper" and result == "rock") or \
            (random_choice == "scissors" and result == "paper"): ##If the bot's choice beats the user's
            print("You lose this match. The bot chose " + random_choice + " and you chose " + result)
            botWins += 1
        else: ##If the user's choice beats the bot's
            print("You win this match. The bot chose " + random_choice + " and you chose " + result)
            userWins += 1
            
        print("Current score: " + username + " " + str(userWins) + " - Bot " + str(botWins))
    
    if botWins == maxWins: ##If the bot has 3 wins
        print("The game has ended, the bot won")
    elif userWins == maxWins: ##If the user has 3 wins
        print("The game has ended, you won")
        
    retry = input("Would you like to replay? (yes/no): ").lower() ##Ask if the user wants to replay
    
    if retry == "yes": ##If yes
        print("Game has been restarted")
        breakLoop = False
    elif retry == "no": ##If no
        print("Game has ended")
        breakLoop = True ##Break the loop
        break