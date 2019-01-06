# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 19:03:46 2019

@author: hiroya
"""

deck = []
for i in range(1, 14):
    club = str(i) + '_C'; dia  = str(i) + '_D' 
    heart = str(i) + '_H'; spade = str(i) + '_S'
    if i == 1:
        club.replace(str(i), 'A'); dia.replace(str(i), 'A')
        heart.replace(str(i), 'A'); spade.replace(str(i), 'A')
    elif i == 11:
        club.replace(str(i), 'J'); dia.replace(str(i), 'J')
        heart.replace(str(i), 'J'); spade.replace(str(i), 'J')
    elif i == 12:
        club.replace(str(i), 'Q'); dia.replace(str(i), 'Q')
        heart.replace(str(i), 'Q'); spade.replace(str(i), 'Q')
    elif i == 13:
        club.replace(str(i), 'K'); dia.replace(str(i), 'K')
        heart.replace(str(i), 'K'); dia.replace(str(i), 'K')
    
    deck.append(club); deck.append(dia); deck.append(heart); deck.append(spade)
    
def AssistantOrderCards():
    print('Cards are character strings as shown below.')
    print('Ordering is:', deck)
    cards, cind, cardsuits, cnumbers = [], [], [], []
    numsuits = [0, 0, 0, 0]
    for i in range(5):
        print('Please give card', i+1, end = ' ')
        card = input('in above format:')
        cards.append(card)
        n = deck.index(card)
        cardsuits.append(n % 4)
        cnumbers.append(n // 4)
        numsuits[n % 4] += 1
        if numsuits[n % 4] > 1:
            pairsuit = n % 4
        cardh = []
        for i in range(5):
            if cardsuits[i] == pairsuit:
                cardh.append(i)
        hidden, other, encode = \
            outputFirstCard(cnumbers, cardh, cards)
        remindices = []
        for i in range(5):
            if i != hidden and i != other: 
                remindices.append(cind[i])
        sortList(remindices)
        outputNext3Cards(encode, remindices)
        return
    