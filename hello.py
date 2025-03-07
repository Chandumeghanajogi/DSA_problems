import random
def game(user,computer):
    if user==computer:
        return f"game is tie"
    elif (user=="rock" and computer=="scissor") or (user=="paper" and computer=="rock") or (user=="scissor" and computer=="paper"):
        return f"user wins"
    else:
        return f"computer wins"
    

choices=["rock","paper","scissor"]
while True:
    user_choice=input("enter the user choice here").lower()
    if user_choice=="exit":
        print(f"thank you....")
        break

    if user_choice not in choices:
        print(f"invalid choice entered")
        print("enter again")
        continue
    
    computer_choice=random.choice(choices)
    print({computer_choice})
    result=game(user_choice,computer_choice)
    print(result)

    #to create a password manager program:

def password(s):
    while True:
        if len(s)>5:
            case1=any(char.isupper() for char in s)
            case2=any(char.isdigit() for char in s)
            case3=any(char.islower() for char in s)
            if case1 and case2 and case3:
                return True
            else:
                return False

       
    
s="S1@@@@"
print(password(s))
   



# Primary conditions for password validation:

# Minimum 8 characters.
# The alphabet must be between [a-z]
# At least one alphabet should be of Upper Case [A-Z]
# At least 1 number or digit between [0-9].
# At least 1 character from [ _ or @ or $ ].

