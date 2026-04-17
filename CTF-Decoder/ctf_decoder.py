from base64 import b64decode


def solve_level_1():
    ctf = '666c61677b68337834646563696d616c5f63346e5f62335f41424144424142457d'
    return bytes.fromhex(ctf)


def solve_level_2():
    # base64
    parte_1 = 'ZmxhZ3t3NDF0XzF0c19hbGxfYjE='
    # intero
    parte_2 = 664813035583918006462745898431981286737635929725

    ctf_1 = b64decode(parte_1)
    ctf_2 = parte_2.to_bytes(20, 'big')

    return ctf_1 + ctf_2


def solve_level_3():
    ctf = 'NjY2YzYxNjc3YjZjMzQ3OTMzNzIzNTVmMzA2ZTVmNmMzNDc5MzM3MjM1N2Q='
    decoded = b64decode(ctf)
    return bytes.fromhex(decoded.decode())


def solve_level_4():
    ctf = 'Wm14aFozdGlOSE16WDNNeGVIUjVYMll3ZFhKZk1XNWpNM0IwTVRCdWZRPT0='
    raw = b64decode(ctf)
    return b64decode(raw)


def solve_level_5():
    ctf = '7d72337474346d5f73337479625f35647234776b6334627b67616c66'
    return bytes.fromhex(ctf)[::-1]


def solve_level_6():
    ctf = '0066006c00610067007b007a003300720030005f00700034006400640031006e0067005f0033007600330072007900770068003300720033007d'
    return bytes.fromhex(ctf).decode('utf-16-be').encode()


def solve_level_7():
    ctf = '4e6a5932597a59784e6a6333596a63304e6a67334d6a4d7a4d7a4d315a6a5a6a4d7a51334f544d7a4e7a49334d7a566d4e6a517a4d7a4d7a4e7a41335a413d3d'
    decoded = b64decode(bytes.fromhex(ctf))
    return bytes.fromhex(decoded.decode())


def solve_level_8():
    parts = [
        '666c6167',
        'e20xeA==',
        '5f346e64',
        'X200dA==',
        '63685f33',
        'bmMwZA==',
        '316e6735',
        'fQ==',
    ]

    flag = ""
    flag += bytes.fromhex(parts[0]).decode()
    flag += base64.b64decode(parts[1]).decode()
    flag += bytes.fromhex(parts[2]).decode()
    flag += base64.b64decode(parts[3]).decode()
    flag += bytes.fromhex(parts[4]).decode()
    flag += base64.b64decode(parts[5]).decode()
    flag += bytes.fromhex(parts[6]).decode()
    flag += base64.b64decode(parts[7]).decode()

    print(flag)




def solve_level_9():
    ctf = 'bXNobntqNDN6NHlfdDMzYXpfaTR6MzY0fQ=='
    decoded = base64.b64decode(ctf).decode()

    print(decoded)


if __name__ == '__main__':
    solvers = [
        solve_level_1,
        solve_level_2,
        solve_level_3,
        solve_level_4,
        solve_level_5,
        solve_level_6,
        solve_level_7,
        solve_level_8,
        solve_level_9,
    ]

    for idx, solver in enumerate(solvers, start=1):
        print(f'Level {idx}: {solver().decode()}')
