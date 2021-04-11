# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 10:56:12 2021

@author: ELCOT
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 10:08:02 2021

@author: ELCOT
"""

"""
creating the input spacing game

"""
def check_sequre_way(x,y,n,r):
    status = False
    if x!=0 and x<(n-1) and y!=0 and y<(n-1):
        print("4 side")
        #position in somewhare middle so we have check all 4 posobile sides
        #right down
        if r[x][y] == r[x][y+1]:
            if r[x][y] == r[x+1][y]:
                if r[x][y] == r[x+1][y+1]:
                    status = True
                    #remove_square(n)
                    #break
        #right up
        if r[x][y] == r[x][y+1]:
            if r[x][y] == r[x-1][y]:
                if r[x][y] == r[x-1][y+1]:
                    status = True 
                    #remove_square(n)
                    #break
        #left down
        if r[x][y] == r[x][y-1]:
            if r[x][y] == r[x+1][y]:
                if r[x][y] == r[x+1][y-1]:
                    status = True 
                    #remove_square(n)
                    #break
        #left up
        if r[x][y] == r[x-1][y]:
            if r[x][y] == r[x-1][y-1]:
                if r[x][y] == r[x][y-1]:
                    status = True 
                    #remove_square(n)
                    #break
    elif x==0 and y==0:
        #top left corne
        #right down
        if r[x][y] == r[x][y+1]:
            if r[x][y] == r[x+1][y]:
                if r[x][y] == r[x+1][y+1]:
                    status = True
                    #remove_square(n)
                    #break
    elif x==0 and y==n-1:
        #top left corner
        #left down
        if r[x][y] == r[x][y-1]:
            if r[x][y] == r[x+1][y]:
                if r[x][y] == r[x+1][y-1]:
                    status = True 
                    #remove_square(n)
                    #break
    elif x==n-1 and y==0:
        #bottom left corner
        #right up
        if r[x][y] == r[x][y+1]:
            if r[x][y] == r[x-1][y]:
                if r[x][y] == r[x-1][y+1]:
                    status = True 
                    #remove_square(n)
                    #break
    elif x==n-1 and y==n-1:
        #bottom right corner
        #left up
        if r[x][y] == r[x-1][y]:
            if r[x][y] == r[x-1][y-1]:
                if r[x][y] == r[x][y-1]:
                    status = True 
                    #remove_square(n)
                    #break
    elif x==n-1 and y<n-1:
        #bottom line
        #right up
        if r[x][y] == r[x][y+1]:
            if r[x][y] == r[x-1][y]:
                if r[x][y] == r[x-1][y+1]:
                    status = True 
                    #remove_square(n)
                    #break
        #left up
        if r[x][y] == r[x-1][y]:
            if r[x][y] == r[x-1][y+1]:
                if r[x][y] == r[x][y+1]:
                    status = True 
                    #remove_square(n)
                    #break
    
    elif x==0 and y<n-1:
        #top line
        #left down
        if r[x][y] == r[x][y-1]:
            if r[x][y] == r[x+1][y]:
                if r[x][y] == r[x+1][y-1]:
                    status = True 
                    #remove_square(n)
                    #break
        #right down
        if r[x][y] == r[x][y+1]:
            if r[x][y] == r[x+1][y]:
                if r[x][y] == r[x+1][y+1]:
                    status = True
                    #remove_square(n)
                    #break
    elif x<n-1 and y==0:
        #right line
        #right down
        if r[x][y] == r[x][y+1]:
            if r[x][y] == r[x+1][y]:
                if r[x][y] == r[x+1][y+1]:
                    status = True
                    #remove_square(n)
                    #break
        #right up
        if r[x][y] == r[x][y+1]:
            if r[x][y] == r[x-1][y]:
                if r[x][y] == r[x-1][y+1]:
                    status = True 
                    #remove_square(n)
                    #break
    
    elif x<n-1 and y==n-1:
        #left line
        #left down
        if r[x][y] == r[x][y-1]:
            if r[x][y] == r[x+1][y]:
                if r[x][y] == r[x+1][y-1]:
                    status = True 
                    #remove_square(n)
                    #break
        #left up
        if r[x][y] == r[x-1][y]:
            if r[x][y] == r[x-1][y-1]:
                if r[x][y] == r[x][y-1]:
                    status = True 
                    #remove_square(n)
                    #break
    print(status)   
        
     
    
def find_adjacent(x , y ,n ,r):
    if x!=0 and x<(n-1) and y!=0 and y<(n-1):
        #position in somewhare middle so we have check all 4 posobile sides
        if r[x][y] == r[x+1][y]:
            x1,y1 = x+1,y
            
        elif r[x][y] == r[x][y+1]:
            x1,y1 = x,y+1
            
        elif r[x][y] == r[x-1][y]:
            x1,y1 = x-1,y
             
        elif r[x][y] == r[x][y-1]:
            x1,y1 = x,y-1
        else:
            return [-1,-1]
    elif x==0 and y==0:
        #top left corner
        if r[x][y] == r[x+1][y]:
            x1,y1 = x+1,y
        elif r[x][y] == r[x][y+1]:
            x1,y1 = x,y+1
        else:
            return [-1,-1]
    elif x==0 and y==n-1:
        #top left corner
        
            if r[x][y] == r[x+1][y]:
                x1,y1 = x+1,y
            elif r[x][y] == r[x][y-1]:
                x1,y1 = x,y-1
            else:
                return [-1,-1]
    elif x==n-1 and y==0:
        #bottom left corner
        if r[x][y] == r[x-1][y]:
            x1,y1 = x-1,y
        elif r[x][y] == r[x][y+1]:
            x1,y1 = x,y+1
        else:
            return [-1,-1]
    elif x==n-1 and y==n-1:
        #bottom right corner
        if r[x][y] == r[x-1][y]:
            x1,y1 = x-1,y
        elif r[x][y] == r[x][y-1]:
            x1,y1 = x,y-1
        else:
            return [-1,-1]
    elif x==n-1 and y<n-1:
        #bottom line
        if r[x][y] == r[x-1][y]:
            x1,y1 = x-1,y
        elif r[x][y] == r[x][y-1]:
            x1,y1 = x,y-1
        elif r[x][y] == r[x][y+1]:
            x1,y1 = x,y+1
        else:
            return [-1,-1]
    elif x==0 and y<n-1:
        #top line
        if r[x][y] == r[x+1][y]:
            x1,y1 = x+1,y
        elif r[x][y] == r[x][y-1]:
            x1,y1 = x,y-1
        elif r[x][y] == r[x][y+1]:
            x1,y1 = x,y+1
        else:
            return [-1,-1]
    elif x<n-1 and y==0:
        #right line
        if r[x][y] == r[x+1][y]:
            x1,y1 = x+1,y
        elif r[x][y] == r[x-1][y]:
            x1,y1 = x-1,y
        elif r[x][y] == r[x][y+1]:
            x1,y1 = x,y+1
        else:
            return [-1,-1]
    elif x<n-1 and y==n-1:
        #left line
        if r[x][y] == r[x+1][y]:
            x1,y1 = x+1,y
        elif r[x][y] == r[x-1][y]:
            x1,y1 = x-1,y
        elif r[x][y] == r[x][y-1]:
            x1,y1 = x,y-1
        else:
            return [-1,-1]
    return [x1,y1]
## allienment
def display(r):
    for row in range(n+1):
        if row == n:
            print(' '*4+'- '*n)
            print(' '*4,end='')
            for i in range(1,n+1):
                print(i,end=' ')
            break
        print(row+1,end =' ')
        print('|',end=' ' )
        
        for col in range(n):
             print(r[row][col],end=' ')            
        print()
import random
n = int(input("Enter N:"))
limit = int(input("Enter the label number limits:"))
#board placing random numbers
r = []

for i in range(n):
    rr=[]
    for j in range(n):
        rand = random.randint(0,limit)
        rr+=[rand]
    r+=[rr]
print("The Board after placing the random number pieces.")
display(r)
#allignment
#ask for changes
while(True):
    print()
    print()
    print("1.Continue to remove")
    print("2.Exit")
    option = int(input("Enter your option ----> 1 or 2:"))
    
    #check for the two conditions
    if(option == 1):
        x, y = list(map(int,(input("Enter the X Y position:").split())))
        if x>n or y>n:
            print("The entered position is invlid-------->")
            print("Kindly Enter the new position below ;)")
            print()
            x, y = list(map(int,(input("Enter the position:").split())))
        x1 , y1 = x-1,y-1
        #second position
        #check for the sequer path
        t=check_sequre_way(x1,y1,n,r)
        if t==True:
            continue
        x2 , y2 = find_adjacent(x1,y1 , n,r)
        if x1 != -1 and y!=-1:
            print()
            print("same number-labeled adjacent position:",end=' ')
            print(x2+1,y2+1)
        else:
            print("No same number-labeled block position found")
            break
        # the second position is x1,y1
        if y1==y2:
            #under the same colum
            #reaisgn the x1 and x2 fi it is not in order
            if x1>x2:
                a,b = x1,y1
                x1,y1 = x2,y2
                x2,y2 = a,b
            #print("THe x1 and y1",x1+1,y1+1)
            while x1>=0:
                if x1==0 and x2==1:
                    r[x1][y1] = random.randint(0,limit)
                    r[x2][y2] = random.randint(0,limit)
                    break
                if x1==1 and x2>1:
                    #print("Under the x1==1 condition")
                    r[x1][y1] = random.randint(0,limit)
                    r[x2][y2] = r[x2-2][y2]
                    r[0][0] = random.randint(0,limit)
                    break
                if x1>1 and x2>1:
                    #at botton position
                    r[x1][y1] = r[x1-2][y1]
                    r[x2][y2] = r[x2-2][y2]
                    x1 = x1-2
                    x2 = x2-2
                    #print("Crossing the column and changing")
                    #print(x1+1,y1+1)
                    #print(x2+1,y2+1)
                    #display(r)
                elif x1<1 and x2>1:
                    #at the second line
                    r[x1][y1] = random.randint(0,limit)
                    r[x2][y2] = r[x-2][y2]
                    r[0][0] = random.randint(0,limit)
                    break
            print("After Removing the blocks")
            print()
            display(r)
                
                    
        else:
            #under the different column
            while x1>=0 and y1>=0:
                if x1==0 and x2==0:
                    r[x1][y1] = random.randint(0,limit)
                    r[x2][y2] = random.randint(0,limit)
                    break
                r[x1][y1] = r[x1-1][y1]
                r[x2][y2] = r[x2-1][y2]
                x1 = x1-1
                x2 = x2-1
            print("After Removing the blocks")
            print()
            display(r)
                
            
        # check for sam column or different column
       
               
    elif(option == 2):
        break