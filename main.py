from distutils.util import strtobool

from student.game import Game
from student.heap import Heap
from student.player import Player


def main():
    """"""
    # assumes valid input
    number_of_players = int(input("Enter the number of players: "))

    # assumes valid input
    number_of_heaps = int(input("Enter the number of heaps: "))

    game = Game()

    add_players(number_of_players, game)
    add_heaps(number_of_heaps, game)

    run_game(game)

    boolean_string = input('Do you want to play another round? '
                           'True or False: ')
    user_continue = bool(strtobool(boolean_string))

    while user_continue:
        game.reset()
        run_game(game)

        boolean_string = input('Do you want to play another round? '
                               'True or False: ')
        user_continue = bool(strtobool(boolean_string))


def run_game(game):
    """
    :param
    :type
    :return: None
    """
    game.print_heaps()

    while not game.is_game_over():
        take_turn(game)
    game.print_round_winner()
    game.print_player_scores()


# Decide if this method should be in this class or somewhere else
# This is more of a control-related method than an entity function
def take_turn(game):
    """
    :param
    :type
    :return: None
    """
    turn_index = game.turn_index
    current_player = game.get_player(turn_index)
    current_player_name = current_player.name

    heap_index, amount = get_heap_amount(game)

    print_move(current_player_name, amount, heap_index)

    # update heap - currently ignoring the value returned
    game.update_heap(heap_index, amount)
    game.print_heaps()

    # increment turn if game is not over, otherwise increment current
    # player's score
    if not game.is_game_over():
        game.increment_turn()
    else:
        game.increment_player_score(turn_index)


def get_heap_amount(game):
    """
    :param
    :type
    :return
    :return
    :rtype
    :rtype
    """
    turn_index = game.turn_index
    current_player = game.get_player(turn_index)
    current_player_name = current_player.name

    valid_index = False
    heap_index = -1
    valid_amount = False
    amount = -1

    while not valid_amount:
        while not valid_index:
            heap_index = int(input(current_player_name
                                   + ": Choose a heap number: ")) - 1
            if heap_index < 0 or heap_index >= game.get_number_of_heaps() \
                    or game.is_heap_empty(heap_index):
                print(str(heap_index + 1) + ' is not a valid heap number.')
            else:
                valid_index = True

        amount = int(input(current_player_name +
                           ": Choose an amount to remove from heap "
                           + str(heap_index + 1) + ": "))
        if not game.is_amount_valid(heap_index, amount):
            print(str(amount) + ' is not a valid heap amount.')
            valid_index = False
        else:
            valid_amount = True
    return heap_index, amount


def add_players(number_of_players, game):
    """
    :param
    :type
    :param
    :type
    :return: None
    """
    for i in range(number_of_players):
        player_name = input("Enter a name for player " + str(i+1)
                            + ": ")
        player = Player(player_name)
        game.add_player(player)


def add_heaps(number_of_heaps, game):
    """
    :param
    :type
    :param
    :type
    :return: None
    """
    for i in range(number_of_heaps):
        heap_size = int(input("Enter a size for heap " + str(i+1)
                              + ": "))
        heap = Heap(heap_size)
        game.add_heap(heap)


def print_move(player_name, amount, heap_index):
    """
    :param
    :type
    :param
    :type
    :param
    :type
    :return: None
    """
    print(player_name, "takes", amount, "from heap", heap_index+1)


if __name__ == '__main__':
    main()
