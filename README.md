# Implementacion_ATM_SYSTEM

## ¿Que se necesita para ejecutarlo? (Linux)

1. version de python3 >= 3.8
2. crear un ambiente virtual o en su defecto instalar la libreria necesaria directamente con el pip por defecto
3. instalar la libreria de PySide2
```bash
pip install PySide2
```
4. Ejecutar el archivo: "main_gui.py"

## ¿Como crear un ambiente virtual? y ¿Como activarlo?

directamente desde la terminal de linux

1. Instalar la libreria venv
```bash
sudo apt install python3.8-venv
```

2. Crear el ambiente virtual (debemos de estar en la carpeta de destino o podemos poner todo el path)
```bash
python3.8 -m venv <path_destino>/<nombre_del_ambiente>
```

3. activar el ambiente virutal
```bash
source <path_destino>/<nombre_del_ambiente>/bin/activate
```


## ¿Como funciona?

Primer partimos de la especificación en SOFL (CDFD y su modulo asociado)

![CDFD del ATM](https://raw.githubusercontent.com/jaggcv/Imagenes/main/SOFL_FIGURES/09_SOFL_FIGURES_ISSUESOFSOFL/EXAMPLE_ATM_EXTERNAL_PROCESS.png)

despues creamos las funciones en python que representan a cada uno de los procesos, despues utilizando la libreria PySide2 y la aplicación de QTCreator, se crea la interfaz de usuario, para posteriormente conectar cada una de los *signals and slots*, correspondiente al comportamiento esperado.
