import secrets
import string

AMBIGUOUS = "Il1O0@"

def generate_password(
    length: int = 12,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
    avoid_ambiguous: bool = False,
) -> str:
    """
    La password deve contenere almeno un carattere per ogni set abilitato
    Se tutte le flag sono false devo ritornare ValueError
    Se N_flags > lenght -> ValueError
    Se avoib_ambigous=True non permettere (I,l,1,O,@)
    """
    groups = []

    if use_upper:
        groups.append(string.ascii_uppercase)
    if use_lower:
        groups.append(string.ascii_lowercase)
    if use_digits:
        groups.append(string.digits)
    if use_symbols:
        groups.append(string.punctuation)
    if avoid_ambiguous:
        groups = [
            "".join(c for c in group if c not in AMBIGUOUS)
            for group in groups
        ]

    # Riformulo la lista come una concatenzione dei caratteri degli insiemi
    groups = [group for group in groups if group]

    if not groups:
        raise ValueError("At least one character set must be enabled")
    if len(groups) > length:
        raise ValueError("Password length is too short for the enabled sets")
    password_chars = [secrets.choice(group) for group in groups]
    all_chars = "".join(groups)

    # Modo più elegante suggerito da chat, .extend() permette di concatenare due liste in una senza finire in ['A', 'B', ['C', 'D']]
    password_chars.extend(
        secrets.choice(all_chars) for _ in range(length - len(password_chars))
    )
    # Mescolo la psw
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)

if __name__ == '__main__':

    print("=== Password generator ===")
    print("1) Profilo default (12 caratteri, tutti i set, visualizza a schermo)")
    print("2) Profilo custom")

    scelta = int(input("Scelta: "))

    if scelta == 1:
        print(f"Password: {generate_password()}")
    elif scelta == 2:
        length = int(input("Length: "))
        upper = input("Maiuscole? (y/n): ").lower()
        lower = input("Minuscole? (y/n): ").lower()
        digits = input("Cifre? (y/n): ").lower()
        symbols = input("Simboli? (y/n): ").lower()
        ambiguous = input("Evita ambigui? (y/n): ").lower()

        upper = True if upper == "y" else False
        lower = True if lower == "y" else False
        digits = True if digits == "y" else False
        symbols = True if symbols == "y" else False
        ambiguous = True if ambiguous == "y" else False

        print(generate_password(length,upper,lower,digits,symbols,ambiguous))
    else:
        print("Opzione non valida")

