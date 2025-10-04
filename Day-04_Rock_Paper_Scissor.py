print("What do you choose")
roo = input("Type '0' for Rock, '1' for Paper, '2' for scissor ")
if roo == "0":
    print("You choose Rock" + """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif roo == "1":
    print("You choose Paper" + """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    """)
else :
    print("You choose Scissor" + """    
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

""")

import random
r_p_s = ["Computer choose Rock" + """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", "Computer choose Paper" + """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)""", "Computer choose Scissor" + """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""]
ran = random.randint(0,2)
print(r_p_s[ran])

if roo == str(ran):
    print("Draw")
elif (roo == "2" and ran == 1) or (roo == "1" and ran == 0) or (roo == "0" and ran == 2):
    print("You Won")
else:
    print("You Lost")