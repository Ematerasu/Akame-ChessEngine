from Akame import Akame
import chess

if __name__ == "__main__":
    print("pick side (white/black):")
    color = False if input() == "white" else True
    print("pick depth: ", end="", flush=True)
    depth = input()
    akame = Akame.Akame(color)
    board = chess.Board()

    if color:
        akame_move = akame.move(board, depth)
        print(f"Akame's move: {akame_move}")
        board.push(akame_move)

    while not board.is_game_over():
        print(board.legal_moves)
        print(board)
        try:
            move = board.parse_san(input())
            if move in board.legal_moves:
                board.push(move)
        except KeyboardInterrupt:
            print("Keyboard interrupt")
            exit(0)
        except:
            print("Illegal move!")
            continue
        
        if board.is_game_over():
            break
        if board.is_repetition():
            break
        akame_move = akame.move(board, depth)
        print(f"Akame's move: {akame_move}")
        board.push(akame_move)
    print(board.result())
    if akame.akame_won():
        print("Akame win!")
    else:
        print("You win!")