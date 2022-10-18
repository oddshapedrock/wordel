import sys
import string
import time
import turtle as tur
from random import sample

y_loc = 125
y_val = 125
x_loc = 0
word_list = []
mega_word_list = []
word = ""
attempt = 0

def main():
    global word
    global mega_word_list
    #create a list of all 5 letter words as contained in words.txt
    mega_word_list = []
    with open("word_list.txt", "r") as file:
        file = file.readline().split()
        for wor in file:
            mega_word_list.append(wor)
    #chose 1 random word from list
    word = sample(mega_word_list, 1)[0]

    set_up_screen()

    #gives player 6 attemps to guess correct
    y_val = 125
    set_keys()
    tur.mainloop()

def write(key):
    tur.onkeypress(None, "Return")
    tur.onkeypress(None, "BackSpace")
    for key2 in string.ascii_letters:
        tur.onkeypress(lambda key2=key2: None, key2)
    key = key.upper()
    global x_loc
    global y_loc
    global word_list
    if len(word_list) < 5:
        tur.penup()
        tur.goto(x_loc * 50 - 100, y_loc)
        tur.write(key, align="center", font=("arial", 32, "normal"))
        tur.pendown()
        x_loc += 1
        word_list.append(key)
    set_keys()

def enter():
    tur.onkeypress(None, "BackSpace")
    tur.onkeypress(None, "Return")
    for key2 in string.ascii_letters:
        tur.onkeypress(lambda key2=key2: None, key2)
    global word_list
    global word
    global attempt
    global x_loc
    global y_val
    global y_loc
    if attempt < 5:
        guess = "".join(word_list)
        if guess in mega_word_list:
            line = check_guess(word, guess)
            draw_word(line, y_val)
            if word == guess:
                end_game(True, word)
            y_loc -= 50
            y_val -= 50
            attempt += 1
            x_loc = 0
            word_list = []
        set_keys()
        if guess == word:
            end_game(True, word)
    else:
        end_game(False, word)

def erase():
    tur.onkeypress(None, "Return")
    tur.onkeypress(None, "BackSpace")
    for key2 in string.ascii_letters:
        tur.onkeypress(lambda key2=key2: None, key2)
    global x_loc
    global y_loc
    global word_list
    if len(word_list) > 0:
        del word_list[-1]
        tur.penup()
        tur.goto(x_loc * 50 -175, y_loc + 50)
        tur.pendown()
        tur.color("BLACK", "WHITE")
        tur.begin_fill()
        draw_box()
        tur.end_fill()
        x_loc -= 1
    set_keys()

def set_keys():
    for key in string.ascii_letters:
        tur.onkeypress(lambda key=key: write(key), key)
    tur.onkeypress(erase, "BackSpace")
    tur.onkeypress(enter, "Return")
    tur.listen()

def end_game(win, word):
    global word_list
    global y_loc
    global y_val
    global x_loc
    global attempt
    tur.penup()
    for index, letter in enumerate(word):
        tur.goto(index * 50 - 100, -175)
        tur.write(letter, align="center", font=("arial", 32, "normal"))
    if win:
        print("You got it!")
    else:
        print("Sorry you did not guess it.")
    cont = tur.textinput("Text Box", "Do you want to play again?")
    if cont == "n":
        sys.exit(0)
    else:
        y_loc = 125
        y_val = 125
        x_loc = 0
        attempt = 0
        word_list = []
        main()

def check_guess(word, guess):
    word = [*word]
    guess = [*guess]
    origional = [*guess]
    colors = []
    
    for index, letter in enumerate(guess):
        #possible error remove duplicate values
        indecies1 = [idx for idx, value in enumerate(guess) if value == letter]
        indecies2 = [idx for idx, value in enumerate(word) if value == letter]
        if not indecies1 <= indecies2:
            amount = len(indecies2)
            for indecie in indecies1:
                if amount <= 0:
                    guess[indecie] = "-"
                amount -= 1
        
        print(guess)
        
        if letter is word[index]:
            colors.append("GREEN")
        elif letter in word and guess.count(letter) <= word.count(letter):
            colors.append("YELLOW")
        else:
            colors.append("WHITE")
    return [origional, colors]

def draw_word(line, y_val):
    for index, letter in enumerate(line[0]):
        tur.penup()
        tur.goto(index * 50 - 125, y_val + 50)
        tur.pendown()
        tur.color("BLACK", line[1][index])
        tur.begin_fill()
        draw_box()
        tur.end_fill()
        tur.penup()
        #write letter
        tur.goto(index * 50 -100, y_val)
        tur.write(letter, align="center", font=("arial", 32, "normal"))

def draw_box():
    for _ in range(4):
        tur.forward(50)
        tur.right(90)

def set_up_screen():
    tur.setup(500, 500)
    tur.clear()
    tur.speed(0)
    tur.delay(0)
    tur.ht()
    tur.color("BLACK", "BLUE")
    for y in range(7):
        for x in range(5):
            if not y:
                tur.begin_fill()
            tur.penup()
            tur.goto(x * 50 - 125, y * 50 - 125)
            tur.pendown()
            draw_box()
            if not y:
                tur.end_fill()
    tur.penup()
    tur.goto(0, 175)
    tur.pendown()
    tur.write("WORDEL", align="center", font=("arial", 32, "normal"))

main()
