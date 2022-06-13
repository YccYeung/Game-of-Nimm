class Game:
    """
    Brief description of class
    author(s):
    """
    def __init__(self):
        """
        Constructor to create a new Game
        """
        self.__heaps = []
        self.__players = []
        self.__turn_index = 0

    @property
    def turn_index(self):
        """
        :return
        :rtype
        """
        return self.__turn_index

    def get_player(self, player_index):
        """
        :return
        :param
        :type
        :rtype
        """
        return self.__players[player_index]

    def get_heap(self, heap_index):
        """
        :return
        :rtype
        :param
        :type'
        """
        return self.__heaps[heap_index]

    def get_number_of_heaps(self):
        """
        :return
        :rtype
        """
        return len(self.__heaps)

    def add_player(self, player):
        """
        :param
        :type
        :return: None
        """
        self.__players.append(player)

    def increment_turn(self):
        """
        :return: None
        """
        self.__turn_index = (self.__turn_index + 1)

        if self.__turn_index >= len(self.__players):
            self.__turn_index = 0

    def add_heap(self, heap):
        """
        :param
        :type
        :return: None
        """
        self.__heaps.append(heap)

    def update_heap(self, heap_index, amount):
        """
        :param
        :type
        :param
        :type
        :return: None
        """
        self.__heaps[heap_index].remove(amount)

    def is_heap_empty(self, heap_index):
        """
        Checks if the heap has a value of 0
        :param heap_index: Index of the heap
        :type
        :return: Returns true if the heap is empty, and false otherwise
        :rtype: boolean
        """
        heap_empty = False
        if self.__heaps[heap_index].current_size == 0:
            heap_empty = True
        return heap_empty

    def is_amount_valid(self, heap_index, amount):
        """
        testing `Game.turn_index`
        Checks if the amount to remove from the heap is less than or
        equal to the current heap size<br>
        :param heap_index: Index of the heap<br>
        :type heap_index: int<br>
        :param amount: The amount to remove from the heap<br>
        :type amount: int<br>
        :return: Returns true if the amount to remove from the heap
        is less than or equal to the heap amount, and false otherwise<br>
        :rtype: boolean<br>
        """
        amount_valid = True
        if amount <= 0:
            amount_valid = False
        elif self.__heaps[heap_index].current_size - amount < 0:
            amount_valid = False
        return amount_valid

    def print_heaps(self):
        """
        :return: None
        """
        i = 0
        while i < len(self.__heaps):
            print('Heap ' + str(i+1) + ' size: ' +
                  str(self.__heaps[i].current_size))
            i = i + 1

    def is_game_over(self):
        """

        :return:
        :rtype
        """
        i = 0
        is_over = True
        while is_over and i < len(self.__heaps):
            heap_size = self.__heaps[i].current_size
            if heap_size > 0:
                is_over = False
            i += 1
        return is_over

    def reset(self):
        """
        :return: None
        """
        self.__turn_index = 0
        for i in self.__heaps:
            i.reset()

    def increment_player_score(self, player_index):
        """
        :param player_index:
        :type
        :return: None
        """
        self.__players[player_index].increment_score()

    def print_player_scores(self):
        """
        :return: None
        """
        i = 0
        while i < len(self.__players):
            print('Player ' + str(i + 1) + ' score: ' +
                  str(self.__players[i].score))
            i = i + 1

    def print_round_winner(self):
        """
        :return: None
        """
        print('Player ' + self.__players[self.__turn_index].name +
              ' has won this round!')
