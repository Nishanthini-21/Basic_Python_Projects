'''This code is building a rock paper scisaor game'''


from random import randint
rock='''
          ___..__
  __..--""" ._ __;
              "-..__
            '"--..__";
 ___        '--...__";
    `-..__ '"---..._";
          """"----'   
'''
paper=''' __________
         |DAILY NEWS|
         |&&& ======|
         |=== ======|
         |=== ==000$|
         |[_] ======|
         |=== ===!##|
         |__________|
'''
scissors='''
    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.

'''
game=[rock,paper,scissors]
user_choice=int(input("Enter your choice 0 for rock, 1 for paper and 3 for scissor?\n"))
if user_choice>3 or user_choice<0:
    print("Invalid entry!")

else:
    print(game[user_choice])
    computer_choice=randint(0,2)
    print(game[computer_choice])
    print()
    if user_choice==computer_choice:
        print("match draw")
    elif user_choice==0 and computer_choice==2:
        print("you won")
    elif computer_choice==0 and user_choice==2:
        print("you lose2")
    elif computer_choice>user_choice:
        print("you lose")
    elif user_choice>computer_choice:
        print("you won")