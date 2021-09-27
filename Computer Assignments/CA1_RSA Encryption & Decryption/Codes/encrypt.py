import math

def encrypt_byte(m, e, n):
    c = pow(m,e) % n 
    return c

def encrypt(input_file, output_file, public_key):
    
    plaintext = open(input_file, "rb") # opening plain text in read-binary mode 
    ciphertext = open(output_file, "wb") # opening cipher text in write-binary mode
    ciphertext.truncate(0) #erasing previous info (overwriting content)

    e = int(open(public_key, "r").readlines()[0][:-1]) # removing '\n' charecter and casting 'n' to 'int' type
    n = int(open(public_key, "r").readlines()[1][:-1]) 
    C_block = (int(math.ceil(math.log2(n-1)))+ 8)//8 # calculating max needed space for cipherblocks (in bytes)
    print(C_block)
    
    while (plain_byte := plaintext.read(1)):
        # Encryption; [byte -> int / encrypt / int -> byte(we denote the number of bytes we have calculated)]:
        cipher_byte = encrypt_byte(int.from_bytes(plain_byte, "big"), e, n).to_bytes(C_block, 'big')
        ciphertext.write(cipher_byte)
        
    ciphertext.close()

encrypt('input.txt', 'input.txt.enc', 'public.key')

