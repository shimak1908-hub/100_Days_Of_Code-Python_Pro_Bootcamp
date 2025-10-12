print(r""" _   _                                             
| | | |                                            
| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __      
|  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \     
| | | | (_| | | | | (_| | | | | | | (_| | | | |    
\_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|    
                     __/ |                         
                    |___/      
""")
words = ["apple", "banana", "orange", "grape", "peach", "mango", "pear", "plum", "melon", "kiwi",
    "cherry", "apricot", "fig", "lime", "lemon", "papaya", "guava", "coconut", "berry", "avocado",
    "table", "chair", "sofa", "bench", "stool", "shelf", "cabinet", "drawer", "mirror", "curtain",
    "pillow", "blanket", "mattress", "wardrobe", "carpet", "lamp", "candle", "vase", "clock", "frame",
    "dog", "cat", "rabbit", "hamster", "turtle", "horse", "sheep", "goat", "cow", "donkey",
    "chicken", "duck", "pigeon", "parrot", "eagle", "falcon", "sparrow", "penguin", "dolphin", "whale",
    "lion", "tiger", "leopard", "cheetah", "panther", "wolf", "fox", "bear", "zebra", "giraffe",
    "pencil", "pen", "eraser", "sharpener", "marker", "crayon", "notebook", "paper", "ruler", "compass",
    "glue", "scissors", "stapler", "tape", "folder", "calculator", "backpack", "lunchbox", "bottle", "brush",
    "car", "truck", "bus", "train", "plane", "ship", "boat", "bicycle", "scooter", "motorcycle",
    "helmet", "engine", "wheel", "brake", "mirror", "bumper", "window", "seat", "pedal", "handle",
    "pizza", "burger", "sandwich", "pasta", "salad", "noodles", "rice", "bread", "cheese", "butter",
    "milk", "yogurt", "cream", "soup", "steak", "sausage", "bacon", "egg", "chocolate", "cookie",
    "doctor", "nurse", "teacher", "engineer", "lawyer", "chef", "pilot", "farmer", "soldier", "police",
    "actor", "singer", "writer", "painter", "dancer", "athlete", "driver", "plumber", "carpenter", "mechanic",
    "mountain", "river", "ocean", "desert", "forest", "island", "valley", "hill", "waterfall", "canyon",
    "storm", "rain", "snow", "thunder", "lightning", "wind", "tornado", "hurricane", "cloud", "sunshine",
    "computer", "laptop", "keyboard", "mouse", "screen", "monitor", "speaker", "printer", "router", "tablet",
    "phone", "camera", "remote", "battery", "charger", "cable", "headphones", "microphone", "joystick", "console",
    "king", "queen", "prince", "princess", "knight", "castle", "sword", "shield", "dragon", "wizard",
    "magic", "potion", "spell", "crystal", "treasure", "map", "key", "door", "bridge", "tower",
    "happy", "sad", "angry", "excited", "bored", "scared", "confused", "proud", "jealous", "lonely",
    "jump", "run", "walk", "swim", "climb", "crawl", "dance", "laugh", "smile", "cry",
    "circle", "square"]
stages = [
    r"""
       --------
       |      |
       |      O
       |     /|\
       |     / \
       |     
    ---------
    """,
    r"""
       --------
       |      |
       |      O
       |     /|\
       |     / 
       |     
    ---------
    """,
    r"""
       --------
       |      |
       |      O
       |     /|\
       |      
       |     
    ---------
    """,
    r"""
       --------
       |      |
       |      O
       |     /|
       |      
       |     
    ---------
    """,
    r"""
       --------
       |      |
       |      O
       |      |
       |      
       |     
    ---------
    """,
    r"""
       --------
       |      |
       |      O
       |     
       |      
       |     
    ---------
    """,
    r"""
       --------
       |      |
       |      
       |     
       |      
       |     
    ---------
    """
]




import random
lives = 6
choosen_word = random.choice(words)
placeholder = ""
word_length = len(choosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
Game_Over = False
correct_word = []
while not Game_Over:
    guess = input("Guess a letter ").lower()
    if guess in correct_word:
        print(f"You've already guessed it {guess}")
    display = ""
    for letter in choosen_word:
        if letter == guess:
            display += letter
            correct_word.append(guess)
        elif letter in correct_word:
            display += letter
        else:
            display += "_"
    if guess not in choosen_word:
        lives -= 1
        print(f"You guessed {guess}, That's not in the word, You lose a life")
        if lives == 0:
            Game_Over = True
            print(f"***************IT WAS {choosen_word} YOU LOST***************")
    print(display)
    if "_" not in display:
        Game_Over = True
        print("***************YOU WIN***************")

    print(stages[lives])