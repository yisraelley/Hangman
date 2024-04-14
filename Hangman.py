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
letter = input("Guess a letter: ")
print(letter)
