"""



"""

import tkinter

class Robot(object):

    """
    Represents a robot

    Arguments:
    name (string): robot's name
    color (string): robot's color
    column (int): robot's location in the columns (default = 0)
    row (int): robot's location in the rows (default = 0)

    Attributes:
    name (string): robot's name
    color (string): robot's color
    column (int): robot's location in the columns
    row (int): robot's location in the rows
    battery (int): robot's battery

    """

    # class variable used by the show method
    unit_size = 60

    # False represents an obstacle, True represents open space
    maze = [[True, True, False, True, True, True, False, True, True, True],
            [True, True, False, True, True, True, False, True, True, True],
            [True, False, True, True, True, True, False, True, True, True],
            [True, True, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, False, False, False, False, True, True, True, True, True],
            [True, True, False, True, True, True, True, True, False, True],
            [True, False, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, False, True]]

    #[row][column]

    maze_size = len(maze)

    # a robot with a fully charged battery can take up to 20 steps
    full = 20

    def __init__(self,  name, color, row=0, column=0):
        self.name = name
        self.color = color
        self.row = row
        self.column = column
        self.battery = self.full

    def __str__(self):
        return self.name + ' is a ' + self.color + ' robot lost in the maze.'

    def __gt__(self, other):
        if self.battery > other.battery:
            return True
        else:
            return False

    def recharge(self):
        """
        recharges the battery to full

        parameter: none
        returns: updated robot object

        """
        self.battery = self.full
        return self

    def one_step_forward(self):
        """
        moves robot one step forward

        parameters: none
        returns: updated robot object

        """
        if self.row != self.maze_size - 1 and self.battery != 0 and \
                self.maze[self.row + 1][self.column]:
            self.row += 1
            self.battery -= 1
            return self

        else:
           return self

    def one_step_back(self):
        """
        moves robot one step backwards

        parameters: none
        returns: updated robot object

        """
        if self.row != 0 and self.battery != 0 and \
                self.maze[self.row-1][self.column]:
            self.row -= 1
            self.battery -= 1
            return self

        else:
            return self

    def one_step_right(self):
        """
        moves robot one step to the right

        parameters: none
        returns: updated robot object

        """

        if self.column != self.maze_size - 1 and self.battery != 0 and \
                self.maze[self.row][self.column + 1]:
            self.column += 1
            self.battery -= 1
            return self

        else:
            return self

    def one_step_left(self):
        """
        moves robot one step to the left

        parameters: none
        returns: updated robot object

        """
        if self.column != 0 and self.battery != 0 and \
                self.maze[self.row][self.column - 1]:
            self.column -= 1
            self.battery -= 1
            return self

        else:
            return self

    def forward(self, steps):
        """
        moves robot n steps forward

        parameters: steps(int) - number of steps user inputs
        returns: updated robot object

        """

        for i in range(steps):
            self.one_step_forward()

        return self

    def backward(self, steps):
        """
        moves robot n steps backward

        parameters: steps(int) - number of steps user inputs
        returns: updated robot object

        """

        for i in range(steps):
            self.one_step_back()

        return self

    def right(self, steps):
        """
        moves robot n steps to the right

        parameters: steps(int) - number of steps user inputs
        returns: updated robot object

        """

        for i in range(steps):
            self.one_step_right()

        return self

    def left(self, steps):
        """
        moves robot n steps to the left

        parameters: steps(int) - number of steps user inputs
        returns: updated robot object

        """
        for i in range(steps):
            self.one_step_left()

        return self

    def show(self):
        """
        Draw a graphical representation of the robot in the maze.

        The robot's position and color are shown.
        The color is assumed to be one of the colors recognized by tkinter
        (https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm)
        If the robot's battery is empty, the robot is shown in a
        horizontal position. Otherwise the robot is shown in an upright
        position.
        The obstacles in the maze are shown in red.

        Parameter: None
        Return: None
        """
        root = tkinter.Tk()
        root.title(self.name + ' in the Maze')
        canvas = tkinter.Canvas(root, background='light green',
                                width=self.unit_size * self.maze_size,
                                height=self.unit_size * self.maze_size)
        canvas.grid()

        # draw a representation of the robot in the maze
        if self.battery:
            upper_x = self.column * self.unit_size + self.unit_size / 4
            upper_y = self.row * self.unit_size
            lower_x = upper_x + self.unit_size / 2
            lower_y = upper_y + self.unit_size
            eye_x = lower_x - 3 * self.unit_size / 20
            eye_y = upper_y + self.unit_size / 10

        else: # the robot ran out of battery
            upper_x = self.column * self.unit_size
            upper_y = self.row * self.unit_size + self.unit_size / 2
            lower_x = upper_x + self.unit_size
            lower_y = upper_y + self.unit_size / 2
            eye_x = lower_x - 9 * self.unit_size / 10
            eye_y = lower_y - 3 * self.unit_size / 20

        rectangle = canvas.create_rectangle(upper_x,
                                            upper_y,
                                            lower_x,
                                            lower_y,
                                            fill=self.color)
        # draw the robot's eyes
        canvas.create_oval(upper_x + self.unit_size / 10,
                           upper_y + self.unit_size / 10,
                           upper_x + 3 * self.unit_size / 20,
                           upper_y + 3 * self.unit_size / 20,
                           fill='black')
        canvas.create_oval(eye_x,
                           eye_y,
                           eye_x + self.unit_size / 20,
                           eye_y + self.unit_size / 20,
                           fill='black')
        # draw the obstacles in the maze
        for row in range(self.maze_size):
            for col in range(self.maze_size):
                if not self.maze[row][col]:
                    canvas.create_rectangle(col * self.unit_size,
                                            row * self.unit_size,
                                            (col + 1) * self.unit_size,
                                            (row + 1) * self.unit_size,
                                            fill='red')
        for row in range(self.maze_size):
            canvas.create_line(0,
                               row * self.unit_size,
                               self.maze_size * self.unit_size,
                               row * self.unit_size)
        for col in range(self.maze_size):
            canvas.create_line(col * self.unit_size,
                               0,
                               col * self.unit_size,
                               self.maze_size * self.unit_size)
        root.mainloop()


class UnderwaterRobot(Robot):
    """
    Represents an UNDERWATER robot with similar traits to the land robot

    Arguments:
    name (string): robot's name
    color (string): robot's color
    depth(int): robot's diving depth
    column (int): robot's location in the columns (default = 0)
    row (int): robot's location in the rows (default = 0)

    Attributes:
    name (string): robot's name
    color (string): robot's color
    depth (int): robot's diving depth
    column (int): robot's location in the columns
    row (int): robot's location in the rows
    battery (int): robot's battery

    """

    def __init__(self, name, color, depth, row=0, column=0):
        self.depth = depth
        super().__init__(name, color, row, column)


    def __str__(self):
        return self.name + ' is a ' + self.color + ' robot diving under water.'

    def dive(self, distance):
        """
        allows robot to "dive" underwater

        parameters: distance(int): the depth the robot is currently under
        returns: updated underwater robot object

        """
        self.depth += distance
        return self



