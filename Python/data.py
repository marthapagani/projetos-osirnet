from datetime import datetime

def diferenca_horas(hora1, hora2, data1, data2):
    try:
        # Combinando as strings de data e hora para formar objetos datetime
        dt1 = datetime.strptime(f'{data1} {hora1}', '%d-%m-%Y %H:%M')
        dt2 = datetime.strptime(f'{data2} {hora2}', '%d-%m-%Y %H:%M')

        # Calculando a diferença
        diferenca = dt2 - dt1

        # Exibindo a diferença em dias, horas e minutos
        dias = diferenca.days * 24
        horas, remainder = divmod(diferenca.seconds, 3600)
        horas = horas + dias
        minutos = remainder // 60 

        print(f'Diferença: {horas}:{minutos}.')

    except ValueError:
        print("Formato inválido. Certifique-se de usar o formato 'DIA-MES-ANO e HORA:MINUTO'.")

if __name__ == "__main__":
    data_inicio = input("Digite a data de início (formato DIA-MES-ANO): ")
    hora_inicio = input("Digite a hora de início (formato HORA:MINUTO): ")
    
    data_fim = input("Digite a data de término (formato DIA-MES-ANO): ")
    hora_fim = input("Digite a hora de término (formato HORA:MINUTO): ")

    diferenca_horas(hora_inicio, hora_fim, data_inicio, data_fim)
