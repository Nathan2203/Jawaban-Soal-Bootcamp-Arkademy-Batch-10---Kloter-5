'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import json

'''def my_function(nama = "Jonathan Benedict Sirait", address = "Griya Permata Blok A No. 229", hobbies = ["Basket", "Berenang"]):
    
my_function()#
'''

def my_function():
    x = {
        "name": "Jonathan Benedict Sirait",
        "address": "Griya Permata Blok A No. 229",
        "is_married": False,
        "school": {"highSchool": "SMKN 1 Batam", "university": "-"},
        "skills": [
            {"name": "Networking & Programming"},
            {"score": 90, "mpg": 24.1}
            ]
            
        }
    print(json.dumps(x, indent=4))
    

my_function()

'''
yoyo = {
        "name": "Jonathan Benedict Sirait",
        "address": "Griya Permata Blok A No. 229",
        "is_married": False,
        "school": {"highSchool": "SMKN 1 Batam", "university": "none"},
        "skills": [
            {"name": "Networking & Programming"},
            {"score": 90}
            ]
        }
        
print(json.dumps(yoyo))
'''

