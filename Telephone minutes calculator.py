tchau = int(input('Digite o valor de minutos consumidos: '))
if tchau <= 200:
    minutos = tchau * 0.20
else:
    if tchau < 400:
        minutos = tchau * 0.18
    else:
        minutos = tchau * 0.15
        if tchau >= 800:
            minutos = tchau * 0.08
print (f'O valor a pagar é de {minutos}')
        
        
