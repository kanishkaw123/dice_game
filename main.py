import random  #this module is used to use randint() function which returns a random rumber.
import sys      
import time
import os
import platform


"""The floowing Player class This class will be used to create objects for both players."""
class Player:

    #Following function defines the general properties for the class
    def __init__(self):
        self.name=""    # name refered to the player's name
        self.score=0        # score is the player's total points
        

    #This is the general function to get two random numbers and give te points according to given rules.
    def roll(self):
        roundScore=0   # roundScore is the points for particular round
        dice1 = random.randint(1,7)
        loadingBar()   #This will show a dinamic text "playing..." for a better user experience
        dice2 = random.randint(1,7)

        roundScore = dice1 + dice2

        #This condition checks if the roll is a double and allow player to roll an extra dice.
        if dice1==dice2:

            print(f"You're so lucky. You rolled a double of {dice1} and you get a extra dice to roll \n")

            print("Plase press any key to play the extra dice")
            wait()
            clean()

            loadingBar()
            dice3=random.randint(1,7)  
            print(f"You rolled {dice3} for the extra turn.")
                
            roundScore+=dice3
            print(f"Points for this turn {roundScore}")

            self.score+=roundScore
            
        #This condition checks if the current roll gave an even number.
        elif roundScore%2==0 :
            print(f"You rolled {dice1} and {dice2}. You get 5 bonus poins")
            roundScore+=5
            print(f"Total points for this round is {roundScore} points.")
            self.score+=(roundScore)
            
        #This condition checks if the current roll gave an odd number.
        else:
            print(f"You rolled {dice1} and {dice2}. Better luck next time.")
            roundScore-=5

            # The condition check if the total is positive or 0 after deducting 5 points from it.
            if roundScore >= 0 :
                print(f"Total points for this for this round = {roundScore}")
                self.score+=roundScore 
            
            # This condition runs if the total is negative after deducting 5 points from it.
            else:

                #This code adds the total of this round to the score.
                self.score+=roundScore

                #This condition checks whether the score is negative or 0 after adding the total of the round.
                if self.score<=0:
                    print("You don't have enough score to deduct 5 points. Your score will be set to 0")
                    self.score=0
                
                #This code checks if the score is positive after adding the total of the round.
                else:
                    print(f"{roundScore} points will be deducted from your score.\n")
    

        print(f"\n \n New score = {self.score}")
        time.sleep(5)

#The forrowing function is to pause the program for any keyboard input
def wait():
    if platform.system()=="Windows":
        os.system("pause >nul")
    else:
        os.system('read -s -n 1 -p ""')
        print()



#The following function is to clean the shell
def clean():
    if os.name=="nt":
        os.system("cls")
        
    else:
        os.system("clear")


#The following function is to display a dynamic "playing..." ststement for a better user experience
def loadingBar():
    for i in range(2):
        sys.stdout.write("\rPlaying    ")
        time.sleep(0.2)
        sys.stdout.write("\rPlaying .  ")
        time.sleep(0.2) 
        sys.stdout.write("\rPlaying .. ")
        time.sleep(0.2) 
        sys.stdout.write("\rPlaying ...")
        time.sleep(0.2)
    
    sys.stdout.write("\r           \n")

