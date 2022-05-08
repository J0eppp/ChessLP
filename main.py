from chess.Chess import Chess


if __name__ == "__main__":
    chess = Chess()
    print(chess.board)

    while True:
        start = input("From: ")
        to = input("To: ")

        start = chess.board.translate_position(start)
        to = chess.board.translate_position(to)

        if start == None or to == None:
            continue
