import pandas as pd
import argparse
import sys

def procesar_csv(archivo):
    try:
        # Cargar el archivo CSV
        df = pd.read_csv(archivo)
        
        # Obtener la transacción con el mayor monto
        fila_mayor = df.loc[df['monto'].idxmax()].squeeze()
        id_mayor = fila_mayor['id']
        monto_mayor = fila_mayor['monto']
        
        # Conteo de transacciones por tipo
        conteo_tipos = df['tipo'].value_counts().to_dict()

       #Estamos buacando el conteo de transacciones por tipo, que son credito y debito 
       #Obteniendo su monto si es creito o debito y con el metodo .sum() sumamos los montos
       #Segun el filtro si es credito o debito
        balance = df.loc[df['tipo']=='Crédito', 'monto'].sum() - df.loc[df['tipo']=='Débito', 'monto'].sum()

        # Mostrar el reporte
        print("\nReporte de transacciones")
        print("----------------------")
        #Balance final
        print(f"")
        print(f"Balance final: {balance:.2f}")
        print(f"Transacción de Mayor Monto: ID {id_mayor} con monto {monto_mayor:.2f}")
        print("Conteo de transacciones:", " | ".join(f"{tipo}: {cantidad}" for tipo, cantidad in conteo_tipos.items()))
    
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo}'.")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print("Error: El archivo CSV está vacío.")
        sys.exit(1)
    except KeyError:
        print("Error: El archivo CSV no contiene las columnas esperadas ('id', 'tipo', 'monto').")
        sys.exit(1)
    except Exception :
        print(f"Error inesperado: Error al procesar el archivo '{archivo}'.")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Procesador de transacciones bancarias desde un CSV.")
    parser.add_argument("archivo", help="Ruta del archivo CSV a procesar")
    args = parser.parse_args()
    
    procesar_csv(args.archivo)
