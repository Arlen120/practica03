from src.procesador import Analizador

def main():
    archivo = "datos/sri_ventas_2024.csv"
    analizador = Analizador(archivo)

    print("Ventas totales por provincia:")
    resumen = analizador.ventas_totales_por_provincia()
    
    provincias_ordenadas = sorted(resumen.keys())
    
    for prov in provincias_ordenadas:
        total = resumen[prov]
        print(f"\t{prov}: ${total:.2f}")

    print("\nCompras para una provincia")
    
    provincias_validas = {prov.upper() for prov in resumen.keys()} 
    
    provincia = ""
    provincia_formateada = ""

    while provincia not in provincias_validas:
        entrada = input("\tIngrese el nombre de una provincia: ")
        provincia = entrada.strip().upper() 
        
        if provincia in provincias_validas:
            for key in resumen.keys():
                if key.upper() == provincia:
                    provincia_formateada = key
                    break

    ventas = analizador.ventas_por_provincia(provincia_formateada)
    print(f"\tVentas de {provincia_formateada}: ${ventas:,.2f}")

    # ======================================================
    # NUEVA ESTADÍSTICA 1: EXPORTACIONES TOTALES POR MES
    # ======================================================
    print("\nExportaciones totales por mes:")

    exportaciones = analizador.exportaciones_totales_por_mes()

    for mes in sorted(exportaciones.keys()):
        print(f"\tMes {mes}: ${exportaciones[mes]:,.2f}")

    # ======================================================
    # NUEVA ESTADÍSTICA 2: PROVINCIA CON MAYOR IMPORTACIÓN
    # ======================================================
    print("\nProvincia con mayor volumen de importaciones:")

    provincia_top = analizador.provincia_mayor_importacion()
    print(f"\tLa provincia con mayor importación es: {provincia_top.upper()}")

if __name__ == "__main__":
    main()
