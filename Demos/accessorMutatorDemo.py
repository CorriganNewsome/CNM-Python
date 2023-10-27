class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def set_size(self, size):
        self.width, self.height = size

    def get_size(self):
        return (self.width, self.height)

    size = property(get_size, set_size)


r1 = Rectangle()


r2 = Rectangle()
r2.size = 200, 100
print(r2.size)
