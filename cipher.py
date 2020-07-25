def find_in_list(query, mainlist):
    mainlist_len = len(query)
    range_for_loop = range(mainlist_len)
    for i in range_for_loop:
        element = mainlist[i]
        if element == query:
            i += i
    return i
chars =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']
def encrypt_message(plain_message):
    encrypted_msg = ""
    for character in encrypted_msg:
        if character in chars:
            char_index = find_in_list(character, chars)
            new_char = shifted_chars[char_index]
            encrypted_msg = encrypted_msg + new_char
        else:
            encrypted_msg = encrypted_msg + char_index
        
def decrypt_message(encrypted_msg):
    decrypted_msg = ""
    for character in decrypted_msg:
        if character in shifted_chars:
            char_index = find_in_list(character, shifted_chars)
            new_char = chars[char_index]
            decrypted_msg = decrypted_msg + new_char
        else:
            decrypted_msg = decrypted_msg + char_index
############################################### Code starts from here ##################################################
flag = True
while flag==True:
    choice = input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter `e` or `d` respectively!")
    if choice == 'e':
        plain_message = input("Enter message to encrypt??")
        (encrypt_message(plain_message))
    elif choice == 'd':
        encrypted_msg = input("Enter message to decrypt?")
        (decrypt_message(encrypted_msg))
    else:
        play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
        if play_again == 'Y':
            continue
        elif play_again == 'N':
            break

# ========================cipher 2.0=======================
# def encrypt():
#   message = input("Enter the message you want to encrypt   ")
#   ascii_message = [ord(char)+3 for char in message]
#   encrypt_message = [ chr(char) for char in ascii_message]  
#   print (''.join(encrypt_message))


# def decrypt():
#   message = input("Enter the message you want to decrypt  ")
#   ascii_message = [ord(char) for char in message]
#   decrypt_message = [ chr(char) for char in ascii_message]  
#   print (''.join(decrypt_message))

# flag = True
# while flag:
#     choice = input("What do you want to do? \n1. Encrypt a message 2. Decrypt a message \nEnter E or D respectively!   ")
#     if choice == 'e':
#         encrypt()
#     elif choice == 'd':
#         decrypt()    
#     else:
#         play_again = input("Do you want to try agian or Do you want to exit? (Y/N)  ")
#         if play_again == 'Y':
#             continue
#         elif play_again == 'N':
#             break











def find_in_list(query, mainlist):
    mainlist_len = len(query)
    range_for_loop = range(mainlist_len)
    index = None
    for i in range_for_loop:
        element = mainlist[i]
        if element == query:
            index = i
    return i
chars =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']
def encrypt_message(plain_msg):
    encrypted_msg = ""
    for character in encrypted_msg:
        if character in chars:
            char_index = find_in_list(character, chars)
            new_char = shifted_chars[char_index]
            encrypted_msg = encrypted_msg + new_char
        else:
            encrypted_msg = encrypted_msg + character
def decrypt_message(encrypted_msg):
    decrypted_msg = ""
    for character in decrypted_msg:
        if character in shifted_chars:
            char_index = find_in_list(character, shifted_chars)
            new_char = chars[char_index]
            decrypted_msg = decrypted_msg + new_char
        else:
            decrypted_msg = decrypted_msg + character
#######################code start##############################
flag = True
while flag == True:
    choice = input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter `e` or `d` respectively!")
    if choice == 'e':
        plain_message = input("Enter message to encrypt??")
        encrypt_message(plain_message)
    elif choice == "d":
        encrypted_msg = input("Enter message to decrypt?")
        decrypt_message(encrypted_msg)
    else:
        play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
        if play_again == 'Y':
            continue
        elif play_again == 'N' and play_again == "n":
            break
        break
  
