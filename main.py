import numpy as np
import random

possible_words = np.loadtxt("possible_word.txt",dtype="str")
word = random.choice(possible_words)
test_word = "clone"

def splitting(word):
    return [char for char in word]

test_list = splitting("clone")
guess_1 = splitting("crane")
res_1 = [0,0,0,0,0]
for i in range(5):
    if test_list.count(guess_1[i]) >= 1:
        res_1[i] = "yellow"
        if test_list[i] == guess_1[i]:
            res_1[i] = "green"
    else:
        res_1[i] = "black" 

print(guess_1)
print(res_1)

