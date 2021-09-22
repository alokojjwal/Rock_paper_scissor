def rock_paper_scissor(a,b,c,d):
    p1=int(a[c])%3
    p2=int(b[d])%3
    if(player_one[p1]==player_two[p2]):
        print(pl1,"and",pl2,"has drawn")
    elif(player_one[p1]=="rock" and player_two[p2]=="paper"):
        print(pl2,"wins")
    elif(player_one[p1]=="paper" and player_two[p2]=="rock"):
        print(pl1,"wins")
    elif(player_one[p1]=="paper" and player_two[p2]=="scissor"):
        print(pl2,"wins")
    elif(player_one[p1]=="scissor" and player_two[p2]=="paper"):
        print(pl1,"wins")
    elif(player_one[p1]=="rock" and player_two[p2]=="scissor"):
        print(pl1,"wins")
    elif(player_one[p1]=="scissor" and player_two[p2]=="rock"):
        print(pl2,"wins")
    

pl1=input("Player 1, Enter your name: ")
pl2=input("Player 2, Enter your name: ")
player_one={0:'rock',1:'paper',2:'scissor'}
player_two={0:'scissor',1:'paper',2:'rock'}
while(1):
    num1=input("Enter the number: ")
    num2=input("Enter the number: ")
    pos1=int(input("Enter the position of the number: "))
    pos2=int(input("Enter the position of the number: "))
    rock_paper_scissor(num1,num2,pos1,pos2)
    cont=input("Do you wish to continue? y/n: ")
    if(cont=="n"):
        break
    