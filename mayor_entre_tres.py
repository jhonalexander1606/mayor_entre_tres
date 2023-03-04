# programa que identifica el numero mayor entre tres

print("--------------------------")
print("----mayor entre tres------")
print("--------------------------")


#input

print("inserte un numero")
n1 = int(input("numero 1: " ))
n2 = int(input("numero 2: " ))
n3 = int(input("numero 3: " ))


#processing

if n1 > n2 and n1 > n3:
#output
    print("el numero" , n1, "es mayor que" , n2, "y que" , n3, )
#output
elif n2 > n1 and n2 > n3: 
    print("el numero" , n2, "es mayor que" , n3, "y que" , n1, )
#output
else:   
    print("el numero" , n3, "es mayor que" , n2, "y que" , n1, )

