import networkx as nx
from enum import Enum

class NodeType(Enum):
    ADDR = 1
    FUNC = 2
    INSTR = 3
    UNKNOWN = 4


class BNxGraph:
    def __init__(self, name, node_type, use_direct=False):
        if use_direct:
            self.nx_graph = nx.DiGraph()
        else:
            self.nx_graph = nx.Graph()
        self.is_direct: bool = use_direct
        self.name: str = name
        self.node_info: NodeType = node_type  # help information
        self.extra: str = '<comment zone>'


class GraphManager:
    def __init__(self):
        self.graphs = {}
        self.graph_cnt = 0
        self.current_graph: BNxGraph = None

    def check_has_graph_quiet(self, name) -> bool:
        if name in self.graphs:
            return True
        else:
            return False

    def check_warn_exist(self, name) -> bool:
        if self.check_has_graph_quiet(name):
            print("[ERROR] : Name already in manager, try another one")
            return True
        else:
            return False

    def check_warn_not_exist(self, name) -> bool:
        if self.check_has_graph_quiet(name):
            return False
        else:
            print("[ERROR] : No Such Graph")
            return True

    def add_graph(self, name, graph) -> bool:
        if self.check_warn_exist(name):
            return False
        else:
            self.graphs[name] = graph
            self.graph_cnt += 1
            self.current_graph = graph
            return True

    def get_graph(self, name) -> BNxGraph:
        if self.check_warn_not_exist(name):
            return None
        return self.graphs[name]

    def auto_gen_name(self, gname_prefix: str, gname_suffix: str, node_type: NodeType, use_direct):
        direct_suffix = 'g'
        if use_direct:
            direct_suffix = 'dg'
        return gname_prefix + '_' + direct_suffix + '_' + str(node_type) + '_' + gname_suffix

    def gen_graph(self, graph_name, node_type: NodeType, use_direct=False) -> bool:
        if self.check_warn_exist(graph_name):
            return False

        graph = BNxGraph(graph_name, node_type, use_direct)
        if self.add_graph(graph_name, graph):
            return True
        else:
            return False

    def list_graphs(self):
        return [i for i in self.graphs]

    def info_graph(self, name: str) -> bool:
        if self.check_warn_not_exist(name):
            return False

        g = self.get_graph(name)
        if g is None:
            print("[ERROR] : NONE GRAPH")
            return False

        print("[GRAPH NAME] : " + name)
        print("[DIRECT] : " + str(g.is_direct))
        print("[NODE_TYPE] : " + str(g.node_info))
        print("[EXTRA] : " + g.extra)

    def delete_graph(self, name):
        pass

    def purge_graph(self):
        pass

    def set_current_graph(self, name):
        if self.check_warn_not_exist(name):
            return False
        pass

    def draw_current_graph(self):
        '''
        call binja to draw ?
        or through xdot ?
        :return:
        '''
        pass

    def load_current_graph(self):
        '''
        load from formatted graph file
        :return:
        '''
        pass

    def save_current_graph(self):
        '''
        export graph to file
        :return:
        '''
        pass

