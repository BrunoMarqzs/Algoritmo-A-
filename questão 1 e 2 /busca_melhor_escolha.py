# DEFINIÇÃO DAS CLASSES E ESTRUTURAS DE DADOS

class MinHeap:
    """Implementação de um Min-Heap (fila de prioridade) do zero."""
    def __init__(self):
        self.contents = []
        self.capacity = 0
        self.size = 0

    def remove_min(self):
        if self.size < 1: return None
        minimo = self.contents[0]
        self.contents[0] = self.contents[self.size-1]
        self.size -= 1
        if self.size < len(self.contents): self.contents.pop(); self.capacity -=1
        if self.size > 0: self.__min_heapify(0)
        return minimo

    def adiciona(self, node):
        indice = self.size
        if self.capacity == self.size: self.contents.append(None); self.capacity += 1
        self.size += 1
        self.__insert(indice, node)

    def __pai(self, i): return (i - 1) // 2
    def __filho_esquerdo(self, i): return i * 2 + 1
    def __filho_direito(self, i): return i * 2 + 2
    def __swap(self, i, j): self.contents[i], self.contents[j] = self.contents[j], self.contents[i]

    def __min_heapify(self, i):
        l, r, minimo = self.__filho_esquerdo(i), self.__filho_direito(i), i
        if l < self.size and self.contents[i].f > self.contents[l].f: minimo = l
        if r < self.size and self.contents[minimo].f > self.contents[r].f: minimo = r
        if minimo != i: self.__swap(i, minimo); self.__min_heapify(minimo)

    def __insert(self, i, node):
        self.contents[i] = node
        while i > 0 and self.contents[self.__pai(i)].f > self.contents[i].f:
            self.__swap(i, self.__pai(i)); i = self.__pai(i)


class No:
    """Representa um nó na árvore de busca."""
    def __init__(self, estado, custo, problema, pai=None, acao=None):
        self.estado = estado
        self.custo = custo
        self.pai = pai
        self.acao = acao
        heuristica = problema.heuristica.get(self.estado, 0)
        self.f = self.custo + heuristica

    def __repr__(self):
        return f"({self.estado}, f={self.f})"

    def filhos(self, problema):
        estado_acoes = next((ea for ea in problema.espaco_estados if ea['estado'] == self.estado), None)
        if not estado_acoes: return []
        return [No(a['destino'], self.custo + a['custo'], problema, self, a['destino']) for a in estado_acoes['acoes']]

    def constroi_solucao(self):
        no, solucao = self, []
        while no: solucao.insert(0, no); no = no.pai
        return solucao


class Problema:
    """Define o problema a ser resolvido, agora incluindo a heurística."""
    def __init__(self, inicial, objetivo, espaco_estados, heuristica):
        self.inicial = inicial
        self.objetivo = objetivo
        self.espaco_estados = espaco_estados
        self.heuristica = heuristica

    def objetivo_alcancado(self, no):
        return self.objetivo(no)


class BuscaAEstrela:
    """Implementa o algoritmo de busca A* usando a MinHeap própria."""
    BUSCA_INICIANDO, BUSCA_EM_CURSO, BUSCA_FALHA, BUSCA_SUCESSO = 0, 1, 2, 3

    def __init__(self, problema):
        self.problema = problema
        self.fronteira = MinHeap()
        self.fronteira.adiciona(problema.inicial)
        self.visitados = set()
        self.situacao = self.BUSCA_INICIANDO
        self.solucao = []

    def passo_busca(self):
        if self.situacao in (self.BUSCA_FALHA, self.BUSCA_SUCESSO): return
        if self.fronteira.size == 0:
            self.situacao = self.BUSCA_FALHA; print("Fronteira vazia. Busca falhou")
            return
        no = self.fronteira.remove_min()
        if no.estado in self.visitados: return self.passo_busca()
        print(f"Nó atual: {no.estado} (custo g(n)={no.custo}, valor f(n)={no.f})")
        self.visitados.add(no.estado)
        if self.problema.objetivo_alcancado(no):
            self.solucao = no.constroi_solucao()
            self.situacao = self.BUSCA_SUCESSO; print("Solução encontrada!")
            return
        for filho in no.filhos(self.problema):
            if filho.estado not in self.visitados:
                self.fronteira.adiciona(filho)
        self.situacao = self.BUSCA_EM_CURSO

    def mostra_solucao(self):
        if not self.solucao: return "Nenhuma solução ainda."
        return " -> ".join([f"({n.estado}, {n.custo})" for n in self.solucao]) + \
               f" | Custo Final: {self.solucao[-1].custo}"

    def mostra_fronteira(self):
        return "[" + " ".join([repr(n) for n in self.fronteira.contents]) + "]"

