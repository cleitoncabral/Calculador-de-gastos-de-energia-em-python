setor_resp = 'sim'
acum_consumo = 0
ICMS = 0.27
PIS = 0.0165
COFINS = 0.0761
impostos = ICMS+PIS+COFINS
print('Olá, seja bem-vindo ao programa!')
tarifa = int(input('Qual o valor em reais, pago por KWh de energia?\n'))
while (setor_resp == 'sim'):
    geladeira = input('Tem geladeira?\n')
    if geladeira =='sim':
        QTD = int(input('Quantos tem?\n'))
        QDM = int(input('Quantos dias por mês é usada?\n'))
        QHD = int(input('Horas de uso por dia?\n'))
        P1 = int(input('Qual a potência?\n'))
        P = P1/1000
        consumo = ((QHD*QDM)*P)*QTD
        acum_consumo = acum_consumo+consumo
        geladeira == 'nao'
    ar_condi = input('Tem ar condicionado?\n')
    if ar_condi =='sim':
       QTD = int(input('Quantos tem?\n'))
       QDM = int(input('Quantos dias por mês é usado\n'))
       QHD = int(input('Horas de uso por dia?\n'))
       P1 = int(input('Qual a potência?\n'))
       P = P1 / 1000
       consumo = ((QHD * QDM) * P) * QTD
       acum_consumo = acum_consumo + consumo
       ar_condi == 'nao'
    compu = input('Tem computador?\n')
    if compu == "sim":
       QTD = int(input('Quantos tem?\n'))
       QDM = int(input('Quantos dias por mês é usado?\n'))
       QHD = int(input('Horas de uso por dia?\n'))
       P1 = int(input('Qual a potência?\n'))
       P = P1 / 1000
       consumo = ((QHD * QDM) * P) * QTD
       acum_consumo = acum_consumo + consumo
       compu == 'nao'
    lampada = input('Tem lâmpada?\n')
    if lampada == "sim":
       QTD = int(input('Quantos tem?\n'))
       QDM = int(input('Quantos dias por mês é usada?\n'))
       QHD = int(input('Horas de uso por dia?\n'))
       P1 = int(input('Qual a potência?\n'))
       P = P1 / 1000
       consumo = ((QHD * QDM) * P) * QTD
       acum_consumo = acum_consumo + consumo
       lampada == 'nao'
    tele = input('Tem televisão?\n')
    if tele == "sim":
       QTD = int(input('Quantos tem?\n'))
       QDM = int(input('Quantos dias por mês é usado?\n'))
       QHD = int(input('Horas de uso por dia?\n'))
       P1 = int(input('Qual a potência?\n'))
       P = P1 / 1000
       consumo = ((QHD * QDM) * P) * QTD
       acum_consumo = acum_consumo + consumo
       tele == 'nao'
    setor_resp = input('Tem mais algum novo setor para adicionar?\n')
total = acum_consumo*tarifa
valor_total = (total*impostos)+total
print ('----------------------------------\n')
print('O total a pagar é {:.2f} reais' .format(valor_total))
