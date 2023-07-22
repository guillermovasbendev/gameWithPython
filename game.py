import random
wincomp=0
winuse=0


print('*'*50)
print('BIENVENIDO AL JUEGO DE PIEDRA,PAPEL, Y TIJERA')
print('*'*50)

print('*'*70)
print('Recuerda siempre ingresar tu eleccion en minuscula y sin errores')
print('*'*70)


total=input('selcciona a cuantas victorias se gana el juego:')
total=int(total)

while (wincomp < total and winuse < total):

    print('VICTORIAS COMPUTADORA = ' + str(wincomp))
    print('VICTORIAS USUARIO = ' + str(winuse))

    lista=['piedra', 'papel','tijera']
    usuario=input('Escoge:piedra,papel o tijera\n') 
    computadora=random.choice(lista)
    

    print('escogiste: ' + usuario)
    print("la computadora escogio: " + computadora)

    
    if usuario == computadora:
        print('tu escogiste ' + usuario + ', la computadora escogio: ' + computadora + ' es un empate')

    if usuario == 'piedra':
        if computadora =='tijera':
            print('escogiste ' + usuario + ' la maquina escogio ' + computadora + " tu ganas ")
            print('por que '+ usuario + ' le gana a ' + computadora)
            winuse+=1
        elif computadora =='papel':    
            print('escogiste ' + usuario + ' la maquina escogio ' + computadora + " tu pierdes")
            print('por que '+ computadora + ' le gana a ' + usuario)
            wincomp+=1

            
    if usuario == 'papel':
        if computadora =='piedra':
            print('escogiste ' + usuario + ' la maquina escogio ' + computadora + " tu ganas")
            print('por que '+ usuario + ' le gana a ' + computadora)
            winuse+=1
        elif computadora =='tijera':    
            print('escogiste ' + usuario + ' la maquina escogio ' + computadora + " tu pierdes")
            print('por que '+ computadora + ' le gana a ' + usuario)
            wincomp+=1

    if usuario == 'tijera':
        if computadora =='papel':
            print('escogiste ' + usuario + ' la maquina escogio  ' + computadora + " tu ganas")
            print('por que '+ usuario + ' le gana a ' + computadora)
            winuse+=1
        elif computadora =='piedra':    
            print('escogiste ' + usuario + ' la maquina escogio ' + computadora + " tu pierdes")
            print('por que '+ computadora + ' le gana a ' + usuario)
            wincomp+=1

if winuse == total:
    print('Felicitaciones usuario GANASTE')
elif wincomp == total:
    print('Lo siento usuario PERDISTE')