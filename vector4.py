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
        res =math.acos(val)* 180 / math.pi
        return res

    # isOrthogonal: solves dotProduct of 2 vectors.
    # true if either vector is 0 vector or if the product is 90 degrees
    def isOrthogonal (v1, v2):
        ninetyDProd= v1.dotProdDegrees(v2)==90.0
        zeroVectorV1= v1.vTimesV(v1)==0
        zeroVectorV2=v2.vTimesV(v2)==0
        return ninetyDProd or zeroVectorV2 or zeroVectorV1

    # isParallel: solves dotProduct of 2 vectors.
    # true if dotproduct is 0 or 180 degrees (parallel lines)
    def isParallel (self, v):
        dProdDegress= self.dotProdDegrees(v)
        return dProdDegress==0 or dProdDegress== 180


#quiz 4
v5 =Vector ([-7.579,-7.88])
w5 =Vector ([22.737,23.64])
v5w5Degrees = v5.dotProdDegrees(w5)
print "v5w5 is orthogonal: %s" %v5.isOrthogonal(w5)
print "v5w5 is isParallel: %s" %v5.isParallel((w5))

v6 =Vector ([-2.029,9.97,4.172])
w6 =Vector ([-9.231,-6.639,-7.245])
v6w6Degrees = v6.dotProdDegrees(w6)
print "v6w6 is orthogonal: %s" %Vector.isOrthogonal(v6,w6)
print "v6w6 is isParallel: %s" %v6.isParallel((w6))

v7 =Vector ([-2.328,-7.284,-1.214])
w7 =Vector ([-1.821,1.072,-2.94])
v7w7Degrees = v7.dotProdDegrees(w7)
print "v7w7 is orthogonal: %s" %Vector.isOrthogonal(v7,w7)
print "v7w7 is isParallel: %s" %v7.isParallel((w7))

v8 =Vector ([2.118,4.827])
w8 =Vector ([0,0])
v8w8Degrees = v8.dotProdDegrees(w8)
print "v8w8 is orthogonal: %s" %Vector.isOrthogonal(v8,w8)
print "v8w8 is isParallel: %s" %v8.isParallel(w8)



