import heapq as hq
from collections import deque
import numpy as np 

OBJETIVO = "12345678_"

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado = '', pai = None, acao = None, custo = 0):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo

class Nodo2:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado = '', pai = None, acao = None, custo = 0):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo

    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return False

    def __lt__(self, other):
        return False

    def __gt__(self, other):
        return False

    def __le__(self, other):
        return False

    def __ge__(self, other):
        return False


class FilaPrioridade:

    def __init__(self):
        self.fila = []
        self.indice = 0

    def adicionar_nodo(self, nodo, prioridade):
        hq.heappush(self.fila, (prioridade, nodo))
        self.indice += 1

    def remover_nodo(self):
        return hq.heappop(self.fila)
    
    def esta_vazia(self):
        if len(self.fila) == 0:
            return True
        else:
            return False


def sucessor(estado):
    """
    Recebe um estado (string) e retorna uma lista de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    lista = []
    c = '_'
    pos_vazio = estado.find(c)

    # ACIMA
    if(pos_vazio != 0 and pos_vazio != 1 and pos_vazio != 2):
        aux = estado
        l = list(aux)
        l[pos_vazio] = l[pos_vazio-3]
        l[pos_vazio-3] = '_'
        aux = "".join(l)
        lista.append(("acima", aux))
    # ESQUERDA
    if(pos_vazio != 0 and pos_vazio != 3 and pos_vazio != 6):
        aux = estado
        l = list(aux)
        l[pos_vazio] = l[pos_vazio-1]
        l[pos_vazio-1] = '_'
        aux = "".join(l)
        lista.append(("esquerda", aux))
    # DIREITA
    if(pos_vazio != 2 and pos_vazio != 5 and pos_vazio != 8):
        aux = estado
        l = list(aux)
        l[pos_vazio] = l[pos_vazio+1]
        l[pos_vazio+1] = '_'
        aux = "".join(l)
        lista.append(("direita", aux))
    # ABAIXO
    if(pos_vazio != 6 and pos_vazio != 7 and pos_vazio != 8):
        aux = estado
        l = list(aux)
        l[pos_vazio] = l[pos_vazio+3]
        l[pos_vazio+3] = '_'
        aux = "".join(l)
        lista.append(("abaixo", aux))
    
    return lista
    

def expande(nodo):
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
    Cada nodo do iterable é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    lista = []
    l = sucessor(nodo.estado)

    for tupla in l:
        aux = Nodo(tupla[1], nodo, tupla[0], nodo.custo+1)
        lista.append(aux)

    return lista


def expande2(nodo):
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
    Cada nodo do iterable é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    lista = []
    l = sucessor(nodo.estado)

    for tupla in l:
        aux = Nodo2(tupla[1], nodo, tupla[0], nodo.custo+1)
        lista.append(aux)

    return lista


def contaInversores(estado):
	tot_inversores = 0
	espaco_vazio = '_'
	for i in range(0, 9):
		for j in range(i + 1, 9):
			if estado[j] != espaco_vazio and estado[i] != espaco_vazio and estado[i] > estado[j]:
				tot_inversores += 1
	return tot_inversores


def ehSolucionavel(estado) :
	tot_inversores = contaInversores([j for sub in estado for j in sub])
	return (tot_inversores % 2 == 0)

#### Funções para Heurística de Hamming ####
def calcula_hamming(estado):
    vet = list(estado)
    obj = list(OBJETIVO)
    h = 0
    
    for i in range(8):
        if vet[i] != obj[i]:
            h = h + 1

    return h



#### Funções para Heurística de Manhattan ####
def criar_matriz(estado):
    """ 
    Recebe um estado (string - ex.: "12345678_") e retorna uma matriz 3x3 
    """
    lista_estado = list(estado)
    matriz = np.array(lista_estado).reshape(3, 3)
    
    return matriz


def calcula_indice_objetivo(matriz):
    indices_objetivo = {}

    for i in range(3):
        for j in range(3):
            numero = matriz[i][j]
            indices_objetivo[numero] = { 'linha': i, 'coluna': j }
    
    return indices_objetivo


matriz_objetivo = criar_matriz(OBJETIVO)
indices_objetivo = calcula_indice_objetivo(matriz_objetivo)


def calcula_manhattan(elemento, elem_linha, elem_coluna, indices_objetivo):
    return int(abs(int(elem_linha) - int(indices_objetivo[str(elemento)]['linha'])) + abs(int(elem_coluna) - int(indices_objetivo[str(elemento)]['coluna'])))


def calcula_distancia_heuristica_manhattan_elemento(estado, elemento):
    """
    Recebe um estado(string) e um elemento
    Retorna a distância heuristica de manhattan até o objetivo
    """
    matriz_estado = criar_matriz(estado)
    linha = int(np.where(matriz_estado == str(elemento))[0][0])
    coluna = int(np.where(matriz_estado == str(elemento))[1][0])
    distancia_heursitica = calcula_manhattan(elemento, linha, coluna, indices_objetivo)

    return int(distancia_heursitica)


def calculla_distancia_heuristica_manhattan_total(estado):
    matriz_estado = criar_matriz(estado)

    """
    Terá elemento: distancia heurística até a posição correta
    # Ex: '8': 3 - 8 é o elemento e 3 é a distancia heurística até a posição correta
    """
    heuristica_manhattan = {}
    distancia_heuristica_total = 0

    for i in range(3):
        for j in range(3):
            if matriz_estado[i][j] != "_":
                if matriz_estado[i][j] != matriz_objetivo[i][j]:
                    elemento = matriz_estado[i][j]
                    distancia_heursitica = calcula_manhattan(elemento, i, j, indices_objetivo)
                    heuristica_manhattan[elemento] = distancia_heursitica
                    distancia_heuristica_total = distancia_heuristica_total + distancia_heursitica
    
    return distancia_heuristica_total


#### Funções de Busca ####
def bfs(estado):
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    if not ehSolucionavel(estado):
        return None
    X = set()
    F = deque()
    caminho = []
    estado_inicial = Nodo(estado)

    F.append(estado_inicial)


    while F :
        v = F.popleft()
        
        if v.estado == OBJETIVO:
            aux = v
            while aux.pai is not None:
                caminho.insert(0, aux.acao)
                aux = aux.pai
            return caminho

        if v.estado not in X:
            X.add(v.estado)
            vizinhos = expande(v)
            for vizinho in vizinhos:
                F.append(vizinho)
    
    return None
    

def dfs(estado):
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    if not ehSolucionavel(estado):
        return None
    X = set()
    F = dict()
    caminho = []
    estado_inicial = Nodo(estado)

    F[estado_inicial.estado] = estado_inicial


    while F != {}:
        v = F.popitem()[1]
        
        if v.estado == OBJETIVO:
            aux = v
            while aux.pai is not None:
                caminho.insert(0, aux.acao)
                aux = aux.pai
            return caminho

        if v.estado not in X:
            X.add(v.estado)
            vizinhos = expande(v)
            for vizinho in vizinhos:
                F[vizinho.estado] = vizinho

    return None


def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    if not ehSolucionavel(estado):
        return None

    X = set()
    F = FilaPrioridade()
    caminho = []
    nodo_inicial = Nodo2(estado)
  
    F.adicionar_nodo(nodo_inicial, 0)

    while not F.esta_vazia():
       
        v = F.remover_nodo()[1]
                
        if v.estado == OBJETIVO:
            aux = v
            while aux.pai is not None:
                caminho.insert(0, aux.acao)
                aux = aux.pai
            return caminho

        if v.estado not in X:
            X.add(v.estado)
            vizinhos = expande2(v)
            
            for vizinho in vizinhos:
                custo_mais_heuristica = (int(vizinho.custo) + int(calcula_hamming(vizinho.estado)))
                F.adicionar_nodo(vizinho, int(custo_mais_heuristica))
                
    return None


def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    if not ehSolucionavel(estado):
        return None

    X = set()
    F = FilaPrioridade()
    caminho = []
    nodo_inicial = Nodo2(estado)
    
    F.adicionar_nodo(nodo_inicial, 0)

    while not F.esta_vazia():
        v = F.remover_nodo()[1]
                
        if v.estado == OBJETIVO:
            aux = v
            while aux.pai is not None:
                caminho.insert(0, aux.acao)
                aux = aux.pai
            return caminho

        if v.estado not in X:
            X.add(v.estado)
            vizinhos = expande2(v)

            for vizinho in vizinhos:
                custo_mais_heuristica = (int(vizinho.custo) + int(calculla_distancia_heuristica_manhattan_total(vizinho.estado)))
                F.adicionar_nodo(vizinho, int(custo_mais_heuristica))


""" print("Ações:")
tempo_inicio = time.time()
print(len(astar_manhattan("2_3541687")))
tempo_fim = time.time()

print("\nTempo decorrido:")
print(tempo_fim - tempo_inicio) """