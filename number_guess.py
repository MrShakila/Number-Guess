
import random

top_of_range = input("Type A Number  ")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print('Plaease Enter Number larger than 0 next time')
else :
     print('Plaease Enter A valid Number')
random_number =random.randrange(0,top_of_range)

print(random_number)

guess = 0

while True:
    guess+=1
    user_guess = input('Guess Your Number ')
    if user_guess.isdigit():
      user_guess=int(user_guess)
    else :
         print('Plaease Enter A valid Number')
         continue
    if user_guess ==random_number:
        print("Correct")
        guess-=1
        break
    elif user_guess<random_number:
        print("You Were below the number")
        continue
    else:
        print('You Were above the number')
        continue

print(
    "You Got It In " ,guess,"guess"
)