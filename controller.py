import random
from Player import Player
from Game import Game
from Board import Board


game = None
board = None
players = None
currentPlayer = None


def newGame():
    global game, board, players, currentPlayer
    game = Game()
    board = Board()
    players = [ Player("Shane", "Blue", 0), Player("Caden", "Red", 1) ]
    currentPlayer = random.choice(players)
    print(board)
    print(str(currentPlayer) + " turn...")
    return [ game, board, players, currentPlayer ]


def playBead(position):
    global game, board, players, currentPlayer
    board.playBead(currentPlayer, position)
    game.beadsPlayed += 1

    # TODO: Update game/players if winning patterns found
    print("Finding winning patterns")
    print(currentPlayer)
    winningPatterns = board.findWinningPatterns(currentPlayer)
    if winningPatterns != []:
        game.winner = True

    if currentPlayer.jumps >= 5:
        game.winner = True

    # TODO: Update game/players if jump patterns found
    # TODO: If jumps exist, remove opponent beads

    print("Finding Jump patterns", position, currentPlayer)
    jumps, positionsFound = board.findJumpPatterns(currentPlayer, position)

    if jumps != []:
        currentPlayer.jumps += len(jumps)
        if jumps[len(jumps) - 1]["pattern"]["name"] == "Jump":
            board.removeFromBoard(jumps[0]["positions"][1])
            board.removeFromBoard(jumps[0]["positions"][0])
        positionsFound = jumps[0]["positions"]

    # TODO: Process announce patterns
    print("Finding announce patterns")
    board.findPatternsToAnnounce(currentPlayer)

    # TODO: Update game/player with scores
    scorePatterns = board.findScorePatterns(currentPlayer)

    print(board)
    print(str(currentPlayer) + " played at " + str(position["column"]) + ", " + str(position["row"]));



    __nextPlayer()

    # TODO: Process announce patterns
    board.findPatternsToAnnounce(currentPlayer)

    # TODO: Update game/player with scores
    scorePatterns = board.findScorePatterns(currentPlayer)

    print(str(currentPlayer) + " turn...")
    print(positionsFound)
    return game, board, players, currentPlayer, positionsFound


def __nextPlayer():
    global game, board, players, currentPlayer
    if currentPlayer.key == 0:
        currentPlayer = players[1]
    else:
        currentPlayer = players[0]
