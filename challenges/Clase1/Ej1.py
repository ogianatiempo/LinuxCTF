import os

try:
    folder = os.listdir("./aca_adentro")
    files = os.listdir("./aca_adentro/frutas")
    folder.extend(files)

    c = [42, 27, 27, 1, 25, 48, 57, 39, 21, 55, 85, 5, 80, 64, 13, 52, 86, 6, 28, 89, 15, 16, 35, 31, 9, 75, 22, 46, 80, 5, 82, 90, 35, 30, 7, 11, 9]
    k = "".join(folder)
    o = ""
    
    for i in range(len(c)):
        o += chr(c[i] ^ ord(k[i%len(k)]))

    if len(k) == 37 and o[8] == "{" and o[36] == "}":
        print(o)
    else:
         print("No se encontraron los archivos correctos")
    
except FileNotFoundError:
    print("No se encontraron los archivos correctos")