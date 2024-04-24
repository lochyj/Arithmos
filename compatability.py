# Graph class is from pynode

class MyGraph(Graph):
    def __init__(self):
        self._nodes = {}
        self._edges = []
        self._has_edge_cache = {}
        self._spread = 80

    def add_node(self, *args, **kwds):
        if "node" in kwds: n = kwds["node"]
        elif len(args) > 0 and isinstance(args[0], Node): n = args[0]
        else: n = Node(*args, **kwds)
        if n._id in self._nodes: raise Exception("Duplicate node '" + str(n._id) + "'")
        self._nodes[n._id] = n
        pynode_core.add_event(pynode_core.Event(pynode_core.js_add_node, [n._data()]))
        pause(25)
        return n

    def remove_node(self, node):
        n = self.node(node)
        pynode_core.enable_events(False)
        for e in n.incident_edges():
            self.remove_edge(e)
        pynode_core.enable_events(True)
        del self._nodes[n._id]
        pynode_core.add_event(pynode_core.Event(pynode_core.js_remove_node, [n._internal_id]))
        pause(25)
        return n

    def node(self, id):
        if isinstance(id, Node) and id._id in self._nodes:
            return id
        elif id in self._nodes:
            return self._nodes[id]
        else:
            return None

    def nodes(self):
        return list(self._nodes.values())

    def add_edge(self, *args, **kwds):
        if "edge" in kwds: e = kwds["edge"]
        elif len(args) > 0 and isinstance(args[0], Edge): e = args[0]
        else:
            arg_source = kwds["source"] if "source" in kwds else args[0]
            arg_target = kwds["target"] if "target" in kwds else args[1]
            arg_weight = kwds["weight"] if "weight" in kwds else args[2] if len(args) > 2 else None
            arg_directed = kwds["directed"] if "directed" in kwds else args[3] if len(args) > 3 else False
            e = Edge(arg_source, arg_target, arg_weight, arg_directed)
        if self.has_edge(e): raise Exception("Instance of edge '" + str(e) + "' already in graph.")
        original_source = e._source
        original_target = e._target
        e._source = graph.node(e._source)
        e._target = graph.node(e._target)
        if e._source is None: raise Exception("Node '" + str(original_source) + "' doesn't exist.")
        if e._target is None: raise Exception("Node '" + str(original_target) + "' doesn't exist.")
        e._source._incident_edges.append(e)
        e._target._incident_edges.append(e)
        self._edges.append(e)
        self._has_edge_cache[e] = True
        pynode_core.add_event(pynode_core.Event(pynode_core.js_add_edge, [e._data()]))
        return e

    def remove_edge(self, *args, **kwds):
        remove_multiple = False
        if "edge" in kwds: edge = kwds["edge"]
        elif len(args) > 0 and isinstance(args[0], Edge): edge = args[0]
        else:
            arg_source = kwds["node1"] if "node1" in kwds else args[0]
            arg_target = kwds["node2"] if "node2" in kwds else args[1]
            arg_directed = kwds["directed"] if "directed" in kwds else args[2] if len(args) > 2 else False
            remove_multiple = True
        if remove_multiple:
            edge_list = self.edges_between(arg_source, arg_target, arg_directed)
            self.remove_all(edge_list)
            return edge_list
        else:
            edge._source._incident_edges.remove(edge)
            edge._target._incident_edges.remove(edge)
            self._edges.remove(edge)
            del self._has_edge_cache[edge]
            pynode_core.add_event(pynode_core.Event(pynode_core.js_remove_edge, [edge._internal_id]))
            return edge

    def edges(self):
        return list(self._edges)

    def set_directed(self, directed=True):
        for e in self._edges:
            e.set_directed(directed)

    def has_node(self, node):
        return self.node(node) is not None

    def has_edge(self, edge):
        return edge in self._has_edge_cache

    def adjacent(self, node1, node2, directed=False):
        if not self.has_node(node1) or not self.has_node(node2): return False
        for n in (self.node(node1).successor_nodes() if directed else self.node(node1).adjacent_nodes()):
            if n is self.node(node2): return True
        return False
    # Deprecated
    def adjacent_directed(self, source, target):
        return self.adjacent(source, target, True)

    def edges_between(self, node1, node2, directed=False):
        if not self.has_node(node1) or not self.has_node(node2): return []
        edge_list = self.node(node1).outgoing_edges() if directed else self.node(node1)._incident_edges
        return [edge for edge in edge_list if edge._target is self.node(node2) or edge._source is self.node(node2)]
    # Deprecated
    def edges_between_directed(self, source, target):
        return self.edges_between(source, target, True)

    def adjacency_matrix(self):
        m = {}
        for r in self._nodes.values():
            row = {}
            for c in self._nodes.values(): row[c._id] = 0
            m[r._id] = row
        for r in self._nodes.values():
            for c in r.successor_nodes():
                m[r._id][c._id] += 1
        return m

    @staticmethod
    def random(order, size, connected=True, mutligraph=False, initial_id=0):
        nodes = []
        edges = []
        adjacency_matrix = [[0 for c in range(order)] for r in range(order)]
        edges_remaining = size
        id_list = random.sample(range(initial_id, initial_id + order), order)
        for i in range(order):
            node = Node(id_list[i])
            if connected and edges_remaining > 0 and len(nodes) > 0:
                connected_node = nodes[random.randint(0, len(nodes) - 1)]
                if random.randint(0, 1) == 0: edges.append(Edge(node, connected_node))
                else: edges.append(Edge(connected_node, node))
                adjacency_matrix[id_list[i] - initial_id][connected_node._id - initial_id] += 1
                adjacency_matrix[connected_node._id - initial_id][id_list[i] - initial_id] += 1
                edges_remaining -= 1
            nodes.append(node)
        possible_edges = [(i, j) for i in range(order) for j in range(order)]
        random.shuffle(possible_edges)
        for e in possible_edges:
            if edges_remaining <= 0: break
            if (adjacency_matrix[e[0]][e[1]] == 0 and e[0] != e[1]) or mutligraph:
                edges.append(Edge(e[0] + initial_id, e[1] + initial_id))
                adjacency_matrix[e[0]][e[1]] += 1
                adjacency_matrix[e[1]][e[0]] += 1
                edges_remaining -= 1
        return nodes + edges

    def add_all(self, elements):
        new_elements = []
        pynode_core.enable_events(False)
        for x in elements:
            if isinstance(x, Node): new_elements.append((0, self.add_node(x)._data()))
            elif isinstance(x, Edge): new_elements.append((1, self.add_edge(x)._data()))
            else: new_elements.append((0, self.add_node(Node(x))._data()))
        pynode_core.enable_events(True)
        pynode_core.add_event(pynode_core.Event(pynode_core.js_add_all, [new_elements]))
        pause(55)

    def remove_all(self, elements):
        new_elements = []
        pynode_core.enable_events(False)
        for x in elements:
            if isinstance(x, Node): new_elements.append((0, self.remove_node(x)._data()))
            elif isinstance(x, Edge): new_elements.append((1, self.remove_edge(x)._data()))
            else: new_elements.append((0, self.remove_node(self.node(x))._data()))
        pynode_core.enable_events(True)
        pynode_core.add_event(pynode_core.Event(pynode_core.js_remove_all, [new_elements]))
        pause(55)

    def order(self): return len(self._nodes.values())
    def size(self): return len(self._edges)

    def set_spread(self, spread=80):
        self._spread = spread
        pynode_core.add_event(pynode_core.Event(pynode_core.js_set_spread, [spread]))

    def clear(self):
        self._reset()
        pynode_core.add_event(pynode_core.Event(pynode_core.js_clear, []))

    def _reset(self):
        self._nodes = {}
        self._edges = []
        self._has_edge_cache = {}