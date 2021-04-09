# Make a clock
# Hours, Minutes, Seconds
# Minutes in an hour (60)
# Seconds in a minute (60)

# for hour in range(1, 24):
#     for minute in range(1, 60):
#         for second in range(1, 60);
#             print(f'')


# 3D - Length, Width, Height

# matrixOne = [[1, 3], [2, 4]] 
# matrixTwo = [[5, 2], [1, 0]]
# matrixSum = []

# # 2x2
# matrixSum = []

# # matrixOne[0][0] + matrixTwo[0][0]
# # [0][0] + [0][0] = 1 + 5 = 6
# # [0][1] + [0][1] = 3 + 2 = 5
# # [1][0] + [1][0] = 2 + 1 = 3
# # [1][1] + [1][1] = 4 + 0 = 4

# for indexOne in range(2): 
#     matrixThree = []
#     for indexTwo in range(2): 
#         matrixThree.append(matrixOne[indexOne][indexTwo] + matrixTwo[indexOne][indexTwo])

#         # matrixThree = [3, 4]
#     matrixSum.append(matrixThree)
#     # matrixSum = [[6, 5], [3, 4]]

# print(matrixSum)

for x in range(2):
    for y in range(2):
        print(f'X: {x}, Y: {y}')