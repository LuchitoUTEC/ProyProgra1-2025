[**Español**](#simulador-de-fábrica-español) | [**English**](#factory-simulator-english)

---

## Simulador de Fábrica

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
└── img/
    ├── fondo1.png
    ├── ... (más fondos)
    └── Eventos/
        ├── evento_carta_1.png
        └── ... (40 imágenes de cartas)
```

* `main.py`: **(No modificar)**. Controla el bucle principal del juego, la interfaz gráfica con Pygame y la interacción con el usuario.
* `estado.py`: Define el estado inicial de la empresa y contiene la función `calcular_estado_final()` que procesa los resultados de cada turno.
* `acciones.py`: Implementa la lógica de todas las decisiones que puede tomar el jugador en las áreas de Producción, Recursos Humanos, Marketing, Compras y Finanzas.
* `cartas.py`: Implementa la lógica de las 40 "Cartas del Caos" que introducen eventos aleatorios en el juego.
* `img/`: Contiene todos los recursos gráficos, como los fondos de cada área y las imágenes para cada carta de evento.

### Requisitos

* Python 3.x
* Pygame

### Instalación

1.  Asegúrate de tener Python 3 instalado en tu sistema.
2.  Instala la librería Pygame usando pip:
    ```bash
    pip install pygame
    ```

### Cómo Jugar

1.  Navega a la carpeta raíz del proyecto desde tu terminal.
2.  Ejecuta el programa con el siguiente comando:
    ```bash
    python main.py
    ```
3.  Usa los botones `<` y `>` para navegar entre las cinco áreas de la empresa.
4.  Para cada área, haz clic en **`Cambiar`**, introduce el número de la acción deseada y presiona **`OK`**.
5.  Una vez que hayas configurado las acciones para las cinco áreas, haz clic en **`Tomar carta`**.
6.  Introduce un número del 1 al 40 para simular una carta del caos y presiona **`OK`**.
7.  Haz clic en **`Continuar`** para finalizar el turno.
8.  Para revisar los resultados y cómo cambió el estado de tu empresa, haz clic en **`Estado de la Empresa`**.

### Nota del Profesor
Según las indicaciones del profesor Ian B., la lógica de las **acciones** debe estar estandarizada y copiada desde el foro del curso para la exposición final. Se recomienda verificar también el foro para la lógica de las cartas y así asegurar la consistencia con los demás grupos.

### Autor(es)

* Luis Jaime Docarmo Rodriguez
* Martin Emilio Espinoza Reto
* Cristopher Wilson Calero Ccana
* Ítalo Pablo Roque Martínez
* Giordano Gonzales Balladares Vilchez

---

## Factory Simulator

This project is a turn-based factory management simulator developed in Python using the Pygame library for the graphical interface. Players take on the role of managers and must make monthly decisions across five key functional areas to ensure the company's profitability and sustainability.

### Core Concepts

The simulator's core is built on three main concepts:

1.  **Modular Management:** The game's logic is separated into Python modules, where each file has a unique responsibility:
    * `acciones.py`: Contains the functions the player can execute (produce, hire, etc.).
    * `cartas.py`: Contains the effects of random events ("Chaos Cards").
    * `estado.py`: Manages the simulation state and end-of-turn calculations.

2.  **Central `estado` Dictionary:** All factory information (cash, inventory, employees, reputation, etc.) is stored in a single Python dictionary named `estado`. All functions read from and write to this dictionary, making it the single source of truth for the game.

3.  **Turn Flow:** Each turn represents one month of operations and follows a strict flow:
    * The player chooses and executes a management action in each of the 5 areas.
    * The effect of a chaos card is resolved, modifying the state.
    * The final indicators for the month are recalculated (sales, payroll, counter updates, etc.).

### Project Structure

```
/
├── main.py
├── estado.py
├── acciones.py
├── cartas.py
└── img/
    ├── fondo1.png
    ├── ... (more backgrounds)
    └── Eventos/
        ├── evento_carta_1.png
        └── ... (40 card images)
```

* `main.py`: **(Do not modify)**. Controls the main game loop, the graphical user interface with Pygame, and user interaction.
* `estado.py`: Defines the company's initial state and contains the `calcular_estado_final()` function, which processes the results of each turn.
* `acciones.py`: Implements the logic for all player decisions in the areas of Production, Human Resources, Marketing, Purchasing, and Finance.
* `cartas.py`: Implements the logic for the 40 "Chaos Cards" that introduce random events into the game.
* `img/`: Contains all graphical assets, such as backgrounds for each area and images for each event card.

### Requirements

* Python 3.x
* Pygame

### Installation

1.  Ensure you have Python 3 installed on your system.
2.  Install the Pygame library using pip:
    ```bash
    pip install pygame
    ```

### How to Play

1.  Navigate to the project's root folder from your terminal.
2.  Run the program with the following command:
    ```bash
    python main.py
    ```
3.  Use the `<` and `>` buttons to navigate between the five company areas.
4.  For each area, click the **`Cambiar`** button, enter the number of the desired action, and press **`OK`**.
5.  Once you have set the actions for all five areas, click the **`Tomar carta`** button.
6.  Enter a number from 1 to 40 to simulate a chaos card and press **`OK`**.
7.  Click **`Continuar`** to end the turn.
8.  To review the results and see how your company's state has changed, click the **`Estado de la Empresa`** button.

### Professor's Note
As per the instructions from Professor Ian B., the logic for the **actions** must be standardized and copied from the course forum for the final presentation. It is recommended to also check the forum for the card logic to ensure consistency with other groups.

### Author(s)

* Luis Jaime Docarmo Rodriguez
* Martin Emilio Espinoza Reto
* Cristopher Wilson Calero Ccana
* Ítalo Pablo Roque Martínez
* Giordano Gonzales Balladares Vilchez
