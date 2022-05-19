from . import graph_mgr
from .GraphManager import NodeType, BNxGraph


def faddr(func):
    return func[0].start


def gen_direct_graph(current_func, use_old=True):
    node_t = NodeType.FUNC
    backtrace_fn_graph_name = graph_mgr.auto_gen_name( 'BTRACE-CALL', hex(faddr(current_func)), node_t.name, True)
    print("[DEBUG] : graph name " + backtrace_fn_graph_name)

    if graph_mgr.check_has_graph_quiet(backtrace_fn_graph_name) and use_old:
        g = graph_mgr.get_graph(backtrace_fn_graph_name)
        return g, True

    if graph_mgr.gen_graph(backtrace_fn_graph_name, node_t, use_direct=True):
        g = graph_mgr.get_graph(backtrace_fn_graph_name)
        return g, False
    else:
        print("Some Error Happend")
        return None, False


def callgraph_of_fn(current_func) -> BNxGraph:
    cg, cache_exist = gen_direct_graph(current_func)
    if cg is None:
        return None

    if cache_exist:
        return cg

    visited = set()
    stack = [current_func]
    while stack:
        callee = stack.pop()
        for caller in set(callee.callers):
            cg.nx_graph.add_edge(faddr(caller), faddr(callee))
            if caller not in visited:
                stack.append(caller)
            visited.add(callee)
    return cg
