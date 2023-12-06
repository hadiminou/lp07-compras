def parser(dato:str)->list[str]:
    res = list()
    for i in dato.split(" "):
        res.append(i.strip())
    #res = [(i.strip() for i in dato.split(" "))]
    return res