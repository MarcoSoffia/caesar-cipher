from caesar_cipher import encrypt

def brute_force(text:str)->list[tuple[int,str]]:
    key = 0
    result = []
    while key <26:
        result.append((key,encrypt(text,key)))
        key = key + 1
    return result


if __name__ == '__main__':
    input_utente = 'WPFKXQPEG'
    result = brute_force(input_utente)

    for k,testo in result:
        print(f'{k}: {testo}')