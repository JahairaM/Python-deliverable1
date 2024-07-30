name_input = input("Welcome to GC mini golf! What is your name?")
game_input = input("Hi, " + name_input + " would you like to play 3 or 6 holes today?")
score = 0
course_par = 0
if int(game_input) == 3:
    hole_1 = int(input("How many putts for hole 1? (par: 3) "))
    hole_2 = int(input("How many putts for hole 2? (par: 3) "))
    hole_3 = int(input("How many putts for hole 3? (par: 3) "))
    score = hole_3 + hole_1 + hole_2
    course_par = 9
elif int(game_input) == 6:
    hole_1 = int(input("How many putts for hole 1? (par: 3) "))
    hole_2 = int(input("How many putts for hole 2? (par: 3) "))
    hole_3 = int(input("How many putts for hole 3? (par: 3) "))
    hole_4 = int(input("How many putts for hole 4? (par: 3) "))
    hole_5 = int(input("How many putts for hole 5? (par: 3) "))
    hole_6 = int(input("How many putts for hole 6? (par: 3) "))
    score = hole_3 + hole_1 + hole_2 + hole_4 + hole_5 + hole_6
    course_par = 18
else:
    game_input = input("please enter either 3 or 6")

# print(f"Good game, {name_input}. Your total score was: {str(score - course_par)} ")
par = score - course_par
if score > course_par :
    print("Nice try,", name_input , "your total score was +" + str(par))
elif score < course_par :
    print("Great job!", name_input, "your total score was " + str(par))
else:
    print("Good game", name_input,"!""Your total score is 0")