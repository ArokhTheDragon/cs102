def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ''

    for char in plaintext:
        if char.islower():
            new_char = chr(ord('a') + (ord(char) - ord('a') + (shift % 26)) % 26)
            ciphertext += new_char
        elif char.isupper():
            new_char = chr(ord('A') + (ord(char) - ord('A') + (shift % 26)) % 26)
            ciphertext += new_char
        else:
            ciphertext += char

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ''

    for char in ciphertext:
        if char.islower():
            new_char = chr(ord('a') + (ord(char) - ord('a') - (shift % 26)) % 26)
            plaintext += new_char
        elif char.isupper():
           new_char = chr(ord('A') + (ord(char) - ord('A') - (shift % 26)) % 26)
           plaintext += new_char
        else:
            plaintext += char

    return plaintext
