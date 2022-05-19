import networkx as nx
from . import graph_mgr
from .GraphManager import NodeType


def faddr(func):
    return func[0].start


def gen_direct_graph(current_func):
    node_t = NodeType.FUNC
    backtrace_fn_graph_name = graph_mgr.auto_gen_name( 'BTRACE-CALL', hex(faddr(current_func)), node_t.name, True)
    print("[DEBUG] : graph name " + backtrace_fn_graph_name)

    if graph_mgr.check_has_graph_quiet(backtrace_fn_graph_name):
        g = graph_mgr.get_graph(backtrace_fn_graph_name)
        return g.nx_graph

    if graph_mgr.gen_graph(backtrace_fn_graph_name, node_t, use_direct=True):
        g = graph_mgr.get_graph(backtrace_fn_graph_name)
        return g.nx_graph
    else:
        print("Some Error Happend")
        return None


def callgraph_of_fn(current_func):
    cg = gen_direct_graph(current_func)
    if cg is None:
        return None

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