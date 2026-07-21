class MutableWithImmutable:
    def __init__(self):
        self.dd = "Shahbaz"


    def add(self, val):
        print(f"earlier id of self.dd was {id(self.dd)}")
        self.dd = self.dd + val
        print(f"new id of self.dd is {id(self.dd)}")
    

r = MutableWithImmutable()

r.add(" Khan")
