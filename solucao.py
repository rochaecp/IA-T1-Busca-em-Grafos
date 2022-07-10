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


def bfs(estado):
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    X = []
    F = []
    caminho = []
    estado_inicial = Nodo(estado)
    F.append(estado_inicial)

    while F != []:
        v = F.pop(0)
        if v.estado == OBJETIVO:
            aux = v
            while aux.pai is not None:
                caminho.insert(aux.custo, aux.acao)
                aux = aux.pai
            return caminho
        if v not in X :
            X.append(v)
            vizinhos = expande(v)
            for vizinho in vizinhos:
                F.append(vizinho)


def dfs(estado):
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError
