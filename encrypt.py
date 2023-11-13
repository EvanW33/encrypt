from cryptography.fernet import Fernet
import hashlib


def get_file(filename):
  # This function gets the file name of what will be encrypted/decrypted
  pass

def get_password(new_password=False):
  # This function asks for the password and returns the SHA-256 key
  if new_password:
    # First time running, this is the encrypting phase
    pass
  else:
    # This is decrypting phase
    key = hashlib.sha256(input("Enter password:\n").encode('utf-8')).hexdigest()
  return key


def encrypt():
  pass


def decrypt():
  pass


def main():
  while True:
    # Gets input until encrypt or decrypt is input
    option = input("What would you like to do; encrypt or decrypt a file?\nEnter \"Encrypt\" or \"Decrypt\"\n")
    if(option.lower() == "encrypt" or option.lower() == "decrypt"):
      break

  # Determines what to do next
  if(option.lower() == "encrypt"):
    encrypt()
  elif(option.lower() == "decrypt"):
    decrypt()
  else:
    raise Exception("Unauthorized text")
  key = get_password()
  print(key)
    

if __name__ == "__main__":
  main()
