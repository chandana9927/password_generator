import random
import string
import sys

SIZE = 10
argv_len = len(sys.argv)

if argv_len > 2:
    raise ValueError("Please provide just the desired password length as argument.")

if argv_len == 2:
    try:
        SIZE = int(sys.argv[1])  
    except ValueError:
        raise ValueError("Please enter a valid integer as argument.")
    
if SIZE < 1 or SIZE > 24:
    raise ValueError("Password size must be between 1 and 24.")  

def pw_gen(size=10, ch=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(ch) for _ in range(size))

print(pw_gen(size=SIZE))
