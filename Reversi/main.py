# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 23:13:15 2018

@author: hiroya
"""

from Reversi import *

if __name__ == "__main__":
    game = Game()
    while(True):
        possible = game.list_possible_cells()
        player_name = game.get_color(game.get_current_player())

        if game.is_finished():
            game.show_board()
            game.show_score()
            print("Winner: {}".format(game.get_color(game.winner)))
            break

        if possible == []:
            print("player {} can not puts.".format(player_name))
            game.pass_moving()
            continue

        game.show_board()
        print("player: " + player_name)
        print("put to: " + str(possible))
        print("If you want to end in the middle, select an index out of range.")
        index = int(input("choose an index(ex.0,1,・・・): "))

        game.put_disk(*possible[index])