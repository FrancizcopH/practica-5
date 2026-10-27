def calcular_envio(peso: float, tipo_envio: str = "estandar") -> float:
    if peso == 0:
        return 0
    if peso <= 5:
        return 50
    return 0