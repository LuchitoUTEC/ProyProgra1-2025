[**Español**](#simulador-de-fábrica-español) | [**English**](#factory-simulator-english)
[**Español**](#simulador-de-fábrica-español) | [**English**](#factory-simulator-english)

---

## Fabrica del Caos

Este proyecto es un simulador de gestión de una fábrica por turnos, desarrollado en Python con la librería Pygame para la interfaz gráfica. Los jugadores asumen el rol de gerentes y deben tomar decisiones mensuales en cinco áreas funcionales clave para asegurar la rentabilidad y sostenibilidad de la empresa.

### Conceptos Clave

El núcleo del simulador se basa en tres conceptos principales:

1.  **Gestión por Módulos:** La lógica del juego está separada en módulos de Python, donde cada archivo tiene una responsabilidad única:
    * `acciones.py`: Contiene las funciones que el jugador puede ejecutar (producir, contratar, etc.).
    * `cartas.py`: Contiene los efectos de los eventos aleatorios ("Cartas del Caos").
    * `estado.py`: Gestiona el estado de la simulación y los cálculos de fin de turno.

2.  **Diccionario `estado` Central:** Toda la información de la fábrica (caja, inventario, empleados, reputación, etc.) se almacena en un único diccionario de Python llamado `estado`. Todas las funciones leen y modifican este diccionario, convirtiéndolo en la única fuente de verdad del juego.

3.  **Flujo del Turno:** Cada turno representa un mes de operaciones y sigue un flujo estricto:
    * El jugador elige y ejecuta una acción de gestión en cada una de las 5 áreas.
    * Se resuelve el efecto de una carta del caos, que modifica el estado.
    * Se recalculan los indicadores finales del mes (ventas, pago de sueldos, actualización de contadores, etc.).

### Estructura del Proyecto

```
/
├── main.py
├── estado.py
├── acciones.py
├── cartas.py
├── requirements.txt
└── img/
    ├── ... (imágenes de fondo)
    └── Eventos/
        └── ... (imágenes de cartas)
```

* `main.py`: **(No modificar)**. Controla el bucle principal del juego, la interfaz gráfica y la interacción con el usuario.
* `estado.py`: Define el estado inicial y contiene la función `calcular_estado_final()`.
* `acciones.py`: Implementa la lógica de las decisiones del jugador.
* `cartas.py`: Implementa la lógica de las 40 "Cartas del Caos".
* `requirements.txt`: Lista las dependencias del proyecto (Pygame).
* `img/`: Contiene todos los recursos gráficos.

### Requisitos

* Python 3.x
* Pygame

### Instalación

1.  Asegúrate de tener Python 3 instalado en tu sistema.
2.  Navega con tu terminal a la carpeta donde descargaste el proyecto.
3.  Ejecuta el siguiente comando para instalar las dependencias necesarias. Esto leerá el archivo `requirements.txt` e instalará Pygame.
    ```bash
    pip install -r requirements.txt
    ```

### Cómo Jugar

1.  Una vez instaladas las dependencias, ejecuta el programa con el siguiente comando:
    ```bash
    python main.py
    ```
2.  Usa los botones `<` y `>` para navegar entre las cinco áreas de la empresa.
3.  Para cada área, haz clic en **`Cambiar`**, introduce el número de la acción deseada y presiona **`OK`**.
4.  Una vez configuradas las acciones, haz clic en **`Tomar carta`**.
5.  Introduce un número del 1 al 40 para simular una carta del caos y presiona **`OK`**.
6.  Haz clic en **`Continuar`** para finalizar el turno.
7.  Para revisar los resultados, haz clic en **`Estado de la Empresa`**.

### Nota del Profesor
Según las indicaciones del profesor Ian B., la lógica de las **acciones** debe estar estandarizada y copiada desde el foro del curso para la exposición final. Se recomienda verificar también el foro para la lógica de las cartas y así asegurar la consistencia con los demás grupos.

### Autor(es)

* **Docarmo Rodríguez, Luis Jaime** (Código: 202510006)
* **Balladares Vílchez, Giordano Gonzalo** (Código: 202510077)
* **Espinoza Reto, Martin Emilio** (Código: 202510153)
* **Calero Ccana, Cristopher Wilson** (Código: 202510117)

### Detalle de Contribuciones
* **Luis Jaime Docarmo Rodríguez:** Encargado de la acción "Pagar deuda" (`acciones.finanzas_pagar_deuda`).
* **Giordano Gonzales Balladares Vílchez:** Encargado de la acción "Negociar crédito" (`acciones.compras_negociar_credito`).
* **Martin Emilio Espinoza Reto:** Encargado de la acción "Invertir en branding" (`acciones.marketing_invertir_branding`).
* **Cristopher Wilson Calero Ccana:** Encargado de la acción "Vender excedentes de insumos" (`acciones.compras_vender_excedentes_insumos`).
* **Ítalo Pablo Roque Martínez:** No respondió a las comunicaciones para la coordinación del proyecto.

---

## Chaos Factory

This project is a turn-based factory management simulator developed in Python using the Pygame library for the graphical interface. Players take on the role of managers and must make monthly decisions across five key functional areas to ensure the company's profitability and sustainability.

### Core Concepts

The simulator's core is built on three main concepts:

1.  **Modular Management:** The game's logic is separated into Python modules, where each file has a unique responsibility:
    * `acciones.py`: Contains the functions the player can execute.
    * `cartas.py`: Contains the effects of the "Chaos Cards".
    * `estado.py`: Manages the simulation state and end-of-turn calculations.

2.  **Central `estado` Dictionary:** All factory information (cash, inventory, etc.) is stored in a single Python dictionary named `estado`, making it the single source of truth.

3.  **Turn Flow:** Each turn represents one month and follows a strict flow: Player Actions -> Chaos Card -> Final Calculation.

### Project Structure

```
/
├── main.py
├── estado.py
├── acciones.py
├── cartas.py
├── requirements.txt
└── img/
    ├── ... (background images)
    └── Eventos/
        └── ... (card images)
```

* `main.py`: **(Do not modify)**. Controls the main game loop and GUI.
* `estado.py`: Defines the initial state and the `calcular_estado_final()` function.
* `acciones.py`: Implements the player's decision logic.
* `cartas.py`: Implements the logic for the 40 "Chaos Cards".
* `requirements.txt`: Lists the project dependencies (Pygame).
* `img/`: Contains all graphical assets.

### Requirements

* Python 3.x
* Pygame

### Installation

1.  Ensure you have Python 3 installed on your system.
2.  Navigate to the project folder using your terminal.
3.  Run the following command to install the required dependencies. This will read the `requirements.txt` file and install Pygame.
    ```bash
    pip install -r requirements.txt
    ```

### How to Play

1.  Once the dependencies are installed, run the program with the following command:
    ```bash
    python main.py
    ```
2.  Use the `<` and `>` buttons to navigate between the five company areas.
3.  For each area, click **`Cambiar`**, enter the number of the desired action, and press **`OK`**.
4.  Once all actions are set, click **`Tomar carta`**.
5.  Enter a number from 1 to 40 to simulate a chaos card and press **`OK`**.
6.  Click **`Continuar`** to end the turn.
7.  To review the results, click **`Estado de la Empresa`**.

### Professor's Note
As per the instructions from Professor Ian B., the logic for the **actions** must be standardized and copied from the course forum for the final presentation. It is recommended to also check the forum for the card logic to ensure consistency with other groups.

### Author(s)

* **Docarmo Rodríguez, Luis Jaime** (Code: 202510006)
* **Balladares Vílchez, Giordano Gonzalo** (Code: 202510077)
* **Espinoza Reto, Martin Emilio** (Code: 202510153)
* **Calero Ccana, Cristopher Wilson** (Code: 202510117)

### Contribution Details
* **Luis Jaime Docarmo Rodríguez:** In charge of the "Pagar deuda" (Pay debt) action (`acciones.finanzas_pagar_deuda`).
* **Giordano Gonzales Balladares Vílchez:** In charge of the "Negociar crédito" (Negotiate credit) action (`acciones.compras_negociar_credito`).
* **Martin Emilio Espinoza Reto:** In charge of the "Invertir en branding" (Invest in branding) action (`acciones.marketing_invertir_branding`).
* **Cristopher Wilson Calero Ccana:** In charge of the "Vender excedentes de insumos" (Sell surplus supplies) action (`acciones.compras_vender_excedentes_insumos`).
* **Ítalo Pablo Roque Martínez:** Did not respond to communications for project coordination.
