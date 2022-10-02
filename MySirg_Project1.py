# Project - 1 Full Stack Web Development using Python MySirG

# Word Puzzle Game

import random

print("Five Times Chance will be given to Enter Word Puzzle Game")
chance=1
while chance<=5:
    correct_word=input("The Answer to Your Question is in the Word Puzzle Game Itself::-")
    if correct_word=='Game':
        break
    chance+=1
if chance==6:
    print("Missed a Golden Opportunity")
else:
    print("You Have Given The Correct Answer You Get a Chance To Play The Game")

def Puzzle_word(wrd):
    convert=random.sample(wrd,k=len(wrd))
    return ''.join(convert)

def printPuzzleQuestion(word,score):
    problem_word=Puzzle_word(word)
    print("\n Solve This Problem")
    print(problem_word)

    userword=input()
    print()
    if userword.upper()==word:
        print("Correct")
        score+=1
    else:
        print("Wrong")
        score-=1
    return score

def Start_Game():
    score=0
    words=["FATHER","BREAK","COUNTRY","PEN","SPORT","BALL","BOY","PLAYER","ELEPHANT","ROHIT"]
    words=random.sample(words,k=len(words))
    for word in words:
        score = printPuzzleQuestion(word,score)

    print("your Total score is",score)

    print()
    
Start_Game()




    
    





    
    
    

   

  



# if problem=='FATHER':
#     print("correct")
# else:
#     print("wrong")
# if problem=='TIME':
#     print("correct")
# else:
#     print("wrong")
# if problem=='CRY':
#     print("correct")
# else:
#     print("wrong")
# if problem=='GREEN':
#     print("correct")
# else:
#     print("wrong")
# if problem=='AEROPLANE':
#     print("correct")
# else:
#     print("wrong")

    


    


  
    









        
        



        




