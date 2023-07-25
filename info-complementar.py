def router (): # Caso bridge
    equipamento = input('Marca da ONU: ')
    serial = input('Serial do equipamento: ')
    slot = int(input('Slot: '))
    porta = int(input('Porta: '))
    id = int(input('ID: '))
    ssid = input('SSID: ')
    senha = input('Senha: ')

    print('Informação complementar: ')
    print(f'{equipamento.capitalize()} Router || SN: {serial.upper()} || Slot: {slot} Porta: {porta} ID: {id} || SSID: {ssid} - Senha: {senha}')

def bridge(): # Caso router
    equipamento = input('Marca da ONU em bridge: ')
    serial = input('Serial do equipamento: ')
    router = input('Marca/modelo do roteador: ')
    slot = int(input('Slot: '))
    porta = int(input('Porta: '))
    id = int(input('ID: '))
    ssid = input('SSID: ')
    senha = input('Senha: ')

    print('Informação complementar: ')
    print(f'{equipamento.capitalize()} Bridge || SN: {serial.upper()} || Autentica no {router.capitalize()} || Slot: {slot} Porta: {porta} ID: {id} || SSID: {ssid} - Senha: {senha}')

# Início

tipo = int(input('Digite:\n[1] Router\n[2] Bridge\n\n'))

if tipo == 1:
    router()
else:
    bridge()