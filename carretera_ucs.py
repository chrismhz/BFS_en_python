# Viaje por Carretera con Busqueda de costo Uniforme
import functools
from arbol import Nodo

# x es el coste y y es el nodo de salida
def compara(x, y):
    return x.get_coste() - y.get_coste()

def buscar_solucion_UCS(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicial = Nodo(estado_inicial)
    nodo_inicial.set_coste(0)
    nodos_frontera.append(nodo_inicial)
    while (not solucionado) and len(nodos_frontera) != 0:
        # Ordenar la lista de nodos_frontera
        # Regresa una lista ordenada de orden ascendente
        nodos_frontera = sorted(nodos_frontera, key = functools.cmp_to_key(compara))
        nodo = nodos_frontera[0]
        # Extraer Nodo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo.get_datos() == solucion:
            # Solucion Encontrada
            solucionado = True
            return nodo
        else:
            # Expandir nodos hijo (Ciudades con conexiones)
            dato_nodo = nodo.get_datos()
            lista_hijos = []
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                coste = conexiones[dato_nodo][un_hijo]
                hijo.set_coste(nodo.get_coste() + coste)
                lista_hijos.append(hijo)
                if not hijo.en_lista(nodos_visitados):
                    # Si esta en la lista, lo sustituimos con el nuevo valor del coste si es menor
                    if hijo.en_lista(nodos_frontera):
                        for n in nodos_frontera:
                            if n.igual(hijo) and n.get_coste() > hijo.get_coste():
                                nodos_frontera.remove(n)
                                nodos_frontera.append(hijo)
                    else:
                        nodos_frontera.append(hijo)
                nodo.set_hijos(lista_hijos)

if __name__ == '__main__':
    conexiones = {
        'CDMX': {'SLP':423, 'EDOMEX':125, 'MICHOACAN':491},
        'EDOMEX': {'SLP':513, 'CDMX':125},
        'GUADALAJARA': {'MOTERREY':394, 'SLP':437},
        'PUEBLA': {'SLP':514},
        'QUERETARO':{'SLP':203, 'HIDALGO':390},
        'SLP': {'CDMX':423, 'EDOMEX':513, 'MICHOACAN':355, 'MONTERREY':313, 'GUADALAJARA':437, 'HIDALGO':599, 'QUERETARO':203, 'PUEBLA':514},
        'HIDALGO': {'SLP':599, 'QUERETARO':203},
        'SONORA': {'MONTERREY':296, 'MICHOACAN':346},
        'MICHOACAN': {'SLP':355, 'MONTERREY':309, 'SONORA':346},
        'MONTERREY': {'SLP':313, 'MICHOACAN':309, 'SONORA':296, 'GUADALAJARA':394}

    }

    estado_inicial = 'EDOMEX'
    solucion = 'HIDALGO'
    nodo_solucion = buscar_solucion_UCS(conexiones, estado_inicial, solucion)

    # Mostrar Resultados
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
    print('Costo: ' + str(nodo_solucion.get_coste()))