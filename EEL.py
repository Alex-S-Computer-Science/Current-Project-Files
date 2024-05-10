

menuTitle = '''
 ██████╗  █████╗ ██╗     ██╗     ███████╗██████╗ ██╗   ██╗
██╔════╝ ██╔══██╗██║     ██║     ██╔════╝██╔══██╗╚██╗ ██╔╝
██║  ███╗███████║██║     ██║     █████╗  ██████╔╝ ╚████╔╝ 
██║   ██║██╔══██║██║     ██║     ██╔══╝  ██╔══██╗  ╚██╔╝  
╚██████╔╝██║  ██║███████╗███████╗███████╗██║  ██║   ██║   
 ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝   

 ██████╗ ██████╗ ██╗   ██╗██████╗                         
██╔════╝ ██╔══██╗██║   ██║██╔══██╗                        
██║  ███╗██████╔╝██║   ██║██████╔╝                        
██║   ██║██╔══██╗██║   ██║██╔══██╗                        
╚██████╔╝██║  ██║╚██████╔╝██████╔╝                        
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═════╝
 '''
menu = '''-----------------------------------------------------------
KRABBY PATTY........ $1.25 (kp)   KRABBY MEAL......... $3.50 (km)
  w/sea cheese...... $1.50        DOUBLE KRABBY M..... $3.75 (dkm)
DOUBLE KRABBY PATTY. $2.00 (dkp)  TRIPLE KRABBY ME.... $4.00 (tkm)
  w/sea cheese...... $2.25        SALTY SEA DOG....... $1.25 (ssd)
TRIPLE KRABBY PATTY. $3.00 (tkp)  FOOTLONG............ $2.00 (fl)
  w/sea cheese...... $3.25        SAILORS SURPRISE.... $3.00 (ss)
                                  GOLDEN LOAF......... $2.00 (gl)
CORAL BITS                 (cb)     w/sauce........... $2.50 
  Small............. $1.25
  Medium............ $1.50        KELP SHAKE.......... $2.00 (ks)
  Large............. $1.75              SEAFOAM SODA (sfs)
                                      Small...... $1.00
  KELP RINGS........ $1.50 (kr)       Medium..... $1.25
    salty sauce..... $0.50            Large...... $1.50
-----------------------------------------------------------
'''
ui = ""
orderInformation=""
total = 0
tax = 0.07
orderItems = ["Order 1"]
orderList = []
subtotal = 0
orderNumber = 1

def printMenu():
  global ui
  global menu
  global menuTitle
  if ui == "m":
    print(f"\033[0;31m {menuTitle}\033[m") 
    print(menu)

def invalidKrabItem():
  global ui
  while ui != "m" and ui != "kp" and ui != "dkp" and ui != "tkp" and ui != "cb" and ui != "kr" and ui != "km" and ui != "dkm" and ui != "tkm" and ui != "ssd" and ui != "fl" and ui != "ss" and ui != "gl" and ui != "ks" and ui != "sfs":
    print("That item does not exist, please try again. ")
    ui = input("What would you like to order?  Menu?(m) ")

