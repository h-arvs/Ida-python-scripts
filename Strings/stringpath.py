import idaapi as api
import idc
import ida_kernwin as kerwin
import idautils as utils
import ida_xref as xr

depth = kerwin.ask_long(3, """
The depth of your search.

1 = Scan only selected function
2 = Scan selected function and all xrefs
3 = Scan selected function, all xrefs and all xrefs xrefs
...

High depths will result in longer scanning times.
""")


def get_strings(func: api.func_t):
    result = []
    for addr in utils.Heads(func.start_ea, func.end_ea):
        insn = api.insn_t()
        api.decode_insn(insn, addr)
        if insn.get_canon_mnem() == 'lea':
            addr2 = insn.ops[1].addr
            strlit = idc.get_strlit_contents(addr2)

            if strlit:
                result.append((strlit, addr))

    return result


def do(depth: int):
    if depth < 1:
        return
    cursor = idc.get_screen_ea()

    initial = api.get_func(cursor)

    funcs = [(initial, f"{hex(initial.start_ea)} (Your function)")]
    newfuncs = []

    strings = []

    iteration = 0
    print("Searching for strings...")
    while True:

        if not funcs:
            break

        iteration += 1
        for func, path in funcs:
            strings2 = get_strings(func)
            for string, addr in strings2:
                strings.append((string, hex(addr), path))

        if iteration == depth:
            break

        for func, path in funcs:
            for xref in utils.XrefsTo(func.start_ea, xr.XREF_ALL):
                x = api.get_func(xref.frm)
                if x:
                    newfuncs.append((x, f"{hex(xref.frm)} -> {path}"))

        funcs = newfuncs.copy()
        newfuncs.clear()

    for i in reversed(strings):
        print(f"String found {i[0]} at {i[1]} in {i[2]}")

    print("Finished!")


do(depth)