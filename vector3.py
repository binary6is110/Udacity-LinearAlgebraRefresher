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

    # vTimesV: vector * vector
    def vTimesV(self, v):
        new_coordinates = [x*y for x,y in zip(self.coordinates, v.coordinates)]
        numerator=0
        for y in new_coordinates:
            numerator+=y
        return numerator

    # dotProd: solves dotProduct of 2 vectors.
    # multiplies one vector by another and adds values for numerator
    # multiplies magnitude of vector a by vector b for divisor
    # checks for 0 divisor, returns 0
    # returns arccos for dot product, rounded to 3 pts
    def dotProd(self, v):
        numerator = self.vTimesV(v)
        divisor = self.magnitude() * v.magnitude()
        if divisor==0:
            return 0
        val=numerator/divisor
        return math.acos(val)

    # dotProdDegrees: solves dotProduct of 2 vectors.
    # multiplies one vector by another and adds values for numerator
    # multiplies magnitude of vector a by vector b for divisor
    # checks for 0 divisor, returns 0
    # returns dot product in degrees
    def dotProdDegrees(self, v):
        numerator = self.vTimesV(v)
        divisor = self.magnitude() * v.magnitude()
        if divisor == 0:
            return 0;
        val=(numerator/divisor)
        print "val %s" %val
        res = math.acos(val)* 180 / math.pi
        return math.round(res,3)

#quiz 3
v =Vector ([7.887,4.138])
w =Vector ([-8.802,6.776])
vw1 = v.vTimesV(w)
print "vw1 %s" % round(vw1,3)
v2 =Vector ([-5.955,-4.904,-1.874])
w2=Vector ([-4.496,-8.755,7.103])
vw2 = v2.vTimesV(w2)
print "vw2 %s" % round(vw2,3)
v3 =Vector ([3.183,-7.627])
w3=Vector ([-2.668,5.319])
v3w3Degrees = v3.dotProd(w3)
print "v3w3Degrees %s" % round(v3w3Degrees,3)
v4 =Vector ([7.35,0.221,5.188])
w4= Vector ([2.751,8.259,3.985])
v4w4Degrees = v4.dotProdDegrees(w4)
print "v4w4Degrees %s" % round(v4w4Degrees,3)


