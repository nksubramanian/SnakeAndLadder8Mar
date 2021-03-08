class Board:
  _all_position = set(range(1, 50))
  _snake={14:2,23:8,43:41,47:37}
  _ladder = {5: 10, 12: 26, 16: 29, 19: 33, 35: 36, 40: 45}
  @classmethod
  def play_move(cls,position_object,dice_roll):
    if (position_object.position + dice_roll) not in cls._all_position:
      position_object.money_available = position_object.money_available - 10
    elif position_object.position + dice_roll in cls._snake:
      position_object.position = cls._snake[position_object.position + dice_roll]
      position_object.money_available = position_object.money_available - 100
    elif position_object.position + dice_roll in cls._ladder:
      print(position_object.position + dice_roll)
      position_object.position = cls._ladder[position_object.position + dice_roll]
      position_object.money_available = position_object.money_available + 100
    else:
      position_object.position = position_object.position + dice_roll

  @staticmethod
  def IsGameOver(position_object):
    if position_object.money_available <= 0:
      return -1
    elif position_object.position == 49:
      return 1
    else:
      return 0