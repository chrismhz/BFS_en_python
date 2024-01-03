#VUELOS CON BUSQUEDA EN AMPLITUD
from arbol import Nodo

def buscar_solucion_bfs(conexiones,estado_incial,solucion):
    solucionado=False
    nodos_visitados=[]
    nodos_frontera=[]
    nodo_inicial=Nodo(estado_incial)
    nodos_frontera.append(nodo_inicial)
    while not solucionado and len(nodos_frontera)!=0:
        nodo=nodos_frontera[0]
        #extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))

        if nodo.get_datos() == solucion:
            #la solucion encobtrada 
            solucionado=True
            return nodo
        else:
            #EXPANDIR LOS NODOS HIJO
            dato_nodo=nodo.get_datos()
            lista_hijos=[]

            for h in conexiones[dato_nodo]:
                hijo=Nodo(h)
                lista_hijos.append(hijo)
                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    nodos_frontera.append(hijo)

            nodo.set_hijos(lista_hijos)

if __name__=="__main__":
        conexiones = {
            'CDMX': {'SLP', 'MEXICALI', 'CHIHUAHUA'},
            'SAPOPAN': {'ZACATECAS', 'MEXICALI'},
            'GUADALAJARA': {'CHIAPAS'},
            'CHIAPAS': {'CHIHUAHUA'},
            'MEXICALI':{'SLP', 'SAPOPAN', 'CDMX', 'CHIHUAHUA', 'SONORA'},
            'SLP': {'CDMX', 'MEXICALI'},
            'ZACATECAS': {'SAPOPAN', 'SONORA', 'CHIHUAHUA'},
            'SONORA': {'ZACATECAS', 'MEXICALI'},
            'MICHOACAN': {'CHIHUAHUA'},
            'CHIHUAHUA': {'MICHOACAN', 'ZACATECAS', 'MEXICALI', 'CDMX', 'CHIAPAS'}
        }

        estado_incial='CDMX'
        solucion='ZACATECAS'
        nodo_solucion= buscar_solucion_bfs(conexiones, estado_incial, solucion)
        #mostrar resultado
        resultado=[]
        nodo=nodo_solucion
        while nodo.get_padre()!=None:
            resultado.append(nodo.get_datos())
            nodo=nodo.get_padre()
        resultado.append(estado_incial)
        resultado.reverse()
        print(resultado)    