# SEÇÃO 2: FUNÇÕES DE DADOS ESPECÍFICAS DO PROBLEMA

def definir_espaco_estados_romenia():
    """Retorna a definição do mapa da Romênia (custos reais entre cidades)."""
    return [
        {'estado': 'Arad', 'acoes': [{'destino': 'Zerind', 'custo': 75}, {'destino': 'Sibiu', 'custo': 140}, {'destino': 'Timisoara', 'custo': 118}]},
        {'estado': 'Zerind', 'acoes': [{'destino': 'Arad', 'custo': 75}, {'destino': 'Oradea', 'custo': 71}]},
        {'estado': 'Timisoara', 'acoes': [{'destino': 'Arad', 'custo': 118}, {'destino': 'Lugoj', 'custo': 111}]},
        {'estado': 'Sibiu', 'acoes': [{'destino': 'Arad', 'custo': 140}, {'destino': 'Oradea', 'custo': 151}, {'destino': 'Fagaras', 'custo': 99}, {'destino': 'Rimnicu Vilcea', 'custo': 80}]},
        {'estado': 'Oradea', 'acoes': [{'destino': 'Zerind', 'custo': 71}, {'destino': 'Sibiu', 'custo': 151}]},
        {'estado': 'Lugoj', 'acoes': [{'destino': 'Timisoara', 'custo': 111}, {'destino': 'Mehadia', 'custo': 70}]},
        {'estado': 'Mehadia', 'acoes': [{'destino': 'Lugoj', 'custo': 70}, {'destino': 'Drobeta', 'custo': 75}]},
        {'estado': 'Drobeta', 'acoes': [{'destino': 'Mehadia', 'custo': 75}, {'destino': 'Craiova', 'custo': 120}]},
        {'estado': 'Craiova', 'acoes': [{'destino': 'Drobeta', 'custo': 120}, {'destino': 'Rimnicu Vilcea', 'custo': 146}, {'destino': 'Pitesti', 'custo': 138}]},
        {'estado': 'Rimnicu Vilcea', 'acoes': [{'destino': 'Sibiu', 'custo': 80}, {'destino': 'Craiova', 'custo': 146}, {'destino': 'Pitesti', 'custo': 97}]},
        {'estado': 'Fagaras', 'acoes': [{'destino': 'Sibiu', 'custo': 99}, {'destino': 'Bucharest', 'custo': 211}]},
        {'estado': 'Pitesti', 'acoes': [{'destino': 'Rimnicu Vilcea', 'custo': 97}, {'destino': 'Craiova', 'custo': 138}, {'destino': 'Bucharest', 'custo': 101}]},
        {'estado': 'Giurgiu', 'acoes': [{'destino': 'Bucharest', 'custo': 90}]},
        {'estado': 'Bucharest', 'acoes': [{'destino': 'Fagaras', 'custo': 211}, {'destino': 'Pitesti', 'custo': 101}, {'destino': 'Giurgiu', 'custo': 90}, {'destino': 'Urziceni', 'custo': 85}]},
        {'estado': 'Urziceni', 'acoes': [{'destino': 'Bucharest', 'custo': 85}, {'destino': 'Vaslui', 'custo': 142}, {'destino': 'Hirsova', 'custo': 98}]},
        {'estado': 'Hirsova', 'acoes': [{'destino': 'Urziceni', 'custo': 98}, {'destino': 'Eforie', 'custo': 86}]},
        {'estado': 'Eforie', 'acoes': [{'destino': 'Hirsova', 'custo': 86}]},
        {'estado': 'Vaslui', 'acoes': [{'destino': 'Urziceni', 'custo': 142}, {'destino': 'Iasi', 'custo': 92}]},
        {'estado': 'Iasi', 'acoes': [{'destino': 'Vaslui', 'custo': 92}, {'destino': 'Neamt', 'custo': 87}]},
        {'estado': 'Neamt', 'acoes': [{'destino': 'Iasi', 'custo': 87}]}
    ]

def definir_heuristica_bucharest():
    """Retorna os valores da heurística (distância em linha reta até Bucharest)."""
    return {
        'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242,
        'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151,
        'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
        'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193,
        'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199,
        'Zerind': 374

    }
