class Mutable:
    def __init__(self):
        self.a = [1, 2, 3]

w = Mutable()
print(w.a)

w.a.append(19)
print(w.a)