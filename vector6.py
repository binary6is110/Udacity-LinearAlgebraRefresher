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

    def crossProduct (v, w):
        x1=v.coordinates[0]
        y1=v.coordinates[1]
        z1=0
        if(v.dimension==3):
            z1=v.coordinates[2]
        print "x1 %s " %x1
        print "y1 %s " %y1
        print "z1 %s" %z1
        x2=w.coordinates[0]
        y2=w.coordinates[1]
        z2=0
        if(w.dimension==3):
            z2=w.coordinates[2]
        print "x2 %s " %x2
        print "y2 %s " %y2
        print "z2 %s" %z2
        x=(y1*z2) - (y2*z1)
        y= -((x1*z2) - (x2*z1))
        z= (x1*y2)-(x2*y1)
        return Vector([ x, y, z])
    
    def parallelogramArea (v,w):
        vector = Vector.crossProduct(v,w)
        x1=vector.coordinates[0]
        y1=vector.coordinates[1]
        z1=0
        if(vector.dimension==3):
            z1=vector.coordinates[2]
        return math.sqrt(x1*x1 + y1*y1 + z1*z1)

#quiz 6
cp1_v = Vector([8.462,7.893,-8.187])
cp1_w = Vector([6.984, -5.975, 4.778])
print "cross product cp1_v x cp1_w: %s" %Vector.crossProduct(cp1_v,cp1_w)

cp2_v = Vector([-8.987,-9.838,5.031])
cp2_w = Vector([-4.268,-1.861,-8.866])
print "parallelogramArea cp2_v x cp2_w: %s" %Vector.parallelogramArea(cp2_v,cp2_w)

cp3_v = Vector([1.5,9.547,3.691])
cp3_w = Vector([-6.007,0.124,5.772])
area=Vector.parallelogramArea(cp3_v,cp3_w) * .5
print "area of triangle by vectors: cp3_v x cp3_w: %s" %area