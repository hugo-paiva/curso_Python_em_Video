import random
v = random.randint(20,200)
if v > 80:
    multa = (v-80)*7
    print('Você foi multado em \033[1;41mR${}\033[m por trafegar a \033[4;31m{}km/h\033[m'.format(multa, v))
else:
    print('Tenha uma boa viagem')