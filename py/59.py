from itertools import product, cycle
from string import ascii_lowercase, punctuation

def _read(filename):
    with open(filename) as f:
        parts = f.read().split(',')
        return [int(p) for p in parts]

def _decrypt(cipher, key):
    #print(key)
    cycled_key = cycle(key)
    for c in cipher:
        k = ord(next(cycled_key))
        yield c ^ k

def decrypt(cipher, key):
    return ''.join(chr(c) for c in _decrypt(cipher, key))

def english(text):
    #return all(c.isalnum() or c.isspace() or c in punctuation for c in text)
    #return text[0].isalnum()
    common = ('the', 'be', 'to')
    return all(word in text for word in common)

def main():
    cipher = _read('p059_cipher.txt')
    #for key in product(ascii_lowercase, repeat=3):
    #    k = ''.join(key)
    #    text = decrypt(cipher, k)
    #    if english(text):
    #        print(k)
    #        print(text)
    text = decrypt(cipher, 'god')
    print(sum(ord(c) for c in text))

main()
