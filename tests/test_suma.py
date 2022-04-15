# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import suma

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación suma
    def test_suma(self):
        assert suma(5) == False
        assert suma(2) == True
        assert suma(7) == False
        assert suma(10) == True
