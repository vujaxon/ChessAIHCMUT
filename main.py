import argparse
from frontend.game import GameFrontEnd
from logic.game import GameController
from logic.attributes import Turn, GameState, QueenPromote, EnterTower
from algorithms.heuristic import Heuristic
from algorithms.searchAlgo import MinMaxAlgo

def main():
  parser = argparse.ArgumentParser(description='Mode games.')
  parser.add_argument("-m", '--mode', choices=['personvspersion', 'personvsagent', 'agentvsagent'], default='personvsagent', help='Specify mode game to run')
  args = parser.parse_args()
  
  game = GameFrontEnd()
  game.setUpPlayer(args.mode)
  game.printInfoBoard()
  game.play()
  # board = [
  #   ['','','','','bK','bP','',''],
  #   ['', '','','','bP','bP','',''],
  #   ['','wR','','','','','',''],
  #   ['','','','','','','',''],
  #   ['','','','','','','',''],
  #   ['','','','','','','',''],
  #   ['', '','','','','','',''],
  #   ['', '','wB','','wK','','',''],
  # ]
  # turn = Turn.WHITE

  # gs = GameState(board, turn)
  # # eval_value = Heuristic.eval(gs)
  # # print(eval_value)
  # gc = GameController()
  # search_algo = MinMaxAlgo()
  # move = search_algo.searchMove(gs)
  # print(f"{move.pos} {move.tar}")
  # hello = gc.isTerminal(gs)
  # print(hello)
  # gc.checkValidMove(gs, EnterTower((0,4),(0,2),(0,0),(0,3)))

if __name__ == '__main__':
  main()


