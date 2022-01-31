import copy
import random
from termcolor import colored


class Cube:
    def __init__(self, size=3):

        self.size = size
        self.cube = self.generate(size)

    @staticmethod
    def generate(size: int) -> list:
        """
        Generates cube with specific size.
        :param size: Size of the cube.
        :return: Cube list.
        """
        cube = list()
        for i in range(size):
            layer = []
            for j in range(size):
                row = []
                for k in range(size):
                    cubie = [1, 2, 3, 4, 5, 6]
                    #INSIDE
                    if 0 < i < size - 1 and 0 < j < size - 1 and 0 < k < size - 1:
                        cubie = [0 for _ in range(6)]
                    #CORNERS
                    #up
                    elif i is 0 and j is 0 and k is 0:
                        cubie[2], cubie[3], cubie[4] = 0, 0, 0
                    elif i is 0 and j is 0 and k is size - 1:
                        cubie[0], cubie[2], cubie[4] = 0, 0, 0
                    elif i is 0 and j is size - 1 and k is 0:
                        cubie[1], cubie[2], cubie[3] = 0, 0, 0
                    elif i is 0 and j is size - 1 and k is size - 1:
                        cubie[0], cubie[1], cubie[2] = 0, 0, 0
                    #down
                    elif i is size - 1 and j is 0 and k is 0:
                        cubie[3], cubie[4], cubie[5] = 0, 0, 0
                    elif i is size - 1 and j is 0 and k is size - 1:
                        cubie[0], cubie[4], cubie[5] = 0, 0, 0
                    elif i is size - 1 and j is size - 1 and k is 0:
                        cubie[1], cubie[3], cubie[5] = 0, 0, 0
                    elif i is size - 1 and j is size - 1 and k is size - 1:
                        cubie[0], cubie[1], cubie[5] = 0, 0, 0
                    #EDGES
                    #up
                    elif i is 0 and j is 0 and 0 < k < size - 1:
                        cubie[0], cubie[2], cubie[3], cubie[4] = 0, 0, 0, 0
                    elif i is 0 and j is size - 1 and 0 < k < size - 1:
                        cubie[0], cubie[1], cubie[2], cubie[3] = 0, 0, 0, 0
                    elif i is 0 and 0 < j < size - 1 and k is 0:
                        cubie[1], cubie[2], cubie[3], cubie[4] = 0, 0, 0, 0
                    elif i is 0 and 0 < j < size - 1 and k is size - 1:
                        cubie[0], cubie[1], cubie[2], cubie[4] = 0, 0, 0, 0
                    #middle
                    elif 0 < i < size - 1 and j is 0 and k is 0:
                        cubie[2], cubie[3], cubie[4], cubie[5] = 0, 0, 0, 0
                    elif 0 < i < size -1 and j is 0 and k is size - 1:
                        cubie[0], cubie[2], cubie[4], cubie[5] = 0, 0, 0, 0
                    elif 0 < i < size - 1 and j is size - 1 and k is 0:
                        cubie[1], cubie[2], cubie[3], cubie[5] = 0, 0, 0, 0
                    elif 0 < i < size -1 and j is size - 1 and k is size - 1:
                        cubie[0], cubie[1], cubie[2], cubie[5] = 0, 0, 0, 0
                    #down
                    elif i is size - 1 and j is 0 and 0 < k < size - 1:
                        cubie[0], cubie[3], cubie[4], cubie[5] = 0, 0, 0, 0
                    elif i is size - 1 and j is size - 1 and 0 < k < size - 1:
                        cubie[0], cubie[1], cubie[3], cubie[5] = 0, 0, 0, 0
                    elif i is size - 1 and 0 < j < size - 1 and k is 0:
                        cubie[1], cubie[3], cubie[4], cubie[5] = 0, 0, 0, 0
                    elif i is size - 1 and 0 < j < size - 1 and k is size - 1:
                        cubie[0], cubie[1], cubie[4], cubie[5] = 0, 0, 0, 0
                    #CENTERS
                    #up
                    elif i is 0 and 0 < j < size - 1 and 0 < k < size - 1:
                        cubie[0], cubie[1], cubie[2], cubie[3], cubie[4] = 0, 0, 0, 0, 0
                    #middle
                    elif 0 < i < size - 1 and 0 < j < size - 1 and k is 0:
                        cubie[1], cubie[2], cubie[3], cubie[4], cubie[5] = 0, 0, 0, 0, 0
                    elif 0 < i < size - 1 and 0 < j < size - 1 and k is size - 1:
                        cubie[0], cubie[1], cubie[2], cubie[4], cubie[5] = 0, 0, 0, 0, 0
                    elif 0 < i < size - 1 and j is 0 and 0 < k < size - 1:
                        cubie[0], cubie[2], cubie[3], cubie[4], cubie[5] = 0, 0, 0, 0, 0
                    elif 0 < i < size - 1 and j is size - 1 and 0 < k < size - 1:
                        cubie[0], cubie[1], cubie[2], cubie[3], cubie[5] = 0, 0, 0, 0, 0
                    # down
                    elif i is size - 1 and 0 < j < size - 1 and 0 < k < size - 1:
                        cubie[0], cubie[1], cubie[3], cubie[4], cubie[5] = 0, 0, 0, 0, 0

                    row.append(cubie)
                layer.append(row)
            cube.append(layer)
        return cube

    def move(self, axis: str, layer: int, direction: int, qty: int = 1, show: bool = False) -> None:
        """
        Moves cube in specific axis, layer and direction.
        :param axis: X / Y / Z.
        :param layer: int 1-self.size.
        :param direction: 0: Clockwise / 1: counterclockwise.
        :param qty: Quantity of moves.
        :param show: True: Display cube after move.
        :return: None
        """

        for _ in range(qty):
            buffer = copy.deepcopy(self.cube)

            if axis is 'Y':
                for i, p in enumerate(buffer[layer]):
                    for j, e in enumerate(p):

                        if direction is 0:
                            e[0], e[1], e[3], e[4] = e[4], e[0], e[1], e[3]
                            self.cube[layer][j][self.size - 1 - i] = e

                        elif direction is 1:
                            e[4], e[0], e[1], e[3] = e[0], e[1], e[3], e[4]
                            self.cube[layer][self.size - 1 - j][i] = e

            elif axis is 'X':
                for i, p in enumerate(buffer):
                    for j, e in enumerate(p):
                        e = e[layer]

                        if direction is 0:
                            e[1], e[2], e[4], e[5] = e[2], e[4], e[5], e[1]
                            self.cube[j][self.size - 1 - i][layer] = e

                        elif direction is 1:
                            e[2], e[4], e[5], e[1] = e[1], e[2], e[4], e[5]
                            self.cube[self.size - 1 - j][i][layer] = e

            elif axis is 'Z':
                for i, p in enumerate(buffer):
                    for j, e in enumerate(p[layer]):

                        if direction is 0:
                            e[0], e[2], e[3], e[5] = e[2], e[3], e[5], e[0]
                            self.cube[j][layer][self.size - 1 - i] = e

                        elif direction is 1:
                            e[2], e[3], e[5], e[0] = e[0], e[2], e[3], e[5]
                            self.cube[self.size - 1 - j][layer][i] = e

        if show:
            self.show()

    def show(self) -> None:
        """
        Displays cube in console.
        :return: None
        """

        colors = [None, 'blue', 'red', 'grey', 'cyan', 'magenta', 'yellow']

        left_side = [[i[0][0] for i in n] for n in self.cube]
        front_side = [[i[1] for i in n[0]] for n in self.cube]
        down_side = [[i[2] for i in n] for n in self.cube[self.size - 1]]
        right_side = [[i[self.size - 1][3] for i in n] for n in self.cube]
        up_side = [[i[5] for i in n] for n in self.cube[0]]
        back_side = [[i[4] for i in n[self.size - 1]] for n in self.cube]

        sign = '■'
        cubie_separator = ' '
        tab = ' ' * (2 * self.size)

        for up_row in reversed(up_side):
            args_up = [[sign, colors[color]] for color in up_row]
            self.print_row(tab, *args_up, separator=cubie_separator)

        for left_row, front__row, right_row, back_row in zip(left_side, front_side, right_side, back_side):
            args_left = [[sign, colors[color]] for color in reversed(left_row)]
            args_front = [[sign, colors[color]] for color in front__row]
            args_right = [[sign, colors[color]] for color in right_row]
            args_back = [[sign, colors[color]] for color in reversed(back_row)]
            self.print_row(*args_left, '', *args_front, '', *args_right, '', *args_back, separator=cubie_separator)

        for down_row in down_side:
            args_down = [[sign, colors[color]] for color in down_row]
            self.print_row(tab, *args_down, separator=cubie_separator)

    @property
    def is_solved(self) -> bool:
        """
        Returns if cube is solved or not.
        :return: True: cube is solved, False: cube is not solved.
        """
        solved = True
        counter = [0, 0, 0, 0, 0, 0]
        grid = [0, 0, 0, 0, 0, 0]

        for i in self.cube:
            for j in i:
                for k in j:
                    for l, m in enumerate(k):
                        if m is not 0:
                            if grid[l] is 0:
                                grid[l] = m
                                counter[l] += 1
                            elif grid[l] == m:
                                counter[l] += 1
                            else:
                                solved = False
        return solved

    def random_moves(self, num: int, show: bool = False) -> list:
        """
        Executes specified number of random moves on cube.
        :param num: Number of moves to execute.
        :param show: True: display cube in console every move.
        :return: List of executed moves.
        """
        moves = []
        for _ in range(num):
            move = [random.choice(['X', 'Y', 'Z']), random.randint(0, self.size - 1), random.randint(0, 1)]
            self.move(*move)
            if show:
                self.show()
            moves.append(move)
        return moves

    @staticmethod
    def print_row(*args, **kwargs) -> None:
        args_ = []

        separator = ''
        color = None

        if 'separator' in kwargs:
            separator = kwargs['separator']
        if 'color' in kwargs:
            color = kwargs['color']

        for i, arg in enumerate(args):
            if i == len(args) - 1:
                separator = ''
            if hasattr(arg, '__len__') and type(arg) is not str:
                if len(arg) > 1 and type(arg) is not str:
                    args_.append([f'{arg[0]}{separator}', arg[1]])
                elif len(arg) > 0 and type(arg) is not str:
                    args_.append([f'{arg[0]}{separator}', color])
            else:
                args_.append([f'{arg}{separator}', color])
        rv = ''

        for arg in args_:
            rv += colored((str(arg[0])), arg[1])
        print(rv)
