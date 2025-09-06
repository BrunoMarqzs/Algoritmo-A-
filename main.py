from busca_melhor_escolha import No, Problema, BuscaAEstrela
from busca_melhor_escolha import definir_espaco_estados_romenia, definir_heuristica_bucharest

print("--- Iniciando Busca A* com Heap Próprio ---")
espaco_estados = definir_espaco_estados_romenia()
heuristica = definir_heuristica_bucharest()
problema_romenia = Problema(
    inicial=None,
    objetivo=lambda no: no.estado == 'Bucharest',
    espaco_estados=espaco_estados,
    heuristica=heuristica
)
no_inicial = No('Arad', 0, problema_romenia)
problema_romenia.inicial = no_inicial
busca = BuscaAEstrela(problema_romenia)
while busca.situacao not in [busca.BUSCA_SUCESSO, busca.BUSCA_FALHA]:
    print(f"Fronteira: {busca.mostra_fronteira()}")
    busca.passo_busca()
print("\n--- Fim da Busca ---")
print(f"Solução encontrada: {busca.mostra_solucao()}")
