for x in range(151):
    print(x)

for y in range(5, 1001):
    if y % 5 == 0:
        print(y)

for z in range(1, 101):
    if z % 10 == 0:
        print("Coding Dojo")
    elif z % 5 == 0:
        print("Coding")
    else:
        print(z)


suma_impares = 0

for a in range(1, 500000):
    if a % 2 == 1:
        suma_impares += a
        
print(suma_impares)


for b in range(2018, 0, -4):
    print(b)


lowNum = 2
highNum = 9
mult = 3

for x in range(lowNum, highNum+1):
    if(x % mult == 0):
        print(x)
    



            
        


