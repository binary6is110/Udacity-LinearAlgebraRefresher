import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
        
        except ValueError:
            raise ValueError('The coordinates must be nonempty')
        
        except TypeError:
            raise TypeError('The coordinates must be an iterable')


def __str__(self):
    return 'Vector: {}'.format(self.coordinates)
    
    def __eq__(self, v):
        return self.coordinates == v.coordinates
    # operation: add
    def plus (self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)
    # operation: minus
    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)
    # operation: multiply scalar
    def times_scalar(self,c):
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)
    
    # magnitude: calculates magnitude of vector
    def magnitude(self):
        new_coordinates = [ x*x for x in self.coordinates]
        sum=0
        for y in new_coordinates:
            sum+=y
        return math.sqrt(sum)
    
    # normalize: normalizes vector
    def normalize(self):
        try:
            magnitude=self.magnitude()
            return self.times_scalar(1./magnitude)
        except ZeroDivisionError:
            raise Exception("Unable to normalize a 0 vector")

#quiz 2
vector6=Vector([-0.221,7.437])
vector7=Vector([8.813,-1.331,-6.247])
print Vector.magnitude(vector6)
print Vector.magnitude(vector7)
vector8=Vector([5.581,-2.136])
mag8=Vector.magnitude(vector8)
print vector8.normalize()
vector9=Vector([1.996,3.108,-4.554])
mag9=Vector.magnitude(vector9)
print vector9.normalize()

