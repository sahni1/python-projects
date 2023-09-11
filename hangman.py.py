import random
from collections import Counter

somewords ='''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach lychee muskmelon'''

somewords = somewords.split(' ')

word =random.choice(somewords)

if __name__ == '__main__':
    print('guess the word hint: it ia a fruit')

    for i in word:
        print('_',end=' ')
    print()

    playing =True

    letterguessed=''
    chances =len(word) + 2
    correct = 0
    flag= 0
    try:
        while (chances != 0) and flag == 0:
            print()
            chances -=1

            try:
                guess = str(input('Enter a letter to guess:'))
            except:
                    print("enter only a letter")
                    continue

            if not guess.isalpha():
                print('Enter only a letter')
                continue
            elif len(guess) > 1:
                print('enter a single letter')
                continue
            elif guess in letterguessed:
                print('You have aready guesses it')
                continue

            if guess in word:
                k=word.count(guess)
                for _ in range(k):
                    letterguessed +=guess

            for char in word:
                if char in letterguessed and (Counter(letterguessed) !=Counter(word)):
                    print(char,end=' ')
                    correct +=1
                elif(Counter(letterguessed)== Counter(word)):
                    print('The word is ', end= ' ')
                    print(word)
                    flag =1
                    print('congo')
                    break
                else:
                    print('_',end=' ')
            if chances <=0 and (Counter(letterguessed)!=Counter(word)):
                print()
                print('you lost')
                print('thwe word was {}'.format(word))

    except keyboardInterrupt:
                print()
                print('bye')
                exit



