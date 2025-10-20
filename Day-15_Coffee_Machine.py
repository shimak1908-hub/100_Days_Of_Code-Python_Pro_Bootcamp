data = [
  {"name": "espresso",
   "water": 50,
   "coffee": 18,
   "price": 1.50},
  {"name": "latte",
   "water": 200,
   "coffee": 24,
   "milk": 150,
   "price": 2.50},
  {"name": "cappuccino",
   "water": 250,
   "coffee": 24,
   "milk": 100,
   "price": 3.00}
]
coffee_machine = [{"water":20,
                   "coffee":50,
                   "milk": 100}]

repeat = True
while repeat:
    print("COFFEE MACHINE☕")
    switch = input("Type 'on' to turn ON the machine ").lower()
    if switch == "on":
        print("The machine has been switched ON")
        type_coffee = input("Type '1' for ESPRESSO\nType '2' for LATTE\nType '3' for CAPPUCCINO\n")
        if type_coffee == "1":
            repeat_1 = True
            while repeat_1:
                if data[0]["water"] <= coffee_machine[0]["water"] and data[0]["coffee"] <= coffee_machine[0]["coffee"]:
                    print("Here is your ESPRESSO... Enjoy:)")
                    coffee_machine[0]["water"] -= data[0]["water"]
                    coffee_machine[0]["coffee"] -= data[0]["coffee"]
                    break
                if data[0]["water"] > coffee_machine[0]["water"]:
                    shortage_water = data[0]["water"] - coffee_machine[0]["water"]
                    print(f"Insufficient Water... Add {shortage_water}ml ")
                if data[0]["coffee"] > coffee_machine[0]["coffee"]:
                    shortage_coffee = data[0]["coffee"] - coffee_machine[0]["coffee"]
                    print(f"Insufficient coffee... Add {shortage_coffee}g")
                if data[0]["water"] > coffee_machine[0]["water"]:
                    add_water = int(input("Add Water to the Coffee Machine... 500ml, 100ml, 50ml "))
                    coffee_machine[0]["water"] += add_water
                if data[0]["coffee"] > coffee_machine[0]["coffee"]:
                    add_coffee = int(input("Add Coffee to the Coffee Machine... 50g, 25g, 10g "))
                    coffee_machine[0]["coffee"] += add_coffee


        elif type_coffee == "2":
            repeat_2 = True
            while repeat_2:
                if data[1]["water"] <= coffee_machine[0]["water"] and data[0]["coffee"] <= coffee_machine[0]["coffee"]:
                    print("Here is your LATTE... Enjoy:)")
                    coffee_machine[0]["water"] -= data[1]["water"]
                    coffee_machine[0]["coffee"] -= data[1]["coffee"]
                    coffee_machine[0]["milk"] -= data[1]["milk"]
                    break
                if data[1]["water"] > coffee_machine[0]["water"]:
                    shortage_water = data[1]["water"] - coffee_machine[0]["water"]
                    print(f"Insufficient Water... Add {shortage_water}ml ")
                if data[1]["coffee"] > coffee_machine[0]["coffee"]:
                    shortage_coffee = data[1]["coffee"] - coffee_machine[0]["coffee"]
                    print(f"Insufficient coffee... Add {shortage_coffee}g")
                if data[1]["milk"] > coffee_machine[0]["milk"]:
                    shortage_milk = data[2]["water"] - coffee_machine[0]["milk"]
                    print(f"Insufficient Milk... Add {shortage_milk}ml ")
                if data[1]["water"] > coffee_machine[0]["water"]:
                    add_water = int(input("Add Water to the Coffee Machine... 500ml, 100ml, 50ml "))
                    coffee_machine[0]["water"] += add_water
                if data[1]["coffee"] > coffee_machine[0]["coffee"]:
                    add_coffee = int(input("Add Coffee to the Coffee Machine... 50g, 25g, 10g "))
                    coffee_machine[0]["coffee"] += add_coffee
                if data[1]["milk"] > coffee_machine[0]["milk"]:
                    add_milk = int(input("Add Milk to the Coffee Machine... 500ml, 100ml, 50ml "))
                    coffee_machine[0]["milk"] += add_milk




        elif type_coffee == "3":
            repeat_3 = True
            while repeat_3:
                if data[1]["water"] <= coffee_machine[0]["water"] and data[0]["coffee"] <= coffee_machine[0]["coffee"]:
                    print("Here is your CAPPUCCINO... Enjoy:)")
                    coffee_machine[0]["water"] -= data[1]["water"]
                    coffee_machine[0]["coffee"] -= data[1]["coffee"]
                    coffee_machine[0]["milk"] -= data[1]["milk"]
                    break
                if data[2]["water"] > coffee_machine[0]["water"]:
                    shortage_water = data[2]["water"] - coffee_machine[0]["water"]
                    print(f"Insufficient Water... Add {shortage_water}ml ")
                if data[2]["coffee"] > coffee_machine[0]["coffee"]:
                    shortage_coffee = data[2]["coffee"] - coffee_machine[0]["coffee"]
                    print(f"Insufficient coffee... Add {shortage_coffee}g")
                if data[2]["milk"] > coffee_machine[0]["milk"]:
                    shortage_milk = data[2]["water"] - coffee_machine[0]["milk"]
                    print(f"Insufficient Milk... Add {shortage_milk}ml ")
                if data[2]["water"] > coffee_machine[0]["water"]:
                    add_water = int(input("Add Water to the Coffee Machine... 500ml, 100ml, 50ml "))
                    coffee_machine[0]["water"] += add_water
                if data[2]["coffee"] > coffee_machine[0]["coffee"]:
                    add_coffee = int(input("Add Coffee to the Coffee Machine... 50g, 25g, 10g "))
                    coffee_machine[0]["coffee"] += add_coffee
                if data[2]["milk"] > coffee_machine[0]["milk"]:
                    add_milk = int(input("Add Milk to the Coffee Machine... 500ml, 100ml, 50ml "))
                    coffee_machine[0]["milk"] += add_milk
        else:
            print("Enter a valid choice")
        hey = True
        while hey:
            hi = input("\nDo you want another coffee? (y/n)").lower()
            if hi == "y":
                repeat = True
                hey = False
            elif hi == "n":
                repeat = False
                hey = False
            else:
                print("Enter a valid choice")

    else:
        print("Machine is not turned ON")