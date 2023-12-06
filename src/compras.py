from collections import namedtuple, Counter, defaultdict
from datetime import date, time, datetime
from typing import*
import csv
from parsers import*

Compra = NamedTuple('Compra',[('dni', str), ('supermercado', str), ('provincia', str),\
                    ('fecha_llegada', datetime), ('fecha_salida', datetime),('total_compra', float)])

def lee_compras(ruta_fichero:str)->list[Compra]:
    res = list()
    with open(ruta_fichero, 'rt', encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ',')
        next(lector)
        for dni, supermercado, privincia, fecha_llegada, fecha_salida, total_compra in lector:
            fecha_llegada = datetime.strptime(fecha_llegada, "%d/%m/%Y %H:%M")
            fecha_salida = datetime.strptime(fecha_salida, "%d/%m/%Y %H:%M")
            total_compra = float(total_compra)
            res.append(Compra(dni, supermercado, privincia, fecha_llegada, fecha_salida, total_compra))
    return res

def compra_maxima_minima_provincia(compras:list[Compra], provincia_dado:str)->tuple[float, float]:
    aux = list()
    res = tuple()
    aux = [i.total_compra for i in compras if i.provincia == provincia_dado or provincia_dado == None]
    res = (max(aux), min(aux))
    return res

def horas_menos_afluencia(compras:list[Compra])->tuple[time, int]:
    aux = defaultdict(list)
    res = dict()
    for i in compras:
        aux[i.fecha_llegada.hour].append(i.dni)
    for c,v in aux.items():
        res[c] = len(v)
    return min(res.items(), key = lambda e:e[1])

def horas_menos_afluencia2(compras:list[Compra])->tuple[time, int]:
    res = Counter(i.fecha_llegada.hour for i in compras)
    return min(res.items(), key = lambda e:e[1])

def supermercados_mas_facturacion(compras:list[Compra], num_marca:int=3)->list[tuple[int, str, float]]:
    res = list()
    aux = defaultdict(float)
    aux2 = list()
    for i in compras:
        aux[i.supermercado]+=i.total_compra
        aux2 = sorted(aux.items(), key = lambda e:e[1], reverse = True)
    for j in range(1, num_marca+1):
        res.append((j,(aux2[j-1])))
    return res

def clientes_itinerantes(compras:list[Compra], num_cliente:int)->list[tuple[str, list]]:
    aux = defaultdict(set)
    res = list()
    for i in compras:
        aux[i.dni].add(i.provincia)
    for c,v in aux.items():
        if len(v) > num_cliente:
            res = [(c,sorted(v))]
    return res

def dias_estrella(compras:list[Compra], super:str, provincia_dado:str)->list[date]:
    res = list()
    lista_aux = list()
    aux = defaultdict(list)
    aux2 = dict()
    aux3 = dict()
    for i in compras:
        if i.supermercado == super and i.provincia == provincia_dado:
            aux[i.fecha_salida.date()].append(i.total_compra)
    for c,v in aux.items():
        aux2[c] = sum(v)
    aux3 = dict(sorted(aux2.items()))
    for c,v in aux3.items():
        lista_aux.append((c,v))
    for i in range(1, len(lista_aux)-1):
        if lista_aux[i-1][1] < lista_aux[i][1] and lista_aux[i][1] > lista_aux[i+1][1]:
            res.append(lista_aux[i][0].strftime("%d/%m/%Y")) #how to change datetime to string
    return res