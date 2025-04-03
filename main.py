import pandas as pd
#import os # Limpiar la consola
#os.system("cls") Comando cls para limpiar consola en Windows

#Estamos usando un try-except para manejar errores al cargar el archivo
try:
    doc = pd.read_csv('datos.csv')
    print("Archivo cargado correctamente")
    print(doc)
except FileNotFoundError:
    print("El archivo no existe")
    exit()
except pd.errors.EmptyDataError:
    print("El archivo está vacío")
    exit()


filaMayor = doc.loc[doc['monto'].idxmax()].squeeze()
#Con squeeze() convierto la fila en una serie para poder acceder a sus valores


idMayor = filaMayor['id']
montoMayor = filaMayor['monto']

tipos = doc['tipo'].value_counts().to_dict() #Conteo de transacciones por credito y debito


print("\nReporte de transacciones")
print("----------------------")
print(f"Transacción de Mayor Monto: ID  {idMayor} con monto {montoMayor:.2f}")
#Estoy agregando el end='' para que no haga un salto de linea al final de la cadena
print(f"Conteo de transacciones:", " | " .join(f"{tipo}: {cantidad}" for tipo, cantidad in tipos.items()))


