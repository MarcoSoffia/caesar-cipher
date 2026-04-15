"""
Cifrario di cesare
Puoi cifrare o decirare un messaggio data la chiave
"""
# Encrypt takes a char and encrypts it
def char_encrypt(text:str, key:int)->str:
    if text.isalpha():
        if text.isupper():
            c_normalization = ord(text) - 65
            c_crypto = (c_normalization + key) % 26
            return chr(c_crypto + 65)
        elif text.islower():
            c_normalization = ord(text) - 97
            c_crypto = (c_normalization + key) % 26
            return chr(c_crypto + 97)
    else:
        return text

# Cycles encrypt for the entire word
def encrypt(text:str, key:int)->str:
    result = []
    for c in text:
        result.append(char_encrypt(c, key))
    result = "".join(result)
    return result

if __name__ == '__main__':
    msg = input("Inserisci il messaggio ")
    key = int(input("Inserisci la chiave "))

    print(encrypt(msg, key))
