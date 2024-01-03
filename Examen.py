# Viaje por carretera con búsqueda de coste uniforme
import functools
from arbol import Nodo

def compara(x, y):
    return x.get_coste() - y.get_coste()

def buscar_solucion_UCS(conexiones, estado_inicial, solucion):
    solucionado=False
    nodos_visitados=[]
    nodos_frontera=[]
    nodo_inicial = Nodo(estado_inicial)
    nodo_inicial.set_coste(0) #costo
    nodos_frontera.append(nodo_inicial)
    while (not solucionado) and len(nodos_frontera)!=0:
        # ordenar la lista de nodos frontera
        nodos_frontera = sorted(nodos_frontera, key= functools.cmp_to_key(compara))
        nodo=nodos_frontera[0]
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo.get_datos() == solucion:
            # solución encontrada
            solucionado=True
            return nodo
        else:
            # expandir nodos hijo (ciudades con conexión)
            dato_nodo = nodo.get_datos()
            lista_hijos=[]
            for un_hijo in conexiones[dato_nodo]:
                hijo=Nodo(un_hijo)
                coste = conexiones[dato_nodo][un_hijo]
                hijo.set_coste(nodo.get_coste() + coste)
                
                lista_hijos.append(hijo)
                if not hijo.en_lista(nodos_visitados):
                    # si está en la lista lo sustituimos con
                    # el nuevo valor de coste si es menor
                    if hijo.en_lista(nodos_frontera):
                        for n in nodos_frontera:
                            if n.igual(hijo) and n.get_coste()>hijo.get_coste():
                                nodos_frontera.remove(n)
                                nodos_frontera.append(hijo)
                    else:
                        nodos_frontera.append(hijo)
                    nodo.set_hijos(lista_hijos)

if __name__ == "__main__":
    conexiones = {
        'CDMX': {'SLP':11,'MEXICALI':12,'CHIHUAHUA':15},
        'SAPOPAN': {'ZACATECAS':14,'MEXICALI':23},
        'GUADALAJARA':{'CHIAPAS':23},
        'CHIAPAS':{'CHIHUAHUA':34},
        'MEXICALI':{'SLP':56,'SAPOPAN':23,'CDMX':45,'CHIHUAHUA':67,'SONORA':98},
        'SLP':{'CDMX':67,'MEXICALI':84},
        'ZACATECAS':{'SAPOPAN':75,'SONORA':32,'CHIHUAHUA':63},  
        'SONORA':{'ZACATECAS':95,'MEXICALI':76},
        'MICHOACAN':{'CHIHUAHUA':65},
        'CHIHUAHUA':{'MICHOACAN':54,'ZACATECAS':54,'MEXICALI':43,'CDMX':95,'CHIAPAS':43}
    }
    estado_inicial='CDMX'
    solucion='ZACATECAS'
    libras = '90lb'
    nodo_solucion = buscar_solucion_UCS(conexiones, estado_inicial, solucion)
    # mostrar resultado
    resultado=[]
    nodo=nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print("Ruta más Corta:")
    print(resultado)
    print("Kilometros: " + str(nodo_solucion.get_coste()) +"km")
    peaje ={
        'CDMX': {'SLP':11,'MEXICALI':12,'CHIHUAHUA':15},
        'SAPOPAN': {'ZACATECAS':14,'MEXICALI':23},
        'GUADALAJARA':{'CHIAPAS':23},
        'CHIAPAS':{'CHIHUAHUA':34},
        'MEXICALI':{'SLP':56,'SAPOPAN':23,'CDMX':45,'CHIHUAHUA':67,'SONORA':98},
        'SLP':{'CDMX':67,'MEXICALI':84},
        'ZACATECAS':{'SAPOPAN':75,'SONORA':32,'CHIHUAHUA':63},  
        'SONORA':{'ZACATECAS':95,'MEXICALI':76},
        'MICHOACAN':{'CHIHUAHUA':65},
        'CHIHUAHUA':{'MICHOACAN':54,'ZACATECAS':54,'MEXICALI':43,'CDMX':95,'CHIAPAS':43}
    }
    #print(peaje['Nuevo Laredo']['Monterrey'])
    suma = 0
    for i in range(len(resultado)-1):
        suma += peaje[resultado[i]][resultado[i+1]]
    print("Tamaño Caja: " + libras)
    print()
    
    nodo_solucion = buscar_solucion_UCS(peaje, estado_inicial, solucion)
    # mostrar resultado
    resultado=[]
    nodo=nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()