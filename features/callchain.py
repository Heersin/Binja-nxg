from .src.callchain import main
from binaryninja.interaction import AddressField, get_form_input


def print_chain(chain_list):
    print("CHAIN: ")
    for item in chain_list:
        print(hex(item), end='')
        print('->', end='')
    print("")


def recipes_callchain(bv):
    source_f = AddressField('src addr (default entry)', default=0)
    sink_f = AddressField('sink addr', default=0)
    get_form_input([source_f, sink_f], 'Target Address Query')

    sink_addr = sink_f.result
    src_addr = source_f.result

    if sink_addr == 0:
        print("Sink Function Address Required")
        return

    call_chain = [hex(i) for i in main(bv, sink_addr, src_addr)]
    print_chain(call_chain)