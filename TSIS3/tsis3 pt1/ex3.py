def solve(numheads, numlegs):
    n_chickens = 0
    n_rabbits = 0

    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        total_legs = (chickens * 2) + (rabbits * 4)
        if total_legs == numlegs:
            n_chickens = chickens
            n_rabbits = rabbits
            break
        return n_chickens, n_rabbits

numheads = input() 
numlegs = input()
chickens, rabbits = solve(numheads, numlegs)
print(chickens)
print(rabbits)
