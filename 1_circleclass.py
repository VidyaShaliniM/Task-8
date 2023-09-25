class Circle:
    _pi = 3.141

    def __init__(self, data_list):
        if len(data_list) > 0:
            self.radius = nl[0]
        else:
            self.radius = 0

    def area(self, radius):
        return self._pi * radius * radius

    def perimeter(self, radius):
        return 2 * self._pi * radius


nl = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(nl)

r = circle.radius
circle_area = circle.area(r)
circle_perimeter = circle.perimeter(r)
print(f"Circle radius: {r}")
print(f"Circle area: {circle_area}")
print(f"Circle area: {circle_perimeter}")
