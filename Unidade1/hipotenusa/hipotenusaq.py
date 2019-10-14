import math

#UFCG
#Programação
#Amanda Moreno
#Cálculo da Hipotenusa

cateto1 = float(input("Medida do Cateto 1? "))
cateto2 = float(input("Medida do Cateto 2? "))

hipotenusa_q  = cateto1**2 + cateto2**2
hipotenusa = math.sqrt( hipotenusa_q)

print("Medida da Hipotenusa: %.2f"%(hipotenusa**2))
