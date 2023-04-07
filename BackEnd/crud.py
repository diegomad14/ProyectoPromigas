import sqlite3
conn = sqlite3.connect('CRUD.db')
import tkinter as tk

c = conn.cursor()

def crear_insumo(nombre, cantidad):
    c.execute("INSERT INTO insumos (nombre, cantidad) VALUES (?, ?)", (nombre, cantidad))
    conn.commit()

def crear_movimiento(fecha, empleado_id, insumo_id, cantidad):
    c.execute("INSERT INTO movimientos (fecha, empleado_id, insumo_id, cantidad) VALUES (?, ?, ?, ?)", (fecha, empleado_id, insumo_id, cantidad))
    c.execute("UPDATE insumos SET cantidad = cantidad - ? WHERE id = ?", (cantidad, insumo_id))
    conn.commit()

def crear_empleado(nombre, puesto):
    c.execute("INSERT INTO empleados (nombre, puesto) VALUES (?, ?)", (nombre, puesto))
    conn.commit()

