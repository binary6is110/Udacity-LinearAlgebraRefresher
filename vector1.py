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
#quiz 1
vector1=Vector([8.218,-9.341])
vector2=Vector([-1.129,2.111])
print vector1.plus(vector2)
vector3=Vector([7.119,8.215])
vector4=Vector([-8.223,0.878])
print vector3.minus(vector4)
vector5=Vector([1.671,-1.012,-0.318])
c = 7.41
print vector5.times_scalar(c)