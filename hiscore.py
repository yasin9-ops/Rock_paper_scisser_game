import random
def game():
    print("you are playing Free Fire.....")
    score = random.randint(1,100)
    with open("hiscore.txt","r")as f:
        hiscore = f.read()
        if(hiscore == ""):
            hiscore = 0
        else:
            hiscore = int(hiscore)
    print(f"Your score is: {score}")
    if(hiscore<score):
        with open("hiscore.txt", "w")as f:
            f.write(str(score))
    return score
            
game()
