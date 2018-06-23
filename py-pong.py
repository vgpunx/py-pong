from game import *
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('-cpu', '--computer', action='store_true', dest='computerPlayer',
                    help='Have the Computer play as Player 2.')
parser.add_argument('-d', '--difficulty', type=float, dest='difficulty', default=0.5,
                    help='Sets the difficulty level of the CPU player.')

if __name__ == "__main__":
    args = parser.parse_args()
    game = Game(CPU_flag=args.computerPlayer, CPU_difficulty=args.difficulty)
    game.run()
    pygame.quit()