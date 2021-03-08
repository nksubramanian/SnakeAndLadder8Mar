import Module1
import Module2
import Module3
if __name__ == '__main__':
    pos1 = Module1.Position(1, 500)
    valid_dicerolls = set(range(1, 7))
    Module3.Display.print_screen(pos1)
    while Module2.Board.IsGameOver(pos1)==0:
        val = input("Enter the die value: ")
        if int(val) not in valid_dicerolls:
            raise Exception("Invalid Dice value")
        else:
            Module2.Board.play_move(pos1, int(val))
        Module3.Display.print_screen(pos1)

    test2 = Module1.Position(32, 500)
    Module2.Board.play_move(test2, 3)
    Module3.Display.print_screen(test2)


