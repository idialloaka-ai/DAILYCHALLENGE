

#  Daily Challenge 



class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            self.radius = 1
    @property
    def diameter(self):
        return self.radius * 2
    @property
    def area(self):
        return math.pi * (self.radius ** 2)
    def __str__(self):
        return (
            f"Circle(radius={self.radius}, "
            f"diameter={self.diameter:.2f}, "
            f"area={self.area:.2f})"
        )
    def __add__(self, other):
        new_radius = self.radius + other.radius
        return Circle(radius=new_radius)
    def __gt__(self, other):
        return self.radius > other.radius
    def __eq__(self, other):
        return self.radius == other.radius
    def __lt__(self, other):
        return self.radius < other.radius
        #
        #
        ## Création des cercles
c1 = Circle(radius=5)
c2 = Circle(diameter=8)
c3 = Circle(radius=2)

# Affichage
print(c1)
print(c2)
print(c3)
# Aire
print("\nAire du cercle 1 :", c1.area)
# Addition
c4 = c1 + c2
print("\nNouveau cercle après addition :")
print(c4)
# Comparaison
print("\nC1 > C2 :", c1 > c2)
print("C1 == C2 :", c1 == c2)
# Tri des cercles
circles = [c1, c2, c3, c4]
circles.sort()
print("\nCercles triés :")
for circle in circles:
    print(circle)


