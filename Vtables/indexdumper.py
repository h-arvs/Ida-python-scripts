import idaapi as api
import idc as idc

path = api.ask_file(True, "*.txt", "Output file for dump")

start = idc.read_selection_start()
end = idc.read_selection_end()

out = ""

for i in range(start, end, 8):
    symbol = idc.get_name(idc.get_qword(i))
    demangled = idc.demangle_name(symbol, idc.get_inf_attr(idc.INF_SHORT_DN))
    if not demangled:
        demangled = symbol
    out += f"[{(i-start)//8}]   {(demangled)}\n"

with open(path, "w") as f:
    f.write(out)

api.msg("\nDumped vtable indexes!")


