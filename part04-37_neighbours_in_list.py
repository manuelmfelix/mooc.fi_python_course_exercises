# Write your solution here
def longest_series_of_neighbours(a: list):
    b = 0
    d = 0
    c = [a[d]]
    e = 0
    # print(c)
    # print(a[d])
    # print(a[d+1])
    # print(abs(a[d]-a[d+1]))
    while d < len(a)-1:
        if abs(a[d]-a[d+1]) == 1:
            c.append(a[d+1])
            b = len(c)
            if b > e:
                e = b
        else:
            c = []
            c.append(a[d])
        d += 1
    return e


if __name__ == "__main__":
    my_list = [0, 2, 4, 5, 6, 7, 10, 11, 12, 100, 101]
    print(longest_series_of_neighbours(my_list))