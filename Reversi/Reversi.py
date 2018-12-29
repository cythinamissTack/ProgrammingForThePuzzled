# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 17:59:24 2018

@author: hiroya
"""

# ボードサイズと石の定義
WHITE = 0; BLACK = 1; BOARD_SIZE = 8

""" リバーシボードクラスの定義 """
class ReversiBoard(object):
    ## 初期条件 ##
    def __init__(self):
        # ２次元リストを生成
        # 各要素の初期値はNone
        self.cells = []
        for i in range(BOARD_SIZE):
            self.cells.append([None for i in range(BOARD_SIZE)])
            
        # ４つの石を初期配置する
        self.cells[3][3] = WHITE
        self.cells[3][4] = BLACK
        self.cells[4][3] = BLACK
        self.cells[4][4] = WHITE
    
    ###########################################################################
    
    ## ひっくりかえせる石の数を列挙するメソッド ##
    def list_flippable_disks(self, x, y, player):
        """
        指定した座標に指定したプレイヤーの石を置いた時、ひっくりかえせる全ての石の座標（タプル）をリストにして返す
        Args:
            x : 置く石のｘ座標
            y : 置く石のｙ座標
            player : 石を置こうとしているプレイヤー(WHITEまたはBLACK)
            
        Returns:
            ひっくりかえすことができるすべての石の座標（タプル）のリスト
            または空リスト
        """
        
        PREV = -1
        NEXT = 1
        DIRECTION = [PREV, 0, NEXT]
        flippable = []

        for dx in DIRECTION:
            for dy in DIRECTION:
                if dx == 0 and dy == 0:
                    continue

                tmp = []
                depth = 0
                while(True):
                    depth += 1

                    # 方向 × 深さ(距離)を要求座標に加算し直線的な探査をする
                    rx = x + (dx * depth)
                    ry = y + (dy * depth)

                    # 調べる座標(rx, ry)がボードの範囲内ならば
                    if 0 <= rx < BOARD_SIZE and 0 <= ry < BOARD_SIZE:
                        request = self.cells[ry][rx]

                        # Noneを獲得することはできない
                        if request is None:
                            break

                        if request == player:  # 自分の石が見つかったとき
                            if tmp != []:      # 探査した範囲内に獲得可能な石があれば
                                flippable.extend(tmp) # flippableに追加

                        # 相手の石が見つかったとき
                        else:
                            # 獲得可能な石として一時保存
                            tmp.append((rx, ry))
                    else:
                        break
        return flippable
    ###########################################################################
                    
    ## 石を置くメソッド ##
    def put_disk(self, x, y, player):
        """指定した座標に指定したプレイヤーの石を置く
        Args:
            x : 置く石のｘ座標
            y : 置く石のｙ座標
            player : 石を置こうとしているプレイヤー(WHITEまたはBLACK)
            
        Returns:
            True : 関数の成功を意味する。指定した座標とそれによって獲得できる石が
                   すべてplayerの色になった場合に返す。
            False : 関数が以下のいずれかのケースによって失敗した場合に返す
                    ・指定した座標に既に別の石がある
                    ・指定した座標に石を置いても相手側の石を獲得できない
        """
        
        # 既にほかの石があれば置くことができない
        if self.cells[y][x] is not None:
            return False
        
        # 獲得できる石がない場合も置くことができない
        flippable = self.list_flippable_disks(x, y, player)
        if flippable == []:
            return False
        
        # 実際に石を置く処理
        self.cells[y][x] = player
        for x,y in flippable:
            self.cells[y][x] = player
            
        return True
    ###########################################################################
    
    ## 盤面を表示するメソッド ##
    def show_board(self):
        """盤面を表示する"""
        print("--" * 20)
        for i in self.cells:
            for cell in i:
                if cell == WHITE:
                    print("W", end=" ")
                elif cell == BLACK:
                    print("B", end=" ")
                else:
                    print("*", end=" ")
            print("\n", end="")
    ###########################################################################
    
    ## プレイヤーが置くことができるマスのリストを返すメソッド ##
    def list_possible_cells(self, player):
        """
        指定したプレイヤー対して、石の置くことができるすべてのマスの座標をリストにして返す
        Args:
            player: 石を置こうとしているプレイヤー

        Returns:
            石を置くことができるマスの座標のリスト
            または空リスト
        """
        
        possible = []
        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                if self.cells[y][x] is not None:
                    continue
                if self.list_flippable_disks(x, y, player) == []:
                    continue
                else:
                    possible.append((x, y))
                
        return possible
    ###########################################################################
    
    # 持ち石を確認するメソッド
    def number_of_disks(self, player):
        """
        指定したプレイヤー対して、石の置くことができるすべてのマスの座標をリストにして返す
        Args:
            player: 石を置こうとしているプレイヤー

        Returns:
            持ち石の数を文字列として返す
        """
        
        num = 0
        for i in self.cells:
            for cell in i:
                if cell == player:
                    num += 1
        
        return str(num)
    ###########################################################################            
        
    
""" ゲームクラスの定義 """
class Game(ReversiBoard):
    DRAW = -1

    def __init__(self, turn=0, start_player=BLACK):
        super().__init__()
        self.player = start_player
        self.turn = turn
        self.winner = None
        self.was_passed = False

    ###########################################################################
    
    def is_finished(self):
        return self.winner is not None
    ###########################################################################

    def list_possible_cells(self):
        return super().list_possible_cells(self.player)
    ###########################################################################
    
    def get_color(self, player):
        if player == WHITE:
            return "WHITE"
        if player == BLACK:
            return "BLACK"
        else:
            return "DRAW"
    ###########################################################################
    
    def get_current_player(self):
        return self.player
    ###########################################################################
   
    def get_next_player(self):
        return WHITE if self.player == BLACK else BLACK
    ###########################################################################
    
    def shift_player(self):
        self.player = self.get_next_player()
    ###########################################################################
    
    def put_disk(self, x, y):
        if super().put_disk(x, y, self.player):
            self.was_passed = False
            self.player = self.get_next_player()
            self.turn += 1
        else:
            return False
    ###########################################################################
    
    def pass_moving(self):
        if self.was_passed:
            return self.finish_game()
    ###########################################################################
    
        self.was_passed = True
        self.shift_player()
        
    ###########################################################################
    def show_score(self):
        """それぞれのプレイヤーの石の数を表示する"""
        print("{}: {}".format("BLACK", super().number_of_disks(BLACK)))
        print("{}: {}".format("WHITE", super().number_of_disks(WHITE)))
    ###########################################################################
    
    def finish_game(self):
        white = int(super().number_of_disks(WHITE))
        black = int(super().number_of_disks(BLACK))

        if white < black:
            self.winner = BLACK
        elif black < white:
            self.winner = WHITE
        else:
            self.winner = self.on_draw()

        return self.winner
    ###########################################################################
    
    def on_draw(self):
        """ゲーム終了時に両社の石の数が同数だった時の処理
        デフォルトでは引き分けを認める
        """
        return self.DRAW
    ###########################################################################