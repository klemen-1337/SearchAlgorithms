import os
from typing import List, Tuple
from copy import deepcopy
from timeit import default_timer as timer

# Statistika
levels = 1
nodes = 1
nodes_generated = 1

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
        while input_algorithm not in {"1","2","3","4"}:
            input_algorithm = input()

        runAlgoritm(input_algorithm,input_matrix,end_matrix)
    except ValueError:
        print("Please input integer only")

def runAlgoritm(num,input_matrix, end_matrix):
    start = timer()
    if(num=="1"):dfs(input_matrix, end_matrix, 0)
    if(num=="2"):bfs(input_matrix, end_matrix)
    if(num == "3"):greedy(input_matrix,end_matrix)
    if(num == "4"):initializeastar(input_matrix,end_matrix)
    end = timer()
    print()
    print(f"Cas izvajanja: {end - start}")
    print("\nŠtevilo obiskanih nivojev: ", levels)
    print("Število premikov za rešitev: ", len(commands))
    print("Število obdelanih vozlišč: ", nodes)
    print("Število generiranih vozlišč: ", nodes_generated)
    print()




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
    global nodes
    global levels
    global nodes_generated

    states.append(input_matrix)

    # Ustavitveni pogoj, z ispisom
    if(input_matrix == end_matrix):
        for line in input_matrix:
            print(line)
        return True

    # Če spreminjamo globino, lahko z zmanjšanjem najde rešitev kasneje, vendar je bolj optimalna.
    if(depth == 40):
        return False

    for i in range(1, P+1):
        for j in range (1, P+1):
            nodes_generated += 1
            nodes += 1
            a = move(input_matrix, i, j)
            if a:
                if a not in states:
                    if dfs(a, end_matrix, depth+1):
                        commands.append("PRESTAVI " + str(i) + " " + str(j))
                        print()
                        for line in a:
                            print(line)
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
    return

def bfs(input_matrix, end_matrix):

    # Slovar otrok: starš
    dict = {}

    # Naslednji nivo
    next_level = []

    # V vrsto trenurnega nivoja dodamo začetni node
    current_level = [input_matrix]
    # Nastavimo začetni node na obiskan
    states.append(input_matrix)

    # Iteriramo dokler ne obiščemo vseh, ali pa najdemo rezultat
    while True:

        global nodes
        global levels
        global nodes_generated

        current_node = current_level.pop(0)
        nodes += 1

        # Ustavitveni pogoj z ispisom
        if current_node == end_matrix:
            for line in current_node:
                print(line)
            # Pri BFS je enako, kot sama dolžina traca, saj je rešitev vedno optimalna.
            return backtrace(dict, input_matrix, current_node)

        # BFS
        for i in range(1, P+1):
            for j in range(1, P+1):
                a = move(current_node, i, j)
                if a:
                    nodes_generated += 1
                    if a not in states:
                        states.append(a)
                        # Slovar child: parent
                        child = str(a)
                        dict[child] = (current_node, i, j)

                        next_level.append(a)

        if (len(current_level) == 0):
            levels+=1
            current_level = next_level.copy()
            next_level = []

    return True


def heuristic(char,input_matrix,end_matrix):
    #spremenljivke za x in y vrednost crke v matriki
    current_x,current_y=0,0
    end_x,end_y=0,0

    #loop cez vse elemente matrike sproti pregleduje in input_matrix in end_matrix
    #ce najde element v matriki, ki je isti kot char shrani indexe x in y
    for index_y,line_y in enumerate(input_matrix):
        for index_x,line_x in enumerate(input_matrix):
            if char == input_matrix[index_y][index_x]:
                current_x=index_x
                current_y=index_y
            if char == end_matrix[index_y][index_x]:
                end_x=index_x
                end_y=index_y

    #Ce je pregledovana crka enaka kot željena AND da je v trenutni matrici to prazno mesto
    if char == end_matrix[end_y][end_x] and not any(letter.isalpha() for letter in input_matrix[end_y][end_x]):

        count = False
        #pregledujemo, ce so pod željenim mestom vse črke pravilno postavljene
        if all(input_matrix[y][end_x]==end_matrix[y][end_x] for y in range(end_y+1, len(input_matrix))):
            count=True

        #če so črke pravilno postavlene, dobi prioriteto vrnemo index kam moramo premikati
        if count==True:
            return -10 , end_x
    #drugaće vrnemo prioriteto, koliko smo odaljeni od željene pozicije
    return abs(end_x-current_x)+abs(end_y-current_y),-1

#pregledamo, v katere stolpce lahko premaknemo željeno črko
def posible_moves(char,input_matrix,end_matrix):
    #pridobimo višino in širitno
    #inicializiramo posible z samimi 1 in char_index
    height=len(input_matrix)
    width=len(input_matrix[0])
    posible=[1]*width
    char_index=-10

    #gre cez matriko ampak najprej cez stolp in nato cez vrstice, da lahko pregledamo od vrha do dna "stacka"
    for x in range(0,width):
        for y in range(0,height):

            #ce smo naleteli na isto crko, katero zelimo premikati (je ne moremo prestaviti v isti "stack")
            if input_matrix[y][x] == char:
                posible[x]=0
                char_index=x

    return char_index,posible

#pregledamo katere črke se lahko premika(da ni prazno oz že postavljena)
def posible_to_move(input_matrix,end_matrix):
    # pridobimo višino in širitno
    # inicializiramo posible z samimi 0 in char_index
    height = len(input_matrix)
    width = len(input_matrix[0])
    posible = [0] * width

    # gre cez matriko ampak najprej cez stolp in nato cez vrstice, da lahko pregledamo od vrha do dna
    for x in range(0,width):
        for y in range(0,height):

            #ce element vsebuje kaksn alfanumericni znak in ce element ni na svojemu mestu
            if any(letter.isalpha() for letter in input_matrix[y][x]) and input_matrix[y][x]!=end_matrix[y][x]:
                posible[x]=input_matrix[y][x]
                break

    return posible


