from .src.callchain import main
from binaryninja.interaction import AddressField, get_form_input, TextLineField
from .ui.utils import try_str2addr_or_neg_one


def print_chain(chain_list):
    print("CHAIN: ")
    for item in chain_list:
        print(item, end='')
        print('->', end='')
    print("|")


def recipes_callchain(bv):
    source_f = TextLineField("src addr (default entry)", default='0x0')
    sink_f = TextLineField('sink addr ', default='0x0')

    get_form_input([source_f, sink_f], 'Target Address Query')

    sink_addr = try_str2addr_or_neg_one(sink_f.result)
    src_addr = try_str2addr_or_neg_one(source_f.result)

    if sink_addr == -1:
        print("Sink Function Address Required")
        return

    call_chain = [hex(i) for i in main(bv, sink_addr, src_addr)]
    print_chain(call_chain)