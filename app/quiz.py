import random

def generate_random_alphabet():
    return chr(random.randint(65, 90))  # 65 is the ASCII value of 'A', 90 is the ASCII value of 'Z'

def generate_options(correct_answer):
    options = [correct_answer]
    while len(options) < 4:
        option = chr(random.randint(65, 90))
        if option not in options:
            options.append(option)
    random.shuffle(options)
    return options

def play_game():
    correct_answer = generate_random_alphabet()
    options = generate_options(correct_answer)
    return correct_answer,options
