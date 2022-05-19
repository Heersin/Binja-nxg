from binaryninja import BackgroundTaskThread

from .src.callchain import main
from binaryninja.interaction import AddressField, get_form_input, TextLineField
from .ui.utils import try_str2addr_or_neg_one


def print_chain(chain_list):
    print("CHAIN: ", end='')
    for item in chain_list:
        print(item, end='')
        print('->', end='')
    print("|")


class RecipeCallchain(BackgroundTaskThread):
    def __init__(self, view, src_addr, sink_addr):
        BackgroundTaskThread.__init__(self, "Analysis Backtrace Call Graph to Find a Call Chain", can_cancel=True)
        self.src_addr = src_addr
        self.sink_addr = sink_addr
        self.view = view

    def run(self):
        call_chain = [hex(i) for i in main(self.view, self.src_addr, self.sink_addr)]
        print_chain(call_chain)


def recipes_callchain(bv):
    source_f = TextLineField("src addr (default entry)", default=hex(bv.entry_point))
    sink_f = TextLineField('sink addr ', default='0x0')

    get_form_input([source_f, sink_f], 'Target Address Query')

    sink_addr = try_str2addr_or_neg_one(sink_f.result)
    src_addr = try_str2addr_or_neg_one(source_f.result)

    if sink_addr == -1:
        print("Sink Function Address Required")
        return

    recipe = RecipeCallchain(bv, src_addr, sink_addr)
    recipe.start()
