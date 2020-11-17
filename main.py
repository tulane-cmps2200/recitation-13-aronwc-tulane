from collections import Counter

def example_graph():
    # the example graph from the edge contraction lecture
    vertices = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])
    edges = set([('a', 'b'), ('a', 'c'), ('b', 'c'), ('b', 'g'), 
                 ('d', 'e'), ('d', 'f'), ('e', 'f'),
                 ('h', 'i'), ('i', 'g'), ('h', 'g')])
    return vertices, edges


def num_components(vertices, edges, partition_graph_f):
    """
    Compute the number of connected components in a graph using contraction.
    This is complete.
    """
    if len(edges) == 0:
        # base case: return the number of super vertices in the final partition
        return len(vertices)
    else:
        new_vertices, vertex_map = partition_graph_f(vertices, edges)
        new_edges = set([(vertex_map[e[0]], vertex_map[e[1]])
                          for e in edges if vertex_map[e[0]] != vertex_map[e[1]]])
        return num_components(new_vertices, new_edges, partition_graph_f)


def edge_contract_seq(vertices, edges):
    """
    Sequential implementation of edge contraction.
    Complete the implementation below.

    Returns:
      new_vertices...set of super vertices in the contracted graph
      vertex_map.....dict from vertex_i->vertex_j, where vertex_j is the 
      super vertiex of vertex_i
    """
    # vertices in all the edges we have selected so far
    selected_vertices = set()
    # dict from vertex->super vertex
    vertex_map = {}
    # set of super vertices
    new_vertices = set()
    for e in edges:
        ### TODO: complete
        pass
    return new_vertices, vertex_map


def test_edge_contract_seq():
    vertices, edges = example_graph()
    # will use a sorted edge list for testing to ensure we get the same result.
    edges = sorted(list(edges))
    # edges in order are:
    # [('a', 'b'), ('a', 'c'), ('b', 'c'), ('b', 'g'), ('d', 'e'), ('d', 'f'), ('e', 'f'), ('h', 'g'), ('h', 'i'), ('i', 'g')]
    new_vertices, vertex_map = edge_contract_seq(vertices, edges)
    # these are the super vertices
    assert sorted(list(new_vertices)) == ['b', 'c', 'e', 'f', 'g', 'i']
    # map: a->b  d->e  h->g, plus the singletons  
    assert vertex_map['a'] == 'b'
    assert vertex_map['b'] == 'b'
    assert vertex_map['c'] == 'c'
    assert vertex_map['d'] == 'e'    
    assert vertex_map['e'] == 'e'
    assert vertex_map['f'] == 'f'
    assert vertex_map['g'] == 'g'
    assert vertex_map['h'] == 'g'
    assert vertex_map['i'] == 'i'

def test_num_components():
    vertices, edges = example_graph()
    assert num_components(vertices, edges, edge_contract_seq) == 2




def edge_contract_seq_sizes(vertices, edges, sizes):
    """
    Modified version of edge contraction that maintains
    a sizes dict that is a map from vertex->int, indicating
    the number of vertices in each component represented
    by each super vertex.

    Complete the implementation below.
    """
    selected_vertices = set()
    vertex_map = {}
    new_vertices = set()
    for e in edges:
        ### TODO: complete
        pass
        
    return new_vertices, vertex_map, sizes


def test_edge_contract_seq_sizes():
    vertices, edges = example_graph()
    sizes = Counter()
    sizes.update(vertices)
    # i'm sorting the edge set so we get the same results for testing.
    new_vertices, vertex_map, sizes = edge_contract_seq_sizes(vertices, sorted(list(edges)), sizes)
    # super vertices e,b,g now have size 2
    assert sizes['b'] == 2
    assert sizes['e'] == 2
    assert sizes['g'] == 2
    assert sizes['a'] == 1
    assert sizes['c'] == 1
    assert sizes['d'] == 1
    assert sizes['f'] == 1
    assert sizes['h'] == 1


def component_sizes(vertices, edges, partition_graph_f, sizes):
    """
    Computes the size of each connected component using
    edge_contract_seq_sizes.
    This is complete.
    """
    if len(edges) == 0:
        # base case: return the sizes of each super vertex in the final graph.        
        return [sizes[v] for v in vertices]
    else:
        new_vertices, vertex_map, sizes = partition_graph_f(vertices, edges, sizes)
        new_edges = set([(vertex_map[e[0]], vertex_map[e[1]])
                          for e in edges if vertex_map[e[0]] != vertex_map[e[1]]])
        return component_sizes(new_vertices, new_edges, partition_graph_f, sizes)


def test_component_sizes():
    vertices, edges = example_graph()
    # initialize counts to be 1 for each vertex.
    sizes = Counter()
    sizes.update(vertices)
    # sizes is: {'a': 1, 'b': 1, ...}
    assert sorted(component_sizes(vertices, edges, edge_contract_seq_sizes, sizes)) == [3, 6]


