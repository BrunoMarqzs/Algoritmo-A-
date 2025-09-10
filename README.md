# Algoritmo A*

Este repositório contém a resolução da **Atividade 6** da disciplina de Inteligência Artificial, baseada no livro *Russell & Norvig* e nos vídeos de apoio disponibilizados.

---

##  Objetivos da atividade
- Implementar o algoritmo **A\*** usando fila de prioridade.  
- Aplicar o A* ao problema de busca de rotas no **mapa da Romênia**.  
- Analisar o funcionamento do algoritmo passo a passo.  
- Criar e utilizar funções heurísticas para diferentes destinos.  
- Resolver um problema adicional de busca em que o custo das ações não seja unitário.  

---

##  Questões propostas
1. **Implementação do A\***: partindo da Busca em Largura, mas com fila de prioridade.  
2. **Problema da Romênia (Arad → Bucareste)**: encontrar a melhor rota, mostrando o passo a passo da busca.  
3. **Outras origens**: simulação do algoritmo partindo de pelo menos duas cidades diferentes até Bucareste.  
4. **Nova heurística**: usar distâncias em linha reta (obtidas em mapas) para resolver rotas até outro destino que não seja Bucareste.  
5. **Outro problema**: formular um problema diferente com custos variáveis e resolvê-lo com o A\*, utilizando uma heurística admissível.  

---

##  Resultados obtidos
- O algoritmo A\* foi implementado com sucesso, garantindo sempre o **caminho ótimo** graças ao uso de heurísticas admissíveis.  
- No **problema clássico da Romênia**, o A\* mostrou como a heurística guia a busca de forma mais eficiente que a Busca em Largura ou Uniforme.  
- Foram simulados caminhos a partir de diferentes cidades de origem, como **Lugoj → Bucareste** (custo 504) e **Sibiu → Bucareste** (custo 278).  
- Uma **nova função heurística** baseada em distâncias geográficas foi criada para resolver rotas com outro destino final.  
- Também foi resolvido um **problema alternativo** com custos não unitários, reforçando a flexibilidade do A\*.  

---

##  Referências
- Russell, S. & Norvig, P. *Artificial Intelligence: A Modern Approach* (3ª ed.).  
- Repositório da disciplina: [github.com/tautologico/intro-ia](https://github.com/tautologico/intro-ia)  
- Vídeos de apoio:  
  - [Busca com Informação - Melhor Escolha](https://youtu.be/t34LW_LnCvU)  
  - [Busca com Algoritmo A*](https://youtu.be/adzNTs2CsjM)  

---

##  Equipe
- Bruno Marques
- Clarice Lopes  
- Rafael Lima 
