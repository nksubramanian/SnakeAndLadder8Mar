import Module1
import Module2
import Module3
if __name__ == '__main__':
    pos1 = Module1.Position(1, 500)
    valid_dicerolls = set(range(1, 7))
    Module3.Printer.print_screen(pos1)
    while Module2.Board.IsGameOver(pos1)==0:
        val = input("Enter the die value: ")
        if int(val) not in valid_dicerolls:
            raise Exception("Invalid Dice value")
        else:
            Module2.Board.update_states(pos1, int(val))
        Module3.Printer.print_screen(pos1)


