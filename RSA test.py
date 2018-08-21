import math
import random
from decimal import Decimal, localcontext
def xgcd(j,k):
    i = 0
    q = []
    r = []
    x = []
    y = []
    k = [k]
    j = [j]
    r += [k[i]%j[i]]

    while r[i-1] != 0:
        q.insert(i,k[i]//j[i])
        r.insert(i,k[i] - q[i] * j[i])
        k.insert(i+1,j[i])
        j.insert(i+1,r[i])
        i+=1

    i-=1
    gcd = j[i]
    y = [None]*(i+1)
    x = [None]*(i+1)
    y[i] = 0
    x[i] = 1
    i = i - 1
    while i >= 0:
       y[i] = x[i + 1]
       x[i] = y[i + 1] - q[i] * x[i + 1]
       i = i - 1
    return [gcd,x[0],y[0]]

def generated_random_prime(n_digits):
    lower = 10**(n_digits-1)
    upper = (10**n_digits)-1
    n = random.randint(lower, upper)
    k = math.sqrt(n)
    while n%2 == 0:
        n = random.randint(lower, upper)
        k = math.sqrt(n)       
    i = 3
    while i<=k:
        if n%i == 0:
             i = 3
             n -=2
             k = math.sqrt(n)
        else:
            i+=2
    return n

def generated_e(p,q):
    

    '''
def generated_random_prime(n_digits):
    lower = 10 ** (n_digits - 1)
    higher = 10 ** n_digits - 1
    nonprimelist = []
    primelist = []
    alist = [2,3,5,7,11,13,17,19]
    for m in range(lower, higher+1):
        a = random.choice(alist)
        if (a ** (m - 1)) % m != 1:
            nonprimelist.append(m)

    for p in range(lower,higher+1):
        if p not in nonprimelist:
            primelist.append(p)
            
    for i in range(1,2):
        prime = random.choice(primelist)
        print(prime)

'''
    '''
def fast_exponentiate(a,e,m):
    i = math.floor(math.log(e,2))
    l = [0]*(i+1)
    l[0]= 1
    e=e//2
    y = 1
    x = (a%m)
    count= 0
    while i>0:
       x= (x**2)%m
       count+=1
       if e%2 == 1:
           l[i-1] = 1
           y = (y*x)%m
           count+=1
       e=e//2
       count+=1
       i-=1
    x = (x**2)%m
    y = (y*x)%m
    return l, y, count
    '''
def find_inverse(e, m):
    return xgcd(e,m)[1]%m

def fast_exponentiate(a,e,m):
    k = e%2
    if e//2 == 0:
         return a%m
    elif k == 1:
         n = (a%m*fast_exponentiate(a%m,e//2,m)**2)%m
         return n
    else:
         n = (fast_exponentiate(a%m,e//2,m)**2)%m
         return n

def nmfast_exponentiate(a,e):
    k = e%2
    if e//2 == 0:
         return a
    elif k == 1:
         n = a*nmfast_exponentiate(a,e//2)**2
         return n
    else:
         n = nmfast_exponentiate(a,e//2)**2
         return n




    
