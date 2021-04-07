# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 12:30:46 2021

@author: ELCOT
"""
"""
Example:

Virus Composition, V = coronavirus

Blood Composition of the person , B = ravus


The person in question is POSITIVE as B is the subsequence of the V. otherwise print NEGATIVE

"""
def main(cov_s , per_s):

    # Write code here 
    print(cov_s , per_s)
    i , j ,l_co , l_per ,status= 0,0 , len(cov_s) , len(per_s) ,1 # 0 for negative 1 for positive
    while i<l_co:
        print('at ehich posiiotn',cov_s[i] , per_s[j] , i, j )
        if j == l_per-1:
            status = 1
            break
        if i == l_co-1 and j!=l_per-1:
            status = 0
        if cov_s[i] == per_s[j]:
            print('match found')
            i+=1
            j+=1
        else:
            i+=1
    if status ==0:
        print('NEGATIVE')
    else:
        print('POSITIVE')
    
        

"""    
cov_s = input()
n= int(input())
for _ in range(n):
    main(cov_s , input()) #calling main for each person input
"""
main('coronavirus' ,  'corona')