def validKrabItem():
  global ui
  global orderItems
  global subtotal
  if ui == "kp":
    ui = input("Would you like sea cheese on that? (y/n) ")
    while ui != "y" and ui != "n":
      ui = input("I asked if you would like sea cheese on that. (y/n) ")
    if ui == "y":
      orderItems.append("KRABBY PATTY w/sea cheese")
      subtotal += 1.50
      print("KRABBY PATTY w/sea cheese")
    else:
      orderItems.append("KRABBY PATTY")
      subtotal += 1.25
      print("KRABBY PATTY")
  elif ui == "dkp":
      ui = input("Would you like sea cheese on that? (y/n) ")
      while ui != "y" and ui != "n":
        ui = input("I asked if you would like sea cheese on that. (y/n) ")
      if ui == "y":
        orderItems.append("DOUBLE KRABBY PATTY w/sea cheese")
        subtotal += 1.50
        print("DOUBLE KRABBY PATTY w/sea cheese")
      else:
        orderItems.append("DOUBLE KRABBY PATTY")
        subtotal += 1.25
        print("DOUBLE KRABBY PATTY")
  elif ui == "tkp":
      ui = input("Would you like sea cheese on that? (y/n) ")
      while ui != "y" and ui != "n":
        ui = input("I asked if you would like sea cheese on that. (y/n) ")
      if ui == "y":
        orderItems.append("TRIPLE KRABBY PATTY w/sea cheese")
        subtotal += 1.50
        print("TRIPLE KRABBY PATTY w/sea cheese")
      else:
        orderItems.append("TRIPLE KRABBY PATTY")
        subtotal += 1.25
        print("TRIPLE KRABBY PATTY")
  elif ui == "cb":
      ui = input("Small, Medium, or Large? (s/m/l) ")
      while ui != "s" and ui != "m" and ui != "l":
        ui = input("Small...Medium...or Large? (s/m/l) ")
      if ui == "s":
        orderItems.append("SMALL CORAL BITS")
        subtotal += 1.25
        print("SMALL CORAL BITS")
      elif ui == "m":
        orderItems.append("MEDIUM CORAL BITS")
        subtotal += 1.50
        print("MEDIUM CORAL BITS")
      else:
        orderItems.append("LARGE CORAL BITS")
        subtotal += 1.75
        print("LARGE CORAL BITS")
  elif ui == "kr":
    ui = input("Would you like salty sauce on that? (y/n) ")
    while ui != "y" and ui != "n":
      ui = input("Do you want salty sauce with that or not? (y/n) ")
    if ui == "y":
      orderItems.append("KELP RINGS w/salty sauce")
      subtotal += 2.00
      print("KELP RINGS w/salty sauce")
    else:
      orderItems.append("KELP RINGS")
      subtotal += 1.50
      print("KELP RINGS")
  elif ui == "km":
    orderItems.append("KRABBY MEAL")
    subtotal += 3.50
    print("KRABBY MEAL")
  elif ui == "dkm":
    orderItems.append("DOUBLE KRABBY MEAL")
    subtotal += 3.75
    print("DOUBLE KRABBY MEAL")
  elif ui == "tkm":
    orderItems.append("TRIPLE KRABBY MEAL")
    subtotal += 4.00
    print("TRIPLE KRABBY MEAL")
  elif ui == "ssd":
    orderItems.append("SALTY SEA DOG")
    subtotal += 1.25
    print("SALTY SEA DOG")
  elif ui == "fl":
    orderItems.append("FOOTLONG")
    subtotal += 2.00
    print("FOOTLONG")
  elif ui == "ss":
    orderItems.append("SAILORS SURPRISE")
    subtotal += 3.00
    print("SAILORS SURPRISE")
  elif ui == "gl":
    ui = input("Would you like sauce with that? (y/n) ")
    while ui != "y" and ui != "n":
      ui = input("I asked if you would like sauce with that. (y/n) ")
    if ui == "y":
      orderItems.append("GOLDEN LOAF w/sauce")
      subtotal += 2.50
      print("GOLDEN LOAF w/sauce")
    else:
      orderItems.append("GOLDEN LOAF")
      subtotal += 2.00
      print("GOLDEN LOAF")
  elif ui == "ks":
    orderItems.append("KELP SHAKE")
    subtotal += 2.00
    print("KELP SHAKE")
  elif ui == "sfs":
    print("SEAFOAM SODA")
    ui = input("What size would you like?  Small, Medium, or Large? (s/m/l) ")
    while ui != "s" and ui != "m" and ui != "l":
      ui = input("What size do you want.  Small...Medium...or Large? (s/m/l) ")
    if ui == "s":
      orderItems.append("SMALL SEAFOAM SODA")
      subtotal += 1.00
      print("SMALL SEAFOAM SODA")
    elif ui == "m":
      orderItems.append("MEDIUM SEAFOAM SODA")
      subtotal += 1.25
      print("MEDIUM SEAFOAM SODA")
    else:
      orderItems.append("LARGE SEAFOAM SODA")
      subtotal += 1.50
      print("LARGE SEAFOAM SODA")
  



keepOrdering=True
while keepOrdering:
    ui = input("Would you like to order? (y/n) ")
    while ui != "y" and ui != "n":
        ui = input("What?  Do you want to order or not? (y/n) ")
    while ui == "y":
        ui = input("What would you like to order?  Menu?(m) ")
        invalidKrabItem()
        printMenu()
        validKrabItem()
        ui = "fix"
        while ui != "y" and ui != "n":
          ui = input("Anything else? (y/n) ")

    orderAgain = input("Got another order? (y/checkout) ")
    if (orderItems.count("SMALL CORAL BITS") >= 1 or orderItems.count("MEDIUM CORAL BITS") >= 1 or orderItems.count("LARGE CORAL BITS") >= 1) and (orderItems.count("SMALL SEAFOAM SODA") >= 1 or orderItems.count("MEDIUM SEAFOAM SODA") >= 1 or orderItems.count("LARGE SEAFOAM SODA") >= 1) and   (orderItems.count("KRABBY PATTY") >= 1 or orderItems.count("DOUBLE KRABBY PATTY") >= 1 or orderItems.count("TRIPLE KRABBY PATTY") >= 1 or orderItems.count("KRABBY PATTY w/sea cheese") >= 1 or orderItems.count("DOUBLE KRABBY PATTY w/sea cheese") >= 1 or orderItems.count("TRIPLE KRABBY PATTY w/sea cheese") >= 1):
      orderItems.append("$0.50 Discount")
      subtotal = subtotal - 0.50
    orderItems.append(f"Subtotal:${subtotal:.2f}")
    total += subtotal
    subtotal = 0
    while orderAgain != "checkout" and orderAgain != "y":
      orderAgain = input("What?  Do have another order or not? (y/checkout) ")
    if orderAgain == "checkout":
        keepOrdering = False
        for i in range(len(orderItems)):
          print(orderItems[i])
    elif orderAgain == "y":
      orderNumber += 1
      orderItems.append("Order " + str(orderNumber))

total = (round(total,2))
tax = (total*tax)
tax = (round(tax,2))
total = (total+tax)
total = (round(total,2))
print(f"Tax:${tax:.2f}")
print(f"Final Total:${total:.2f}")