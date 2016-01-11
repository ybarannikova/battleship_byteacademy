class Ship:
  def __init__(self, name, length):
    self.name = name
    self.length = length
    self.location = None

  def place_ship(self, row, column, direction, player_ships):
    ship_coords = [[row ,column]]
    for i in range(1, self.length):
      if direction == 'n':
        row -= 1
      elif direction == 's':
        row += 1
      elif direction == 'e':
        column += 1
      elif direction == 'w':
        column -= 1
      else:
        print('Coordinate out of range.')
        return False
      ship_coords.append([row, column])
    for each_coord_set in ship_coords:
      if each_coord_set[0] not in range(1,11) or each_coord_set[1] not in range(1,11):
        print('Placement off the board. Try again, idiot.')
        return False
    for created_ships in player_ships:
      for coordinate in created_ships.location:
        if coordinate in ship_coords:
          print('Already placed ship here. Try again, butthead...')
          return False
    self.location = ship_coords
    return True

class Player:
  def __init__(self, name):
    self.name = (name)
    self.hits = []
    self.misses = []
    self.ships = []