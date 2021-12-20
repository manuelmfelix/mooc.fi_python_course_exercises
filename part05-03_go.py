# Write your solution here
def who_won(game_board: list):
    a1=0
    a2=0
    b=0
    for row in game_board:
        for a in row:
            if a == 1:
                a1 += 1
            elif a == 2:
                a2 += 1
    if a1>a2:
        b=1
    elif a1<a2:
        b=2
    return b

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 0, 1], [2, 1, 0]]
    print(who_won(m))