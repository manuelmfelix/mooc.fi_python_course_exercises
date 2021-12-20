# Write your solution here
def create_tuple(x: int, y: int, z: int):
    a = min(x,y,z)
    b = max(x,y,z)
    c = x+y+z
    d = (a,b,c)
    return d



if __name__ == "__main__":
    print(create_tuple(5, 3, -1))