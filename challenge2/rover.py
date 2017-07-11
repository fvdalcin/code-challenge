import sys

class Rover:
    """This class is intended to solve the problem proposed in
    https://github.com/fvdalcin/code-challenge/blob/master/challenge2.md

    Args:
        initial_position (str): The initial position of the rover: two integers
        and one upper-case cardinal point sepparated by spaces.
    """
    def __init__(self, initial_position):
        self.__directions = ("N", "E", "S", "W")
        self.__x = int(initial_position.split(" ")[0])
        self.__y = int(initial_position.split(" ")[1]) 
        self.heading = initial_position.split(" ")[2]
    
    @property
    def heading(self):
        """:obj:`str`: The direction to which the Rover is pointing."""        
        return self.__directions[self.__heading]
    
    @heading.setter
    def heading(self, heading):
        self.__heading = self.__directions.index(heading)
        
    def move(self, instructions):
        """This method is used to control the Rover.
            
        Args:
            instructions (:obj:`str`): A sequence of characters containing the
            instructions to the Rover.
            Each instruction can be one the following actions:
                'L': turn left
                'R': turn right
                'M': move forward            
        """
        for instruction in instructions:
            if instruction == "M":
                if self.heading == "N":
                    self.__y = self.__y + 1
                elif self.heading == "S":
                    self.__y = self.__y - 1
                elif self.heading == "E":
                    self.__x = self.__x + 1
                elif self.heading == "W":
                    self.__x = self.__x - 1
            elif instruction == "L":
                self.__heading = (self.__heading - 1) % 4
            elif instruction == "R":
                self.__heading = (self.__heading + 1) % 4
    
    @property
    def position(self):
        """:obj:`str`: The position of the Rover in the following format: X Y H"""
        return "{0} {1} {2}".format(self.__x, self.__y, self.heading)
        
def main():
    """The main function reads the input file and moves the Rovers around as described
    in the GitHub page of the problem.
    """
    with open(sys.argv[1]) as input:
        input.readline()
        while True:
            line1 = input.readline().rstrip()
            line2 = input.readline().rstrip()
            if not line1: break
            rover = Rover(line1)
            rover.move(line2)
            print(rover.position)
            
if __name__ == "__main__": main()