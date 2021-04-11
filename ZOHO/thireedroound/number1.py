# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 10:08:02 2021

@author: ELCOT
"""

"""
creating the input spacing game

"""
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
    print("1.Modify the label number")
    print("2.Exit")
    option = int(input("Enter your option ----> 1 or 2:"))
    
    #check for the two conditions
    if(option == 1):
        x, y = list(map(int,(input("Enter the position:").split())))
        if x>n or y>n:
            print("The entered position is invlid-------->")
            print("Kindly Enter the new position below ;)")
            print()
            x, y = list(map(int,(input("Enter the position:").split())))
        new_label = int(input("Enter the new label number:"))
        
        #board changing 
        r[x-1][y-1] = new_label
        display(r)
    elif(option == 2):
        break