def water_left(astronauts, water, days_left):
    for argument in [astronauts, water, days_left]:
        try:
            argument / 10
        except TypeError:
            raise TypeError(f"All arguments must be of type int, but received: '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    totalwater_left = water - total_usage
    if totalwater_left < 0:
        raise RuntimeError(f"No hay suficiente agua para {astronauts} astronautas pasando {days_left} días!")
    return f"Total de agua pasando {days_left} días son: {totalwater_left} litros"
water_left(5, 100, 2)
