"Programa para saber cuantos rebotes da una pelota :v"

print("""-----------------------------------------""")
print("""-----------rebotes de la pelota----------""")
print("""-----------------------------------------""")

#input 

h = int(input("Digite la altura a la que se lanzo la pelota: ")) 
a = h / 5
n = int(0) 
b = h - (h*0.10) 

#processing

while h > a:
    h = h - b
    n = n + 1

#output

print("el numero de veces que rebota la pelota es ")