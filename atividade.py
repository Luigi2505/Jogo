a = 0
b = 1
c = 10

while c > 0:
    a += 1
    b += 1
    c = a + b
    if c > 10:
        break

print(f"Valores finais: {a}; {b}; {c}")