def game():
  import random
  print("\n\n----Welcome to ROCK PAPER SCISSORS game-----")
  print("\n\nRULES")
  print("\n1.Rock wins against Scissors\n2.Paper wins against Rock\n3.Scissors wins against Paper")
  Rock=("""
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  """)


  Paper=("""
       _______
  ---'    __)__
             ______)
            _______)
           _______)
  ---.__________)
  """)

  Scissors=("""
      _______
  ---'   __)__
            ______)
         __________)
        (____)
  ---.__(___)
  """)
  image=[Rock,Paper,Scissors]
  user_choice=int(input("\n\nselect any one of the choice\n0 for rock\n1 for paper\n or \n2 for scissor"))
  if user_choice>=3 or user_choice<0:
    print("Invalid,You lose")
  else:
    print(f"You choose {user_choice}")
    print(image[user_choice])

    computure_choice=random.randint(0,2)
    print(f"Computure choose {computure_choice}")
    print(image[computure_choice])

    if (user_choice==0) and (computure_choice==2):
      print("You win")
    elif (user_choice==2) and (computure_choice==0):
      print("You loss")
    elif user_choice>computure_choice:
      print("You win")
    elif computure_choice>user_choice:
      print("You lose")
    elif user_choice==computure_choice:
      print("It's a draw")
  repeat=input("\n\nYou want to play this game again?Type Y for yes and N for no----->").upper()
  if repeat=="Y":
        game()
  else:
        print("\n\nThanks for playing")
game()