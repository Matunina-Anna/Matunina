def create_spiral(n):
    if n < 1 or not isinstance(n, int):
        return []

    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        matrix.append(row)

    top = 0           
    bottom = n - 1    
    left = 0         
    right = n - 1     
    num = 1           

    while num <= n * n:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1  


        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1  


        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1 


        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1  

    return matrix
