import time, os, sys

os.system("clear")

print(time.time())

i = 0

while i <= 10000:
    i += 1

print(time.time())

sys.stdout.write("Fim do programa")