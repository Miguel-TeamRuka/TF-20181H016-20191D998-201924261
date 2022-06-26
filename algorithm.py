import json
import final

def graph():
    #Loc = [(10, 10), (10, 24), (23, 22), (22, 11),(60,87)]
    Loc=final.leerNodosLatLon()
    #G = [[(1, 2), (3, 1)],
    #     [(2, 3)],
    #     [(3, 3)],
    #     [(0, 2)]]
    G=final.LeerListaAd()

    response = {"loc": Loc, "g": G}

    return json.dumps(response)

def paths():
    #bestpath = [-1, 0, 1, 0]
    #path1 = [-1, 0, 1, 0]
    #path2 = [-1, 0, 1, 0]
    bestpath,path1,path2=final.rutas(21,1740)

    response = {"bestpath": bestpath, "path1": path1, "path2": path2}

    return json.dumps(response)