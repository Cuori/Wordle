from ast import While
import numpy as np
import random

possible_words = np.loadtxt("possible_word.txt",dtype="str")
word = random.choice(possible_words)


def splitting(word):
    return [char for char in word]

game = "on"
guess = ""
input_stat = True
word_ = splitting(word)
counter = 0

while(game == "on"):
    while (input_stat == True):
        guess = str(input("Type 5 letter word"))
        guess_ = splitting(guess)
        if guess in possible_words:
            input_stat = False
    res_1 = [0,0,0,0,0]
    for i in range(5):
        if word_.count(guess_[i]) >= 1:
            res_1[i] = "yellow"
            if word_[i] == guess_[i]:
                res_1[i] = "green"
        else:
            res_1[i] = "black"
    counter+= 1
    print(f"Round {counter}")
    print(guess_)
    print(res_1)
    if res_1.count("green") == 5:
        print("Congratz")
    guess = ""
    if (counter >= 6):
        game = "off"
        print(f"You lose the word is {word}")
    else:
        input_stat = True


    


