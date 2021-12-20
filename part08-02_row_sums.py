# Write your solution here
def row_sums(my_matrix: list):
    for a in my_matrix:
        b = sum(a)
        a.append(b)
        
    

if __name__ == "__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)
