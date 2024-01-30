import sys

 # Created a encryption function that takes two parameter (message, k)  
def encrypt(message, k):
  encrypted = "" # Then empty string stores the encrypted message.
  for char in message:
      if char.isalpha(): #The Isalpha built-in function takes alphabet letters.
          stay_in_alphabet = ord(char) + k
          if char.isupper(): # The isupper() and islower functions are booleans for upper case and lower case letters.
              if stay_in_alphabet > ord('Z'):
                  stay_in_alphabet -= 26
              elif stay_in_alphabet < ord('A'):
                  stay_in_alphabet += 26
          elif char.islower():
              if stay_in_alphabet > ord('z'):
                  stay_in_alphabet -= 26
              elif stay_in_alphabet < ord('a'):
                  stay_in_alphabet += 26
          final_letter = chr(stay_in_alphabet) # The final_letter is added to the encrypted string.
          encrypted += final_letter
      else:
          encrypted += char
  return encrypted
# Passing the encrypt function and adding the encrypt function so it can reverted to its original input.
def decrypt(message, k):
  return encrypt(message, -k)

if __name__ == "__main__":
  message = input("Enter your message: ")
  while True: # creating a while loop if the number(s) is true.
      try:
          key = int(input("Enter your key (an integer): "))
          break # we are going to break the loop if the user does not enter a number(key)
      except ValueError: #we are going to create an exception if the user does not enter a number it will prompt the user to input the correct format.
          print("That's not a valid integer. Please try again.")

  encrypted = encrypt(message, key)
  decrypted = decrypt(encrypted, key)

  print("Your encrypted word is", encrypted)
  print("Your decrypted word is", decrypted)