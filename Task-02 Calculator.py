num1=int(input("Enter your first number"))
num2=int(input("Enter your second number"))
choice=int(input("select your option\n1 for addition\n2 for subtraction\n3 for multiplication\n4 for division\n5 for remainder--->"))
if choice==1:
   addition=num1+num2
   print(f"addition of two number gives {addition} ")
elif choice==2:
   subtraction=num1-num2
   print(f"subtraction of two number gives {subtraction} ")
elif choice==3:
   multiplication=num1*num2
   print(f"product of two number gives {multiplication} ")
elif choice==4:
   if num2==0:
    print("Invalid")
   else:
     division=num1/num2
     print(f"division of two number gives{division}")
else:
  remainder=num1%num2
  print(f"remainder of two number gives{remainder}")