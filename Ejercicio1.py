Num1 = int (input("ingrese por favor el primer numero: \n"))
Num2 = int (input("Ingrese por favor el segundo numero: \n"))
Num3 = int (input("Ingrese por favor el tercer numero: \n"))

if Num1 < Num2 and Num1 < Num3:
    print("El numero mas pequeño es el primero ")

elif Num2 < Num1 and Num2 < Num3:
    print("El numero mas pequeño es el segundo")
    
elif Num3 < Num1 and Num3 < Num2:
    print("El numero mas pequeño es el tercero")
