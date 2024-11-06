import igraph
from igraph import Graph


# Função auxiliar para percorrer a árvore e coletar arestas e rótulos
def traverse_tree(node, edges, labels, current_id=0, parent_id=None):
    """
    Percorre a árvore e coleta arestas e rótulos.
    
    Parameters:
    - node: nó atual (instância de Node)
    - edges: lista para armazenar as arestas como tuplas
    - labels: lista para armazenar os rótulos dos nós
    - current_id: ID atual do nó
    - parent_id: ID do nó pai
    
    Returns:
    - next_id: próximo ID disponível após esta subárvore
    """
    labels.append(str(node.value))
    node_id = current_id
    if parent_id is not None:
        edges.append((parent_id, node_id))
    current_id += 1
    if node.left:
        current_id = traverse_tree(node.left, edges, labels, current_id, node_id)
    if node.right:
        current_id = traverse_tree(node.right, edges, labels, current_id, node_id)
    return current_id

# Função auxiliar para criar um objeto igraph a partir da árvore
def create_igraph_from_tree(root):
    """
    Cria um objeto igraph a partir da árvore.
    
    Parameters:
    - root: raiz da árvore (instância de Node)
    
    Returns:
    - G: objeto igraph representando a árvore
    """
    edges = []
    labels = []
    traverse_tree(root, edges, labels)
    G = Graph(edges=edges, directed=False)
    G.vs["label"] = labels
    return G

# Função auxiliar para criar as anotações no Plotly
def make_annotations(pos, text, M, font_size=10, font_color='rgb(250,250,250)'):
    """
    Cria anotações para os nós da árvore.
    
    Parameters:
    - pos: dicionário com as posições dos nós
    - text: lista de rótulos dos nós
    - M: valor máximo de Y para ajuste de posição
    - font_size: tamanho da fonte das anotações
    - font_color: cor da fonte das anotações
    
    Returns:
    - annotations: lista de dicionários com as configurações das anotações
    """
    annotations = []
    for k in range(len(pos)):
        annotations.append(
            dict(
                text=text[k],
                x=pos[k][0], y=2*M - pos[k][1],
                xref='x', yref='y',
                font=dict(color=font_color, size=font_size),
                showarrow=False
            )
        )
    return annotations