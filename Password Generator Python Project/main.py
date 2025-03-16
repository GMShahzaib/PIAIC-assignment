import random

def generate_password(length=8):
  characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
  password = ''.join(random.choice(characters) for i in range(length))
  return password

# Example usage
password = generate_password()
print("Generated password:", password)
password = generate_password(length=12)
print("Generated password of length 12:", password)