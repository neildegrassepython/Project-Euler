# Find the sum of every multiple of 3 or 5 under 1000

multiples = []

for i in range (0, 1000):
    if i % 3 == 0 or i % 5 == 0:
        multiples.append(i)

print(sum(multiples))
