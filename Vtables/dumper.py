import idaapi as api
import idc as idc
import json


path = api.ask_file(True, "*.json", "Output file for dump")

start = idc.read_selection_start()
end = idc.read_selection_end()

out = []

for i in range(start, end, 8):
    out.append(idc.get_name(idc.get_qword(i)))

with open(path, "w") as f:
    f.write(json.dumps(out))

api.msg("\nDumped vtable!")


