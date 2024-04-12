def restaurant(name,order,tableNumber):
    menu = ["rice cakes","meat","apple pie","sodas"]
    for i in menu:
      if(i == order):
        print(f"{name} {tableNumber} {order} is on the way!")
    else:
        print(f"{name} {tableNumber} {order} not in menu but try these: {menu}")    
    
    
        