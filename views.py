import os

class View:
  def __init__(self):
    pass

  def inputRowOrColumn(self, row_or_column, shot_or_ship = ''):
    while True:
      valid_inputs = ['1','2','3','4','5','6','7','8','9','10']
      user_input = input('Enter the {}{} coordinate: '.format(shot_or_ship, row_or_column))
      if user_input in valid_inputs:
        return int(user_input)

  def inputDirection(self):
    while True:
      valid_inputs = ['n','s','e','w']
      user_input = input('(\'n\' = North, \'s\' = South, \'e\' = East, \'w\' = West)\nEnter direction:')
      if user_input in valid_inputs:
        return user_input

  def boardDisplay(self, player_hits, player_misses, player_ships, enemy_hits, enemy_misses, enemy_ships):
    os.system('clear')
    enemy_display = '   1 2 3 4 5 6 7 8 9 10'
    for row in range(1,11):
      if row == 10:
        enemy_display += '|\n' + str(row) + ' '
      else:
        enemy_display += '|\n ' + str(row) + ' '
      for column in range(1,11):
        if [row, column] in player_hits:
          for each_ship in enemy_ships:
            if [row, column] in each_ship.location:
              enemy_display += '{} '.format(each_ship.name[0])
        elif [row, column] in player_misses:
          enemy_display += 'o '
        else:
          enemy_display += '~ '
    enemy_display += '| \n   - - - - - - - - - -\n'
    display = '   1 2 3 4 5 6 7 8 9 10'
    for row in range(1,11):
      if row == 10:
        display += '|\n' + str(row) + ' '
      else:
        display += '|\n ' + str(row) + ' '
      for column in range(1,11):
        ship_here = 'no'
        if [row, column] in enemy_hits:
          for each_ship in player_ships:
            if [row, column] in each_ship.location:
              display += '{} '.format(each_ship.name[0])
        elif [row, column] in enemy_misses:
          display += 'o '
        else:
          for each_ship in player_ships:
            if [row, column] in each_ship.location:
                display += '{} '.format(each_ship.name[0].upper())
                ship_here ='yes'
                break
          if ship_here == 'no':
            display += '~ '
    display += '| \n   - - - - - - - - - -'
    full_display = enemy_display + display
    print(full_display)