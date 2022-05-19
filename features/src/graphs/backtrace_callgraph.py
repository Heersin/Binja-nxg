import networkx as nx
from . import graph_mgr

def gen_direct_graph():
    return nx.DiGraph()

def faddr(func):
    return func[0].start

def callgraph_of_fn(current_func):
    cg = gen_direct_graph()
    visited = set()
    stack = [current_func]
    while stack:
        callee = stack.pop()
        for caller in set(callee.callers):
            cg.add_edge(faddr(caller), faddr(callee))
            if caller not in visited:
                stack.append(caller)
            visited.add(callee)
    return cg

# for directly generate backtrace function
def main(func_addr):
    pass