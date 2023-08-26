#The game() function in a program lets a user play a game and returns the score as a integer.You need to read a file "Hiscore.txt" which is either blank or contains the previous Hi-score.You need to write a program to update the Hi-score whenever game() breaks the Hi-score.

def game():
    score=int(input("Enter score: "))
    return score
x=game()
with open("Hiscore.txt","r") as f:
    y=int(f.read())
if (str(y)=="") :
    with open("Hiscore.txt","w") as f:
        f.write(str(x))
if (x >y):
    with open("Hiscore.txt","w") as f:
        f.write(str(x))
with open("Hiscore.txt","r") as f:        
    print ("Hi-Score : ",f.read())
