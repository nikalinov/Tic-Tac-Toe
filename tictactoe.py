def main():

    s = "_________"

    print(f"""
    ---------
    | {s[0]} {s[1]} {s[2]} |
    | {s[3]} {s[4]} {s[5]} |
    | {s[6]} {s[7]} {s[8]} |
    ---------""")

    state, player = "Game not finished", "X"

    while state == "Game not finished":

        is_valid = False
        row, col = -1, -1

        # Forces the user to input a valid cell index
        while not is_valid:
            row, col = input().split(" ")
            try:
                row, col = int(row), int(col)
            except ValueError:
                print("You should enter numbers!")
                continue
            if not (1 <= row <= 3 and 1 <= col <= 3):
                print("Coordinates should be from 1 to 3!")
                continue
            row -= 1
            col -= 1
            if s[row * 3 + col] != "_":
                print("This cell is occupied! Choose another one!")
            else:
                is_valid = True

        i = row * 3 + col
        s = s[:i] + player + s[i + 1:]
        player = "O" if player == "X" else "X"

        print(f"""
        ---------
        | {s[0]} {s[1]} {s[2]} |
        | {s[3]} {s[4]} {s[5]} |
        | {s[6]} {s[7]} {s[8]} |
        ---------""")

        ls = [s[0:3], s[3:6], s[6:9], s[0] + s[3] + s[6], s[1] + s[4] + s[7],
              s[2] + s[5] + s[8], s[0] + s[4] + s[8], s[6] + s[4] + s[2]]

        if "_" not in s and "XXX" not in ls and "OOO" not in ls:
            state = "Draw"
        elif "_" in s and "XXX" not in ls and "OOO" not in ls:
            state = "Game not finished"
        elif "XXX" in ls:
            state = "X wins"
        elif "OOO" in ls:
            state = "O wins"
        print(state)


if __name__ == "__main__":
    main()
