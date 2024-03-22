from board import Board

b = Board()

keep_going = True

while keep_going:
    b.reset_board()
    b.print()
    while not b.winner:
        b.next_move()
        b.print()

    if b.winner == 'DRAW':
        print("A draw!")
    else:
        print(f"Winner!: Player {b.winner}!")

    keep_going = input("Another round? (y/n): ").lower() == 'y'


