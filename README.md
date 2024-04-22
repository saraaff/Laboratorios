# Cuentos Infantiles Interactivos 

## Introducción

Este proyecto es una aplicación interactiva diseñada para niños, que combina narrativas personalizadas con una interfaz visual atractiva desarrollada con Python y la biblioteca Turtle. La aplicación busca ofrecer una experiencia educativa y entretenida, permitiendo a los niños influir en el curso de la historia mediante sus elecciones personales.

## Características

- **Personalización del Usuario:** El programa solicita datos básicos del usuario (nombre, edad y color favorito) para personalizar la experiencia narrativa.
- **Interactividad:** Los niños pueden decidir en puntos clave si desean continuar la historia, lo que les da control sobre la narración.
- **Gráficos Turtle:** Utiliza gráficos simples para mantener la atención de los niños y hacer la historia visualmente interesante.

## Configuración del Proyecto

### Clonar el Repositorio

Para obtener una copia del proyecto y comenzar, clona el repositorio a tu máquina local usando el siguiente comando en tu terminal:

```bash
git clone
```
### Características
Navegar al Directorio del Proyecto

```bash
cd pensamiento
```
### Activar el entorno Virtual
```bash
python -m venv venv
```
En Windows:

```bash
.\venv\Scripts\activate
```

En MacOs y Linux:

```bash
source venv/bin/activate
```
Instalar dependecias

```bash
pip install -r requirements.txt
```

##Ejecutar el programa
Una vez activado el entorno y las dependencias instaladas, puedes ejecutar el programa con:

```bash
python main.py
```
#Diagrama de Flujo 
![Diagrama sin título drawio](https://github.com/nexbox09/pensamiento/assets/68700670/457480ae-7fb4-418c-b26c-57f058232f2c)

#Resultados esperados
Al correr el programa, se realizarán las siguientes acciones:

Solicitud de Datos Personales: El programa pedirá al niño ingresar su nombre, edad y color favorito.
Narrativa Interactiva: La historia se presentará en una ventana de Turtle, con texto y gráficos que cambian en función de las interacciones del usuario.
Decisiones de Continuación: En varios puntos, se preguntará al niño si desea continuar con la siguiente parte de la historia.
Conclusión de la Historia: Al finalizar, se mostrará un mensaje de agradecimiento y el programa concluirá, cerrando automáticamente la ventana.


