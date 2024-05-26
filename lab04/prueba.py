from magpylib.source.magnet import Cylinder
x = Cylinder(mag=(500,0,500), dim=(4,5))

print(x.getB((4,4,4)))      # Salida: [7.698 15.407 6.401]
print(x.position)           # Salida: [0 0 0]
print(x.angle)              # Salida: 0
print(x.axis)               # Salida: [0 0 1]
print(x.dimension)          # Salida: [4 5]
print(x.magnetization)      # Salida: [500 0 500]

x.rotate(90, (0,0,1), anchor=(4,4,0))

print(x.getB((4,4,4)))      # Salida: [-15.407 7.698 6.401]
print(x.position)           # Salida: [8 0 0]
print(x.angle)              # Salida: 90
print(x.axis)               # Salida: [0 0 1]
print(x.dimension)          # Salida: [4 5]
print(x.magnetization)      # Salida: [500 0 500]


