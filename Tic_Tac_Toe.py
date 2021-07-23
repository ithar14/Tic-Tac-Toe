import random

solution = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
num = [1,2,3,4,5,6,7,8,9]
player = ['X','O']
p1=[] #player1 solutions
p2=[] #player2 solutions

def output(num): 
    for i in range (0,3):
        print(' | ',num[i], sep='', end=' | ', flush=True)
    print('\n')
    for i in range (3,6):
        print(' | ',num[i], sep='', end=' | ', flush=True)
    print('\n')
    for i in range (6,9):
        print(' | ',num[i], sep='', end=' | ', flush=True)
        
def sol(p1,p2):
    p1.sort()
    p2.sort()
    random.shuffle(p2)
    if p1 in solution :
        print(player1,'is the winner!')
    elif p2 in solution :
        print(player2,'is the winner!')
    else:
        print('no winner!')

def pos(position,num,player1,player2):
#change num with the position of player1
    if int(position1)>=1 or int(position1)>=10 :
        num[int(position1)-1]=player1
        p1.append(int(position1))
    else:
        print('number out of range!')
    
#change num with the position of player2
    num2 =[j for j in num if isinstance(j, (int, float))] #the new list with the left numbers
    if num2==[] :
        print('no more choices')
    else:
        position2 = random.choice(num2)
    while position2 in num:
        if isinstance(position2, (int,float)) :
            num[int(position2)-1]=player2
            p2.append(position2)
    output(num)
    
player1 = input('X or O ? : ')
if player1=='X':
    player2='O'
else:
    player2='X'
    
print("you've got 3 tries")
for i in range(1,4):
    print(player1,'choose a position')
    position1 = input('?')
    pos(position1,num,player1,player2)
print('\n')    
sol(p1,p2)