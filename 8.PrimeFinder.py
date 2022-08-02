def prime_checker(n):
  prime = True
  for a in range(2,n-1):
    if n % a == 0:
      prime = False
  if prime:
    print("It's a prime number")
  else:
    print("It's not a prime number")

number = int(input("Check this number: "))
prime_checker(number)



