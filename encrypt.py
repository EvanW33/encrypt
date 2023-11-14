import hashlib
import os


def get_file(filename):
  # This function gets the file name of what will be encrypted/decrypted
  pass

def private_key_generation(new_password=False):
  # This function asks for the password and private key generated using PBKDF2 and a salt
  return hashlib.sha256(input("Enter password:\n").encode('utf-8')).hexdigest()


def encrypt(key):
  # Encrypts the file using the inputted key
  pass


def decrypt(key):
  pass


def main():
  while True:
    # Gets input until encrypt or decrypt is input
    option = input("What would you like to do; encrypt or decrypt a file?\nEnter \"Encrypt\" or \"Decrypt\"\n")
    if(option.lower() == "encrypt" or option.lower() == "decrypt"):
      break

  # Gets the key that will be used to encrypt/decrypt the file
  key = private_key_generation()

  # Determines what to do next
  if(option.lower() == "encrypt"):
    encrypt(key)
  elif(option.lower() == "decrypt"):
    decrypt(key)
  else:
    raise Exception("Unauthorized text")

  
    

if __name__ == "__main__":
  main()
