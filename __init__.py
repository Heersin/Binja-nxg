from binaryninja import *

# Note that this is a sample plugin and you may need to manually edit it with
# additional functionality. In particular, this example only passes in the
# binary view. If you would like to act on an addres or function you should
# consider using other register_for* functions.

# Add documentation about UI plugin alternatives and potentially getting
# current_* functions

def main(bv):
    import networkx as nx
    import os
    
    def gen_direct_graph():
        return nx.DiGraph()
    
    def faddr(func):
        return func[0].start
    
    # TODO : could we use another libirary ?
    def callgraph_rev(current_func):
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
    
    # src : source function addr
    # sink: sink function addr
    def find_call_chain(graph, src, sink):
        src_node = str(int(src))
        sink_node = str(int(sink))
        if not nx.has_path(graph, src, sink):
            print("No Such a call chain found")
            return []
        str_path = nx.shortest_path(graph, src, sink)
        call_chain = [int(f) for f in str_path]
        return call_chain
    
    # ========== For pwn01 ==================
    # ========== binaryninja related ========
    def is_case_bb(bb):
        if bb[0].operation == bb[0].operation.HLIL_CASE:
            return True
        else:
            return False
    
    def is_call_callee_bb(bb, callee):
        if not is_case_bb(bb):
            return False
    
        fn_addr = bb[1].operands[1].operands[0].value.value
        cval = bb[0].operands[0][0].operands[0]
        #print("{} -> case {}".format(hex(fn_addr), str(cval)))
        #print("callee : " + hex(callee[0].start))
        if fn_addr != callee[0].start:
            return False
        return True
    
    def get_case_val(bb):
        return bb[0].operands[0][0].operands[0]
    
    def get_callee_cval(caller, callee):
        hlil_fn = caller.hlil
        for bb in hlil_fn:
            if is_call_callee_bb(bb, callee):
                return get_case_val(bb)
        print("No case val found")
        return -1
    
    def proc_switch_case(call_chain):
        result = []    
        for i in range(len(call_chain) - 1):
            caller = bv.get_function_at(call_chain[i])
            callee = bv.get_function_at(call_chain[i + 1])
            result.append(get_callee_cval(caller, callee))
        return result
    
    # ============= Main ================
    main_addr = 0x81096e3
    entry_addr = 0x080488ce
    vuln_addr = 0x81096be
    
    source_addr = entry_addr
    sink_addr = vuln_addr
    
    source = bv.get_function_at(source_addr)
    sink = bv.get_function_at(sink_addr)
    
    print("os : %s" %(os.getcwd()))
    
    cg = callgraph_rev(sink)
    print("Call Graph For vuln generated")
    #nx.write_gexf(cg, "pwn01.gexf")
    #nx.write_gml(cg, "pwn01.gml")
    #nx.write_graphml_lxml(cg, "pwn01_cg.graphml")
    
    chain = find_call_chain(cg, source_addr, sink_addr)
    print("Call chain generated")
    print([hex(f) for f in chain])
    
    case_inputs = proc_switch_case(chain)
    print("Case inputs to reach vuln addr : ")
    print(case_inputs)
    


PluginCommand.register('callgraph', 'generate callchain', main)

