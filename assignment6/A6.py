import random

N = int(input("How many random points to generate? "))
n = 0

for i in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    distance = x**2 + y**2
    
    if distance < 1:
        n = n + 1

pi_approx = 4 * n / N
print(pi_approx)