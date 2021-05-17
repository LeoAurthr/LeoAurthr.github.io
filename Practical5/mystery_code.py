# What does this piece of code do?
# Answer:get a random number from 1 to 100 until the random number is less than 50, and output it.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5


p=False
while p==False:
    p = True 
    n = randint(1,100)
    if n > 50:
        p = False

print(n)
