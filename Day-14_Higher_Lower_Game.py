import random
logo = (r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/      
""")
vs = (r"""
     _    __    
    | |  / /____
    | | / / ___/
    | |/ (__  ) 
    |___/____(_)
    """)
data = [
    {"name": "Cristiano Ronaldo", "followers": 665000000, "profession": "Footballer", "country": "Portugal"},
    {"name": "Lionel Messi", "followers": 507000000, "profession": "Footballer", "country": "Argentina"},
    {"name": "Selena Gomez", "followers": 418000000, "profession": "Musician and Actress", "country": "USA"},
    {"name": "Kylie Jenner", "followers": 392000000, "profession": "Media Personality", "country": "USA"},
    {"name": "Dwayne 'The Rock' Johnson", "followers": 392000000, "profession": "Actor and Wrestler", "country": "USA"},
    {"name": "Ariana Grande", "followers": 373000000, "profession": "Musician and Actress", "country": "USA"},
    {"name": "Kim Kardashian", "followers": 355000000, "profession": "Media Personality", "country": "USA"},
    {"name": "Beyoncé", "followers": 309000000, "profession": "Musician and Actress", "country": "USA"},
    {"name": "Khloé Kardashian", "followers": 301000000, "profession": "Media Personality", "country": "USA"},
    {"name": "Nike", "followers": 293000000, "profession": "Sportswear Brand", "country": "USA"},
    {"name": "Justin Bieber", "followers": 292000000, "profession": "Musician", "country": "Canada"},
    {"name": "Kendall Jenner", "followers": 298000000, "profession": "Media Personality", "country": "USA"},
    {"name": "Taylor Swift", "followers": 284000000, "profession": "Musician", "country": "USA"},
    {"name": "National Geographic", "followers": 268000000, "profession": "Magazine", "country": "USA"},
    {"name": "Virat Kohli", "followers": 273000000, "profession": "Cricketer", "country": "India"},
    {"name": "Jennifer Lopez", "followers": 253000000, "profession": "Musician and Actress", "country": "USA"},
    {"name": "Neymar", "followers": 220000000, "profession": "Footballer", "country": "Brazil"},
    {"name": "Nicki Minaj", "followers": 229000000, "profession": "Musician", "country": "Trinidad & Tobago"},
    {"name": "Kourtney Kardashian", "followers": 224000000, "profession": "Media Personality", "country": "USA"},
    {"name": "Miley Cyrus", "followers": 218000000, "profession": "Musician and Actress", "country": "USA"},
    {"name": "Katy Perry", "followers": 207000000, "profession": "Musician", "country": "USA"},
    {"name": "Real Madrid CF", "followers": 145000000, "profession": "Football Club", "country": "Spain"},
    {"name": "Zendaya", "followers": 190000000, "profession": "Actress and Singer", "country": "USA"},
    {"name": "Kevin Hart", "followers": 188000000, "profession": "Comedian and Actor", "country": "USA"},
    {"name": "Cardi B", "followers": 168000000, "profession": "Musician and Actress", "country": "USA"},
    {"name": "LeBron James", "followers": 167000000, "profession": "Basketball Player", "country": "USA"},
    {"name": "Demi Lovato", "followers": 145000000, "profession": "Musician and Actress", "country": "USA"},
    {"name": "Rihanna", "followers": 126000000, "profession": "Musician", "country": "Barbados"},
    {"name": "Chris Brown", "followers": 110000000, "profession": "Musician", "country": "USA"},
    {"name": "FC Barcelona", "followers": 100000000, "profession": "Football Club", "country": "Spain"},
    {"name": "Drake", "followers": 108000000, "profession": "Musician", "country": "Canada"},
    {"name": "Ellen DeGeneres", "followers": 100000000, "profession": "Television Host", "country": "USA"},
    {"name": "Kylian Mbappé", "followers": 87000000, "profession": "Footballer", "country": "France"},
    {"name": "Billie Eilish", "followers": 90000000, "profession": "Musician", "country": "USA"},
    {"name": "UEFA Champions League", "followers": 87000000, "profession": "Football Competition", "country": "Europe"},
    {"name": "Gal Gadot", "followers": 109000000, "profession": "Actress", "country": "Israel"},
    {"name": "Lisa", "followers": 90000000, "profession": "Musician", "country": "South Korea"},
    {"name": "Vin Diesel", "followers": 65000000, "profession": "Actor", "country": "USA"},
    {"name": "Narendra Modi", "followers": 89000000, "profession": "Politician", "country": "India"},
    {"name": "NASA", "followers": 80000000, "profession": "Space Agency", "country": "USA"},
    {"name": "Shraddha Kapoor", "followers": 65000000, "profession": "Actress", "country": "India"},
    {"name": "Shakira", "followers": 90000000, "profession": "Musician", "country": "Colombia"},
    {"name": "Priyanka Chopra", "followers": 70000000, "profession": "Actress", "country": "India"},
    {"name": "NBA", "followers": 85000000, "profession": "Basketball League", "country": "USA"},
    {"name": "Snoop Dogg", "followers": 87000000, "profession": "Musician", "country": "USA"},
    {"name": "Jennie", "followers": 85000000, "profession": "Musician", "country": "South Korea"},
    {"name": "David Beckham", "followers": 87000000, "profession": "Footballer", "country": "UK"},
    {"name": "Dua Lipa", "followers": 78000000, "profession": "Musician", "country": "UK"},
    {"name": "Alia Bhatt", "followers": 83000000, "profession": "Actress", "country": "India"}
]
score = 0
repeat = True

while repeat:
    rand_1 = random.choice(data)
    rand_2 = random.choice(data)
    print(logo)
    print(f"\nCompare A: {rand_1["name"]}, {rand_1["profession"]}, {rand_1["country"]}")
    print(vs)
    print(f"Compare B: {rand_2["name"]}, {rand_2["profession"]}, {rand_2["country"]}")
    follow = input("Who has more followers in insta? Type 'A' or 'B':").lower()
    repeat = True
    if rand_1["followers"] > rand_2["followers"]:
        choice = "a"
    else:
        choice = "b"
    if follow == choice:
        score += 1
        print(f"You're right! Current score: {score} ")

    else:
        print("\n" * 100)
        print(f"Sorry, that's wrong. Final score: {score}")
        repeat = False
