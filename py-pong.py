from game import *
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('-c', '--computer', action='store_true', dest='computerPlayer',
                    help='Have the Computer play as Player 2.')

if __name__ == "__main__":
    args = parser.parse_args()
    game = Game(args.computerPlayer)
    game.run()
    pygame.quit()