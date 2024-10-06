import sqlite3

conn = sqlite3.connect('mi_base_de_datos.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS mensajes
             (id INTEGER PRIMARY KEY, nombre TEXT, email TEXT, mensaje TEXT)''')

conn.commit()
conn.close()