def izpis(matrix):
    print()
    for line in matrix:
        print(line)


mozniPremikiMatrike=[]
def greedy(input_matrix,end_matrix):

    mozniPremikiMatrike.append(input_matrix)
    izpis(input_matrix)

    global nodes
    global levels
    global nodes_generated

    if(input_matrix==end_matrix):
        return True

    nodes += 1
    min_char = ''
    min_razd = 10000
    indexPremika=-1

    #pridobimo katere elemente lahko premikamo
    for char in posible_to_move(input_matrix,end_matrix):
        if char!=0:
            #izracunamo hevristiko za vsak element
            razd,indexPremika=heuristic(char,input_matrix,end_matrix)
            nodes_generated += 1

            #ce hevristika vidi, da lahko element premaknemo na končno lokacijo, ne pregledujemo naprej dobi prioriteto
            if razd==-10:
                min_razd=razd
                min_char=char
                break

            #hranimo informacijo, kater element ima najbolšo hevristiko za premik
            if min_razd>razd:
                min_razd=razd
                min_char=char

    #za element z najbolso hevristiko, pogledamo, kam ga lahko premaknemo
    index,posible= posible_moves(min_char,input_matrix,end_matrix)

    #ce je premik z prioriteto
    if indexPremika>-1:
        premik=move(input_matrix, index+1,indexPremika+1)
        if premik:
            if premik not in mozniPremikiMatrike:
                print(f"PRESTAVI {index+1} {indexPremika + 1}")
                commands.append(f"PRESTAVI {index+1} {indexPremika + 1}")
                return greedy(premik,end_matrix)

    else:
        #za vsak mozen premik prooba in gre v rekurzijo
        for i,x in enumerate(posible):
            if x==1:
                premik=move(input_matrix, index+1,i+1)
                if premik:
                    if premik not in mozniPremikiMatrike:
                        print(f"PRESTAVI {index + 1} {i + 1}")
                        commands.append(f"PRESTAVI {index + 1} {i + 1}")
                        return greedy(premik, end_matrix)


def updateChar(char,hevr):
    hevrOfChars[char]=hevr

#hranimo slovar elementov in trenutne hevristike
hevrOfChars={}
#pred zacetkom izvajanja potrebujemo v slovar, zapisti zacetne hevristike
def initializeastar(input_matrix,end_matrix):
    for index_y,line_y in enumerate(input_matrix):
        for index_x,line_x in enumerate(input_matrix[0]):
            char=input_matrix[index_y][index_x]
            if any(letter.isalpha() for letter in char):
                char=char.replace('"','')
                hevrOfChars[char],_=heuristic(char,input_matrix,end_matrix)

    astar(input_matrix,end_matrix)


def astar(input_matrix,end_matrix):
    mozniPremikiMatrike.append(input_matrix)
    izpis(input_matrix)

    global nodes
    global levels
    global nodes_generated

    if (input_matrix == end_matrix):
        return True

    nodes += 1
    min_char = ''
    min_razd = 10000
    indexPremika = -1

    # pridobimo katere elemente lahko premikamo
    for char in posible_to_move(input_matrix, end_matrix):
        if char != 0:
            # izracunamo hevristiko za vsak element
            razd, indexPremika = heuristic(char, input_matrix, end_matrix)
            nodes_generated += 1

            razd+=hevrOfChars[char]

            # ce hevristika vidi, da lahko element premaknemo na končno lokacijo, ne pregledujemo naprej dobi prioriteto
            if razd == -10:
                min_razd = razd
                min_char = char
                break

            # hranimo informacijo, kater element ima najbolšo hevristiko za premik
            if min_razd > razd:
                min_razd = razd
                min_char = char

    # za element z najbolso hevristiko, pogledamo, kam ga lahko premaknemo
    index, posible = posible_moves(min_char, input_matrix, end_matrix)

    # ce je premik z prioriteto
    if indexPremika>-1:
        premik = move(input_matrix, index+1,indexPremika+1)
        updateChar(min_char,min_razd)

        if premik:
            if premik not in mozniPremikiMatrike:
                print(f"PRESTAVI {index +1} {indexPremika+1 }")
                commands.append(f"PRESTAVI {index +1} {indexPremika+1}")
                return astar(premik,end_matrix)

    #za vsak mozen premik prooba in gre v rekurzijo
    else:
        for i,x in enumerate(posible):
            if x==1:
                premik = move(input_matrix, index+1,i+1)
                updateChar(min_char, min_razd)
                if premik:
                    if premik not in mozniPremikiMatrike:
                        print(f"PRESTAVI {index+1 } {i + 1}")
                        commands.append(f"PRESTAVI {index+1 } {i + 1}")
                        return astar(premik, end_matrix)



def main():
    print("Your input matrix is :")

    izpis(input_matrix)
    print()
    print("Goal input matrix is :")
    izpis(end_matrix)
    print()

    print("Please choose an algoririthm to run: \n(press a number)\n")
    print("1. DFS \t 2. BFS \t3. Greedy search \t 4. A*")

    read_input()

    print("Zaporedje ukazov, ki pripelje do podane rešitve: ")
    commands.reverse()
    print(commands)

# P == Št odstavnih položajev (št. stolpcev v matriki)
# N == Št možnik škatel na posameznam odstavnem položaju (št. vrstic v matriki)
P, N, input_matrix = read_file("Data/primer5_zacetna.txt")
_, _, end_matrix = read_file("Data/primer5_koncna.txt")


if __name__ == '__main__':
    main()
