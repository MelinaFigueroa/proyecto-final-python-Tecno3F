# Proyecto Final de Sistemas

## Integrante
- Melina Figueroa

## Descripción General
Este proyecto consta de dos módulos principales:
1. Sistema de Gestión de Tickets
2. Conversor de Temperaturas

### 1. Sistema de Gestión de Tickets

#### Descripción
Aplicación de gestión de tickets que permite:
- Crear nuevos tickets
- Leer tickets existentes
- Almacenar tickets en un archivo CSV
- Interfaz gráfica intuitiva

#### Características
- Generación automática de número de ticket
- Almacenamiento persistente
- Interfaz gráfica con Tkinter
- Validación de campos

#### Requisitos
- Python 3.x
- Tkinter (incluido en instalación estándar de Python)

#### Instalación
```bash
# Clonar repositorio
git clone [URL del repositorio]

# Cambiar al directorio del proyecto
cd proyecto-sistemas
```

#### Estructura de Archivos
```
proyecto-sistemas/
│
├── sistema_tickets.py       # Script principal de tickets
└── tickets.csv              # Archivo de almacenamiento de tickets
```

#### Uso
```bash
# Ejecutar la aplicación de tickets
python sistema_tickets.py
```

#### Capturas de Pantalla
![Pantalla de inicio](images/pantalla_bienvenida.png)
![Pantalla de alta de ticket](images/pantalla_alta_ticket.png)
![Pantalla para buscar el ticket por numero](images/pantalla_buscar_ticket.png)
![Pantalla del ticket encontrado](images/pantalla_ticket_encontrado.png)
![Pantalla del ticket no encontrado](images/pantalla_ticket_no_encontrado.png)
![Pantalla para leer un nuevo ticket](images/pantalla_buscar_nuevo_ticket.png)


#### Funcionalidades
- [x] Alta de tickets
- [x] Lectura de tickets
- [x] Almacenamiento en CSV

### 2. Conversor de Temperaturas

#### Descripción
Aplicación de conversión de temperaturas con:
- Conversión manual entre Celsius a Fahrenheit y viseversa
- Interfaz gráfica desarrollada con Tkinter

#### Características
- Conversión directa entre escalas
- Interfaz simple e intuitiva
- Validación de entradas

#### Requisitos
- Python 3.x
- Tkinter (incluido en instalación estándar de Python)

#### Instalación
```bash
# Clonar repositorio
git clone [URL del repositorio]

# Cambiar al directorio del proyecto
cd conversor-temperaturas
```

#### Estructura de Archivos
```
conversor-temperaturas/
│
└── conversor_temperaturas.py  # Script principal
```

#### Uso
```bash
# Ejecutar la aplicación de conversión
python conversor_temperaturas.py
```

#### Capturas de Pantalla
![Pantalla de inicio del conversor](images/pantalla_bienvenida_conversor.png)
![Convirtiendo de Fahrenheit a Celcius](images/fahrenheit_celcius.png)
![Convirtiendo de Celcius a Fahrenheit](images/celcius_fahrenheit.png)

#### Funcionalidades
- [x] Conversión de Celsius a Fahrenheit
- [x] Conversión inversa (Fahrenheit a Celsius)
- [x] Interfaz gráfica

## Instrucciones de Ejecución

### Requisitos Previos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación
1. Clonar el repositorio
2. (Opcional) Crear entorno virtual
3. Instalar dependencias

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows
venv\Scripts\activate
# En macOS/Linux
source venv/bin/activate

# Instalar dependencias
pip install tkinter
```

## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](./LICENSE) para más detalles.

## Contacto
Autora: Melina Figueroa
https://www.linkedin.com/in/melinagfigueroa/

```
https://github.com/MelinaFigueroa/proyecto-final-python-Tecno3F.git
