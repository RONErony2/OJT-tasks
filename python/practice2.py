class count:
    def __init__(self):
        self.c = 0
    def __iter__(self):
        return self
    
    def __next__(self):
        self.c += 1
        return self.c
x = count()

if __name__ == "__main__":
    print(dir(x))
    print(next(x))
    print(next(x))
    print(next(x))

