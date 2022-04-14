# numbrix.py: Template para implementação do projeto de Inteligência Artificial 2021/2022.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes já definidas, podem acrescentar outras que considerem pertinentes.

# Grupo 00:
# 00000 Nome1
# 00000 Nome2

import sys
from search import Problem, Node, astar_search, breadth_first_tree_search, depth_first_tree_search, greedy_search, recursive_best_first_search


class NumbrixState:
    state_id = 0

    def __init__(self, board):
        self.board = board
        self.id = NumbrixState.state_id
        NumbrixState.state_id += 1

    def __lt__(self, other):
        return self.id < other.id

    # TODO: outros metodos da classe


class Board:
    """ Representação interna de um tabuleiro de Numbrix. """

    def get_number(self, row: int, col: int) -> int:
        """ Devolve o valor na respetiva posição do tabuleiro. """
        return self.matrix[row][col]

    def adjacent_vertical_numbers(self, row: int, col: int) -> (int, int):
        """ Devolve os valores imediatamente abaixo e acima, 
        respectivamente. """
        if row-1 < 0:
            above = None
        else:
            above = self.matrix[row-1][col]

        if row+1 >= self.size:
            below = None
        else:
            below = self.matrix[row+1][col]
        return (below, above)

    def adjacent_horizontal_numbers(self, row: int, col: int) -> (int, int):
        """ Devolve os valores imediatamente à esquerda e à direita, 
        respectivamente. """
        if col-1 < 0:
            left = None
        else:
            left = self.matrix[row][col-1]

        if col+1 >= self.size:
            right = None
        else:
            right = self.matrix[row][col+1]
        return (left, right)

    @staticmethod
    def parse_instance(filename: str):
        """ Lê o ficheiro cujo caminho é passado como argumento e retorna
        uma instância da classe Board. """
        board = Board()
        with open(filename) as f:
            board.size = int(f.readline())
            board.matrix = [[int(num) for num in line.split(' ')]
                            for line in f]

        return board

    # TODO: outros metodos da classe
    def set_position(self, row: int, col: int, num: int):
        self.matrix[row][col] = num

    def copy_board(self):
        new_board = Board()
        new_board.size = self.size
        for r in range(self.size):
            for c in range(self.size):
                new_board.matrix[r][c] = self.matrix[r][c]
        return new_board


class Numbrix(Problem):
    state = None

    def __init__(self, board: Board):
        """ O construtor especifica o estado inicial. """
        self.state = NumbrixState(board)

    def actions(self, state: NumbrixState):
        """ Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento. """
        not_attributed = []
        actions_list = []
        for num in range(1, state.board.size * state.board.size + 1):
            if not any(num in sublist for sublist in state.board.matrix):
                not_attributed.append(num)
        for r in range(self.state.board.size):
            for c in range(self.state.board.size):
                if self.state.board.matrix[r][c] == 0:
                    for num in not_attributed:
                        actions_list.append((r, c, num))
        return actions_list

    def result(self, state: NumbrixState, action):
        """ Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de 
        self.actions(state). """
        if action not in self.actions(state):
            return
        return NumbrixState(state.board.copy_board().set_position(row=action[0], col=action[1], num=action[2]))

    def goal_test(self, state: NumbrixState):
        """ Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se todas as posições do tabuleiro 
        estão preenchidas com uma sequência de números adjacentes. """
        # TODO
        pass

    def h(self, node: Node):
        """ Função heuristica utilizada para a procura A*. """
        # TODO
        pass

    # TODO: outros metodos da classe


if __name__ == "__main__":
    # TODO:
    # Ler o ficheiro de input de sys.argv[1],
    board = Board.parse_instance(filename=sys.argv[1])
    numbrix = Numbrix(board=board)
    print(numbrix.state.board.matrix)
    print(numbrix.actions(numbrix.state))
    # Usar uma técnica de procura para resolver a instância,
    # Retirar a solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.
    pass
