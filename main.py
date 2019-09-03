from modulos.Aritmetica import Aritmetica

sigue = "y"

while sigue=="y":
    try:
        operacion = int(input("\nIngrese la operación que desea realizar:\n\t1.-Suma.\n\t2.-Resta.\n\t3.-Producto.\n\t4.-División.\n\t5.-Salir.\n\t\t"))
        switcher = {
            1:"Suma",
            2:"Resta",
            3:"Producto",
            4:"División", 
            5:"Salir"
        }
        seleccion = switcher.get(operacion,"Valor invalido")
        if seleccion==5:
            print("\nUd. prefirio salir de la operación", seleccion)
        else:
            print("\nUd. selecciono operación", seleccion)

        aritmetica = Aritmetica()
        if seleccion=="Suma":
            valor_1 = input("\n\tIngresa el primer valor:  ")
            valor_2 = input("\n\tIngresa el segundo valor: ")
            while valor_1.isalpha() or valor_2.isalpha():
                valor_1 = input("\n\tIngresa el primer valor:  ")
                valor_2 = input("\n\tIngresa el segundo valor: ")
            aritmetica.setSuma(valor_1, valor_2)
            print("\n\tEl resultado de la suma es: ", aritmetica.getSuma())

        elif seleccion=="Resta":
            valor_1 = input("\n\tIngresa el primer valor:  ")
            valor_2 = input("\n\tIngresa el segundo valor: ")
            while valor_1.isalpha() or valor_2.isalpha():
                valor_1 = input("\n\tIngresa el primer valor:  ")
                valor_2 = input("\n\tIngresa el segundo valor: ")
            aritmetica.setResta(valor_1, valor_2)
            print("\n\tEl resultado de la Resta es: ", aritmetica.getResta())

        elif seleccion=="División":
            valor_1 = input("\n\tIngresa el primer valor:  ")
            valor_2 = input("\n\tIngresa el segundo valor: ")
            while valor_1.isalpha() or valor_2.isalpha():
                valor_1 = input("\n\tIngresa el primer valor:  ")
                valor_2 = input("\n\tIngresa el segundo valor: ")
            aritmetica.setDivi(valor_1, valor_2)
            print("\n\tEl resultado de la División es: ", aritmetica.getDivi())

        elif seleccion=="Producto":
            valor_1 = input("\n\tIngresa el primer valor:  ")
            valor_2 = input("\n\tIngresa el segundo valor: ")
            while valor_1.isalpha() or valor_2.isalpha():
                valor_1 = input("\n\tIngresa el primer valor:  ")
                valor_2 = input("\n\tIngresa el segundo valor: ")
            aritmetica.setMulti(valor_1, valor_2)
            print("\n\tEl resultado de la Multiplicar es: ", aritmetica.getMulti())
        
        else:
            print("Adios")
            break
        
    except ValueError as identifier:
        print("\n\tDebe ingresar valores númericos.")
     
    
    sigue = input("\n\tDesea realizar otra operación presione \"y\" para continuar o \"n\" para salir\n")        