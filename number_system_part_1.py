from decimal import Decimal as d
# h=d(0.7+0.2) #0.899999999911111188888...... we will get exat answer but length answer
# h=d(0.7)+d(0.2) #0.899999991.. we get exat answer but half anser
# h=d("0.7")+d("0.2") #0.9 we get the answer but short and exat what the answer we need 
# print(h)

from fractions import Fraction as f 
# a=f(1,0) #zero division error
# print(a)
a=f(1,1) #1
print(a)
# a=f(1,5) #1/5
# print(a)
# a=f(2) #2
# print(a)
# a=f(0,5) #0
# print(a)
# a=f(5,25) #1/5
# print(a)