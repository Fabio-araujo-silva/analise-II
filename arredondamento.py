# arredondamento.py

def arredondar_especial(numero, casas_decimais):
    """
    Arredonda um número de acordo com a regra especificada:
    - Para x < 0, o resultado é -round(|x|, numero_de_casas).
    - Para x >= 0, o resultado é round(x, numero_de_casas).

    Exemplo:
    arredondar_especial(1.20195, 4) -> 1.202
    arredondar_especial(-1.20195, 4) -> -1.202
    (Nota: O round() padrão do Python 3 arredonda para o par mais próximo em caso de empate)
    """
    if numero < 0:
        return -round(abs(numero), casas_decimais)
    else:
        return round(numero, casas_decimais)