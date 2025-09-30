print("""Welcome to the treasure island!
Your mission is to find the treasure
You are at a cross road. Where do you want to go?""")
direction = input("     Choose Left or Right ")
if direction == "l":
    print("You've come across a lake. There is an island in the middle of the lake ")
    action = input("Type w to wait for a boat or type s to swim across river ")
    if action == "w":
        print("You've reached the island using the boat")
        color = input("""In front of you is 3 doors Red, Blue, Yellow
        Type r for Red, b for Bluw or y for Yellow """)
        if color == "r":
            print("Burned by fire. GAME OVER!")
        elif color == "y":
            print("YOU WIN!")
        elif color == "b":
            print("Eaten by beasts. GAME OVER!")
        else:
            print("GAME OVER!")
    elif action == "s":
        print("Attacked by trout. GAME OVER!")
    else:
        print("GAME OVER!")
elif direction == "r":
    print("Fell into a hole. GAME OVER!")
else:
    pint("GAME OVER!")




