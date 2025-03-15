import math


class Vector:
    def __init__(self, *components):
        if not components:
            raise ValueError("A vector must have at least one component.")
        self.components = list(components)

    def show(self):
        return f"Vector{tuple(self.components)}"

    def add(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for addition.")
        result = [a + b for a, b in zip(self.components, other.components)]
        return Vector(*result)

    def subtract(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for subtraction.")
        result = [a - b for a, b in zip(self.components, other.components)]
        return Vector(*result)

    def dot_product(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for dot product.")
        return sum(a * b for a, b in zip(self.components, other.components))

    def scalar_multiply(self, scalar):
        result = [a * scalar for a in self.components]
        return Vector(*result)

    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        result = [a / mag for a in self.components]
        return Vector(*result)


