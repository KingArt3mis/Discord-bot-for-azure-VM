import random

def randomWord(lista):
    words = open(lista, 'r', encoding='UTF-8').readlines()
    return random.choice(words)