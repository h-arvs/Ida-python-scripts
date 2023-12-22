import idaapi as api
import idautils as utils
import ida_name as idaname
import idc as idc
import json

# ask for a path
path = api.ask_file(True, "*.json", "Output file for dump")

# get names
names = dict(utils.Names())

# read user selection start
selection = idc.read_selection_start()

# Find nearest name at selection address
address, n, pos = idaname.NearestName(names).find(selection)

# get nearest name before our address
if address > selection:
    start = list(names.keys())[pos - 1]
    finish = address
else:
    start = address
    finish = list(names.keys())[pos + 1]

# base dict
vtable = {
"Name": {"Symbol": n,
         "Demangled": idc.demangle_name(n, api.cvar.inf.long_demnames)},
"Size": finish - start,
"Info": {"HexSize": hex(finish-start),
         "Functions": (finish-start) // 8},
"Functions": {}
}

index = 0
while start < finish:
    # grab symbol then append to functions dict with func index and that symbol
    vtable.get("Functions")[index] = idc.get_func_name(idc.get_qword(start))
    index += 1
    start += 8

# dump into specified path, will create a file if file not there
with open (path, "w") as out:
    out.write(json.dumps(vtable, indent=4))

api.msg(f"\nDumped vtable: {vtable.get('Name').get('Symbol')}")


