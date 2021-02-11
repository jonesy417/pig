# Austin Jones
# Game of Pig
import random

def askUsers() -> str:
    """Asks players for Usernames"""
    global player1
    player1 = input('Please Enter a Username for Player 1: ')
    global player2
    player2 = input('Please Enter a Username for Player 2: ')
#assert askUsers() == str(player1,player2)

def possibilities() -> str:
    """Adds All Possible Outcomes for Rolls, Adds Weights for each outcome"""
    allpos = ['Double Side', 'Double Razor', 'Double Trot', 'Double Snout', 'Double Jowler', 'Oinker', 'Piggyback', 'Mixed Combo']
    global rollweight
    rollweight = "".join(random.choices(allpos, weights=(30, 13, 11, 7, 5, 1, 1, 32), k=1))
#assert possibilities() == str(rollweight)

def game() -> str:
    """Calculates whose turn it is and each players scores based on roles, averages mixed combo points to 7"""
    command = ""
    turns = 0
    turnScore1 = 0
    turnScore2 = 0
    while turns < 1000:
        print("{} Points:{} ----- {} Points:{}".format(player1, turnScore1, player2, turnScore2))
        print('===================Turn:{}===================='.format(turns))
        if turns % 2 == 0 or turns == 0:
            print("{} Roll or Pass? ".format(player1))
            command = input(" ").lower()
            if command == "roll":
                possibilities()
                if rollweight == 'Double Side':
                    doubleSide = 1
                    print('{} rolled {}, {} points added'.format(player1, rollweight, doubleSide))
                    print('-------------------------------')
                    turnScore1 += 1
                    turns += 1
                elif rollweight == 'Double Razor':
                    doubleRazor = 20
                    print('{} rolled {}, {} points added'.format(player1, rollweight, doubleRazor))
                    print('-------------------------------')
                    turnScore1 += 20
                    turns += 1
                elif rollweight == 'Double Trot':
                    doubleTrot = 20
                    print('{} rolled {}, {} points added'.format(player1, rollweight, doubleTrot))
                    print('-------------------------------')
                    turnScore1 += 20
                    turns += 1
                elif rollweight == 'Double Snout':
                    doubleSnout = 40
                    print('{} rolled {}, {} points added'.format(player1, rollweight, doubleSnout))
                    print('-------------------------------')
                    turnScore1 += 40
                    turns += 1
                elif rollweight == 'Double Jowler':
                    doublejowler = 60
                    print('{} rolled {}, {} points added'.format(player1, rollweight, doublejowler))
                    print('-------------------------------')
                    turnScore1 += 60
                    turns += 1
                elif rollweight == 'Oinker':
                    oinker = 0
                    print('{} rolled {}, {} points added'.format(player1, rollweight, oinker))
                    print('-------------------------------')
                    turnScore1 = turnScore1 - turnScore1
                    turns += 1
                elif rollweight == 'Piggyback':
                    Piggyback = 1000
                    print('{} rolled {}, {} Wins!!!'.format(player2, rollweight, player2))
                    print('-------------------------------')
                    turnScore2 += 1000
                    turns += 1
                    print('===================Game of Pig Results====================')
                    print("{} Points:{} ----- {} Points:{}".format(player1, turnScore1, player2, turnScore2))
                    print('===================Turn:{}===================='.format(turns))
                    break
                else:
                    mixedCombo = 7
                    print('{} rolled {}, {} points added'.format(player1, rollweight, mixedCombo))
                    print('-------------------------------')
                    turnScore1 += 7
                    turns += 1
            elif command == 'pass' or 'PASS' or 'Pass':
                print("You've passed your turn.")
                print('-------------------------------')
                turnScore1 += 0
                turns += 1
            else:
                print("Invalid Input")
        if turns % 2 == 1:
            print("{} Roll or Pass? ".format(player2))
            command = input(" ")
            if command == "roll":
                possibilities()
                if rollweight == 'Double Side':
                    doubleSide = 1
                    print('{} rolled {}, {} points added'.format(player2, rollweight, doubleSide))
                    print('-------------------------------')
                    turnScore2 += 1
                    turns += 1
                elif rollweight == 'Double Razor':
                    doubleRazor = 20
                    print('{} rolled {}, {} points added'.format(player2, rollweight, doubleRazor))
                    print('-------------------------------')
                    turnScore2 += 20
                    turns += 1
                elif rollweight == 'Double Trot':
                    doubleTrot = 20
                    print('{} rolled {}, {} points added'.format(player2, rollweight, doubleTrot))
                    print('-------------------------------')
                    turnScore2 += 20
                    turns += 1
                elif rollweight == 'Double Snout':
                    doubleSnout = 40
                    print('{} rolled {}, {} points added'.format(player2, rollweight, doubleSnout))
                    print('-------------------------------')
                    turnScore2 += 40
                    turns += 1
                elif rollweight == 'Double Jowler':
                    doublejowler = 60
                    print('{} rolled {}, {} points added'.format(player2, rollweight, doublejowler))
                    print('-------------------------------')
                    turnScore2 += 60
                    turns += 1
                elif rollweight == 'Oinker':
                    oinker = 0
                    print('{} rolled {}, Score Reduced to Zero :('.format(player2, rollweight))
                    print('-------------------------------')
                    turnScore2 = turnScore2 - turnScore2
                    turns += 1
                elif rollweight == 'Piggyback':
                    Piggyback = 1000
                    print('{} rolled {}, {} Wins!!!'.format(player2, rollweight, player2))
                    print('-------------------------------')
                    turnScore2 += 1000
                    turns += 1
                    print('===================Game of Pig Results====================')
                    print("{} Points:{} ----- {} Points:{}".format(player1, turnScore1, player2, turnScore2))
                    print('===================Turn:{}===================='.format(turns))
                    break
                else:
                    mixedCombo = 7
                    print('{} rolled {}, {} points added'.format(player2, rollweight, mixedCombo))
                    print('-------------------------------')
                    turnScore2 += 7
                    turns += 1
            elif command == "pass" or "PASS" or "Pass":
                print("You've passed your turn.")
                print('-------------------------------')
                turnScore2 += 0
                turns += 1
            else:
                print("Invalid Input")
# assert game() == str(player1,player2,turnscore1,turnscore2)

def main() -> str:
    """Runs askUsers() function and game() function"""
    askUsers()
    game()
#assert main() == str(askUsers(), game())

if __name__ =="__main__":
    main()