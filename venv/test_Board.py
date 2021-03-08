import Module1
import Module2
import Module3

def test_position():
    test1 = Module1.Position(1,500)
    assert test1.position == 1
    assert test1.money_available == 500

def test_movecheck():
    test1 = Module1.Position(1, 500)
    Module2.Board.play_move(test1,1)
    assert test1.position == 2
    Module2.Board.play_move(test1,2)
    assert test1.position == 4

def test_laddercheck():
    test2 = Module1.Position(1, 500)
    Module2.Board.play_move(test2,4)
    assert test2.position == 10
    assert test2.money_available == 600
    Module2.Board.play_move(test2,2)
    assert test2.position == 26
    assert test2.money_available == 700
    Module2.Board.play_move(test2,6)
    assert test2.position == 32
    assert test2.money_available == 700
    Module2.Board.play_move(test2,3)
    assert test2.position == 36
    assert test2.money_available == 800
    Module2.Board.play_move(test2,4)
    assert test2.position == 45
    assert test2.money_available == 900
    test3 = Module1.Position(1, 500)
    Module2.Board.play_move(test3,4)
    Module2.Board.play_move(test3,6)
    assert test3.position == 29
    assert test3.money_available == 700


def test_snakecheck():
    test4 = Module1.Position(1, 500)
    Module2.Board.play_move(test4,4)
    Module2.Board.play_move(test4,4)
    assert test4.position == 2
    assert test4.money_available == 500
    Module2.Board.play_move(test4, 3)
    assert test4.position == 10
    assert test4.money_available == 600
    Module2.Board.play_move(test4,5)
    assert test4.position == 15
    assert test4.money_available == 600
    Module2.Board.play_move(test4,6)
    Module2.Board.play_move(test4,2)
    assert test4.position == 8
    assert test4.money_available == 500
    Module2.Board.play_move(test4,4)
    Module2.Board.play_move(test4,6)
    Module2.Board.play_move(test4,6)
    Module2.Board.play_move(test4,5)
    assert test4.position == 41
    assert test4.money_available == 500
    Module2.Board.play_move(test4,6)
    assert test4.position == 37
    assert test4.money_available == 400
