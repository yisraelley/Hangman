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


def all_in(st):
    low_letters = "abcdefghijklmnopqrstuvwxyz"
    up_letters = low_letters.upper()
    all_letters = low_letters + up_letters
    for i in range(len(st)):
        if st[i] not in all_letters:
            return False
    return True


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


def is_valid_input(letter_guessed):
    if len(letter_guessed) > 1 or not all_in(letter_guessed):
        return False
    return True


print(is_valid_input("a"))
print(is_valid_input("A"))
print(is_valid_input("$"))
print(is_valid_input("ab"))
print(is_valid_input("app$"))
