def generador():
    n = 1
    yield n

    n += 1
    yield n
    
    n += 2
    yield n
    
    n += 4
    yield n

gen1 = generador()

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))


gen1 = generador(1)


def generador()