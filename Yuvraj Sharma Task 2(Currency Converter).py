#  According to the problem,the function display_menu should not return any value.It should just display the menu
def display_menu():
  print("1. Convert USD to Euro(EUR)")
  print("2. Convert USD to UNITED ARAB EMIRATES DIRHAM(DIR)")
  print("3. Convert USD to INDIAN (IND)")
  print("4. Convert USD to Canadian Dollar(CAD)")
  print("5. Exit")
#The other four functions that convert currencies accept a value through an argument and return the converted value
def USD_to_EU(value):
  return value*0.93
def USD_to_DIR(value):
  return value*3.67
def USD_to_IND(value):
  return value*83.55
def USD_to_CAD(value):
  return value*1.37
while True:
  display_menu()
  choice=int(input())
  if choice==5:
    print("Bye!")
    break
  else:
    amount=float(input("Enter an amount in US dollars: "))
    if choice==1:
      print(amount,"USD",USD_to_EU(amount),"Euro")
    elif choice==2:
      print(amount,"USD",USD_to_DIR(amount),"DIR")
    elif choice==3:
      print(amount,"USD",USD_to_IND(amount),"IND")
    elif choice==4:
      print(amount,"USD",USD_to_CAD(amount),"CAD")