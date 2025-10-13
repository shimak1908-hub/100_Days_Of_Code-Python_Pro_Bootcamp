print(r""""
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88    
      """)

alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                  'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']


def caesar(org_text , shift_amt, encode_and_decode):
    output_text = ""
    cipher_text = ""
    if encode_and_decode == "decode":
        shift_amt *= -1
    for letters in org_text:
        if letters not in alphabet_lower:
            output_text += letters
        else:
            shifted_pos = alphabet_lower.index(letters) + shift_amt
            shifted_pos %= len(alphabet_lower)
            cipher_text += alphabet_lower[shifted_pos]
    print(f"Here is the {encode_and_decode}d result: {cipher_text}")

should_continue = True
while should_continue:
    diretion = input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower()
    text = input("Type your message:\n").lower()
    number = int(input("Type your shift number:\n"))
    caesar(org_text=text , shift_amt=number , encode_and_decode=diretion)
    s_or_no = input("Type 'Yes' to continue or 'No' to discontinue\n")
    if s_or_no == "no":
        should_continue = False
        print("Thank you!")