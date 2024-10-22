# Ejemplos de Uso del Módulo TM1638 con MicroPython
Este repositorio contiene varios ejemplos prácticos para interactuar con el módulo TM1638 utilizando MicroPython. El TM1638 es un controlador multifuncional que permite manejar displays de 7 segmentos, botones y LEDs mediante pocos pines. Los ejemplos están diseñados para trabajar con la librería tm1638 y muestran cómo realizar tareas comunes como:

Mostrar texto y números en el display de 7 segmentos.
Controlar LEDs de manera individual o simultánea.
Leer el estado de los botones y reaccionar en consecuencia.
# Contenido
# Ejemplos incluidos:
Mostrar mensajes de texto en el display
  Un ejemplo simple que alterna entre los mensajes "HELLO" y "WORLD" en el display.

Contador de números en el display
  Un contador que incrementa un número en el display de 7 segmentos cada segundo.

Intermitencia de LEDs en secuencia
  Control de los LEDs del TM1638, encendiéndolos uno a uno y luego apagándolos en secuencia.

Mostrar el botón presionado en el display
  Detecta el botón presionado y muestra su número correspondiente en el display.

Control de LEDs mediante botones
  Cada botón enciende o apaga su LED correspondiente.

# Requisitos
  MicroPython
  Placa de desarrollo compatible (como ESP8266, ESP32)
  Módulo TM1638
  Librería TM1638 para MicroPython

# Instalación de la libreria
Para utilizar los ejemplos, necesitas la librería tm1638.
Descarga el archivo tm1638.py desde el repositorio oficial.
Guarda una copia del archivo en la placa MicroPython en la raíz del sistema de archivos o en el mismo directorio donde están tus scripts.
