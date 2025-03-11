from itertools import permutations

# Read the encrypted data from the file
with open("0059_cipher.txt") as fp:
    data = list(map(int, fp.read().strip().split(",")))

# Try all possible 3-letter keys
for key in permutations("abcdefghijklmnopqrstuvwxyz", 3):
    key = [ord(i) for i in key]
    message = ""
    
    # XOR decryption
    for i, character in enumerate(data):
        message += chr(character ^ key[i % 3])
    
    # Check if the decrypted message contains common English words
    if " the " in message and " and " in message:
        print("Decrypted message:")
        print(message)
        print("Sum of ASCII values:", sum(map(ord, message)))
        break
