def spiral(n):
    matrix = [[0]*n for _ in range(n)]
    top, bottom = 0, len(matrix)-1 
    left, right = 0, len(matrix[0])-1
    num = 1

    while top <= bottom and left <= right:
        #top row(forward)
        for col in range(left, right+1):
            matrix[top][col] = num
            num += 1      
        top += 1

        #right column(downward)
        for row in range(top, bottom+1):
            matrix[row][right] = num
            num += 1
        right -= 1

        #bottom row(reverse)
        if top <= bottom:
            for col in range(right, left-1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1
        #left column(upward)
        if left <= right:
            for row in range(bottom, top-1, -1):
                matrix[row][left] = num
                num += 1
            left += 1
    
    for i in range(n):
        print(matrix[i])

spiral(5)