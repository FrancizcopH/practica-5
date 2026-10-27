import pytest

from paqueteria import calcular_envio

def test_paquete_pesa_cero():
    peso = 0
    tipo_envio = "estandar"
    esperado = 0
    resultado = calcular_envio(peso, tipo_envio)
    assert resultado == esperado