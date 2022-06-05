def make_car(marca, modelo, version='', puertas='', potencia='', asientos='', color='', tow_package=''):
    car = {}
    car['marca'] = marca
    car['modelos'] = modelo
    
    if version != '':
        car['version'] = version
    
    if puertas != '':
        car['puertas'] = puertas
    
    if potencia != '':
        car['potencia'] = potencia
    
    if asientos != '':
        car['asientos'] = asientos
    
    if color != '':
        car['color'] = color
    
    if tow_package != '':
        car['tow_package'] = tow_package

    print(car)



make_car(
    "bugatti",
    "veyron"
)

make_car(
    "lambo",
    "aventador",
    version="4.0 Turbo",
    puertas=5,
    tow_package=False
)

make_car(
    "subaru",
    "outback",
    color="blue",
    tow_package=True
)