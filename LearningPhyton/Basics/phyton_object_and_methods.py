class AreaRect:

    def __init__(self, l, b):
        self.l = l
        self.b = b
   #methods
    def calculate_area(self):
        return self.l * self.b

#object
area1 = AreaRect(10,8)
area2 = AreaRect(100,90)

print(area1.calculate_area())