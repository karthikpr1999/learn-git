import string
import random
#time consumuption
import time
start_time = time.time()

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    
    s2 = string.ascii_uppercase
    
    s3 = string.digits
    
    #s4 = string.punctuation
    s5 = string.printable
    
    #Length of password
    plen = int(input("Enter the length of pasword: \n "))
    
    s = []
    
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    #s.extend(list(s4))
    s.extend(list(s5))
    
    random.shuffle(s)
    
    print("".join(s[0:plen]))
    print("%s"%(time.time() - start_time))  
