import os
from typing import List, Tuple
from copy import deepcopy

# Prebere vsebino datoteke ter vrne P,N, seznam z vrsticami matrike.
def read_file(file_name: str) -> Tuple[int, int, List[List[str]]]:

    with open(file_name, 'r') as f:
        lines = [[cube.strip() for cube in lines.split(",")] for lines in f]

    return len(lines[0]), len(lines),lines

# Prebere uporabnikov vnos kater algoritem izbere za preiskovanje prostora,
# poleg tega zažene algoritem, ki je bil izbran znotraj switcherja.
def read_input():

    try:
        input_algorithm = input()
    except ValueError:
        print("Please input integer only")

    return {
        #"1": dfs(input_matrix, end_matrix, 0),
        "2" : bfs(input_matrix, end_matrix)
    }.get(input_algorithm, "Please choose a valid algorithm")

# Vsebuje sam premik elementa iz p-te pozicije,
# na r-to pozicijo. Če je kock več, da na vrh sklada.
# Preveri tudi, če je premik veljaven, drugače ga ne opravi.
def move(matrix, p: int, r: int):

    matrix = deepcopy(matrix)

    if p == r \
            or len([x[r-1] for x in matrix if x[r-1] != "' '"]) == N \
            or len([x[p-1] for x in matrix if x[p-1] != "' '"]) == 0:
        return False

    foo = None

    for y in range(len(matrix)):
        if matrix[y][p-1] != "' '":
            foo = matrix[y][p-1]
            matrix[y][p-1] = "' '"
            break
    for y in reversed(range(0, len(matrix))):
        if matrix[y][r-1] == "' '":
            matrix[y][r-1] = foo
            break

    return matrix


states = []
commands = []

def dfs(input_matrix, end_matrix, depth):

    global states

    states.append(input_matrix)

    if(input_matrix == end_matrix):
        for line in input_matrix:
            print(line)
        return True

    # Če spreminjamo globino, lahko z zmanjšanjem najde rešitev kasneje, vendar je bolj optimalna.
    if(depth == 40):
        return False

    for i in range(1, P+1):
        for j in range (1, P+1):
            a = move(input_matrix, i, j)
            if a:
                if a not in states:
                    if dfs(a, end_matrix, depth+1):
                        commands.append("PRESTAVI " + str(i) + " " + str(j))
                        return True

    return False

def backtrace(dict, input_matrix, end_matrix):

    path = [(end_matrix, None, None)]

    while path[-1][0] != input_matrix:
        item = dict.get(str(path[-1][0]))
        path.append(item)

    path.reverse()
    print()
    for line, i, j in path:
        for ele in line:
            print(ele)
        if(i and j):
            commands.append("PREMIK: " + str(i) + " " + str(j))
        print()

    commands.reverse()
    return path

def bfs(input_matrix, end_matrix):

    # Slovar otrok: starš
    dict = {}

    # Statistika
    levels = 1
    nodes = 0
    nodes_generated = 1

    # Naslednji nivo
    next_level = []

    # V vrsto trenurnega nivoja dodamo začetni node
    current_level = [input_matrix]
    # Nastavimo začetni node na obiskan
    states.append(input_matrix)

    # Iteriramo dokler ne obiščemo vseh, ali pa najdemo rezultat
    while True:

        current_node = current_level.pop(0)
        nodes += 1

        # Ustavitveni pogoj
        if current_node == end_matrix:
            for line in current_node:
                print(line)
            # Pri BFS je enako, kot sama dolžina traca, saj je rešitev vedno optimalna.
            print("\nŠtevilo obiskanih nivojev: ", levels)
            print("Število premikov za rešitev: ", levels - 1)
            print("Število obdelanih vozlišč: ", nodes)
            print("Število generiranih vozlišč: ", nodes_generated)
            return backtrace(dict, input_matrix, current_node)

        for i in range(1, P+1):
            for j in range(1, P+1):
                a = move(current_node, i, j)
                if a:
                    nodes_generated += 1
                    if a not in states:

                        states.append(a)
                        child = str(a)
                        dict[child] = (current_node, i, j)

                        next_level.append(a)

        if (len(current_level) == 0):
            levels+=1
            current_level = next_level.copy()
            next_level = []

    return True

def main():
    print("Your input matrix is :")
    for line in input_matrix:
        print(line)
    print()

    print("Please choose an algoririthm to run: \n(press a number)\n")
    print("1. DFS \t 2. BFS")

    read_input()
    print()

    print("Zaporedje ukazov, ki pripelje do podane rešitve: ")
    commands.reverse()
    print(commands)

# P == Št odstavnih položajev (št. stolpcev v matriki)
# N == Št možnik škatel na posameznam odstavnem položaju (št. vrstic v matriki)
P, N, input_matrix = read_file("Data/primer2_zacetna.txt")
_, _, end_matrix = read_file("Data/primer2_koncna.txt")


if __name__ == '__main__':
    main()