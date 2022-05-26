from binaryninja import get_text_line_input
from .src.graphs import graph_mgr


def list_graphs(bv):
    g_list = graph_mgr.list_graphs()
    cnt = 0
    for g in g_list:
        print("-------------[{}]------------".format(cnt))
        graph_mgr.info_graph(g)
        cnt += 1


def info_show(bv):
    name = graph_mgr.current_graph.name
    graph_mgr.info_graph(name)


def set_current_graph(bv):
    res = get_text_line_input("Name : ", "Set Current Graph")

    if res is None:
        return

    res = str(res)
    print("[DEBUG]: " + res)
    graph_mgr.set_current_graph(res)
