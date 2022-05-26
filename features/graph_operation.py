from binaryninja import get_text_line_input
from .src.graphs import graph_mgr


def has_node(bv):
    res = get_text_line_input("Node Name : ", "Check If Node In Graph")

    if res is None:
        return

    res = str(res)
    print("[DEBUG] : " + res)
    nx_graph = graph_mgr.current_graph.nx_graph

    if nx_graph.has_node(res):
        print("[YES]")
    else:
        print("[No]")
