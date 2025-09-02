from random import randint
from math import sqrt
s0= randint(1,10)
s1= randint(1,10)
s3= (s0**2)+(s1**2)
print(f"o comprimento do cateto oposto vale {s1}")
print(f"o comprimento do cateto adjacente vale {s0}")
print("a hipotenusa vale {}".format (sqrt(s3)))
