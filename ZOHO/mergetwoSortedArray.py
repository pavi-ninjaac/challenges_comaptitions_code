# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 15:04:24 2021

@author: ELCOT
"""

"""
merge the two sorted array
i/p : 2 4 5 6 7 9 10 13
2 3 4 5 6 7 8 9 11 15

o/p: 2,3,4,5,6,7,8,9,10,11,13,15
"""

a1 = list(map(int , input().split()))
a2 = list(map(int , input().split()))

l1,l2 = len(a1),len(a2)
i,j = 0, 0
res = []

while i<=l1 and j<=l2:
        print(i,j)
        if i == l1:
            bal = l2-j
            for b in range(bal):
                res+=[a2[j]]
                j+=1
                
            break# when one array reaches the end of the list
        if j==l2:
            bal = l1-i
            for b in range(bal):
                res+=[a1[i]]
                i+=1
                
            break
        if(a1[i]<a2[j]):
            res+=[a1[i]]
            
            i+=1
        elif a1[i]>a2[j]:
            res+=[a2[j]]
            
            j+=1
        elif a1[i]==a2[j]:
            res += [a1[i]]
            
            i+=1
            j+=1
        print(res)
print('out from the while')
#for c in range((l1+l2)-1 , -1,-1):
print(res)  
        
