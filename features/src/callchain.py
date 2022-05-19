# TODO: use binaryninja log
import networkx as nx
from .graphs.backtrace_callgraph import callgraph_of_fn


# src : source function addr
# sink: sink function addr
def find_call_chain(graph, src, sink):
    if (src not in graph) or (sink not in graph) :
        print("Either Src or Sink not in Backtrace Graph")
        return []

    if not nx.has_path(graph, src, sink):
        print("No Such a call chain found")
        return []
    str_path = nx.shortest_path(graph, src, sink)
    call_chain = [int(f) for f in str_path]
    return call_chain


def main(bv, entry_addr, target_addr):
    target_fn = bv.get_function_at(addr=target_addr)

    if target_fn is None:
        print("No Function at " + hex(target_addr))
        return []

    cg = callgraph_of_fn(target_fn)
    return find_call_chain(cg.nx_graph, entry_addr, target_addr)

