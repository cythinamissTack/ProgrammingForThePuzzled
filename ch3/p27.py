# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 19:03:46 2019

@author: hiroya
"""

"""カードデッキの作成"""
deck = []
for i in range(1, 14):
    club = str(i) + '_C'; dia  = str(i) + '_D' 
    heart = str(i) + '_H'; spade = str(i) + '_S'
    if i == 1:
        club = club.replace(str(i), 'A'); dia = dia.replace(str(i), 'A')
        heart = heart.replace(str(i), 'A'); spade = spade.replace(str(i), 'A')
    elif i == 11:
        club = club.replace(str(i), 'J'); dia = dia.replace(str(i), 'J')
        heart = heart.replace(str(i), 'J'); spade = spade.replace(str(i), 'J')
    elif i == 12:
        club = club.replace(str(i), 'Q'); dia = dia.replace(str(i), 'Q')
        heart = heart.replace(str(i), 'Q'); spade = spade.replace(str(i), 'Q')
    elif i == 13:
        club = club.replace(str(i), 'K'); dia = dia.replace(str(i), 'K')
        heart = heart.replace(str(i), 'K'); dia = dia.replace(str(i), 'K')
    
    deck.append(club); deck.append(dia); deck.append(heart); deck.append(spade)
    

"""助手の作業のコーディング"""
# 隠しておくカード、最初に示すカード、伝える数値の３つを返す関数 outputFirstCard 
def outputFirstCard(ns, oneTwo, cards):
    encode = (ns[oneTwo[0]] - ns[oneTwo[1]]) % 13
    if encode>0 and encode<=6:
        hidden = oneTwo[0]
        other = oneTwo[1]
    else:
        hidden = oneTwo[1]
        other = oneTwo[0]
        encode = (ns[oneTwo[1]] - ns[oneTwo[0]]) % 13
    print('First card is:', cards[other])
    return hidden, other, encode

# 引数リストindに格納された３枚のカードを引数codeの数を表すように順に並べる手順関数 outputNext3Cards
def outputNext3Cards(code, ind):
    if code == 1:
        s,t,f = ind[0],ind[1],ind[2]
    elif code == 2:
        s,t,f = ind[0],ind[2],ind[1]
    elif code == 3:
        s,t,f = ind[1],ind[0],ind[2]
    elif code == 4:
        s,t,f = ind[1],ind[2],ind[0]
    elif code == 5:
        s,t,f = ind[2],ind[0],ind[1]
    else:
        s,t,f = ind[2],ind[1],ind[0]
    
    print('Second card is:', deck[s])
    print('Third card is:', deck[t])
    print('Fourth card is:', deck[f])
    
# ソートの手順関数 sortList
def sortList(tlist):
    for ind in range(0, len(tlist)-1):
        iSm = ind
        for i in range(ind, len(tlist)):
            if tlist[iSm] > tlist[i]:
                iSm = i
            tlist[ind], tlist[iSm] = tlist[iSm], tlist[ind]
    
# 助手の作業をあらわす関数 AssistantOrderCards
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
