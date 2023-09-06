name = input("Welcome to GC Mini Golf. What is your name? ")
total_holes = int(input("Hi," +name +"! Would you like to play 3 or 6 holes today?"))
if total_holes == 3:
   hole_1 = int(input ("How many puts for hole 1? (par is 3)"))
   hole_2 = int(input("How many puts for hole 2? (par is 3)"))
   hole_3 = int(input("How many puts for hole 3? (par is 3)"))
   total_score = int(hole_1 + hole_2 + hole_3 - 9)
   par = total_score == 9

else:
   hole_1 = int(input("How many puts for hole 1? (par is 3)"))
   hole_2 = int(input("How many puts for hole 2? (par is 3)"))
   hole_3 = int(input("How many puts for hole 3? (par is 3)"))
   hole_4 = int(input("How many puts for hole 4? (par is 3)"))
   hole_5 = int(input("How many puts for hole 5? (par is 3)"))
   hole_6 = int(input('How many puts for hole 6? (par is 3)'))
   total_score = int(hole_1 + hole_2 + hole_3 + hole_4 + hole_5 + hole_6 - 18)
   par = total_score == 18


if total_score == par:
   print(f"Good game, {name}! Your total score was 0")
if total_score < par:
   print(f"Great job, {name}! Your total score was {total_score}.")
if total_score > par:
   print(f"Nice try, {name}! Your total score was +{total_score}.")