logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)


def calculation (f_num , s_num , sym):
    if sym == "+":
        add = f_num + s_num
        return add
    elif sym == "-":
        sub = f_num - s_num
        return sub
    elif sym == "*":
        multiply = f_num * s_num
        return multiply
    elif sym == "/":
        if s_num == 0:
            print("Zero Division Error")
        return f_num / s_num

    else:
        return "Invalid Operation"
while True:
    num1 = float(input("Enter the First Number:  "))
    while True:
        symbols = input("""+\n-\n*\n/\nPick an operation:  """)
        num2 = float(input("Enter the Second Number:  "))
        calculation(f_num=num1, s_num=num2, sym=symbols)
        answer = calculation(num1 , num2 , symbols)
        print(answer)
        repeat = input(f"Type 'Y' to continue calculating with {answer} or Type 'N' for Starting new calculation:  ").lower()
        if repeat == "y":
            num1 = answer
        else:
            print("\n" * 20)
            print(logo)
            break
