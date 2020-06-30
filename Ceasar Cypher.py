# -*- coding: cp1252 -*-
# ceasar cipher is the simplest form of a cipher , 
#its not very secure,but as a basic i am giving a code which can help you to transform it,
#also i am giving how it works
#This cryptosystem is generally referred to as the Shift Cipher.
#The concept is to replace each alphabet by another alphabet which is ‘shifted’ by some fixed number between 0 and 25.
#which is called the key.
#here is the code
def ceasar(text,key):
    # here text is yor plain text
    #key is the number
    u=""
    #its an empty veriable to store the ciphered text
    def greaterA(number):
        #if the number exceeds 90 then it is called
        while number>90:
            v=number-90
            number=64+v
        return number
    def greatera(num):
        #if the number exceeds 122 then it is called
        while num > 122:
            z=num-122
            num=96+z
        return num
    for x in text:
        if ord(x)>64 and ord(x)<91:
            y=ord(x)+key
            if y>90:
                y=greaterA(y)
                x=chr(y)
                u=u + x
            else:
                x=chr(y)
                u=u + x
        elif ord(x)>96 and ord(x)<123:
            y=ord(x)+key
            if y > 122:
                y = greatera(y)
                x=chr(y)
                u=u + x
            else:
                x=chr(y)
                u = u + x
        else:
            x=x
            u =u + x
            
    return u

        
    
        
    
        

