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

