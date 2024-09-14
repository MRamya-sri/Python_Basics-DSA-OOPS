vertex_Data = ['A', 'B', 'C', 'D']

adjacent_Matrix = [
    [0,1,1,1],
    [1,0,1,0],
    [1,1,0,0],
    [1,0,0,0]
]

def print_Adjacent_Matrix(matrix):
    print("Adjacency Matrix: ")
    for row in matrix:
        print(row)

print('Vertex Data: ', vertex_Data)
print_Adjacent_Matrix(adjacent_Matrix)