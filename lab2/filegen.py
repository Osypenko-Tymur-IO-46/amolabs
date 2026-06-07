import random
 
def generate():
    for i in range(1, 11):
        count = i * 1000
        numbers = [random.randint(-10000, 10000) for j in range(count)]
        filename = f"numbers_{count}.txt"
        with open(filename, "w") as f:
            f.write(" ".join(map(str, numbers)))


