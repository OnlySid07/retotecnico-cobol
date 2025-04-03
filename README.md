# Reto Técnico - Análisis de Transacciones con Python y Pandas

## Introducción
Este proyecto consiste en analizar un archivo CSV que contiene un conjunto de transacciones con su tipo e importe. La aplicación identifica la transacción con el mayor monto y cuenta la cantidad de transacciones por tipo (Crédito/Débito). El propósito de este reto es demostrar habilidades en Python y el uso de la biblioteca Pandas para el procesamiento de datos.

## Instrucciones de Ejecución
### Requisitos previos
Asegúrate de tener instalado Python 3 y la biblioteca Pandas. Si no la tienes instalada, puedes hacerlo con el siguiente comando:
```sh
pip install pandas
```

### Ejecución
1. Clona o descarga el repositorio.
2. Ubica el archivo `datos.csv` en el mismo directorio donde está el script.
3. Ejecuta el script con:
```sh
python cli.py datos.csv
```

## Enfoque y Solución
La solución implementada sigue estos pasos:
1. Carga los datos desde un archivo CSV usando Pandas.
2. Identifica la transacción con el mayor monto usando `idxmax()`.
3. Cuenta las transacciones por tipo utilizando `value_counts()`.
4. Presenta los resultados en un formato claro y estructurado.

Se ha priorizado la claridad del código y la eficiencia en la manipulación de datos.

## Estructura del Proyecto
```
/reto-tecnico/
│── script.py  # Código principal que procesa los datos
│── datos.csv  # Archivo de entrada con los datos de transacciones
│── cli.py     # Archivo de entrada desde linea de comando (CLI)
│── README.md  # Documentación del proyecto
```

## Formato del Archivo CSV
```csv
id,tipo,monto
1,Crédito,100.00
2,Débito,50.00
3,Crédito,200.00
4,Débito,75.00
5,Crédito,150.00
```

## Documentación y Calidad del Código
El código ha sido diseñado para ser claro y legible. Se han utilizado comentarios explicativos en las secciones clave del código para facilitar su comprensión. Además, se han aplicado buenas prácticas como:
- Uso de `try-except` para manejar errores en la lectura del archivo CSV.
- Uso de `.squeeze()` para evitar estructuras de datos innecesarias.
- Impresión estructurada para una salida de resultados clara.

Si tienes alguna duda o sugerencia, no dudes en contribuir o comentar. 🚀

