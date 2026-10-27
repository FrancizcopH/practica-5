def calcular_envio(peso: float, tipo_envio: str = "estandar") -> float:
    if peso <= 5:
        return 50
    return 0