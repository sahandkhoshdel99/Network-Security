import math 

def decrypt_bytes(c, n, d):
    m = pow(c,d) % n 
    return m

def decrypt(input_file, output_file, private_key):
    
    ciphertext = open(input_file, "rb") # opening plain text in read-binary mode 
    decrypted = open(output_file, "wb") # opening cipher text in write-binary mode
    decrypted.truncate(0) #erasing previous info (overwriting content)

    d = int(open(private_key, "r").readlines()[0][:-1]) # removing '\n' charecter and casting 'd' to 'int' type
    n = int(open(private_key, "r").readlines()[1][:-1]) 
    C_block = (int(math.ceil(math.log2(n-1)))+ 8)//8 # calculating max needed space for cipherblocks (in bytes)
    print(C_block)
    
    while (cipher_byte := ciphertext.read(C_block)):
        # Decryption; ['C' bytes -> int / decrypt / int -> byte]:
        plain_byte = decrypt_bytes(int.from_bytes(cipher_byte, "big"), n, d).to_bytes(1, 'big')
        decrypted.write(plain_byte)

    decrypted.close()

decrypt('input.txt.enc', 'output.txt', 'private.key')

