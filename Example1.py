from decimal import Decimal
def sqrt(n): 
  low = 0 
  high = n 
  while high-low > 0.00001: 
    mid = (low+high) / 2 
    if mid*mid <= n: 
      low = mid 
    else: 
      high = mid 
  return low 

def sqrtx(n, x): 
  low = 0 
  high = n 
  while high-low > 0.00001: 
    mid = (low+high) / 2 
    if pow(mid, x) <= n: 
      low = mid 
    else: 
      high = mid 
  return low 

def sqrty(n, x, y): 
    low = 0 
    high = n 
    while high-low > 0.00001: 
        mid = (low+high) / 2 
        if pow(mid, y) <= n: 
          low = mid 
        else: 
          high = mid 
    return pow(low, x) 

def sqrtz(n, x):
  low = 0
  high = n
  for i in range(1, n):
    if (i ** x) >= n:
      high = i
      low = high - 1
      break
  while high-low > 0.00001: 
    mid = (low+high) / 2 
    if pow(mid, x) <= n: 
      low = mid 
    else: 
      high = mid 
  return low

import math
def sqrtBig(n, x, p):
    logn = math.log(n) / x
    difference = 1 / (10 ** p)
    low = 1
    high = n
    mid = (low + high) / 2
    while True:        
        if abs(math.log(mid) - logn) < difference:
            break        
        mid = (low + high) / 2
        if (math.log(mid) - logn) > 0:
            high = mid
        else:
            low = mid
    return high
  
