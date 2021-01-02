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

def main():

    print("Please choose an algoririthm to run: \n(press a number)\n")
    print("1. DFS \t 2. BFS\n")
    print(read_input())

    # P == Št odstavnih položajev (št. stolpcev v matriki)
    # N == Št možnik škatel na posameznam odstavnem položaju (št. vrstic v matriki)
    P, N, input_matrix = read_file("Data/primer1_zacetna.txt")

if __name__ == '__main__':
    main()