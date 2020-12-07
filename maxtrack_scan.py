#!/usr/bin/env python3

from sys import argv
from sys import exit
from time import sleep
from requests import get

#Verificando se foi passado argumento
try:
    ID_MODULO = argv[1]

except:
    print('Parâmetro ausente')
    print('Informe o ID do modulo.')
    print(f'Exemplo: {argv[0]} >> ID DO MODULO <<')
    exit(1)

mirror_off = []

for mirror in range(100, 300):
    sleep(2)
    try: 
        mirror_primario = get(f'http://50.30.39.2:{mirror}06/')
        sleep(1)
    except:
        print(f'Não foi possivel carregar a pagina de status do mirror {mirror}(Primário)')
        mirror_off.append(f'{mirror} Primário')
        ('='*50)
    try:
        mirror_secundario = get(f'http://85.25.19.214:{mirror}06/')
        sleep(1)
    except:
        print(f'Não foi possivel carregar a pagina de status do mirror {mirror}(Secundário)')
        mirror_off.append(f'{mirror} Secundário')
        ('='*50)
    
    if ID_MODULO in mirror_primario.text:
        print(f'Encontramos o modulo no mirror {mirror} primário!!!')
        exit(1)
    elif ID_MODULO in mirror_secundario.text:
        print(f'Encontramos o modulo no mirror {mirror} secundário!!!')
        exit(1)
    else:
        print(f'Buscando pelo modulo: {ID_MODULO} no mirror: {mirror}...')
        print('='*50)

print(f"""Não encontramos o modulo: {ID_MODULO}.
Considere reiniciar ou corrigir os serviços dos mirrors {mirror_off}
para uma melhor varredura..
""")