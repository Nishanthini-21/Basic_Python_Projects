import random

letters=['a','f','P','Q','R','S','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','T','b','c','d','e','U','V','W','X','Y','Z']
# numbers=[1,2,3,4,5,6,7,8,9,0]
specialcharacters=['@','$','%','^','*']

print("Password Generator")
password=""

letter=int(input("Enter how many letters do you need?"))
for i in range(letter):
    password=password+random.choice(letters)

number=int(input("Enter how many numbers do you need?"))
for i in range(number):
    password=password+str(random.randint(0,9))

specialcharacter=int(input("Enter how many specialcharacters do you need?"))
for i in range(specialcharacter):
    password=password+random.choice(specialcharacters)   

password_list=list(password)
random.shuffle(password_list)
print("your password generated is",''.join(password_list))