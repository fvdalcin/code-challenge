import unittest
from rover import Rover

class TestRover(unittest.TestCase):

    def test_constructor(self):
        rover = Rover("1 2 N")
        self.assertEqual(rover.position, "1 2 N")

    def test_move_up(self):
        rover = Rover("1 2 N")
        rover.move("M")
        self.assertEqual(rover.position, "1 3 N")
    
    def test_move_down(self):
        rover = Rover("1 2 S")
        rover.move("M")
        self.assertEqual(rover.position, "1 1 S")
        
    def test_move_right(self):
        rover = Rover("1 2 E")
        rover.move("M")
        self.assertEqual(rover.position, "2 2 E")
        
    def test_move_left(self):
        rover = Rover("1 2 W")
        rover.move("M")
        self.assertEqual(rover.position, "0 2 W")
        
    def test_turn_left_from_north_to_west(self):
        rover = Rover("1 2 N")
        rover.move("L")
        self.assertEqual(rover.position, "1 2 W")

    def test_turn_left_from_west_to_south(self):
        rover = Rover("1 2 W")
        rover.move("L")
        self.assertEqual(rover.position, "1 2 S")
    
    def test_turn_left_from_south_to_east(self):
        rover = Rover("1 2 S")
        rover.move("L")
        self.assertEqual(rover.position, "1 2 E")
        
    def test_turn_left_from_east_to_north(self):
        rover = Rover("1 2 E")
        rover.move("L")
        self.assertEqual(rover.position, "1 2 N")
        
    def test_turn_right_from_north_to_east(self):
        rover = Rover("1 2 N")
        rover.move("R")
        self.assertEqual(rover.position, "1 2 E")
        
    def test_turn_right_from_east_to_south(self):
        rover = Rover("1 2 E")
        rover.move("R")
        self.assertEqual(rover.position, "1 2 S")
    
    def test_turn_right_from_south_to_west(self):
        rover = Rover("1 2 S")
        rover.move("R")
        self.assertEqual(rover.position, "1 2 W")
        
    def test_turn_right_from_west_to_north(self):
        rover = Rover("1 2 W")
        rover.move("R")
        self.assertEqual(rover.position, "1 2 N")
    
    def test_case_one(self):
        rover = Rover("1 2 N")
        rover.move("LMLMLMLMM")
        self.assertEqual(rover.position, "1 3 N")
    
    def test_case_two(self):
        rover = Rover("3 3 E")
        rover.move("MMRMMRMRRM")
        self.assertEqual(rover.position, "5 1 E")
        