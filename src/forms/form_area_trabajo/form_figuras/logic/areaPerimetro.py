
PI = 3,1416

def CalcularResultado(fig, l1, l2, l3):
    if(fig == 0):
        perimetro = l1+l2+l1+l2
        area = l1*l2 
        
    elif(fig == 1):
        perimetro = l1+l2+l1
        area =  (l1*l2)/2
        
    elif(fig == 2):
        perimetro = l1+l2+l1+l2
        area = l1*l2 
    
    elif(fig == 3):
        perimetro = PI * l1
        area = (PI * (l2**2))
        
    elif(fig == 4):
        perimetro = l1+l2+l3+l2
        area = (l1(l1 + l3))/2
        
    return area, perimetro