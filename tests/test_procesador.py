import unittest
from src.procesador import Analizador

class TestAnalizador(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.analizador = Analizador("datos/sri_ventas_2024.csv")

    # ================================================================
    # PRUEBAS BÁSICAS
    # ================================================================
    
    def test_ventas_totales_como_diccionario(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertIsInstance(resumen, dict)

    def test_ventas_totales_todas_las_provincias(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        total_provincias = len(resumen)

        # El dataset 2024 contiene 25 provincias (incluye ND)
        self.assertEqual(total_provincias, 25)

    def test_ventas_totales_no_negativas(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertTrue(all(float(v) >= 0 for v in resumen.values()))

    def test_ventas_por_provincia_inexistente(self):
        with self.assertRaises(KeyError):
            self.analizador.ventas_por_provincia("Narnia")

    def test_ventas_por_provincia_existente(self):
        resultado = self.analizador.ventas_por_provincia("PICHINCHA")
        self.assertGreaterEqual(resultado, 0)

    # ================================================================
    # PRUEBAS PARA LAS ESTADÍSTICAS ADICIONALES
    # ================================================================

    def test_exportaciones_por_mes_es_diccionario(self):
        resumen = self.analizador.exportaciones_totales_por_mes()
        self.assertIsInstance(resumen, dict)

    def test_exportaciones_por_mes_valores_validos(self):
        resumen = self.analizador.exportaciones_totales_por_mes()
        self.assertTrue(all(float(v) >= 0 for v in resumen.values()))

    def test_provincia_mayor_importacion_es_cadena(self):
        resultado = self.analizador.provincia_mayor_importacion()
        self.assertIsInstance(resultado, str)

    def test_provincia_mayor_importacion_existe(self):
        resultado = self.analizador.provincia_mayor_importacion()

        # Normalización a mayúsculas para evitar fallos
        resultado = resultado.upper()
        provincias = {fila["PROVINCIA"].upper() for fila in self.analizador.datos}

        self.assertIn(resultado, provincias)


if __name__ == "__main__":
    unittest.main()