from compras import*

def test_lee_compras(compras:list[Compra]):
    print('\ntest_lee_compras')
    print("\nnumero de registros leidos es: ", len(compras))
    print("\nlos tres primeros son: ", compras[:3])
    print("\nlos tres ultimos son: ", compras[-3:])

def test_compra_maxima_minima_provincia(compras:list[Compra]):
    print("\ntest_compra_maxima_minima_provincia")
    prov = "Huelva"
    prov2 = None
    print(f"importe maximo de la provincia de {prov} es: {compra_maxima_minima_provincia(compras, prov)[0]}.\
        importe minimo: {compra_maxima_minima_provincia(compras, prov)[1]}")
    print(f"importe maximo de la provincia de {prov2} es: {compra_maxima_minima_provincia(compras, prov2)[0]}.\
        importe minimo: {compra_maxima_minima_provincia(compras, prov2)[1]}")
    
def test_horas_menos_afluencia(compras:list[Compra]):
    print("\ntest_horas_menos_afluencia")
    print(f"la hora con menos afluencia es: {horas_menos_afluencia(compras)[0]}\
        con {horas_menos_afluencia(compras)[1]} llegadas de clientes")
    
def test_horas_menos_afluencia2(compras:list[Compra]):
    print("\ntest_horas_menos_afluencia2")
    print(f"la hora con menos afluencia es: {horas_menos_afluencia2(compras)[0]}\
        con {horas_menos_afluencia2(compras)[1]} llegadas de clientes")
    
def test_supermercados_mas_facturacion(compras:list[Compra]):
    print("\ntest_supermercados_mas_facturacion")
    numero_marca = 2
    print(f"los {numero_marca} supermercados con mas facturacion son:\
           {supermercados_mas_facturacion(compras, numero_marca)}")
    
def test_clientes_itinerantes(compras:list[Compra]):
    print("\ntest_clientes_itinerantes")
    numero = 7
    print(f"Los clientes itinerantes que han comprado al menos en {numero} provincias son:\
           {clientes_itinerantes(compras, numero)}")
    
def test_dias_estrella(compras:list[Compra]):
    print("\ntest_dias_estrella")
    supermercado = "Aldi"
    provincia = "Huelva"
    print(f"Los días estrella del supermercado {supermercado} de la provincia de {provincia} son:", \
        dias_estrella(compras, supermercado, provincia))

if __name__=="__main__":
    datos = lee_compras("Proyectos Python\WSPython\git\lp07-compras-hadiminou-main\data\compras.csv")
    #test_lee_compras(datos)
    #test_compra_maxima_minima_provincia(datos)
    #test_horas_menos_afluencia(datos)
    #test_horas_menos_afluencia2(datos)
    #test_supermercados_mas_facturacion(datos)
    #test_clientes_itinerantes(datos)
    #test_dias_estrella(datos)