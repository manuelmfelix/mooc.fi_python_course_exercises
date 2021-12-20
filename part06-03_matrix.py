# write your solution here
def matrix_sum():
    with open("matrix.txt") as new_file:
        sum = 0
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(",")
            for a in parts:
                sum += int(a)
        return sum

def matrix_max():
    with open("matrix.txt") as new_file:
        max = 0
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(",")
            for a in parts:
                if max < int(a):
                    max = int(a)
        return max


def row_sums():
    with open("matrix.txt") as new_file:
        rowsum = []
        for line in new_file:
            sum = 0
            line = line.replace("\n", "")
            parts = line.split(",")
            for a in parts:
                sum += int(a)
            rowsum.append(sum)
        return rowsum

if __name__ == "__main__":
    print(matrix_max())
    print(matrix_sum())
    print(row_sums())