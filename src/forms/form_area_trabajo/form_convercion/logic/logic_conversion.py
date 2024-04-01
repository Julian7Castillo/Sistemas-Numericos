    
def calConversion(sisInicial, n, sisFinal):  
    
    print(sisInicial)
    print(n)
    print(sisFinal)
    
    #si el sistenma inicial es binario
    if(sisInicial == "Binario"):
        if(sisFinal == "Octal"):
            r1 = int(n, 2)
            r = oct(r1)
            return r[2::]
            
        elif(sisFinal == "Decimal"):
            r = int(n, 2)
            return r 
            
        elif(sisFinal == "Haxadecimal"):
            r1 = int(n, 2)
            r = hex(r1)
            return r [2::]
        
        else:
            print("Digite un sistema numerico diferente")
        
    #si el sistenma inicial es octal
    elif(sisInicial == "Octal"):
        if(sisFinal == "Binario"):
            r1 = int(n, 8)
            r = bin(r1)
            return r [2::]
            
        elif(sisFinal == "Decimal"):
            r1 = int(n, 8)
            r = int(r1)
            return r
            
        elif(sisFinal == "Haxadecimal"):
            r1 = int(n, 8)
            r = hex(r1)
            return r [2::]
        else:
            print("Digite un sistema nuemrtico diferente")
        
    #si el sistenma inicial es decimal
    elif(sisInicial == "Decimal"):
        if(sisFinal == "Binario"):
            r = bin(n)
            return r[2::]
            
        elif(sisFinal == "Octal"):
            r = oct(n)
            return r[2::]
            
        elif(sisFinal == "Haxadecimal"):
            r = hex(n)
            return r[2::]
        else:
            print("Digite un sistema nuemrtico diferente")
        
    #si el sistenma inicial es hexadecimal
    elif(sisInicial == "Haxadecimal"):
        if(sisFinal == "Binario"):
            r1 = int(n, 16)
            r = bin(r1)
            return r [2::]
            
        elif(sisFinal == "Octal"):
            r1 = int(n, 16)
            r = oct(r1)
            return r [2::]
            
        elif(sisFinal == "Decimal"):
            r = int(n, 16)
            return r
        else:
            print("Digite un sistema nuemrtico diferente")
        
    # bandera de valor resultante 
    #print(r)