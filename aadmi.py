
# def game():
#     import random 
#     print("Winning Rules of the Rock paper scissor game as follows: \n"
#                                     +"Rock vs paper->paper wins \n"
#                                     + "Rock vs scissor->Rock wins \n"
#                                     +"paper vs scissor->scissor wins \n") 

#     while True: 
#         print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")  
#         choice = int(input("User turn: ")) 
#         while choice > 3 or choice < 1: 
#             choice = int(input("enter valid input: ")) 
#         if choice == 1: 
#             choice_name = 'Rock'
#         elif choice == 2: 
#             choice_name = 'paper'
#         else: 
#             choice_name = 'scissor'
#         print("user choice is: " + choice_name) 
#         print("\nNow its computer turn.......")
#         comp_choice = random.randint(1, 3)  
#         while comp_choice == choice: 
#             comp_choice = random.randint(1, 3) 
#         if comp_choice == 1: 
#             comp_choice_name = 'Rock'
#         elif comp_choice == 2: 
#             comp_choice_name = 'paper'
#         else: 
#             comp_choice_name = 'scissor'	
#         print("Computer choice is: " + comp_choice_name) 
#         print(choice_name + " V/s " + comp_choice_name)
#         if((choice == 1 and comp_choice == 2) or
#         (choice == 2 and comp_choice ==1 )): 
#             print("paper wins => ", end = "") 
#             result = "paper"	
#         elif((choice == 1 and comp_choice == 3) or
#             (choice == 3 and comp_choice == 1)): 
#             print("Rock wins =>", end = "") 
#             result = "Rock"
#         else: 
#             print("scissor wins =>", end = "") 
#             result = "scissor"
#         if result == choice_name: 
#             print("<== User wins ==>") 
#         else: 
#             print("<== Computer wins ==>") 
#         print("Do you want to play again? (Y/N)") 
#         ans = input() 
#         if ans == 'n' or ans == 'N': 
#             break
#     print("\nThanks for playing")
# game() 

# ===================================
# cipher 0.1
# ====================================
# def find_in_list(query, mainlist):
#     mainlist_len = len(query)
#     range_for_loop = range(mainlist_len)
#     index = None
#     for i in range_for_loop:
#         element = mainlist[i]
#         if element == query:
#             index = i
#     return i
# chars =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']
# def encrypt_message(plain_msg):
#     encrypted_msg = ""
#     for character in encrypted_msg:
#         if character in chars:
#             char_index = find_in_list(character, chars)
#             new_char = shifted_chars[char_index]
#             encrypted_msg = encrypted_msg + new_char
#         else:
#             encrypted_msg = encrypted_msg + character
# def decrypt_message(encrypted_msg):
#     decrypted_msg = ""
#     for character in decrypted_msg:
#         if character in shifted_chars:
#             char_index = find_in_list(character, shifted_chars)
#             new_char = chars[char_index]
#             decrypted_msg = decrypted_msg + new_char
#         else:
#             decrypted_msg = decrypted_msg + character
# #######################code start##############################
# flag = True
# while flag == True:
#     choice = input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter `e` or `d` respectively!")
#     if choice == 'e':
#         plain_message = input("Enter message to encrypt??")
#         encrypt_message(plain_message)
#     elif choice == "d":
#         encrypted_msg = input("Enter message to decrypt?")
#         decrypt_message(encrypted_msg)
#     else:
#         play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
#         if play_again == 'Y':
#             continue
#         elif play_again == 'N' and play_again == "n":
#             break
#         break
  




# import random
# NUMDIGITS = 3
# MAXGUESS = 10

# def getSecretNum(numDigits):
#     numbers = list(range(10))
#     random.shuffle(numbers)
#     secretNum = ''
#     for i in range(numDigits):
#         secretNum += str(numbers[i])
#     return secretNum

# def getClues(guess, secretNum):
#   if guess == secretNum:
#     return 'You got it!'
#   clue = []
#   for i in range(len(guess)):
#     if guess[i] == secretNum[i]:
#       clue.append('Fermi')
#     elif guess[i] in secretNum:
#       clue.append('Pico')
#   if len(clue) == 0:
#       return 'None'
#   return ' '.join(clue)

# def isOnlyDigits(num):
#   if num == '':
#     return False

#   for i in num:
#     if i not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
#       return False
#   return True

# def playAgain():
#   play = input("Do you want to play again? Yes or No?") 
#   if play == "yes" or play == 'y':
#     return True
#   else:
#     return False



# print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUMDIGITS))
# print('Here are some clues:')
# print('When I say:    That means:')
# print('  Pico         One digit is correct but in the wrong position.')
# print('  Fermi        One digit is correct and in the right position.')
# print('  None       No digit is correct.')

# while True:
#   secretNum = getSecretNum(NUMDIGITS)
#   print('I have thought up a number. You have %s guesses to get it.' % (MAXGUESS))
#   numGuesses = 1
#   while numGuesses <= MAXGUESS:
#     guess=''
#     while len(guess) != NUMDIGITS or not isOnlyDigits(guess):
#       print ('Guess' + str(numGuesses))
#       guess = input("Guess Again")

#     clue = getClues(guess, secretNum)
#     print(clue)
#     numGuesses += 1
#     if guess == secretNum:
#       break
#     if numGuesses > MAXGUESS:
#       print ('You ran out of guesses. The answer was ' + secretNum)
#     if not playAgain:
#       break  
#   user = input("enter your   ")
#   if user == "n":
#     break

 


# def split(string, delimiters=' \t\n'):
#     result = []
#     word = ''
#     for c in string:
#         if c not in delimiters:
#             word += c
#         elif word:
#             result.append(word)
#             word = ''
#     if word:
#         result.append(word)
#     return result

values = 'This is a sentence'
split_values = []
tmp = ''
for words in values:
    if words == ' ':
        split_values.append(tmp)
    tmp = "soniya"
else:
    tmp += words
if tmp:
    split_values.append(tmp)
    print(split_values)