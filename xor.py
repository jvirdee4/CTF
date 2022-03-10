key = 'F'
location = "Kinsey Pavilion 1200B"

#ascii representation of key and location
key_a = bin(ord(key))[2:].zfill(8)
#print(key_a)

location_a = []

for c in location:
    location_a.append(bin(ord(c))[2:].zfill(8))



#XOR each character

encrypted_format = []

for l in location_a:
    encrypted_format.append(bin(int(key_a, 2) ^ int(l, 2))[2:].zfill(8))

#print(encrypted_format)

encrypted_location = ''

for x in encrypted_format:
    encrypted_location += x

#print(encrypted_location)

#decrpytion

decrypted_c = ""
for y in encrypted_format:
    decrypted_c += (chr((int(key_a, 2) ^ int(y, 2))))


#print(decrypted_c)

#game portion
print("You are given a key and it is your task to decrypt a secret message that was encrypted using XOR encryption. Once you crack the code, you will know the location of the classroom!")
print("The key is: "  + key)
print("The ciphertext is: " + encrypted_location)
print()
print("Your task is to split up the cipher text into eigths in order to isolate each encrypted character. Next, you will be able to decrypt each code with the key (in its corresponding ASCII code) and then be able to map each code to a character using an ASCII lookup table.")
print("Use this for reference: https://upload.wikimedia.org/wikipedia/commons/1/1b/ASCII-Table-wide.svg")
print()



while True:
    answer = input("Input answer here: ")
    if answer == location:
        print("Congrats, you have found the location, on to the next task!")
        break
    else:
        print("Incorrect, try again!")
