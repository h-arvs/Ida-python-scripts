import idaapi as api
import idautils as utils
import ida_name as idaname
import idc as idc
import json


path = api.ask_file(True, "*.json", "Output file for dump")

names = dict(utils.Names())

selection = idc.read_selection_start()

address, n, pos = idaname.NearestName(names).find(selection)

if address > selection:
    start = list(names.keys())[pos - 1]
    finish = address
else:
    start = address
    finish = list(names.keys())[pos + 1]

# base dict
vtable = {
"Name": {"Symbol": n,
         "Demangled": idc.demangle_name(idc.get_name(start), api.cvar.inf.long_demnames)},
"Size": finish - start,
"Info": {"HexSize": hex(finish-start),
         "Functions": (finish-start) // 8},
"Functions": {}
}

index = 0
while start < finish:
    vtable.get("Functions")[index] = idc.get_func_name(idc.get_qword(start))
    index += 1
    start += 8

with open (path, "w") as out:
    out.write(json.dumps(vtable, indent=4))

api.msg(f"\nDumped vtable: {vtable.get('Name').get('Symbol')}")


