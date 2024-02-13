import string
import random


lower_char = list(string.ascii_lowercase)
upper_char = list(string.ascii_uppercase)
digits = list(string.digits)
special_char = list(string.punctuation)
char_num = input("Enter the number of characters: ")

while True:
    try:
        char_num = int(char_num)
        if char_num < 6 :
            print("The number of characters must be more than 6 : ")
            char_num = input("Enter the number of characters again ")
        else:
            break
    except:
        print("enter numbers only")
        char_num = input("Enter the number of characters again ")
        
random.shuffle(lower_char)
random.shuffle(upper_char)
random.shuffle(digits)
random.shuffle(special_char)

part1 = round(char_num*0.3) 
part2 = round(char_num*0.2)
password = []
for i in range (part1):
    password.append(lower_char[i])
    password.append(upper_char[i])

for i in range (part2):
    password.append(digits[i])
    password.append(special_char[i])

random.shuffle(password)
password = "".join(password)
print("------------------------")
print("Your password is: "+ password)
print("------------------------")