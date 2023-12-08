import random
import string

characters=string.digits+string.ascii_letters+string.punctuation
print("----Welcome to the password generator----")
user_length=int(input("Enter input length of the password\n\n"))
password=[]
for _char in range(1,user_length+1):
  password+=random.choice(characters)
#shuffling the list
random.shuffle(password)

#converting list into a string
Password=""
for char in password:
  Password+=char
print(f"Your password is {Password}")