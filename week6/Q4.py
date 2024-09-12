def encrypt(main,sym):
    enc=""
    for i in range(len(main)-1):
        enc += main[i]+sym
    enc += main[-1]
    return enc

def decrypt(enc,sym):
    n=len(sym)
    dec= ""
    for i in range(0, len(enc), n+1):
        dec += enc[i]
    return dec

main = input("Enter a string to encrypt: ")
sym = str(input("Enter symbol string used for encryption: "))
enc_string = encrypt(main,sym)
print("Encrypted string:", enc_string)
print("Decrypted string:", decrypt(enc_string,sym))
    
