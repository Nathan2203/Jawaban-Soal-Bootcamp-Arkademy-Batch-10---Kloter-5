'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import math
'''
a = 2.54
for x in range(round(math.floor(a))):
  print(x) 
'''
def asd (n) :
    if(n/2 == 0):
        return 0;
        
    res = ''
    # res += "X X X X X \n"
    s = round(math.floor(n/2))
    for x in range(n):
        for y in range(n):
            if(x > 0 and x != n - 1):
                if(y == s):
                    res += "X "
                else:
                    res += "= "
            else :
                res += "X "
    
        res += "\n"
    # res += "X X X X X \n"
    print(res)

asd(9)