answer_one = "no"   
submitted_answer1 = input("Do I sleep?\n>")    
answer_two = "draw"    
submitted_answer2 = input("What do I do in my free time?\n>")    
answer_three = "no one noticed"    
submitted_answer3 = input("Maybe I lost my mind, but ______________\n>")   
answer_four = "princess"    
submitted_answer4 = input("What does my brother refer Hatsune Miku as?\n>")    
answer_five = "7"    
submitted_answer5 = input("How many tallies do I have?\n>")

def calculate():
    if answer_one.lower() == submitted_answer1:
     score = score + 1

    if answer_two.lower() == submitted_answer2:
       score = score + 1

    if answer_three.lower() == submitted_answer3:
       score = score + 1

    if answer_four.lower() == submitted_answer4:
       score = score + 1

    if answer_five.lower() == submitted_answer5:
       score = score + 1

       print("Score: " + str(score) + "/5")


    calculate()
