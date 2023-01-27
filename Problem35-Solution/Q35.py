coins=int(input("Enter the starting number of coins\n"))
turn=0
while coins>=0:
    if turn%2==0:
        num=int(input("Player1: Enter a number\n"))
        while num==0:
            num=int(input("Player1: Enter a number\n"))
        if coins - num**2 <0:
            num=int(input("Player1: Enter a smaller number\n"))
        else: coins= coins-num**2
    else:
        num=int(input("Player2: Enter a number\n"))
        while num==0:
            num=int(input("Player2: Enter a number\n"))
        if coins - num**2 <0:
            num=int(input("Player2: Enter a smaller number\n"))
        else: coins-=num**2
    print("Remaining coins: ",coins)
    if coins == 0:
        if turn%2==0:
            print("Player 1 has won!\n")
            break
        else:
            print("Player 2 has won!\n")
            break
    turn+=1