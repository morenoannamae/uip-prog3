

input("Laboratorio")

n = 10
h = 0
while n <= 5000:
    if n!=100 and n !=1000:
      if n%2 == 0:
        print (n)
        h += n
    n += 1


print ('cantidad sumada: %i' % h)
