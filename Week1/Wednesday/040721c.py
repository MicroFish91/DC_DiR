# Ran through problem for student

# 1 star 3 spaces on each side
# 3 stars 2 spaces on each side
# 5 stars 1 space on each side
# 7 stars 0 spaces each side

# each row increments by 2

for x in range(1, 8, 2):
    print(("*" * x).center(7))