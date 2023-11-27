from scipy.interpolate import interp1d

# Dados fornecidos
temperaturas =        [0.01,       10,         20,         30,        40,        50,        60,        70,        80,       90,       100,      110,      120,      130,      140,      150]
densidade_liquida =   [1000,       999.7,      998.2,      995.6,     992.2,     988.0,     983.2,     977.7,     971.8,    965.3,    958.3,    950.9,    943.1,    934.8,    926.1,    917.0]
viscosidade_liquida = [0.00000922, 0.00000946, 0.00000973, 0.0000100, 0.0000103, 0.0000106, 0.0000109, 0.0000113, 0.0000116,0.0000119,0.0000123,0.0000126,0.0000130,0.0000133,0.0000137,0.0000140]

# Funções de interpolação
densidade_interp = interp1d(temperaturas, densidade_liquida, kind='cubic')
viscosidade_interp = interp1d(temperaturas, viscosidade_liquida, kind='cubic')

def propriedades_agua(temperatura):
    # Interpolação para encontrar densidade e viscosidade
    densidade = densidade_interp(temperatura)
    viscosidade = viscosidade_interp(temperatura)
    
    # Calcular massa específica (inverso da densidade)
    massa_especifica = 1 / densidade
    
    return massa_especifica, viscosidade

