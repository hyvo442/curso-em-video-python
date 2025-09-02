import math
import random
s0=int(random.randint(1,360))
s1=math.cos(math.radians(s0))
s2=math.sin(math.radians(s0))
s3=math.tan(math.radians(s0))
print("o angulo escolhido foi {} \n o seu coseno é {}\n o seu seno é {} \n a sua tangente é {}".format (s0,s1,s2,s3))
