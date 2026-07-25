import random
import string

print("=== CEO PASSWORD GENERATOR v1.0 ===")
print("Bank-level security. Hackers can't crack this.\n")

length = int(input("How long should the password be? 12-16 recommended: "))

characters = string.ascii_letters + string.digits + "!@#$%^&*()"

password = ''.join(random.choice(characters) for i in range(length))

print("\n--- YOUR STRONG PASSWORD ---")
print(password)
print("----------------------------")
print("Copy this and save it safely CEO!")
print("Never use '123456' again.")
