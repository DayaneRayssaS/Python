nome = input ("digite seu nome completo")
idade = input ("digite sua idade por favor")

idade = int (idade)

print (f"Ola {nome}, voce tem {idade} anos de idade e possui dois cachorros e um namorado que te incomoda💪💟")

try:
    numero = int(input("digite um numero: "))
    print (f"O numero digitado  foi {numero}.")
    except ValueError:
        print ("Erro: Por favor digite um numero valido.")