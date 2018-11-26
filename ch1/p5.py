# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 16:06:53 2018

@author: hiroya
"""

# 入力リスト
cap1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']
cap3 = []

def pleaseConform(caps):
    # 変数の初期化
    start = forward = backward = 0
    intervals = []
    for i in range(1, len(caps)):
        # これがTrueなら、区間がひとつ終わる
        if caps[start] != caps[i]:
            intervals.append((start, i-1, caps[start]))
            if caps[start] == 'F':
                forward += 1
            else:
                backward += 1
            start = i
            
    # 最後の区間をループの外で追加
    intervals.append((start, len(caps)-1, caps[start]))
    if caps[start] == 'F':
        forward += 1
    else:
        backward += 1
        
    # どちらの区間を逆向きにするか決定（小さいほうの集合を選択）
    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'
    for t in intervals:
        if t[2]  == flip:
            # t[0]が区間開始、t[1]が区間終了、t[2]が種類
            print('People in positions', t[0],
                  'through', t[1], 'flip your caps!')

# 入力リストが空でもエラーが出ない            
def pleaseConform2(caps):
    # 変数の初期化
    start = forward = backward = 0
    intervals = []
    caps = caps + ['END']
    for i in range(1, len(caps)):
        # これがTrueなら、区間がひとつ終わる
        # cap[start]が'F'でも'B'でもTrueとなり、最後の区間が追加される
        if caps[start] != caps[i]:
            intervals.append((start, i-1, caps[start]))
            if caps[start] == 'F':
                forward += 1
            else:
                backward += 1
            start = i
                    
    # どちらの区間を逆向きにするか決定（小さいほうの集合を選択）
    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'
    for t in intervals:
        if t[2]  == flip:
            # t[0]が区間開始、t[1]が区間終了、t[2]が種類
            if t[0] != t[1]:
                print("{}番から{}番、帽子を反対向きにしなさい！".format(t[0], t[1]))
            else:
                print("{}番、帽子を反対向きにしなさい！".format(t[0]))
                
## リストの作成と変更 ##
# 引数のリストが変更されることを避ける

# 〇
def listConcrete(caps):
    caps = caps + ['END']
    print(caps)
capA = ['F', 'F', 'B']
listConcrete(capA)
print(capA)

# ×
def listAppend(caps):
    caps.append('END')
    print(caps)
capA = ['F', 'F', 'B']
listAppend(capA)
print(capA)

## 1パスアルゴリズム ##
# 先頭の人の防止が前向きなら、前向き区間の個数が後ろ向き区間の個数より少ないことはあり得ない。逆もしかり
def pleaseConformOnepass(caps):
    caps = caps + [caps[0]]
    for i in range(1, len(caps)):
        # 直前の要素と違う要素が初めて出てきたら、区間を開始
        if caps[i] != caps[i-1]:
            if caps[i] != caps[0]:
                print('People in positions', i, end='')
            else:
                print(' through', i-1, 'flip your caps!')