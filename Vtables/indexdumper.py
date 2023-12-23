import idaapi as api
import idautils as utils
import ida_name as idaname
import idc as idc

path = api.ask_file(True, "*.txt", "Output file for dump")

names = dict(utils.Names())

selection = idc.read_selection_start()

address, n, pos = idaname.NearestName(names).find(selection)

if address > selection:
    start = list(names.keys())[pos - 1]
    finish = address
else:
    start = address
    finish = list(names.keys())[pos + 1]

with open (path, "w") as out:
    index = 0
    while start < finish:
        # demangle name
        func = idc.demangle_name(idc.get_func_name(idc.get_qword(start)),api.cvar.inf.short_demnames)
        out.write(f"{index}: {func}\n")
        index += 1
        start += 8

api.msg(f"\nDumped indexes into {path}")


