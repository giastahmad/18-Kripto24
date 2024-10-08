def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plain_text_int = [ord(i) for i in plain_text]

    for i in range(len(plain_text_int)):
        value = (plain_text_int[i] + key_as_int[i % key_length]) % 26
        encrypted_text += chr(value + 65)  # Mengonversi kembali ke karakter

    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    encrypted_text_int = [ord(i) for i in encrypted_text]

    for i in range(len(encrypted_text_int)):
        value = (encrypted_text_int[i] - key_as_int[i % key_length]) % 26
        decrypted_text += chr(value + 65)  # Mengonversi kembali ke karakter

    return decrypted_text

def main():
    while True:
        print("\nVIGENERE CIPHER:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Keluar")

        choice = input("Pilih opsi (1/2/3): ")

        if choice == '1':
            plain_text = input("Masukkan teks (hanya huruf kapital): ").upper()
            key = input("Masukkan kunci (hanya huruf kapital): ").upper()
            encrypted_text = vigenere_encrypt(plain_text, key)
            print(f"\nTeks terenkripsi: {encrypted_text}")

        elif choice == '2':
            encrypted_text = input("Masukkan teks terenkripsi (hanya huruf kapital): ").upper()
            key = input("Masukkan kunci (hanya huruf kapital): ").upper()
            decrypted_text = vigenere_decrypt(encrypted_text, key)
            print(f"\nTeks terdekripsi: {decrypted_text}")

        elif choice == '3':
            break

        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
