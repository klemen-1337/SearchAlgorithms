import os
from typing import List, Tuple
from SearchAlgorithms import Bfs, Dfs

# Prebere vsebino datoteke ter vrne P,N, seznam z vrsticami matrike.
def read_file(file_name: str) -> Tuple[int, int, List[List[str]]]:

    with open(file_name, 'r') as f:
        lines = [[cube.strip() for cube in lines.split(",")] for lines in f]

    return len(lines[0]), len(lines),lines

# Prebere uporabnikov vnos kater algoritem izbere za preiskovanje prostora,
# poleg tega zažene algoritem, ki je bil izbran znotraj switcherja.
def read_input():

    try:
        input_algorithm = int(input())
    except ValueError:
        print("Please input integer only")

    switcher={
            1:Dfs.main(),
            2:Bfs.main()
            }

    return switcher.get(input_algorithm, "Please choose a valid algorithm")

# Pregleda koliko mest (vertikalno) je še prostih, da lahko nanje položimo kocke
# vrne seznam, ki za vsak stolpec pove število prostih.
def check_status(matrix: List[List[str]]) -> List[int]:

    status = [0] * len(matrix)

    for line in matrix:
        for ind, spot in enumerate(line):
            if(not spot[1].isalpha()):
                status[ind] += 1

    return status

# Vsebuje sam premik elementa iz p-te pozicije,
# na r-to pozicijo. Če je kock več, da na vrh sklada.
# Vrne zapis v obliki PRESTAVI p,r
# Preveri tudi, če je premik veljaven, drugače ga ne opravi.
def move(p: int, r: int) -> str:

    status = check_status(input_matrix)

    if(validate_move(p, r)):

        # Vzameš element iz mesta p-1
        char_line = input_matrix[status[p-1]]
        char = char_line[p-1]
        char_line.remove(char)
        char_line.insert(p-1, "' '")

        # Postaviš element na mesto r-1
        char_line2 = input_matrix[status[r-1]-1]
        char2 = char_line2[r-1]
        char_line2.remove(char2)
        char_line2.insert(r-1, char)


# Pregleda če je željen premik veljaven, vrne true/false
def validate_move(p: int, r: int) -> bool:

    status = check_status(input_matrix)

    if(status[p-1] > 0 and status[r-1] > 0 and p != r):
        return True

    return False

# P == Št odstavnih položajev (št. stolpcev v matriki)
# N == Št možnik škatel na posameznam odstavnem položaju (št. vrstic v matriki)
P, N, input_matrix = read_file("Data/primer1_zacetna.txt")

def main():

    print("Please choose an algoririthm to run: \n(press a number)\n")
    print("1. DFS \t 2. BFS\n")
    print(read_input())

    for line in input_matrix:
        print(line)

    move(1, 2)
    print()


    for line in input_matrix:
        print(line)



if __name__ == '__main__':
    main()