#The following funcion register the new players
def register(loginDetailsFile,usersDict):
    
    newPlayer=Player() #"newPlayer" local variable will be used as a object made by Player class throughout this function.
    
    #following list will be used to validate the first name, last name and the password.
    specialCharacters=["!","£","$","$","%","^","&","*","(",")","_","-","+","=","{","}",":",";","'","@",",","/","<",">","?"]

    """The following while loop will take player's details(first name and second name) and
        they will be validated. The while loop will run untill the player enter valid deails."""
    while True:
        specialCharactersInName=0
        numbersInName=0
        lengthOfName=True
        print("Please enter your Details\n\n")
        
        firstName=(input("Please enter your first name: ").strip().lower()).capitalize()
        
        if len(firstName)>=2:
            for character in firstName:
                if character in specialCharacters:
                    specialCharactersInName += 1
                else:
                    pass

                if character.isnumeric():
                    numbersInName +=1
                else:
                    pass
        else:
            lengthOfName=False
        
        
        lastName=(input("Please enter your last name: ").strip().lower()).capitalize()
        if len(lastName)>=2:
            for character in lastName:
                if character in specialCharacters:
                    specialCharactersInName += 1
                else:
                    pass

                if character.isnumeric():
                    numbersInName +=1
                else:
                    pass
        else:
            lengthOfName=False

        if lengthOfName==False:
            print("\n*Your first name and last name should be longer than two characters!")

        #If the player has entered valid details the first name and last name will be appended to the names list and while loop will stop.
        elif specialCharactersInName==0 and numbersInName==0:
            
            break
        else:
            print("\n The details you entered are not valid\n")
            print(" * Your first name and last name should not include any numbers or special characters.")

        print("\n   Please press any key to re-enter your name.")
        wait()
        clean()

    clean()

    """ In the following while loop, a new password will be taken from the user and it will be validated.
        The while loop will run until the user enter a valid password. """
    while True:

        password=input(f"Hello! {firstName}. Please enter a password:\n* Password must contain 1 capital letter , 2 numbers and 1 special character \n \n :  ").strip()
        if len(password)>=8 and len(password)<=16:

            specialCharactersInPassword=0
            numbersInPassword=0
            capitalLettersInPassword=0
            whiteSpacesInPassword=0

            for character in password:
                if character in specialCharacters:
                    specialCharactersInPassword +=1
                else:
                    pass

                if character.isnumeric():
                    numbersInPassword += 1
                else:
                    pass

                if character.isupper():
                    capitalLettersInPassword +=1
                else:
                    pass

                if character==" ":
                    whiteSpacesInPassword+=1
                else:
                    pass
            #If the user has entered a valid password, the while loop will stop from the followinf code.
            if specialCharactersInPassword>=1 and numbersInPassword>=2 and capitalLettersInPassword >=2 and whiteSpacesInPassword==0:
                break
            else:
                print("\nThe password you entered is not valid \n")
                if whiteSpacesInPassword>0:
                    print("* You cannot include spaces in your password")
                else:
                    pass

                if specialCharactersInPassword<1:
                    print("* Your password must contain at least 1 special character")
                else:
                    pass
                    

                if numbersInPassword<2:
                    print("* Your password must contain at least 2 numbers")
                else:
                    pass
                     
                if capitalLettersInPassword<1 :
                    print("* Your password must contain at least 1 capital letter")
                else:
                    pass
                
                print("\nPress any key to re-enter the password")
                wait()
                clean()
        else:
            print("\n Sorry!, Your password should be 8 to 16 characters long.")
            print(" Please press any key to re-enter the password")
            wait()
            clean()

    """In the following while loop, a new username will be generated for the user.
        The while loop will run until a new user name that is not already registered is generated 
        for the user."""                
    while True:
        userName=(firstName[:2]+lastName+str(random.randint(1,9))).lower()
        if userName not in usersDict:
                break
        else:
            pass

    """ In the following while loop, the user will be asked to enter the age and the age will be verified to make
        sure that the user is eligible to register and play the game. """
    while True:
        clean()
        age=input("Please enter your age: ")
        if age.isnumeric():
            if int(age)>=8:
                break
            else:
                print("You're not eligible to play the game.")
                exit()
        else:
            print("Please enter your age as a number.")
            time.sleep(3)
            
    clean()
    newPlayer.name=firstName+"-"+lastName
    print(f"\n Hello {newPlayer.name}! Your new username is {userName}.")
    time.sleep(3.5)
    clean()

    #In the following few lines, the new user's details will be registered in a external file called login.txt ,
    writableUserData=newPlayer.name+" "+userName+" "+password+"\n"
    dataFile=open(loginDetailsFile,"a")
    dataFile.write(writableUserData)
    dataFile.close()

    return newPlayer





