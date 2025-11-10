import csv


class Analizador:
    """
    Clase para leer un archivo CSV de ventas y calcular
    totales agrupados por provincia.
    """
    def __init__(self, ruta_csv):
        # NOTA: El constructor debe ser __init__ (con doble guion bajo)
        # El código original tiene _init_ (un solo guion bajo)

        # Guardamos la ruta del archivo CSV
        self.ruta_csv = ruta_csv
        
        # Leemos el archivo CSV y guardamos los datos en memoria
        self.datos = self._leer_csv()  # Usamos un nombre de método más privado

    def _leer_csv(self):
        """
        Lee el archivo CSV y devuelve una lista de filas (diccionarios).
        """
        datos = []
        try:
            # Usamos `_leer_csv` en lugar de `leer_csv` para indicar
            # que es un método interno de la clase.
            with open(self.ruta_csv, "r", encoding="utf-8") as archivo:
                lector = csv.DictReader(archivo, delimiter='|')
                for fila in lector:
                    datos.append(fila)
        except FileNotFoundError:
            print(f"Error: El archivo '{self.ruta_csv}' no se encontró.")
            return []
            
        return datos

    def ventas_totales_por_provincia(self):
        """
        Calcula y devuelve un diccionario con el total de ventas por provincia.

        Retorna:
            dict: {'Pichincha': 1000.0, 'Guayas': 2000.5, ...}
        """
        totales = {}

        # Recorremos todas las filas del archivo
        for fila in self.datos:
            try:
                provincia = fila["PROVINCIA"]
                # Convertimos el valor a float y sumamos
                total_venta = float(fila["TOTAL_VENTAS"])
            except KeyError as e:
                # Manejo de error si faltan columnas
                print(f"Advertencia: Columna faltante en la fila: {e}")
                continue
            except ValueError:
                # Manejo de error si el valor no es un número
                print(f"Advertencia: 'TOTAL_VENTAS' no es un número en la fila: {fila}")
                continue

            # Acumulación de ventas (más simple usando .get())
            totales[provincia] = totales.get(provincia, 0.0) + total_venta

        return totales

    def ventas_por_provincia(self, nombre):
        """
        Devuelve el total de ventas de una provincia específica.

        Args:
            nombre (str): Nombre de la provincia a consultar.

        Retorna:
            float: El total de ventas. Retorna 0.0 si la provincia no existe.
        """
        # Obtenemos todos los totales (se reutiliza la lógica)
        totales = self.ventas_totales_por_provincia()

        # Usamos .get() para retornar el valor o 0.0 si no se encuentra
        return totales.get(nombre, 0.0)

