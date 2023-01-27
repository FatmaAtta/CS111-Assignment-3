list=[1,2,3,4,5,6,7,8,9]
player1,player2=[],[]
turn=0
#function to check if the sum of 3 numbers in a list equals y
def summation(list,sum):
    for i in range(0,len(list)-2): #stops at 7 bec, k will always be 2 more than i
        for j in range(i+1,len(list)-1):#starts at 1 and not 0 to make sure it doesnt sum the same numbers
            for k in range(j+1,len(list)):
                if list[i]+list[j]+list[k]==sum:
                    print(list[i],' + ',list[j],' + ',list[k], '=', sum)
                    winner=True
                    break
                else: 
                    winner=False
            if winner:
                break
        if winner:
                break
    return winner 

for i in range(10):
    if turn%2==0:
        print("Player 1: Enter a number from ",list,"\n")
        num=int(input())
        list.remove(num)
        player1.append(num)
        if len(player1)>=3:
            x=summation(player1,15)
            if x:
                print("Player 1 won!")
                break
    else:
        print("Player 2: Enter a number from ",list,"\n")
        num=int(input())
        list.remove(num)
        player2.append(num)
        if len(player1)>=3:
            x=summation(player2,15)
            if x:
                print("Player 2 won!")
                break
            else: print("Draw")
    turn+=1
    