def authenticate(playerNumber):

    thisFolder=os.path.dirname(os.path.abspath(__file__))
    loginDetailsFile=os.path.join(thisFolder,"login.txt")

    usersDict={}
    fileDataList=[]
    
    if os.path.isfile(loginDetailsFile):
        dataFile=open(loginDetailsFile,"r")
        for line in dataFile:
            fileDataList.append(line.split())
        dataFile.close()
        for userDataList in fileDataList:
            usersDict[userDataList[1]]=userDataList[2]
    else:
        pass


    userStatus=(input(f"\n Hello! Player-{playerNumber}. Do you have an account ( enter 'Yes' if you have) ?  ").strip()).lower()
    clean()
    if "y" in userStatus:
        while True:
            userName=(input("\n Please enter your username:  ").strip()).lower()
            if userName in usersDict:
                password=input(" Please enter your password: ").strip()
                if password==usersDict[userName]:
                    player=Player()
                    for userDataList in fileDataList:
                        if userName in userDataList:
                            player.name=userDataList[0]
                            break
                        else:
                            pass
                    clean()
                    break
                else:
                    userContinue=input("\n\nYour password is incorrect.\n\n Do want to try again (Enter ‘Yes’ you want to retry)?  ")
                    clean()
                    if "y" in userContinue:
                        pass
                    else:
                        print("See you next time")
                        exit()
            else:
                userContinue=input("Sorry! Your username is not registered. \n\n Do you want to try again (Enter ‘Yes’ you want to register)? ")
                clean()
                if "y" in userContinue:
                    pass
                else:
                    userRegister=input("Do you want to redister?  ")
                    if "y" in userRegister:
                        clean()
                        player=register(loginDetailsFile,usersDict)
                    else:
                        print("See you next time")
                        exit()
    else:
        player=register(loginDetailsFile,usersDict)


    print("You're authorised to play the game.")
    time.sleep(3)
    clean()
    return player

