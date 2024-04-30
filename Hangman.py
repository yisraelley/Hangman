HANGMAN_ASCII_ART = '''
Welcome to the game Hangman
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \\ / _' | '_ ' _ \\ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                        __/ |
                       |___/
'''
MAX_TRIES = 6
print(HANGMAN_ASCII_ART, MAX_TRIES)

picture_1 = '''
    x-------x
'''
picture_2 = '''
    x-------x
    |
    |
    |
    |
    |
'''
picture_3 = '''
    x-------x
    |       |
    |       0
    |
    |
    |
'''
picture_4 = '''
    x-------x
    |       |
    |       0
    |       |
    |
    |
'''
picture_5 = '''
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
'''
picture_6 = '''
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
'''
picture_7 = '''
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
'''


# word = input("Please enter a word: ")
# word_box = "_" + " _" * (len(word) - 1)
# print(word_box)


# def all_in(st):
#     low_letters = "abcdefghijklmnopqrstuvwxyz"
#     up_letters = low_letters.upper()
#     all_letters = low_letters + up_letters
#     for i in range(len(st)):
#         if st[i] not in all_letters:
#             return False
#     return True


# letter_guessed = input("Guess a letter: ")
#
# if all_in(letter_guessed):
#     if len(letter_guessed) > 1:
#         print("E1")
#     else:
#         print(letter_guessed.lower())
# else:
#     if len(letter_guessed) > 1:
#         print("E3")
#     else:
#         print("E2")


# def is_valid_input(letter_guessed):
#     if len(letter_guessed) > 1 or not all_in(letter_guessed):
#         return False
#     return True
#
#
# print(is_valid_input("a"))
# print(is_valid_input("A"))
# print(is_valid_input("$"))
# print(is_valid_input("ab"))
# print(is_valid_input("app$"))


def check_valid_input(letter_guessed, old_letters_guessed):
    if len(letter_guessed) > 1 or letter_guessed in old_letters_guessed:
        return False
    if ord('a') <= ord(letter_guessed) <= ord('z') and letter_guessed.upper() not in old_letters_guessed:
        return True
    if ord('A') <= ord(letter_guessed) <= ord('Z') and letter_guessed.lower() not in old_letters_guessed:
        return True
    return False


def old_letters_guessed_viewer(old_letters_guessed):
    for i in range(len(old_letters_guessed)):
        if i == len(old_letters_guessed) - 1:
            print(old_letters_guessed[i])
            break
        print(old_letters_guessed[i], end=" -> ")


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        if ord('A') <= ord(letter_guessed) <= ord('Z'):
            letter_guessed = letter_guessed.lower()
        old_letters_guessed.append(letter_guessed)
        return True
    print("X")
    old_letters_guessed_viewer(sorted(old_letters_guessed))
    return False


old_letters = ['a', 'p', 'c', 'f']
print(try_update_letter_guessed('A', old_letters))
# X
# a -> c -> f -> p
# False
print(try_update_letter_guessed('s', old_letters))
# True
print(old_letters)
# ['a', 'p', 'c', 'f', 's']
print(try_update_letter_guessed('$', old_letters))
# X
# a -> c -> f -> p -> s
# False
print(try_update_letter_guessed('d', old_letters))
# True
print(old_letters)
# ['a', 'p', 'c', 'f', ‘s’, 'd']
