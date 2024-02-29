"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61  # velocidade atual do carro
local_carro = 100  # km em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # km onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

vel_carro_pass_radar = velocidade > RADAR_1
carro_passou_radar = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado = carro_passou_radar and vel_carro_pass_radar

if vel_carro_pass_radar:
    print('A velocidade do carro passou do permitido do Radar 1')

if carro_passou_radar:
    print('Carro passou no radar 1')

if carro_multado:
    print('Carro foi multado')