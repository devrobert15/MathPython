#Conversão de segundos para dias, horas, minutos e segundos
numSegundos=int(input("Por favor, insira o número de segundos que deseja converter: "))
numDias=numSegundos//86400
numSegundos -=numDias*86400
numHoras=numSegundos//3600
numSegundos -= numHoras*3600
numMinutos=numSegundos//60
numSegundos -=numMinutos*60

'''Ou em alternativa
numDias=numSegundos//86400
numHoras=(numSegundos%86400)//3600
numMinutos=((numSegundos%86400)%3600)//60
numSegundosRes=numSegundos-numDias*86400-numHoras*3600-numMinutos*60'''

print("{} dias {} horas {} minutos {} segundos".format(numDias,numHoras,numMinutos,numSegundos))