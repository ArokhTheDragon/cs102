# -*- coding: utf-8 -*-
def encrypt_caesar(plaintext):
    """
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
        if 'a' <= char <= 'z':
            new_char = chr(ord(char) % ord('a') + 3) % 26 + ord('a')
            ciphertext += new_char
        elif 'A' <= char <= 'Z':
            new_char = chr(ord(char) % ord('A') + 3) % 26 + ord('A')
            ciphertext += new_char
        else:
            new_char = char
            ciphertext += new_char
    return ciphertext


def decrypt_caesar(plaintext):
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for char in ciphertext:
        if 'a' <= char <= 'z':
            new_char = chr(ord(char) % ord('a') - 3) % 26 - ord('a')
            plaintext += new_char
        elif 'A' <= char <= 'Z':
            new_char = chr(ord(char) % ord('A') - 3) % 26 - ord('A')
            laintext += new_char
        else:
            new_char = char
            laintext += new_char
    return plaintext
