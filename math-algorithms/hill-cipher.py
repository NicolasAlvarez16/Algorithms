from gcd import gcd, extended_gcd, swap
import numpy as np

MOD = 26

def encode_alphabet():
    aux = 'A'
    j = 0
    alphabet = [chr(ord(aux) + i) for i in range(MOD)]
    alphabet_dict = {}

    for i in alphabet:
        alphabet_dict.update({i : j})
        j += 1
    return alphabet_dict

def matrix_multiply(input_text, matrix, alphabet_dict):
    keys = list(alphabet_dict) # Letters
    values = list(alphabet_dict.values()) # Values
    output_text = ""

    for i in range(len(input_text)):
        if i % 2 == 0:
            # Upper row of the matrix
            j = 0 # Matrix variable
            x = 0 # Matrix variable
            aux = matrix[j][x] * values[keys.index(input_text[i])]
            aux = aux + (matrix[j][x + 1] * values[keys.index(input_text[i + 1])])
            if(aux > MOD):
                aux = aux % MOD
            output_text = " ".join([output_text, keys[aux]])
        else:
            # Lower row of the matrix
            j = 1
            x = 0
            aux = matrix[j][x] * values[keys.index(input_text[i - 1])]
            aux = aux + (matrix[j][x + 1] * values[keys.index(input_text[i])])
            if(aux > MOD):
                aux = aux % MOD
            output_text = " ".join([output_text, keys[aux]])
    return output_text

def decrypt(alphabet_dict):
    # Inverse of a mtrix = (det)^-1 * adj
    encrypted_text = input("Enter your encripted text: ")
    encrypted_text = encrypted_text.replace(" ", "")
    encrypted_text = encrypted_text.upper()
    add_extra_letter = False
    decrypted_text = ""
    matrix = [[int(input("Enter a number for your matrix: ")) for j in range(2)] for i in range(2)]
    r = []
    q = []

    if(len(encrypted_text) % 2 != 0):
        add_extra_letter = True
        encrypted_text = encrypted_text + 'X'
    
    # Getting the determinant (det)
    det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0]) 
    aux, r, q = gcd(MOD, det, r, q) # Calling gcd not to rewrite code
    x, y = extended_gcd(r, q, 1, 0, 0, 1, 0) # Calling extended_gcd not to rewrite code
    det = (y % MOD)

    # Swapping the positions of matrix (adj)
    matrix[0][0], matrix[1][1] = swap(matrix[0][0], matrix[1][1])
    matrix[0][1] *= -1
    matrix[1][0] *= -1
    matrix = [[(det * matrix[i][j]) % MOD for j in range(2)] for i in range(2)]

    decrypted_text = matrix_multiply(encrypted_text, matrix, alphabet_dict)

    if(add_extra_letter):
        decrypted_text = decrypted_text[:-1]

def encrypt(alphabet_dict):
    plain_text = input("Enter your plain text: ")
    plain_text = plain_text.replace(" ", "")
    plain_text = plain_text.upper()
    add_extra_letter = False
    encripted_text = ""
    matrix = [[int(input("Enter a number for your matrix: ")) for j in range(2)] for i in range(2)]

    if(len(plain_text) % 2 != 0):
        add_extra_letter = True
        plain_text = plain_text + 'X' # To make sure all letters have pairs

    encripted_text = matrix_multiply(plain_text, matrix, alphabet_dict)

    if(add_extra_letter):
        encripted_text = encripted_text[:-1]
    return encripted_text

def main():
    alphabet_dict = encode_alphabet()
    option = -1
    while(option != 0):
        print("------------------HILL CIPHER------------------")
        print("1. Encrypt")
        print("2. Decrypt")
        print("0. Exit")
        print("-----------------------------------------------")
        option = int(input("Enter option: "))
        if(option == 1): 
            print(encrypt(alphabet_dict))
        elif(option == 2):
            print(decrypt(alphabet_dict))
        else:
            print("Exit")

if "__main__" == __name__:
    main()