from src.util.fracciones.ClaseFraccines import Fraccion

class FracMix(Fraccion):

    #comntructor
    def __init__(self, ent, num=0, den=1):
        self.ent = ent
        super().__init__(num,den)
        self.simplificar()
        super().simplificar()
    
    #imprersion
    def __str__(self):
        return str(self.ent) + super().__str__() + "\n"
  
    #simplificacion
    def simplificar(self):
        if self.num > self.den:
            aux = self.num//self.den
            self.ent = self.ent+aux
            self.num-=(aux*self.den)
    
    def toFraccion(self):
        n, d = self.num, self.den
        if self.ent != 0:
            n = (self.ent * d) + n
        f = Fraccion(n,d)
        return f
    
    def __add__(self, obj):
        r = self.toFraccion() + obj.toFraccion()
        r = FracMix(0, r.num, r.den)
        r.simplificar()
        return r
    
    def __sub__(self, obj):
        r = self.toFraccion() - obj.toFraccion()
        r = FracMix(0, r.num, r.den)
        r.simplificar()
        return r
    
    def __mul__(self, obj):
        r = self.toFraccion() * obj.toFraccion()
        r = FracMix(0, r.num, r.den)
        r.simplificar()
        return r
    
    def __truediv__(self, obj):
        r = self.toFraccion() / obj.toFraccion()
        r = FracMix(0, r.num, r.den)
        r.simplificar()
        return r
    
    #igualdad}
    def __eq__(self,b):
        if self.toFraccion() == b.toFraccion():
            return True
        else:
            return False