#This is the main part of the programme which includes the game    
def main():

    player1=authenticate(1)
    player2=authenticate(2)
    playersList=[player1,player2]
    for roundNumber in range(1,6): # runs the following code for 5 times in order to play 5 rounds.

        print(f"Round {roundNumber} begins")
        time.sleep(2)
        clean()

            #The following code runs for each player in a round(two times in a round)
        for player in playersList:
            print("***   Score Board   ***\n")
            print(f"Player {playersList[0].name} score =", playersList[0].score)
            print(f"Player {playersList[1].name} score =", playersList[1].score)
            print("\n \n \n")

            print("Hello",player.name,"! This is your",roundNumber,"round. \n")
            print("Please press any key to roll the dice. \n\n")
            wait()
            clean()

            print(f"Round {roundNumber} - ",player.name, "\n\n")
            player.roll()
            clean()

            

    """ The floowing code checks if the both players have same score and if so, the following coe will run
        it will let users to play with ony one dice"""
    if playersList[0].score==playersList[1].score:

        print("***    Score Board    ****")
        print(f"Player {playersList[0].name} score =", playersList[0].score)
        print(f"Player {playersList[1].name} score =", playersList[1].score)
        print("\n")

        print("The game is draw. Let's continue the game with one dice untill one of you win")

        time.sleep(3)
        clean()

        bonusRound=1
            #Following while function runs until one of the players get a higher score than the other.
        while playersList[0].score==playersList[1].score:


            for player in playersList:
                   
                print(f"Hello! {player.name}. This is your bonus round {bonusRound}. \n \n ")
                print("Please enter any key to continue.")
                wait()
                clean()
                
                print(f"{player} - Bonus round{bonusRound}.")
                loadingBar()
                bonusPoints=random.randint(1,7)
                print(f"You got {bonusPoints} points for this round")

                player.score+=bonusPoints

                
            bonusRound+=1
            print("***    Score Board    ****")
            print(f"Player {playersList[0].name} score =", playersList[0].score)
            print(f"Player {playersList[1].name} score =", playersList[1].score)
            print("\n")
            
        
    else:
        
        print("***    Score Board    ****")
        print(f"Player {playersList[0].name} score =", playersList[0].score)
        print(f"Player {playersList[1].name} score =", playersList[1].score)
        print("\n")

        
    if playersList[0].score > playersList[1].score:
        print(f"Conradulations! {playersList[0].name}. You win the game. \n \n")
        winnerOfGame=player1
    else:
        print(f"Conradulations! {playersList[1].name}. You win the game. \n \n")
        winnerOfGame=player2



    """ I am using the statements in line 119 and 120 because it allows user to run the code from
        any location in addition to the python path."""
    thisFolder=os.path.dirname(os.path.abspath(__file__))
    myFile=os.path.join(thisFolder,"high_score_data.txt")

    highScoreDict={}
    addableToHighscore=False # if the addable to highscore is true, name will be added to the highcore dictionary
        
    """Follwing code checks the existance of the "data.txt" file 
        and takes the data from it to "dataDict" dictionary. """
    if os.path.isfile(myFile):
        data=open(myFile,"r")
        for line in data:
            (name,score) = line.split()
            highScoreDict[name]=int(score)

        data.close()
    else:
        pass

    if bool(highScoreDict): #This checks if the dictionary is empty.
        """The follwing code firstly check if the winner is already in the dictionary 
            where he/she may have scored a highscore in a previous game. If the player's name found in the 
            dictionary, marks he got for the new round will be compared and assigned if the new score is more
            than existing score."""
        
        if winnerOfGame.name in highScoreDict:
            if highScoreDict[winnerOfGame.name]>=winnerOfGame.score:
                pass
            else:
                addableToHighscore=True 
        else:
            addableToHighscore=True 
    else:
        addableToHighscore=True



    if addableToHighscore:
        highScoreDict[winnerOfGame.name]=winnerOfGame.score
    else:
        pass
    

        

    print("***   Highscores   ***")
    
    playerRank=1
        
    for item in sorted(highScoreDict,key=highScoreDict.get,reverse=True):
        if playerRank>5:
            break
        else:
            pass  
        print(playerRank,item,"=",highScoreDict[item])  
        playerRank+=1

    highScoreData=open(myFile,"w")
    for winner in highScoreDict:
        highScoreData.write(winner)
        highScoreData.write(" ")
        highScoreData.write(str(highScoreDict[winner]))
        highScoreData.write("\n")
    highScoreData.close()
    print("\n \n \n")








#The game starts from here
if __name__ == "__main__":
    while True:
        print("                  Welcome to Katarina's dice game.")
        print("\n")
        print("                          Rules of the game")
        print("\n")
        print(" * Players have to play with two dice")
        print("\n * The points rolled from two dice will be added to the score.")
        print("\n * If a player rolled an even number in total from both dice in a round,\n   5 bonus points will be added to the player's score")
        print("\n * If a player rolled an odd number in total from both dice in a round,\n   5 points will be deducted from the player's score")
        print("\n * If a player’s score goes minus when deducting 5 pints, the score will be\n   set to zero")
        print("\n * If a player rolled a double, player will be given an extra dice to roll\n   and total from three dice will be added to the player's score")
        
        print("\n \n")
        print("Please press any key to start the game")
        wait()
        clean()

        main()
        playAgain=input("Do you want to play again?   ")
        if "y" in playAgain:
            clean()
        else:
            break
else:
    print("Sorry! Something went wrong")
    
        
    
print("Press any key to exit from the game.")
wait()
print("See You later...")
exit()


