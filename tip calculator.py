'''This code is building a simple tip calculator '''

# code:
print("Welcome to Tip Calculator")
total=float(input("What is the total amount of bill? "))
tip=int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people=int(input("How many people are going to split this bill? "))

# calculations
tip_amount=(tip/100)*total
total_amount=total+tip_amount 
each_share=total_amount/people 

# to display final answer
print(round(each_share,2))