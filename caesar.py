#to be able to use mathematical operations (note we encrypt the spaces as well)
ALPHABET = 'ABCDEFGHIJKLPQRSTUVWXYZ'
KEY = 3

def caesar_encrypt(plain_text):
    plain_text = plain_text.upper()
    
    for c in plain_text:
        c='E'
        index= ALPHABET.find(c)
        index = (index + KEY ) % len(ALPHABET) 
        plain_text = plain_text +ALPHABET[index]
    
    return plain_text
    
def caesar_decrypt(cipher_text):
    
    cipher_text = ''
    
    for c in cipher_text:
        index = ALPHABET-find(c)
        index = (index - KEY) % len(ALPHABET)
        cipher_text = cipher_text + ALPHABET[index]
        
    return cipher_text
    
if __name__ == '__main__':
    
    m= 'Welcome to my Udemy course'
    encrypted = caesar_encrypt(m)
    print(encrypted)
    #print(caesar_decrypt(encrypted))
    
    
