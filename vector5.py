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

    # projection:
    # normalize b,
    # take product of v * normalized b
    # projection = product (as scalar) by normalized b
    def projection (v,b):
        normalizedB = b.normalize()
        product = normalizedB.vTimesV(v)
        return normalizedB.times_scalar(product)
    
    # orthagonalVector:
    # return vector - projected vector
    def orthagonalVector (v,b):
        projectedVector=Vector.projection (v,b)
        return v.minus(projectedVector)

#quiz 5
p1_v = Vector([3.039,1.879])
p1_b = Vector([0.825, 2.036])
print "projection of p1_v on p1_b: %s" % Vector.projection(p1_v,p1_b)

p2_v = Vector([-9.88, -3.264,-8.159])
p2_b = Vector([-2.155,-9.353,-9.473])
print "orthagonalVector of p2_v on p2_b: %s" % Vector.orthagonalVector(p2_v,p2_b)

p3_v = Vector([3.009,-6.172, 3.692,-2.51])
p3_b = Vector([6.404,-9.144, 2.759,8.718])
p3_projection=Vector.projection(p3_v,p3_b)
print "projection of p3_v on p3_b: %s" % p3_projection
print "orthagonalVector of p3_projection: %s" % Vector.orthagonalVector(p3_v,p3_b)