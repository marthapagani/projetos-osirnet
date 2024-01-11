import datas 

def proporcional (plano, dias): #! função para calcular valor proporcional
    valor = (plano / 30) * dias
    return valor

def vigencia (meses): #! função para calcular rescisão contratual
    valor = meses * 25
    return valor

valorFixoPlano = float(input("Valor do plano: R$ "))
valorPlano = valorFixoPlano #? será que é mesmo necessária essa atribuição?

boleto = input("Possui boleto em aberto? [S/N] ")

if boleto.upper() == 'S': # caso tenha boleto em aberto
    gerarProporcional = input("Vai efetuar pagamento do valor integral? [S/N] ")
    
    if gerarProporcional.upper() == 'N': # caso vá fazer o pagamento de valor proporcional
        diasUtilizados = datas.numeroDias()
        print(f'São {diasUtilizados} dias de utilização. ')
        valorPlano = proporcional(valorFixoPlano, diasUtilizados) # recebe o valor proporcional
else:
    valorPlano = valorFixoPlano

possuiVigencia = input("Possui vigência contratual ativa? [S/N] ")

if possuiVigencia.upper() == 'S': # caso tenha meses de vigência contratual ativa
    meses = int(input("Quantos meses? [1-12] "))
    valorVigencia = vigencia(meses)
else:
    valorVigencia = 0

valorTotal = valorPlano + valorVigencia # caso haja vigência, o valor do plano também recebe o valor de vigência

print(f"Valor a ser pago será R$ {valorPlano}. ")

#TODO: ponto flutuante para que arredonde sempre para o menor
#TODO: tratamento de erros