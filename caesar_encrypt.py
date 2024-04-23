ALPHABET = ' ABCDEFGHIJKLPQRSTUVWXYZ'
encrypted = 'VJKUBKUBCBOGUUCIG'

def crack_caesar(cipher_text):
    for key in range(len(ALPHABET)):
        plain_text = ''
        for c in cipher_text:
            index = ALPHABET.find(c)
            index = (index - key) % len(ALPHABET)
            plain_text = plain_text + ALPHABET[index]
        print('With key %s, the result is: %s' % (key, plain_text))
        
if __name__ == '__main__':
    
    #encrypted = 'VJKUBKUBCBOGUUCIG'
    crack_caesar(encrypted)
