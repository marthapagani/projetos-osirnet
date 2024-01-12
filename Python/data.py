from datetime import datetime

def diferenca_horas(hora1, hora2, data1, data2):
    try:
        # Combinando as strings de data e hora para formar objetos datetime
        dt1 = datetime.strptime(f'{data1} {hora1}', '%d%m%Y %H:%M')
        dt2 = datetime.strptime(f'{data2} {hora2}', '%d%m%Y %H:%M')

        # Calculando a diferença
        diferenca = dt2 - dt1

        # Exibindo a diferença em horas e minutos
        dias = diferenca.days
        horas, resto = divmod(diferenca.seconds, 3600)
        horas =+ horas + (dias * 24)
        minutos = resto // 60

        print(f'{horas}:{minutos} de diferença')

    except ValueError:
        print("Formato inválido. Certifique-se de usar o formato 'DIA/MÊS/ANO HH:mm'.")

if __name__ == "__main__":

    vezes = int(input("Quantas vezes precisa que esse código se repita?"))

    for _ in range(vezes):
        data_inicio = input("Data de início (formato DIA/MÊS/ANO): ")
        hora_inicio = input("Hora de início (formato HH:mm): ")
        
        data_fim = input("Data de término (formato DIA/MÊS/ANO): ")
        hora_fim = input("Hora de término (formato HH:mm): ")

        diferenca_horas(hora_inicio, hora_fim, data_inicio, data_fim)