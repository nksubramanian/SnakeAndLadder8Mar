class Printer:
  @staticmethod
  def print_screen(position_object):
    print("You are in position " + str(position_object.position) + " and availabe money is " + str(position_object.money_available))
    if position_object.position==49:
      print("You won!")
    elif position_object.money_available<=0:
      print("You lost!")
    else:
      print("Continue to play")