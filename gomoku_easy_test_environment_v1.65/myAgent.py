import random, sys, time, copy, math
from gomoku import Board, Move, GameState, valid_moves, pretty_board, move
from GmUtils import GmUtils
from GmGameRules import GmGameRules
from gomoku_ai_marius1_webclient import gomoku_ai_marius1_webclient
from gomoku_ai_marius_tng_webclient import gomoku_ai_marius_tng_webclient  # a bit better than marius1
from gomoku_ai_random_webclient import gomoku_ai_random_webclient
from basePlayer import basePlayer
from GmGame import GmGame
from GmQuickTests import GmQuickTests

class treeNode:
    def __init__(self, gamestate, last_move = None, parentNode = None, valid_move_list = None):
        """Constructor tree node"""
        self.gamestate = gamestate
        self.finished = GmUtils.isWinningMove(last_move, gamestate[0])
        self.last_move = last_move
        self.parent = parentNode
        self.children = []
        self.visited = []
        self.Q = 0  # number of wins
        self.N = 0  # number of visits
        self.valid_moves = valid_move_list

    def fully_expanded(self):
        return len(self.children) is len(self.valid_moves)

    def calculateUTC(self):
        win_ratio = self.Q / self.N
        c = math.sqrt(2)
        res = win_ratio + c * math.sqrt(math.log2(self.parent.N) / self.N)
        return res

    def FindSpotToExpand(self):
        if self.finished == True:
            return self
        if self.fully_expanded() == False:
            move_to_do = random.choice(self.valid_moves)
            new_state = move(self.gamestate, random.choice(self.valid_moves))
            new_valid_moves = copy.deepcopy(self.valid_moves)
            new_valid_moves.remove(move_to_do)
            new_node = treeNode(
                new_state, last_move=move_to_do, parentNode=self, valid_move_list=new_valid_moves
            )
            self.children.append(new_node)
            return new_node
        best_child = None
        best_value = 0
        for ch in self.children:
            child_UTC = ch.calculateUTC()
            if best_child == None:
                best_value = child_UTC
                best_child = ch
                continue
            if child_UTC > best_value:
                best_value = child_UTC
                best_child = ch
        return best_child.FindSpotToExpand()
    
    def Rollout(self):
        if self.finished:
            if self.won == 1:
                return 1
            elif self.won == 2:
                return -1
            else:
                return 0

class supremePlayer:
    def __init__(self, black_: bool = True):
        """Constructor for the player."""
        self.black = black_

    def new_game(self, black_: bool):
        """At the start of each new game you will be notified by the competition.
        this method has a boolean parameter that informs your agent whether you
        will play black or white.
        """
        self.black = black_

    def move(self, state: GameState, last_move: Move, max_time_to_move: int = 1000) -> Move:
        """This is the most important method: the agent will get:
        1) the current state of the game
        2) the last move by the opponent
        3) the available moves you can play (this is a special service we provide ;-) )
        4) the maximum time until the agent is required to make a move in milliseconds [diverging from this will lead to disqualification].
        """
        start_time = time.perf_counter()
        max_time = (max_time_to_move / 1000) - 0.05
        time_elapsed = time.perf_counter() - start_time
        valid_moves = valid_moves(state)
        root = treeNode(state, last_move, valid_move_list=valid_moves)
        while time_elapsed < max_time:
            leaf = root.FindSpotToExpand()

            # while time not over
            # nodes make voor huidige state




            time_elapsed = time.perf_counter() - start_time
        return random.choice(moves)

        

    def id(self) -> str:
        return "Ka Long Yang (1676436)"
    
    start_time = time.perf_counter()
    print(start_time)
    time.sleep(1.3)
    stop_time = time.perf_counter()
    print(stop_time)
    time.sleep(1.3)
    stop_time = time.perf_counter()
    print(stop_time)