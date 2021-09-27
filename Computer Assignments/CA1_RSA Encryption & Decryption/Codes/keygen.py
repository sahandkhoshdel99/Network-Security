from math import sqrt, floor
import random 

def eed(a, b): #extended_euclidean _algorithm L computes the gcd and proper factors for modular equation, recursilvely by long division
    if(a==0):
        return b, 0, 1 # long division has reached the end 
    
    gcd,w,z = eed(b%a, a)
    x = z - (b//a) * w #substituting equations bottom to up to find x = d, y
    y = w
    return gcd, x, y

def get_primes():
    p, q = input("Enter p and q (the two prime numbers for RSA key genration). Separate them by space : ").split()
    p = int(p)
    q = int(q)
    
    if (p == q): # verifying inequality:
        raise ValueError("Entered numbers shouldn't be equal!")
    
    if(p*q<=256): # verifying (n = p.q) > 256 = :
        raise ValueError("n = p * q (Product) should be larger than 256!")
        
    for i in range(2, floor(sqrt(p))+1): # verifying primality:
        if(p % i ==0):
            raise ValueError(f"First Entered Number(p) isn't prime. {p} = {i} * {int(p/i)}\n")
 

    for j in range(2, floor(sqrt(q))+1): # verifying primality:
        if(q % j ==0):
            raise ValueError(f"Second Entered Number(q) isn't prime. {q} = {j} * {int(q/j)}\n") 
    return p,q

def key_generation():
    p, q = get_primes()
    n = p*q
    phi_n = (p-1)*(q-1)
    
    while(True):
        e = random.randrange(2,phi_n)
        if(eed(e, phi_n)[0] == 1):# checking e and phi are coprime:
            break
    d = eed(e, phi_n)[1]
    while(d<0):
        d += phi_n
    print(f"\np = {p}, q = {q}, n = {n}, phi = {phi_n}, e = {e}, d= {d}") #printing all parameters
    
    # generating public and private keys:
    publickey_lines = [str(e)+'\n', str(n)+'\n'] 
    privatekey_lines = [str(d)+'\n', str(n)+'\n']
    
    public = open("public.key","w")
    public.truncate(0) #erasing previous info (overwriting content)
    public.writelines(publickey_lines)  
    public.close()
    
    private = open("private.key","w")
    private.truncate(0)
    private.writelines(privatekey_lines)  
    private.close()
    
    return n, e, d

key_generation()