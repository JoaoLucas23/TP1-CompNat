import plotly.graph_objects as go

from .plot_tree import create_igraph_from_tree, make_annotations


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value  
        self.left = left  
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None
    
    def get_all_nodes(self):
        nodes = [self]
        if self.left:
            nodes.extend(self.left.get_all_nodes())
        if self.right:
            nodes.extend(self.right.get_all_nodes())
        return nodes
    
    def view_tree(self):
        """
        Plota a árvore interativa usando Plotly.
        """
        G = create_igraph_from_tree(self)
        lay = G.layout("rt")  # Layout Reingold-Tilford

        position = {k: lay[k] for k in range(len(G.vs))}
        Y = [lay[k][1] for k in range(len(G.vs))]
        M = max(Y) if Y else 1

        E = G.get_edgelist()
        
        Xn = [position[k][0] for k in range(len(G.vs))]
        Yn = [2*M - position[k][1] for k in range(len(G.vs))]
        
        Xe = []
        Ye = []
        for edge in E:
            Xe += [position[edge[0]][0], position[edge[1]][0], None]
            Ye += [2*M - position[edge[0]][1], 2*M - position[edge[1]][1], None]

        labels = G.vs["label"]

        # Criação dos Traços do Plotly
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=Xe,
                                 y=Ye,
                                 mode='lines',
                                 line=dict(color='rgb(210,210,210)', width=1),
                                 hoverinfo='none'
                                 ))
        fig.add_trace(go.Scatter(x=Xn,
                                  y=Yn,
                                  mode='markers',
                                  name='Nodes',
                                  marker=dict(symbol='circle-dot',
                                              size=18,
                                              color='#6175c1',
                                              line=dict(color='rgb(50,50,50)', width=1)
                                              ),
                                  text=labels,
                                  hoverinfo='text',
                                  opacity=0.8
                                  ))
        
        # Adiciona as anotações nos nós
        fig.update_layout(title='Tree with Reingold-Tilford Layout',
                          annotations=make_annotations(position, labels, M),
                          font_size=12,
                          showlegend=False,
                          xaxis=dict(showline=False,
                                     zeroline=False,
                                     showgrid=False,
                                     showticklabels=False),
                          yaxis=dict(showline=False,
                                     zeroline=False,
                                     showgrid=False,
                                     showticklabels=False),
                          margin=dict(l=40, r=40, b=85, t=100),
                          hovermode='closest',
                          plot_bgcolor='rgb(248,248,248)'
                          )
        fig.show()


    def view_expression(self):
        if self.is_leaf():
            return str(self.value)
        else:
            left_str = self.left.view_expression()
            right_str = self.right.view_expression()
            return f'({left_str} {self.value} {right_str})'
        
    def depth(self):
        if self.is_leaf():
            return 1
        else:
            return 1 + max(self.left.depth(), self.right.depth())
    
    def sum(x, y):
        return x + y

    def sub(x, y):
        return x - y
    
    def mul(x, y):
        return x * y

    def protected_division(x, y):
        if y == 0:
            return 0
        return x / y

    operators = {
        '+': sum,
        '-': sub,
        '*': mul,
        '/': protected_division
    }



