import random
number=random.randint(1,50)
guess=0
while guess!=number:
  guess=int(input("Hello friend, Guess the number between 1 to 50:"))
  if(guess<number):
        print("Guess Higher Number you entered incorrect number")
  elif(guess>number):
        print("Guess Lower Number you entered incorrect number")
  else:
        print("Yuuppiiee You Won The Game")
