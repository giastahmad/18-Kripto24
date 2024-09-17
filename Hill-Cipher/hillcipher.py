import numpy as np
from sympy import Matrix, mod_inverse, gcd

def encryptHillCipher(pText, key):
    result = ""
    pText = pText.replace(" ", "").upper()
    block_size = len(key)

    determinanKey = int(np.round(np.linalg.det(np.array(key))))
    if determinanKey % 2 == 0 or determinanKey == 13 or determinanKey == -13:
        return "Nilai determinan kunci tidak valid, perhitungan tidak bisa dilanjutkan!"

    if len(pText) % block_size != 0:
        pText += "X" * (block_size - len(pText) % block_size)

    blocks = [pText[i : i + block_size] for i in range(0, len(pText), block_size)]

    for block in blocks:
        numeric_plain_block = np.array([ord(char) - ord("A") for char in block])
        numeric_cipher_block = np.dot(key, numeric_plain_block) % 26
        result += "".join(chr(num + ord("A")) for num in numeric_cipher_block)

    return result


def decryptHillCipher(cText, key):
    result = ""
    cText = cText.replace(" ", "").upper()
    block_size = len(key)

    if len(cText) % block_size != 0:
        cText += "X" * (block_size - len(cText) % block_size)

    blocks = [cText[i : i + block_size] for i in range(0, len(cText), block_size)]
    determinanKey = int(np.round(np.linalg.det(np.array(key))))

    key_matrix = Matrix(key)
    inverse_key = np.array(key_matrix.inv_mod(26), dtype=int)

    for block in blocks:
        numeric_cipher_block = np.array([ord(char) - ord("A") for char in block])
        numeric_plain_block = np.dot(inverse_key, numeric_cipher_block) % 26
        result += "".join(chr(num + ord("A")) for num in numeric_plain_block)

    return result


def textToMatrix(text, keySize):
    matrix = []

    text = text[: keySize * keySize]

    for i in range(0, len(text), keySize):
        row = [ord(char) - ord("A") for char in text[i : i + keySize]]
        matrix.append(row)

    matrix = np.array(matrix)

    if matrix.shape != (keySize, keySize):
        raise ValueError(f"Matriks tidak sesuai ukuran {keySize}x{keySize}")

    return matrix


def keyFindHillCipher(pText, cText, keySize):
    if len(pText) % keySize != 0:
        pText += "X" * (keySize - len(pText) % keySize)

    if len(cText) % keySize != 0:
        cText += "X" * (keySize - len(cText) % keySize)

    matrixPlainText = textToMatrix(pText, keySize)
    matrixCipherText = textToMatrix(cText, keySize)

    if matrixPlainText.shape != (keySize, keySize) or matrixCipherText.shape != (
        keySize,
        keySize,
    ):
        raise ValueError(
            "Plaintext or Ciphertext matrices are not of the correct size."
        )

    detMatrixPlainText = (
        int(np.round(np.linalg.det(matrixPlainText))) % 26
    )

    if gcd(detMatrixPlainText, 26) != 1:
        raise ValueError(
            f"Plaintext matrix is not invertible mod 26. Determinant: {detMatrixPlainText}"
        )

    inverseMatrixPlainText = Matrix(matrixPlainText).inv_mod(26)
    inverseMatrixPlainText = np.array(inverseMatrixPlainText).astype(int)

    key = np.dot(matrixCipherText, inverseMatrixPlainText) % 26

    return key

# Menu program
def main():
    while True:  # Loop terus sampai opsi keluar dipilih
        print("\n=== Hill Cipher Program ===")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Key Find")
        print("4. Exit")
        choice = input("Choose an option (1/2/3/4): ")

        if choice == "1":
            pText = input("Enter the plaintext: ")
            keySize = int(input("Enter the key size: "))
            key = []
            print(f"Enter the {keySize}x{keySize} key matrix:")
            for i in range(keySize):
                row = list(map(int, input().split()))
                key.append(row)

            encrypted_text = encryptHillCipher(pText, key)
            print(f"Encrypted Text: {encrypted_text}")

        elif choice == "2":
            cText = input("Enter the ciphertext: ")
            keySize = int(input("Enter the key size: "))
            key = []
            print(f"Enter the {keySize}x{keySize} key matrix:")
            for i in range(keySize):
                row = list(map(int, input().split()))
                key.append(row)

            decrypted_text = decryptHillCipher(cText, key)
            print(f"Decrypted Text: {decrypted_text}")

        elif choice == "3":
            pText = input("Enter the plaintext: ")
            cText = input("Enter the ciphertext: ")
            keySize = int(input("Enter the key size: "))

            try:
                key = keyFindHillCipher(pText, cText, keySize)
                print(f"Key matrix:")
                print(key)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "4":
            print("Exiting program...")
            break  # Keluar dari loop dan program berakhir

        else:
            print("Invalid option! Please choose again.")

main()
