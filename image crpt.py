from cryptography.fernet import Fernet
from tkinter import *
from tkinter import filedialog
from functools import partial

global filename
button_height = 2
button_width = 25

def browseFiles():
    try:
        browseFiles.filename = filedialog.askopenfilename(initialdir="/", title="Select a File",)
        if browseFiles.filename:
            label_file_explorer.configure(text="File Opened: " + browseFiles.filename)

            pass_label.pack()
            password.pack()
            temp_label.pack()
            button_encrypt.pack()
            button_decrypt.pack()
    except Exception as e:
        status_label.configure(text="Error: " + str(e))
        status_label.pack()

def encrypt_file(p_word):
    try:
        temp_key = p_word.get()
        temp_key = ''.join(e for e in temp_key if e.isalnum())
        key = temp_key + ("s" * (43 - len(temp_key)) + "=")

        fernet = Fernet(key)

        with open(browseFiles.filename, 'rb') as file:
            original = file.read()
        encrypted = fernet.encrypt(original)

        with open(browseFiles.filename, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

        status_label.configure(text="Encrypted")
        status_label.pack()
    except Exception as e:
        status_label.configure(text="Error: " + str(e))
        status_label.pack()

def decrypt_file(p_word):
    try:
        temp_key = p_word.get()
        temp_key = ''.join(e for e in temp_key if e.isalnum())
        key = temp_key + ("s" * (43 - len(temp_key)) + "=")

        fernet = Fernet(key)

        with open(browseFiles.filename, 'rb') as enc_file:
            encrypted = enc_file.read()
        decrypted = fernet.decrypt(encrypted)

        with open(browseFiles.filename, 'wb') as dec_file:
            dec_file.write(decrypted)

        status_label.configure(text="Decrypted")
        status_label.pack()
    except Exception as e:
        status_label.configure(text="Error: " + str(e))
        status_label.pack()

window = Tk()

window.title('File Explorer')
window.geometry("940x740")
window.config(background="black")

main_title = Label(window, text="File Encryptor and Decryptor", width=100, height=2, fg="white", bg="black", font=("", 30))
passwd = StringVar()

submit_para_en = partial(encrypt_file, passwd)
submit_para_de = partial(decrypt_file, passwd)

label_file_explorer = Label(window, text="File Name : ", width=100, height=2, fg="white", bg="black", font=("", 20))
pass_label = Label(window, text="Password for encryption/decryption : ", width=100, height=2, fg="white", bg="black", font=("", 20))
temp_label = Label(window, text="", height=3, bg="black")

button_explore = Button(window, text="Browse File", command=browseFiles, width=button_width, height=button_height, font=("", 15))

password = Entry(window, textvariable=passwd, show="*")

button_encrypt = Button(window, text="Encrypt", command=submit_para_en, width=button_width, height=button_height, font=("", 15))
button_decrypt = Button(window, text="Decrypt", command=submit_para_de, width=button_width, height=button_height, font=("", 15))

status_label = Label(window, text="", width=100, height=4, fg="white", bg="black", font=("", 17))

main_title.pack()
label_file_explorer.pack()
button_explore.pack()
pass_label.pack()
password.pack()
temp_label.pack()
button_encrypt.pack()
button_decrypt.pack()
status_label.pack()

window.mainloop()