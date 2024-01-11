import datetime

def numeroDias():
    
    venc = input('Data de vencimento de boleto anterior [Formato XX/XX/XXXX]: ') # data inicial: vencimento das faturas
    ret = input('Data de abertura da primeira retenção [Formato XX/XX/XXXX]: ') # último dia de utilização

    venc = datetime.datetime.strptime(venc, '%d/%m/%Y') # converte a data inicial
    ret = datetime.datetime.strptime(ret, '%d/%m/%Y') # converte a data final
    
    venc += datetime.timedelta(days=1) # converte a primeira data para contar um dia depois do dia do vencimento
    
    return abs((venc - ret).days)
