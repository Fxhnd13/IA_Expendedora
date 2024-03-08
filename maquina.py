estados = ['sin-moneda', 'recibi-moneda', 'servido-c1', 'servido-c2', 'servido-c3']
percepciones = ['moneda', 'c1', 'c2', 'c3', 'servido']
reglas = {
    'sin-moneda': 'pedir-moneda',
    'recibi-moneda': 'pedir-codigo',
    'servido-c1': 'servir-c1-esperar',
    'servido-c2': 'servir-c2-esperar',
    'servido-c3': 'servir-c3-esperar'
}

acciones = {
    'pedir-moneda':      "---------------- Ingrese una moneda ---------------",
    'pedir-codigo':      "---------- Ingrese el código del refresco ---------",
    'servir-c1-esperar': "----- Sirviendo refresco 1, por favor, espere -----",
    'servir-c2-esperar': "----- Sirviendo refresco 2, por favor, espere -----",
    'servir-c3-esperar': "----- Sirviendo refresco 3, por favor, espere -----"
}

modelo = {
    ('sin-moneda', 'pedir-moneda', 'moneda'): 'recibi-moneda',
    ('recibi-moneda', 'pedir-codigo', 'c1'): 'servido-c1',
    ('recibi-moneda', 'pedir-codigo', 'c2'): 'servido-c2',
    ('recibi-moneda', 'pedir-codigo', 'c3'): 'servido-c3',
    ('recibi-moneda', 'pedir-codigo', 'moneda'): 'recibi-moneda',
    ('servido-c1', 'servir-c1-esperar', 'servido'): 'sin-moneda',
    ('servido-c2', 'servir-c2-esperar', 'servido'): 'sin-moneda',
    ('servido-c3', 'servir-c3-esperar', 'servido'): 'sin-moneda'
}

def actualizar_estado(estado, accion, percepcion):
    if (estado, accion, percepcion) in modelo:
        return modelo[(estado, accion, percepcion)]
    else:
        return 'sin-moneda'

estado_actual = 'sin-moneda'
accion_actual = 'pedir-moneda'
percepcion = 'espera'

while percepcion != 'salir':
    print(acciones[accion_actual])
    percepcion = input("Ingresar percepcion: ") 
    estado_actual = actualizar_estado(estado_actual, accion_actual, percepcion)
    accion_actual = reglas[estado_actual]