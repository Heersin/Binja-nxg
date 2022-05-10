from binaryninja.interaction import AddressField, get_form_input

def ui_query_target_addr():
    source_f = AddressField('src addr (default entry)', default=-1)
    sink_f = AddressField('sink addr', default=-1)

    get_form_input([source_f, sink_f], 'Target Address Query')

    if sink_f.result == -1:
        print("Target Address Is Required")

    return (source_f.result, sink_f.result)