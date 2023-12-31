import hashlib
import os
from cryptography.fernet import Fernet


def get_file(filename):
  # This function gets the file name of what will be encrypted/decrypted
  pass


def get_key():
  # Reads and returns the key from crypto.key
  with open("crypto.key", "rb") as file:
    key = file.read()
    return key


def key_generation():
  # Creates the private key
  key = Fernet.generate_key()

  with open("crypto.key", "wb") as k:
    k.write(key)


def print_prompts(prompt):
  # Used to print prompts that are needed for input
  if prompt == 1: # Gets input for what action (encrypt or decrypt) is going to be performed
    while True:
      # Gets input until encrypt, e, decrypt, or d is entered
      option = input("What would you like to do; Encrypt(E) or Decrypt(D)?\n")
      if(option.lower() == "encrypt" or option.lower() == "decrypt" or option.lower() == "d" or option.lower() == "e"):
        return option
    
  if prompt == 2: # Gets input for the filename that will be encrypted or decrypted
    while True:
      filename = input("Please enter the file and file extension:\n")
      if os.path.exists(filename):
        print("The file exists!")
        return filename
      else:
        print("Invalid file name!")



def encrypt(key):
  # Encrypts the file using the key
  f = Fernet(key)


def decrypt(key):
  # Decrypts the file using the key
  pass


def main():
  # Gets the key that will be used to encrypt/decrypt the file
  if not os.path.exists("crypto.key"):
    print("Created new crypto.key file")
    key_generation()
  key = get_key()
  print("Key: {}".format(key))

  # Gets what will be done
  option = print_prompts(1)  

  # Determines what to do next
  if(option.lower() == "encrypt" or option.lower() == "e"):
    encrypt(key)
  elif(option.lower() == "decrypt" or option.lower() == "d"):
    decrypt(key)
  else:
    raise Exception("Unauthorized text")
  
  # Gets the file to be encrypted/decrypted
  filename = print_prompts(2)


if __name__ == "__main__":
  main()