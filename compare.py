import math
import random
import time
import numpy as np
from functools import reduce

# def sltn(n):
#     i=5
#     while True:
#         trng=sum(range(1,i+1))
#         # break
#         j=0
#         for k in range(1,trng+1):
#             if trng%k==0:
#                 j+=1
#         if j>n:
#             print(i)
#             print(trng)
#             break
#         i+=1
# sltn(500)
# print([i for i in range(1,101)if 100%i==0])
# n=3
# while True:
#     trng=n*(n+1)//2
#     n+=1
#     dic={}
#     i=2
#     while i < trng:
#         if trng%i==0:
#             # print(i)
#             trng=trng//i
#             if i in dic:
#                 dic[i]+=1
#             else:
#                 dic[i]=1
#             i-=1
#         i+=1
#     p=map(lambda x: (x+1),dic.values())
#     d=reduce(lambda x,y: x*y,p)
#     if d > 500:
#         print((n-2)*(n-1)//2) 
#         break
    
def f(L, nMax=45000):
    d = [0]*nMax
    print(d)
    for n in range(1, nMax):
        for j in range(n, nMax,n):
            d[j]+= 1
        nDiv = d[n-1]*d[n//2] if n%2==0 else d[(n-1)//2]*d[n]
        if nDiv > L: return (n-1)*n//2
for _ in range(int(input())):
    print (f(int(input()))) 
# d = [34]*4500
# print(d)
# for j in range(1,10,5):
#     print(j)
    
        
    
        
            



# j=1
# while True:
#     n=int(j*(j+1)/2)
#     k=0
#     for i in range(1,n+1):
#         if n%i==0:
#             k+=1
#     if k>500:
#         print(n)
#         print(j)
#         break
#     j+=1
# n=5
# print(int(n*(n+1)/2))

    


# numbers='''
# 08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
# 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
# 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
# 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
# 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
# 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
# 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
# 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
# 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
# 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
# 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
# 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
# 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
# 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
# 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
# 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
# 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
# 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
# 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
# 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'''
# numbers = numbers.strip().split('\n')
# numbers=[list(map(int,x.strip().split(' '))) for x in numbers]
# def sltn(a):
#     largest=0
#     for i in a:
#         multiple=reduce(lambda x,y: x*y,i)
#         if multiple>largest:
#             largest=multiple
#     for i in range(len(a)):
#         multiple=1
#         for j in range(len(a)):
#             multiple*=a[j][i]
#             if multiple>largest:
#                 largest=multiple
#     multiple=1
#     rorl=1
#     for i in range(len(a)):
#         multiple*=a[i][i]
#         rorl*=a[len(a)-1-i][i]
#     if multiple>largest:
#         largest=multiple
#     if rorl>largest:
#         largest=rorl
#     return largest
# a=[]
# for i in range(len(numbers)-3):
#     for j in range(len(numbers)-3):
#         sub=[]
#         sub.append(numbers[i][j:j+4])
#         sub.append(numbers[i+1][j:j+4])
#         sub.append(numbers[i+2][j:j+4])
#         sub.append(numbers[i+3][j:j+4])
#         print(sub)
#         a.append(sub)
# a=map(sltn,a)
# print(max(a))
# def algo1():
#     grid = ("08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 "
#             "49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 "
#             "81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 "
#             "52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 "
#             "22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 "
#             "24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 "
#             "32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 "
#             "67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 "
#             "24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 "
#             "21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 "
#             "78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 "
#             "16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 "
#             "86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 "
#             "19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 "
#             "04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 "
#             "88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 "
#             "04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 "
#             "20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 "
#             "20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 "
#             "01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48").split(" ")
#     intList = list(map(lambda x: int(x), grid))

#     npGrid = np.zeros((28,28))

#     # Fill 2-D npGrid
#     for (i, value) in enumerate(grid):
#         col = i % 20
#         row = (i - col) // 20
#         npGrid[row + 4, col + 4] = value

#     # The original grid has 0 zeroes on all sides.
#     # If we try to index outside of original grid this causes * 0 => no worries.

#     maxProd = 1
#     for row in range(4, 24):
#         for col in range(4, 24):
#             for i in range(4):
#                 # Vertical
#                 prod = reduce(lambda a,b: a*b, npGrid[row-i:row+(4-i),col])
#                 if prod > maxProd:
#                     maxProd = prod
#                 # Horizontal
#                 prod = reduce(lambda a,b: a*b, npGrid[row,col-i:col+(4-i)])
#                 if prod > maxProd:
#                     maxProd = prod
#                 # Diagonal from top-left to bottom-right
#                 rows = np.arange(row-i, row+(4-i))
#                 cols = np.arange(col-i, col+(4-i))
#                 prod = reduce(lambda a,b: a*b, npGrid[rows, cols])
#                 if prod > maxProd:
#                     maxProd = prod
#                 # Diagonal from top-right to bottom-left
#                 rows = np.arange(row-i, row+(4-i))
#                 cols = np.arange(col+i, col-(4-i), -1)
#                 prod = reduce(lambda a,b: a*b, npGrid[rows, cols])
#                 if prod > maxProd:
#                     maxProd = prod

#     return int(maxProd)
# print(algo1())


# a,b=1,2
# l=0
# while True:
#     if a < 4000004:
#         if a%2==0:
#             l+=a
#         a,b=b,a+b
#     else:
#         break
# print(l)
# ml=time.time()


# print(sum(i for i in range(1,1000) if i%5==0 or i%3==0))

# def is_prime(n):
#     for i in range(2,int(math.sqrt(n)+1)):
#         if n%i==0:
#             return False
#     return True
# print(sum(i for i  in range(2,2000001) if is_prime(i) ))
# # l=[]
# print([l.append(i) for i in range(2,2000001 ) if is_prime(i)])
# print(sum(l))
# l=[]
# for i in range(2,2000001):
#     if is_prime(i):
#         l.append(i)
# print(l)
# print(sum(l))


# st=time.time()
# num='''
# 717653133167306249192251196744265747423553491949349698352031277450632623957831801698480186947885184385861560789112949495459501737958331952853208805511125406987471585238630507156932909632952274430435576689664895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749303589072962904915604407723907138105158593079608667017242712188399879790879227492190169972088809377665727333001053367881220235421809751254540594752243525849077116705560136048395864467063244157221553975369781797784617406495514929086256932197846862248283972241375657056057490261407972968652414535100474821663704844031998900088952434506585412275886668811642717147992444292823086346567481391912316282458617866458359124566529476545682848912883142607690042242190226710556263211111093705442175069416589604080719840385096245544436298123098787992724428490918884580156166097919133875499200524063689912560717600588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'''
# print(num[-1])
# num = num.strip().split('\n')
# num = ''.join(num)
# l=0
# for i in range(1000-13):
#     x=num[i:i+13]
#     x=list(x)
#     x=map(int,x)
#     m=reduce(lambda x,y:x*y,x)
#     if m>l:
#         l=m
# print(l)
# ml=time.time()
# print(st-ml)

# n=1234
# m=0
# while n>0:
#     a=n%10
#     m=m*10+a
#     n=n//10
# print(m)


# from random import randint
# while True:
#     a=randint(1,1000)
#     b=randint(1,1000)
#     c=1000-(a+b)
#     if (a**2) + (b**2)==c**2:
#         print(a*b*c)
#         break


# def rev(n):
#     m=0
#     while n > 0:
#         k=n%10
#         m=m*10+k
#         n=n//10
#     return m
# l=[]
# for i in range(10):
#     while True:
#         n=random.randint(900,999)
#         m=random.randint(900,999)
#         y=n*m
#         ry=rev(y)
#         if y==ry*1:
#             l.append(y)
#             break
# print(max(l))
# palindromes = []
# for x in range(100,999):
#     for i in range(100,999):
#         num = str(i*x).split()[0]
#         if len(num) == 6:
#             if num[0] == num[-1] and num[1] == num[-2] and num[2] == num[-3]:
#                 palindromes.append(i * x)
# print (max(palindromes))


# def prime(n):
#     for i in range(2,int(math.sqrt(n)+1)):
#         if n%i==0:
#             return False
#     return True
# def sltn(n):
#     i=2
#     j=0
#     while True:
#         if prime(i):
#             j+=1
#         if j==n:
#             print(i)
#             break
#         i+=1

# sltn(6)
# def insqr(n):
#   i=1
#   m=0
#   while True:
# insqr(6)
# check = range(10,21)
# a = 232792559
# b = False

# while b == False:
#     if a % 2520 == 0:
#         if all(a % n ==0 for n in check):
#             b = True
#         else:
#             a = a + 2520
#     else:
#         a = a + 1
# print(a)
# print(2520*2)
# for i in range(int(input())):
#     n,k=map(int,input().split())
#     print(max(n%i for i in range(1,k+1))))
# l=[]
# for i in range(int(input("Enter the lenght of the list\n"))):
#     m=int(input("enter the element of the list\n"))
#     l.append(m)
# nl=[]
# while l:
#     low=l[0]
#     for i in l:
#         if i < low:
#             low = i
#     l.remove(low)
#     nl.append(low)
# print("Here is your Sorted List")
# print(nl)


# for i in range(int(input())):
#     l=1
#     for i in range(1,int(input())+1):
#         l*=i
#     print(l)

# n,k=map(int,input().split())
# l=0
# for i in range(n):
#     if int(input())%k==0:
#         l+=1
# print(l)
# def fibn(n):
# cook your dish here
# for _ in range(int(input())):
#     n,k=map(int,input().strip().split())
#     print(max(n%i for i in range(1,k+1)))

#     if n==2:
#         return 1
#     elif n==1:
#         return 0
#     return fibn(n-1) + fibn(n-2)

# # print(fibn(4))
# #0112358
# a=0
# b=1
# for i in range(4):
#     c=a+b
#     # print(c)
#     a,b=b,c
# print(c)

# def swap(b):
#     for i in range(len(b)):
#         b[i]=i+1

# b=[4,5,6,7,87,9]
# swap(b)
# print(b)
# def reverse_list(arr):
#     i=0
#     j=len(arr)-1
#     if len(arr)%2==0:
#         l=len(arr)/2
#     else:
#         l=math.floor(len(arr)/2)
#     while i < l:
#         temp=arr[i]
#         arr[i]=arr[j]
#         arr[j]=temp
#         i+=1
#         j-=1
# arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,28,29,20]
# print("\0before functions\n",arr)
# reverse_list(arr)
# print("\0after functions\n",arr)
# def parser(arr):
#     jl=""
#     for ind,i in enumerate(arr):
#         if arr[ind]!="<":
#             jl=jl[:ind] + i + jl[ind:]
#     jls=""
#     for ind,i in enumerate(jl):
#         if jl[ind]!="h":
#             jls=jls[:ind] + i + jls[ind:]
#     print(jls)

# parser()
# def h(a):
#     b=a+1
# a=2
# print(a)
# a=2
# h(a)
# print(a)
# a="       hel lo  and    "
# print(" ".join(a.split()))
# arr=[]
# j=int(input("Enter the length of your list\n"))
# for i in range(j):
#     x=int(input("Enter the element of your list\n"))
#     arr.append(x)
# a=0
# av=[]
# for i in range(100):
#     if i in arr:
#         av.append(i)
# print(av)
# arr=[]
# for i in range(int(input())):
#     x=int(input())
#     arr.append(x)
# arr.sort(reverse=True)
# for i in arr:
#     print(i)
# for i in range(int(input())):
#     print(int(input()) + int(input()))
# T=int(input())
# for i in range(T):
#     a,b=map(int,input().split(" "))
#     print(a+b)
# a,b=map(float,input().split())
# c=0.50
# if a+c < b and a%5==0:
#     b=b-(a+c)
#     print(b)
# else:
#     print(b)
# da, bal = input().split(" ")
# debit_amount = float(da)
# balance = float(bal)
# charge = 0.50
# if (debit_amount + charge) < balance and debit_amount % 5 == 0:
#     balance = balance - (debit_amount + charge)
#     print(balance)
# else:
#     print(balance)

# print(0.01<0.2)


# from functools import reduce
# def LCM(a, b):
#     return a // math.gcd(a, b) * b
# N = int(input("The LCM for numbers 1 through "))
# print ("is", reduce(LCM, range(1, N+1)))