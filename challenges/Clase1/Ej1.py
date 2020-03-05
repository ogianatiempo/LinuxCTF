import os

try:
    folder = os.listdir("./aca_adentro")
    files = os.listdir("./aca_adentro/frutas")

    if folder == ['frutas'] and files == ['manzana.jpg', 'banana.txt', 'tomate.exe']:
        c = [0, 0, 0, 0, 0, 0, 0, 0, 36, 11, 53, 60, 125, 7, 9, 49, 73, 49, 39, 96, 25, 119, 56, 100, 63, 37, 95, 30, 75, 2, 22, 118, 44, 53, 41]
        k = [76, 105, 110, 117, 120, 67, 84, 70, 95, 70, 84, 87]
        o = ""
        for i in range(len(c)):
            o += chr(c[i] ^ k[i%len(k)])
        print(o)
    else:
        print("No se encontraron los archivos correctos")
except FileNotFoundError:
    print("No se encontraron los archivos correctos")