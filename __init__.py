from binaryninja import *
from .features.callchain import recipes_callchain
from .features.gen_graphs import gen_what
from .features.graph_manager import list_graphs, info_show, set_current_graph
from .features.graph_operation import has_node

# Note that this is a sample plugin and you may need to manually edit it with
# additional functionality. In particular, this example only passes in the
# binary view. If you would like to act on an addres or function you should
# consider using other register_for* functions.

# Add documentation about UI plugin alternatives and potentially getting
# current_* functions


# ******* For Develop Reference ********
def test_address(bv, addr):
    print("Plugin Detect Address : " + hex(addr))


def test_function(bv, fn):
    print("Plugin Detect Function : " + hex(fn.start))


def test_llil(bv, llil):
    print("Plugin Detect LLIL : " + str(llil))


def test_llil_fn(bv, llil_fn):
    print("Plugin Detect LLIL FN" + str(llil_fn))


PluginCommand.register_for_address("BinjaNxG\\Dev\\addr", "test addr", test_address)
PluginCommand.register_for_function("BinjaNxG\\Dev\\func", "test funtion", test_function)
PluginCommand.register_for_low_level_il_instruction("BinjaNxG\\Dev\\LLIL", "test LLIL", test_llil)
PluginCommand.register_for_low_level_il_function("BinjaNxG\\Dev\\LLILFN", "test LLIL FN", test_llil_fn)

# ===================== Plugin Features =========================
# ******** Recipes *********
PluginCommand.register('BinjaNxG\\Recipes\\Callchain', 'generate callchain', recipes_callchain)

# ******** Graphs **********
PluginCommand.register('BinjaNxG\\GenGraphs\\what', "test", gen_what)
PluginCommand.register('BinjaNxG\\Manager\\list', "test", list_graphs)
PluginCommand.register('BinjaNxG\\Manager\\info current', "test", info_show)
PluginCommand.register('BinjaNxG\\Manager\\set current', "test", set_current_graph)
PluginCommand.register('BinjaNxG\\Operation\\has node', "test", has_node)
