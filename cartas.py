# cartas.py
import math


def aplicar_carta(numero, estado):
    # --- Verificación de Cartas de Protección ---
    if numero in [5, 10, 11, 16, 25, 27, 32, 35, 36, 37] and estado.get("Fondo emergencia", False):
        estado["Fondo emergencia"] = False;
        return estado
    if numero in [2, 8] and estado.get("TurnosProteccionMantenimiento", 0) > 0: return estado
    if numero == 9 and estado.get("TurnosProteccionClima", 0) > 0: return estado
    if numero in [4, 37, 38] and estado.get("TurnosProteccionSeguridad", 0) > 0: return estado
    if numero in [12, 17, 19, 20, 23, 26, 29, 33, 34] and (
            estado.get("TurnosProteccionDemanda", 0) > 0 or estado.get("TurnosProteccionReputacion",
                                                                       0) > 0): return estado
    if numero == 3 and estado.get("TurnosProteccionEcommerce", 0) > 0: return estado

    # --- Lógica de cada carta ---
    if numero == 1:
        return estado
    elif numero == 2:  # Falla critica en maquinaria
        t, a, d = map(int, estado["Maquinas (total/activas/dañadas)"].split('/'));
        m = min(a, 2)
        estado["Maquinas (total/activas/dañadas)"] = f"{t}/{a - m}/{d + m}"
    elif numero == 3:  # Virus informatico
        estado["TurnosSinVisibilidad"] = 2;
        estado["Prohibir Produccion"] = True;
        estado["NoVenderEsteTurno"] = True
        n = int(estado["Reputacion del mercado"].split(" ")[1]);
        estado["Reputacion del mercado"] = f"Nivel {max(1, n - 1)}"
    elif numero == 4:
        estado["Inventario"] = 0
    elif numero == 5:  # Auditoria desfavorable
        estado["Multas e indemnizaciones"] += 5000
        n = int(estado["Reputacion del mercado"].split(" ")[1]);
        estado["Reputacion del mercado"] = f"Nivel {max(1, n - 1)}"
    elif numero == 6:  # Producto retirado del mercado
        n = int(estado["Reputacion del mercado"].split(" ")[1]);
        estado["Reputacion del mercado"] = f"Nivel {max(1, n - 2)}"
        estado["Inventario"] = max(0, estado["Inventario"] - estado["Pedidos por atender"]);
        estado["ReduccionDemandaProductoRetirado"] = 2
    elif numero == 7:
        estado["Insumos disponibles"] = math.floor(estado["Insumos disponibles"] * 0.70)
    elif numero == 8:  # Fuga de talento clave
        t, a, d = map(int, estado["Maquinas (total/activas/dañadas)"].split('/'));
        if a > 0: estado["Maquinas (total/activas/dañadas)"] = f"{t}/{a - 1}/{d + 1}"
        if estado["Cantidad de empleados"] > 0: estado["Cantidad de empleados"] -= 1
    elif numero == 9:  # Huelga por ambiente laboral
        estado["Prohibir Produccion"] = True;
        n = int(estado["Reputacion del mercado"].split(" ")[1]);
        estado["Reputacion del mercado"] = f"Nivel {max(1, n - 3)}"
    elif numero == 10:  # Hacker secuestra datos
        r = 5000;
        f = max(0, r - estado["Caja disponible"]);
        estado["Caja disponible"] = max(0, estado["Caja disponible"] - r);
        estado["Deuda pendiente"] += f * 1.12
        n = int(estado["Reputacion del mercado"].split(" ")[1]);
        estado["Reputacion del mercado"] = f"Nivel {max(1, n - 2)}";
        estado["Multas e indemnizaciones"] += 5000
    elif numero == 11:  # Multa ambiental
        estado["Multas e indemnizaciones"] += 5000;
        n = int(estado["Reputacion del mercado"].split(" ")[1]);
        estado["Reputacion del mercado"] = f"Nivel {max(1, n - 1)}"
    elif numero == 12:
        estado["ReduccionVentasBoicot"] = 2
    elif numero == 13:  # Error de etiquetado
        c = (estado["Ventas del turno anterior"] * estado["Precio de venta"]) + 15000;
        f = max(0, c - estado["Caja disponible"])
        estado["Caja disponible"] = max(0, estado["Caja disponible"] - c);
        estado["Deuda pendiente"] += f * 1.12
    elif numero == 14:
        estado["Prohibir Importaciones"] = True
    elif numero == 15:
        estado["Prohibir Compras Nacionales"] = True
    elif numero == 16:
        estado["Caja disponible"] = max(0, estado["Caja disponible"] - 8000)
    elif numero == 17:
        n = int(estado["Reputacion del mercado"].split(" ")[1]); estado[
            "Reputacion del mercado"] = f"Nivel {max(1, n - 2)}"
    elif numero == 18:
        estado["TurnosProduccionPlaga"] = 3
    elif numero == 19:
        estado["Pedidos por atender"] = math.floor(estado["Pedidos por atender"] * (2 / 3))
    elif numero == 20:
        n = int(estado["Reputacion del mercado"].split(" ")[1]); estado[
            "Reputacion del mercado"] = f"Nivel {max(1, n - 3)}"
    elif numero == 21:
        estado["Prohibir Produccion"] = True
    elif numero == 22:
        estado["Multas e indemnizaciones"] += 30000; estado["Prohibir Produccion"] = True
    elif numero == 23:
        n = int(estado["Reputacion del mercado"].split(" ")[1]); estado[
            "Reputacion del mercado"] = f"Nivel {max(1, n - 2)}"
    elif numero == 24:
        estado["TurnosSinVentasBloqueo"] = 2
    elif numero == 25:
        estado["Multas e indemnizaciones"] += 15000
    elif numero == 26:
        estado["ReduccionVentasCompetidor"] = 3; estado["Multas e indemnizaciones"] += 5000
    elif numero == 27:
        estado["Caja disponible"] = max(0, estado["Caja disponible"] - 10000)
    elif numero == 28:
        estado["AumentoCostosCrisis"] = 5
    elif numero == 29:
        n = int(estado["Reputacion del mercado"].split(" ")[1]); estado[
            "Reputacion del mercado"] = f"Nivel {max(1, n - 2)}"; estado["ReduccionVentas75"] = True
    elif numero == 30:
        estado["TurnosSinOperacionesHuelgaNacional"] = 3; estado["Multas e indemnizaciones"] += 10000
    elif numero == 31:
        estado["NoVenderEsteTurno"] = True; estado["Multas e indemnizaciones"] += 10000
    elif numero == 32:
        estado["Caja disponible"] = max(0, estado["Caja disponible"] - 7000)
    elif numero == 33:
        estado["NoVenderEsteTurno"] = True; n = int(estado["Reputacion del mercado"].split(" ")[1]); estado[
            "Reputacion del mercado"] = f"Nivel {max(1, n - 2)}"
    elif numero == 34:
        estado["TurnosReduccionVentasEmpaque"] = 2; n = int(estado["Reputacion del mercado"].split(" ")[1]); estado[
            "Reputacion del mercado"] = f"Nivel {max(1, n - 2)}"
    elif numero == 35:
        n = int(estado["Reputacion del mercado"].split(" ")[1]); estado[
            "Reputacion del mercado"] = f"Nivel {max(1, n - 3)}"; estado["Multas e indemnizaciones"] += 30000
    elif numero == 36:
        estado["Caja disponible"] = max(0, estado["Caja disponible"] - 15000); estado[
            "Deuda pendiente"] += 15000; n = int(estado["Reputacion del mercado"].split(" ")[1]); estado[
            "Reputacion del mercado"] = f"Nivel {max(1, n - 2)}"
    elif numero == 37:  # Trabajador se accidenta
        estado["Multas e indemnizaciones"] += 4000
        if estado["Cantidad de empleados"] > 0: estado["Cantidad de empleados"] -= 1; estado[
            "TurnosEmpleadoAccidentado"] = 2; estado["_empleado_accidentado_flag"] = True
    elif numero == 38:
        estado["Inventario"] = 0; estado["Insumos disponibles"] = 0; estado["TurnosSinProduccionDerrame"] = 2
    elif numero == 39:
        estado["Prohibir Produccion"] = True; estado["NoVenderEsteTurno"] = True
    elif numero == 40:
        estado["Prohibir Contratacion"] = True

    return estado