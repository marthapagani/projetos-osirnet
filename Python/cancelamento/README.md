# Cálculos de Cancelamento

Uma pequena rotina de programação que fiz para me auxiliar a fazer cálculos em uma rotina simples de um provedor de internet. O pequeno código calcula o valor que um cliente precisa pagar ao efetuar o cancelamento do seu plano de internet, que possui uma vigência contratual de no mínimo 1 ano.

## Passo a passo

- insere o valor do plano base do cliente
- verifica se o cliente possui boleto em aberto
- caso o cliente tenha boleto em aberto, verifica se a pessoa pretende pagar o valor integral do boleto ou os dias proporcionais de utilização
- verifica se a pessoa possui vigência contratual ativa
- caso sim, verifica quantos meses para calcular o valor de multa