#Battleship Game
import numpy as np
from numpy.random import randint
def hide(no_of_ships,rows,columns):
    b=[]
    while len(b)<int(no_of_ships):
        a=[]
        a=a+[randint(0,rows)]
        a=a+[randint(0,columns)]
        if a not in b:
            b=b+[a]
    
    return b

def build_grid(rows,columns,shots):
    grid=[]
    orow=[]
    for n in range(0,columns):
        orow=orow+['O']
    d={}
    for x in range(1,rows+1):
        d["row{0}".format(x)]=orow[:]
    n=0
    for k in d:
        for m in range(0,len(shots)):
            if n == shots[m][0]:
                d[k][(shots[m][1])]='X'
        n=n+1
    for k in d:
        grid=grid+[d[k]]
    return grid

def print_grid(x):
    grid=''
    for a in range(0,len(x)):
        grid=''
        b=x[a]
        for c in range(0,len(b)):
            d=b[c]
            grid=grid+d+'  '
        print(grid)

def shoot(shot_list,rows,columns):
    c=len(shot_list)
    x=0
    y=0
    while c<(len(shot_list)+1):
        while x<=0:
            row1=input('Row number?')
            if row1.isnumeric()==False:
                print('Invalid input! Please input an integer.')
            elif int(row1)>rows:
                print('Out of bounds!')
            else:
                x=x+1
        while y<=0:
            column1=input('Column number?')
            if column1.isnumeric()==False:
                print('Invalid input! Please input an integer.')
            elif int(column1)>columns:
                print('Out of bounds!')
            else:
                y=y+1
        if x==1 and y==1:
                row=int(row1)
                column=int(column1)
                shot=[(row-1)]+[(column-1)]
                if shot in shot_list:
                    print('You have already shot at these coordinates!')
                    x=x-1
                    y=y-1
                else:
                    c=c+1
    print('Shot taken at ('+ str(row)+','+str(column)+')')
    shot_list=shot_list+[shot]
    return shot_list

def check(shot_list,hidden_ships,no_of_shots,destroyed):
    ships1=len(hidden_ships)
    ships=ships1-destroyed
    shots_left=no_of_shots-len(shot_list)
    g=0
    if shot_list[-1] in hidden_ships:
        print("A hit! Enemy ship sunk!")
        ships=ships-1
        destroyed=destroyed+1
        if ships>0:
            print("There are "+ str(ships) + " enemy ship(s) remaining.")
            if shots_left>0:
                print("You have "+str(shots_left)+" shots remaining.")
            elif shots_left==0:
                print("You have ran out of shots! Game Over")
                g=1
        else:
            print("All ships sunk! Congratulations! You've won!")
            g=1
    elif shots_left>0 and ships>0:
        print("You missed! You have "+str(shots_left)+" shots remaining.")
        print("There are "+ str(ships) + " enemy ship(s) remaining.")
    elif shots_left==0 and ships>0:
        print("You missed and you have ran out of shots! Game Over")
        g=1
   
    d=[destroyed]+[g]
    return d
while True:
    t=0
    h=0
    while t==0:
        custom=input("Do you want a custom game? (Y/N)")
        if custom not in ('y', 'n','Y','N'):
            print('Invalid input.')
        if custom == 'n' or custom == 'N':
            rows=5
            columns=5
            no_of_ships=5
            no_of_shots=10
            print("Objective: Destroy all enemy ships \n You have 10 shots and 5 enemy ships remaining. \n Good luck captain!")
            t=1
        elif custom == 'y' or custom == 'Y':
            print("Set your grid size.")
            e=0
            f=0
            while e==0:
                rows1=input("Number of rows?")
                if rows1.isnumeric()==False or int(rows1)==0:
                        print('Invalid input! Please input a positive integer.')
                else:
                    e=1
            rows=int(rows1)
            while f==0:
                columns1=input("Number of columns?")
                if columns1.isnumeric()==False or int(columns1)==0:
                        print('Invalid input! Please input a positive integer.')
                else:
                    f=1
            columns=int(columns1)
            while h==0:
                no_of_ships1=input("How many enemy ships? Ships are represented as points in this game.")
                if int(no_of_ships1)>(int(columns1)*int(rows)) or no_of_ships1.isnumeric()==False or int(no_of_ships1)==0:
                    print('Invalid input! Please input a positive integer.')
                else:
                    h=1
            no_of_ships=int(no_of_ships1)
            i=0
            while i==0:
                no_of_shots1=input("How many shots?")
                if no_of_shots1.isnumeric()==False or int(no_of_shots1)==0:
                    print('Invalid input! Please input a positive integer.')
                else:
                    i=1
            no_of_shots=int(no_of_shots1)
            t=1
            print("Objective: Destroy all enemy ships \n You have " + str(no_of_shots) + " shot(s) and " + str(no_of_ships) + " enemy ships remaining. \n Good luck captain!")
    
    shot_list=[]
    d=[0,0]
    hidden=hide(no_of_ships,rows,columns)
    while d[0]<len(hidden) and d[1]==0:
        grid=build_grid(rows,columns,shot_list)
        print_grid(grid)
        print("Please enter target coordinates.")
        shot_list=shoot(shot_list,rows,columns)
        d=check(shot_list,hidden,no_of_shots,d[0])
    if d[1]==1:
        grid=build_grid(rows,columns,shot_list)
        print_grid(grid)
    while True:
        answer=input('Play again? (Y/N): ')
        if answer in ('y', 'n','Y','N'):
            break
        else:
            print('Invalid input.')
    if answer == 'y' or answer == 'Y':
        continue
    else:
        print('Thank you for playing.')
        input("Press return to close the window.")
        break
