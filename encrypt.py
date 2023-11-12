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
  key = get_password()
  print(key)
    

if __name__ == "__main__":
  main()
