from numbers import Number
class Circle:
    def __init__(self, c, r):
        if not (isinstance(c,(list,tuple)) or len(c)!=2):
            raise ValueError
        if not isinstance(r,Number):
            raise ValueError
        self.centre = c
        self.radius = r
    
    def __contains__(self,other):
        c = self.centre
        distance = ((c[0]-other[0])**2 + (c[1]-other[1])**2)**0.5
        return distance<self.radius

        

