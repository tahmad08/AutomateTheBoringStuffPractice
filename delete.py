def angle(hour, minute):
    ang = (30*hour - (5.5*minute))%360
    return ang
print(angle(3,27))

hora = 3
minuto = 27
anglo = 360 - ((hora*30 - 5.5*minuto)%360)
print(anglo)
