from cube import Cube


def main():
    cube = Cube(3)
    cube.show()
    print("Making 3 moves...")
    cube.move('X', 1, 0, qty=2)
    cube.move('Y', 0, 0, qty=1)
    cube.move('Z', 1, 1, qty=2)
    cube.show()
    print(f'Cube is{"" if cube.is_solved else " not"} solved.')

    print('Reversing these moves...')
    cube.move('Z', 1, 0, qty=2)
    cube.move('Y', 0, 1, qty=1)
    cube.move('X', 1, 1, qty=2)
    cube.show()
    print(f'Cube is{"" if cube.is_solved else " not"} solved.')

    print('Executing 100 random moves...')
    moves = cube.random_moves(100)
    cube.show()
    print(f'Cube is{"" if cube.is_solved else " not"} solved.')

    print('Reversing 100 random moves...')
    for move in reversed(moves):
        # Moves need to be executed in reversed order and also in opposite direction
        if move[2] == 0:
            move[2] = 1
        elif move[2] == 1:
            move[2] = 0
        cube.move(*move)
    cube.show()
    print(f'Cube is{"" if cube.is_solved else " not"} solved.')


if __name__ == '__main__':
    main()