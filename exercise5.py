def summe_funktion(a, r, n):
  s=0
  i=0
  for i in range(1, n):
      s=s+a*(r**(i-1))
  print(s)  

summe_funktion(1, 0.5, 10)