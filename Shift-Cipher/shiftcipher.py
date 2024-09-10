def shift_cipher(text, shift, mode):
    result = ""

    
    if mode == 'decrypt':
        shift = -shift


    for char in text:
        if char.isalpha():

            base = ord('A') if char.isupper() else ord('a')

            result += chr((ord(char) - base + shift) % 26 + base)
        else:

            result += char

    return result

def read_text(input_mode):
    if input_mode == 'input':
        return input("Masukkan teks: ")
    elif input_mode == 'file':
        file_path = input("Masukkan nama file (.txt) atau ketik 'kembali' untuk kembali: ")
        if file_path.lower() == 'kembali':
            return None
        try:
            with open(file_path, 'r') as file:
                text = file.read()
                if not text:
                    print(f"File '{file_path}' kosong, coba lagi.")
                    return None
                return text
        except FileNotFoundError:
            print(f"File '{file_path}' tidak ditemukan, coba lagi.")
            return None

def save_to_file(text):
    save = input("Apakah Anda ingin menyimpan hasil ke file? (y/n): ").lower()
    if save == 'y':
        file_path = input("Masukkan nama file untuk menyimpan hasil (misal: hasil.txt): ")
        with open(file_path, 'w') as file:
            file.write(text)
        print(f"Hasil telah disimpan ke file '{file_path}'.")

def menu():
    while True:
        print("----------------------------")
        print("|       Shift Cipher       |")
        print("----------------------------")
        print("| 1. Enkripsi              |")
        print("| 2. Dekripsi              |")
        print("| 3. Keluar                |")
        print("----------------------------")
        choice = input("Pilih opsi (1/2/3): ")

        if choice in ['1', '2']:
            operation = 'encrypt' if choice == '1' else 'decrypt'
            
            print("----------------------------")
            print("| Pilih Metode Input       |")
            print("| 1. Input Langsung        |")
            print("| 2. Baca dari File        |")
            print("| 3. Kembali               |")
            print("----------------------------")
            input_choice = input("Pilih opsi (1/2/3): ")

            if input_choice == '1':
                input_mode = 'input'
            elif input_choice == '2':
                input_mode = 'file'
            elif input_choice == '3':
                continue
            else:
                print("Opsi tidak valid, silakan coba lagi.\n")
                continue

            text = None
            while text is None:
                text = read_text(input_mode)
                if text is None and input_mode == 'file':
                    break

            if text is None:
                continue

            while True:
                try:
                    shift = int(input("Masukkan jumlah pergeseran (shift): "))
                    break
                except ValueError:
                    print("Harap masukkan angka valid untuk shift.")

            result_text = shift_cipher(text, shift, operation)

            if choice == '1':
                print(f"Teks terenkripsi: {result_text}\n")
            else:
                print(f"Teks terdekripsi: {result_text}\n")
                
            save_to_file(result_text)

        elif choice == '3':
            print("Terima kasih telah menggunakan Program!")
            break

        else:
            print("Opsi tidak valid, silakan coba lagi.\n")

# Memulai program
menu()
