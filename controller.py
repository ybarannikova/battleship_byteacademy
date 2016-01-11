from models import Ship
from models import Player
from views import View
import os

p1 = Player('Player 1')
p2 = Player('Player 2')

class Battleship:
  def __init__(self):
    self.players = [p1, p2]
    self.ship_names = ['aircraft carrier', 'battleship','submarine','destroyer','patrol']
    self.ship_lengths = [5,4,3,3,2]
    self.play_view = View()

  def set_up(self):
    for each_player in self.players:
      for i in range(5):
        self.play_view.boardDisplay([], [],each_player.ships, [], [], [])
        x = Ship(self.ship_names[i], self.ship_lengths[i])
        print ("Place your {} (length {}).".format(x.name, x.length))
        valid_placement = 'invalid'
        while valid_placement == 'invalid':
          row = self.play_view.inputRowOrColumn('ROW', 'ship\'s starting ')
          column = self.play_view.inputRowOrColumn('COLUMN', 'ship\'s starting ')
          direction = self.play_view.inputDirection()
          placement = x.place_ship(row,column,direction, each_player.ships)
          if placement == True:
            break
        each_player.ships.append(x)
      self.play_view.boardDisplay([], [], each_player.ships, [], [], [])
      end_turn = input('Finished placing ships.\n\nENTER to clear the screen.')

  def play(self):
    while True:
      self.play_view.boardDisplay([], [], [], [], [], [])
      begin_turn = input('{}, ENTER to begin your turn.'.format(self.players[0].name))
      self.play_view.boardDisplay(self.players[0].hits, self.players[0].misses, self.players[0].ships, self.players[-1].hits, self.players[-1].misses, self.players[-1].ships)
      print(self.players[0].name)
      while True:
        row = self.play_view.inputRowOrColumn('ROW')
        column = self.play_view.inputRowOrColumn('COLUMN')
        shot = [row, column]
        if shot in self.players[0].misses or shot in self.players[0].hits:
          print('You already took this shot, jackass...')
        else:
          break
      hit_or_miss = 'miss'
      for each_ship in self.players[-1].ships:
        if shot in each_ship.location:
          hit_or_miss = 'hit'
      if hit_or_miss == 'hit':
        self.players[0].hits.append(shot)
      else:
        self.players[0].misses.append(shot)
      self.play_view.boardDisplay(self.players[0].hits, self.players[0].misses, self.players[0].ships, self.players[-1].hits, self.players[-1].misses, self.players[-1].ships)
      if len(self.players[0].hits) == 17:
        input("- - - {} WINS! - - -".format(self.players[0].name))
        break
      end_turn = input('{}, {} is a {}. \n\nENTER to clear the screen and end your turn.'.format(self.players[0].name,shot, hit_or_miss.upper()))
      next_player = self.players.pop()
      self.players.insert(0, next_player)

os.system('clear')
play_or_quit = input('                                     |__\n                                     |\\/\n                                     ---\n                                     / | [        Welcome To\n                              !      | |||        BATTLESHIP\n                            _/|     _/|-++\'\n                        +  +--|    |--|--|_ |-\n                     { /|__|  |/\\__|  |--- |||__/\n                    +---------------___[}-_===_.\'____                 /\\\n                ____`-\' ||___-{]_| _[}-  |     |_[___\\==--            \\/   _\n __..._____--==/___]_|__|_____________________________[___\\==--____,------\' .7\n|                            U.S.S. SCALPERS                           BB-61/\n \\_________________________________________________________________________|\n\n                          ENTER to Start Playing')
while play_or_quit != 'q':
  new_game = Battleship()
  new_game.set_up()
  new_game.play()
  os.system('clear')
  play_or_quit = input('                                     |__\n                                     |\\/\n                                     ---\n                                     / | [        Welcome To\n                              !      | |||        BATTLESHIP\n                            _/|     _/|-++\'\n                        +  +--|    |--|--|_ |-\n                     { /|__|  |/\\__|  |--- |||__/\n                    +---------------___[}-_===_.\'____                 /\\\n                ____`-\' ||___-{]_| _[}-  |     |_[___\\==--            \\/   _\n __..._____--==/___]_|__|_____________________________[___\\==--____,------\' .7\n|                            U.S.S. SCALPERS                           BB-61/\n \\_________________________________________________________________________|\n\n                     ENTER to Play Again / \'q\' to Quit')
