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
    print(f'{equipamento.capitalize()} Bridge || SN: {serial.upper()} || Autentica no {router.upper()} || Slot: {slot} Porta: {porta} ID: {id} || SSID: {ssid} - Senha: {senha}')

def telefonia(): # Caso tenha telefonia
    tipo = int(input("Selecione: \n[1] Telefonia Osirnet ou Toptech\n[2] Telefonia Tchenet\n\n"))
    if tipo == 1:
        iptel = input('IP da telefonia: ')
    numtel = int(input('Número do telefone: '))
    senhatel = int(input('Senha da telefonia: '))
    if tipo == 2:
        print(f'|| + Telefonia || Número Tel: {numtel} || Senha Tel: {senhatel}')
    else:
        print(f'|| + Telefonia || IP Tel: {iptel} || Número Tel: {numtel} || Senha Tel: {senhatel}')

# Início

tipo = int(input('Digite:\n[1] Router\n[2] Router com telefonia\n[3] Bridge\n[4] Bridge com telefonia\n'))

if tipo == 1:
    router()
if tipo == 2:
    router()
    telefonia()
if tipo == 3:
    bridge()
if tipo == 4:
    bridge()
    telefonia()

#TODO tratamento de erros