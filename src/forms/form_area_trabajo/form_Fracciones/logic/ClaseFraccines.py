class Fraccion:

    #comntructor
    def __init__(self, num=0, den=1):
        if isinstance(num, int):
            self.num=num
        else:
            self.num = 0
        if isinstance(den, int) and den!=0:
            self.den=den
        else:
            self.den = 1
            
        self.simplificar()
    
    #imprersion
    def __str__(self):
        return "{"+ str(self.num) + "/" + str(self.den) +"}"

    #Eliminacion
    #def __del__(self):
        #print("Destruyendo el objeto ", self.num,"/",self.den)
    
    #multiplcacion
    def __mul__(self, b):
        n = self.num * b.num
        d = self.den * b.den
        r = Fraccion(n,d)
        r.simplificar()
        return r
    
    #division
    def __truediv__(self, b):
        n = self.num * b.den
        d = self.den * b.num
        r = Fraccion(n,d)
        r.simplificar()
        return r
    
    #suma
    def __add__(self, b):
        n = self.num * b.den + self.den * b.num
        d = self.den * b.den
        r = Fraccion(n,d)
        r.simplificar()
        return r
    
    #resta
    def __sub__(self, b):
        n = self.num * b.den - self.den * b.num
        d = self.den * b.den
        r = Fraccion(n,d)
        r.simplificar()
        return r
    
    #igualdad}
    def __eq__(self,b):
        if self.num/self.den == b.num/b.den:
            return True
        else:
            return False
        
    #simplificacion
    def simplificar(self):
        
        #mcd maximo como un divisor (funcion en capsulada por que no se usa en nunguna otra parte)
        def mcd(a,b):
            if b == 0:
                return a
            else:
                return mcd(b,a%b)
            
        d = mcd(self.num,self.den)
        self.num = int(self.num/d)
        self.den = int(self.den/d)
