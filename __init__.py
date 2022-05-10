from binaryninja import *
from .features.callchain import recipes_callchain

# Note that this is a sample plugin and you may need to manually edit it with
# additional functionality. In particular, this example only passes in the
# binary view. If you would like to act on an addres or function you should
# consider using other register_for* functions.

# Add documentation about UI plugin alternatives and potentially getting
# current_* functions

PluginCommand.register('BinjaNxG\\Recipes\\Callchain', 'generate callchain', recipes_callchain)
