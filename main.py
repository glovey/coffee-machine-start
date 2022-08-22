MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


#variables

is_on = True

#Functions

def Check_Drink(choice):  
  for ing in MENU[choice]["ingredients"]:    
    if MENU[choice]["ingredients"][ing] > resources[ing]:
      return False
  return True
 

def Resources():
  for ing in MENU[choice]["ingredients"]:
         resources[ing] = resources[ing] - MENU[choice]["ingredients"][ing]

def Change (pay):
  change = float(pay - MENU[choice]["cost"])
  if change > 0:
    print (f"Here's your change: £{'{:.2f}'.format(change)}")
  else:
    print ("No change due :p")
      
def Money():
  resources["money"] += MENU[choice]['cost']

#Code

while is_on is True:
  choice = input( "\nWhat would you like? (espresso/latte/cappuccino)").lower()

  if choice == "off":
    print ("Switching off")
    is_on = False
  
  elif choice == "report":
    print ("")
    print(f"water: {resources['water']}")
    print(f"milk: {resources['milk']}")
    print(f"coffee: {resources['coffee']}")
    print(f"money: £{resources['money']}")
    print ("")

  elif choice in ["espresso","latte","cappuccino"]:
    if Check_Drink(choice) == True:
      pay = float(input(f"please insert money: £{MENU[choice]['cost']}\n"))
      
      if pay >= MENU[choice]["cost"]:
        print (f"Here is your {choice}, enjoy! ☕")
        Resources()
        Change(pay)
        Money()
        
        
          
      else:
        print ("insufficient funds")
      
    else:
      print ("I'm sorry, I do not have enough ingredients for that :(")
  else:
    print ("That's not a valid choice")