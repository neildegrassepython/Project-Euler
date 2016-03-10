# Script to find the sum of all even numbers in the fibonacci sequence
# under 4,000,000

fib_seq = [0, 1] # The Sequence
fib_sum = 0 # The end goal!

while fib_seq[-1] < 4000000:
    fib_seq.append(fib_seq[-1] + fib_seq[-2])

for i in range(0, len(fib_seq)):
    if fib_seq[i] % 2 == 0: # If it divides by two with no remainder it gets added
        fib_sum += fib_seq[i]

print(fib_sum) # Correct!
