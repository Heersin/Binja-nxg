import networkx as nx
from binaryninja import BinaryView as bv
from graphs.backtrace_callgraph import callgraph_of_fn

# src : source function addr
# sink: sink function addr
def find_call_chain(graph, src, sink):
    if not nx.has_path(graph, src, sink):
        print("No Such a call chain found")
        return []
    str_path = nx.shortest_path(graph, src, sink)
    call_chain = [int(f) for f in str_path]
    return call_chain

def main(target_addr, entry_addr=bv.entry_point):
    target_fn = bv.get_function_at(target_addr)
    cg = callgraph_of_fn(target_fn)
    return find_call_chain(cg, entry_addr, target_addr)

