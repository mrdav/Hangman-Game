import random
import string
import os
global letters, won, lost, played
engalphabet = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']
letters = []
won = 0
lost = 0
played = 0
lowerabc = string.ascii_lowercase
upperabc = string.ascii_uppercase
for letter in lowerabc:
    letters.append(letter)
for letter in upperabc:
    letters.append(letter)
letters = letters + engalphabet
def start():
    global played
    played += 1
    with open('words.txt', 'r') as f:
        words = f.readlines()
        words = [x.strip() for x in words]
    if len(words) == 0:
        print("There are no words in the words.txt file!")
        os.system('pause')
        quit()
    pickWord(words)
def pickWord(wordlist):
    word = random.choice(wordlist)
    wordletters = []
    for letter in word:
        wordletters.append(letter)
    ask(word, wordletters)
def ask(word, wordletters):
    global won,lost,played
    wordskl = wordletters[:]
    wordskel = []
    for i in range(0,len(wordletters)):
        wordskel.append("_")
    print("I chose a word that consists of {} letters, try to find it. You have 6 tries!".format(len(word)))
    tries = 0
    inp = ''
    while tries <= 6:
        tries += 1
        if inp == word or len(wordletters) == 0:
            print()
            print("You found the word with {} failed tries! Congratulations!!!".format((tries - 1)))
            won += 1
            break
        if tries > 6:
            print("Your tries are over, the word was {}".format(word))
            lost += 1
            break
        inp = input("Type a letter: ")
        if inp == word or len(wordletters) == 0:
            print()
            print("You found the word with {} failed tries! Congratulations!!!".format((tries - 1)))
            won += 1
            break
        if inp not in letters:
            print("The letter is not accepted, try again")
        if inp not in wordletters:
            print("The letter you entered does not exist in the word , try again!")
        if inp in wordletters:
            if inp == word or len(wordletters) == 0:
                print()
                print("You found the word with {} failed tries! Congratulations!!!".format((tries - 1)))
                won += 1
                break
            print("The letter you entered exists in the word, nice, continue!")
            fnd = wordskl.count(inp)
            for i in range(0, fnd):
                indx = wordskl.index(inp)
                wordskel[indx] = inp
                wordskl[indx] = ''
                wordletters.remove(inp)
                wordsk = "".join(wordskel)
            print(wordsk)
            tries -= 1

    replay()
def replay():
    yess = ("Yes", "yes", "y", "Y", "YES")
    choices = ("Yes", "yes", "y", "Y", "YES", "No", "n", "N", "NO")
    print()
    rpl = input("Would you like to play again? [Y(Yes)/N(No)]: ")
    while rpl not in choices :
        print("Wrong answer!")
        rpl = input("Would you like to play again? [Y(Yes)/N(No)]: ")
    if rpl in yess:
        os.system('cls')
        start()
    else:
        print()
        print("Statistics:")
        if played == 1:
            print("You played 1 game")
            print("You won {} game".format(won))
            print("You lost {} game".format(lost))
        else:
            print("You played {} games".format(played))
            print("You won {} games".format(won))
            print("You lost {} games".format(lost))
    os.system('pause')
    quit()
print("Hangman Game! Guess the word i thought of!")
start()
