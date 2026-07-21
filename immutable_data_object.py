class Immutable:
    def __init__(self):
        self.b = "Shahbaz"

x = Immutable()
print(x.b)

x.b = "Ali"

print(x.b)