import random

def vytvor_matici(n: int, m: int) -> list[list[int]]:
    """Vytvoří matici n x m s náhodnými celými čísly od 0 do 9."""
    return [[random.randint(0, 9) for _ in range(m)] for _ in range(n)]

def reprezentace_matice(matice: list[list[int]]) -> str:
    """Vrátí stringovou reprezentaci matice."""
    if len(matice) == 0:
        return ''
    return '\n'.join([' '.join(map(str, radek)) for radek in matice]) + '\n'

def soucet_matic(matice1: list[list[int]], matice2: list[list[int]]) -> list[list[int]]:
    """Sečte dvě matice, pokud mají stejné rozměry."""
    if matice1 == [] or matice2 == []:
        if matice1 == [] and matice2 == []:
            return []
        else:
            return None

    if len(matice1) != len(matice2) or len(matice1[0]) != len(matice2[0]):
        return None

    return [[matice1[i][j] + matice2[i][j] for j in range(len(matice1[0]))] for i in range(len(matice1))]

def nasobeni_matic(matice1: list[list[int]], matice2: list[list[int]]) -> list[list[int]]:
    """Vynásobí dvě matice, pokud je násobení proveditelné."""
    if matice1 == [] or matice2 == []:
        if matice1 == [] and matice2 == []:
            return []
        else:
            return None

    if len(matice1[0]) != len(matice2):
        return None

    return [[sum(matice1[i][k] * matice2[k][j] for k in range(len(matice2))) for j in range(len(matice2[0]))] for i in range(len(matice1))]

def transpozice_matice(matice: list[list[int]]) -> list[list[int]]:
    """Provede transpozici matice."""
    if matice == []:
        return []
    if matice == [[]]:
        return [[]]
    return [[matice[j][i] for j in range(len(matice))] for i in range(len(matice[0]))]

if __name__ == "__main__":
    matice1 = vytvor_matici(3, 2)
    matice2 = vytvor_matici(2, 4)

    print("Matice 1:")
    print(reprezentace_matice(matice1))
    print("Matice 2:")
    print(reprezentace_matice(matice2))

    soucet = soucet_matic(matice1, matice1)  # Sečteme matici1 samu se sebou
    print("Součet matic:")
    print(reprezentace_matice(soucet))

    nasobek = nasobeni_matic(matice1, matice2)
    print("Násobení matic:")
    print(reprezentace_matice(nasobek))

    transponovana = transpozice_matice(matice1)
    print("Transponovaná matice:")
    print(reprezentace_matice(transponovana))