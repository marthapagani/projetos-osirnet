def redir():
    desc = input('PPPOE + Nome do cliente: ')
    porta_interna = int(input('Porta interna: '))
    ipprivado = input('IP público privado (100.65): ')
    porta_externa = int(input('Porta externa: '))
    ippublico = input('IP público de acesso externo: ')

    print(f'\n/ip firewall nat add action=dst-nat chain=dstnat comment="{desc}" dst-address={ippublico} dst-port={porta_externa} protocol=tcp to-addresses={ipprivado} to-ports={porta_interna}')
    print(f'/ip firewall nat add action=dst-nat chain=dstnat comment="{desc}" dst-address={ippublico} dst-port={porta_externa} protocol=udp to-addresses={ipprivado} to-ports={porta_interna}')

def abertura():
    porta_interna = int(input('Porta interna: '))
    porta_externa = int(input('Porta externa: '))
    ipprivado = input('IP do equipamento: ')

    print(f'\n/ip firewall nat add action=dst-nat chain=dstnat dst-port={porta_interna} protocol=tcp to-addresses={ipprivado} to-ports={porta_externa}')
    print(f'/ip firewall nat add action=dst-nat chain=dstnat dst-port={porta_interna} protocol=udp to-addresses={ipprivado} to-ports={porta_externa}')

# INÍCIO

tipo = int(input('Digite:\n[1] Redirecionamento de portas\n[2] Abertura de portas\n\n'))

if tipo == 1:
    redir()
else:
    abertura()