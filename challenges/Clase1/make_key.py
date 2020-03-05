import os

folder = os.listdir("./aca_adentro")
files = os.listdir("./aca_adentro/frutas")

folder.extend(files)

t = "LinuxCTF{M4k1ngD1rs4ndF1l3sL1k34B0ss}"
k = "".join(folder)

print(len(t))
print(k)
print(len(k))

c = []
for i in range(len(t)):
    c.append(ord(t[i]) ^ ord(k[i%len(k)]))
print(c)