    
def calConversion(sisInicial, n, sisFinal):  
    
    print(sisInicial)
    print(n)
    print(sisFinal)
    
    #si el sistenma inicial es binario
    if(sisInicial == "Binario"):
        if(sisFinal == "Octal"):
            r = oct(n)
            return r
            
        elif(sisFinal == "Decimal"):
            r = int(n, 2)
            return r
            
        elif(sisFinal == "Haxadecimal"):
            r = hex(n)
            return r
        
        else:
            print("Digite un sistema nuemrtico diferente")
        
    #si el sistenma inicial es octal
    elif(sisInicial == "Octal"):
        if(sisFinal == "Binario"):
            r = bin(n)
            return r
            
        elif(sisFinal == "Decimal"):
            r = int(n, 8)
            return r
            
        elif(sisFinal == "Haxadecimal"):
            r = hex(n)
            return r
        else:
            print("Digite un sistema nuemrtico diferente")
        
            
    #si el sistenma inicial es decimal
    elif(sisInicial == "Decimal"):
        if(sisFinal == "Binario"):
            r = bin(n)
            return r
            
        elif(sisFinal == "Octal"):
            r = oct(n)
            return r
            
        elif(sisFinal == "Haxadecimal"):
            r = hex(n)
            return r
        else:
            print("Digite un sistema nuemrtico diferente")
        
            
    #si el sistenma inicial es hexadecimal
    elif(sisInicial == "Haxadecimal"):
        if(sisFinal == "Binario"):
            r = bin(n)
            return r
            
        elif(sisFinal == "Octal"):
            r = oct(n)
            return r
            
        elif(sisFinal == "Decimal"):
            r = int(n, 16)
            return r
        else:
            print("Digite un sistema nuemrtico diferente")
        
    # bandera de valor resultante 
    #print(r)