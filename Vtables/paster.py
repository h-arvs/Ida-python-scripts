import idaapi as api
import idc as idc
import json

path = api.ask_file(False, "*.json", "Input dump file")

start = idc.get_screen_ea()

file = open(path, "r")

symbols = json.loads(file.read())

file.close()

for i in range(0, len(symbols)):
    idc.set_name(idc.get_qword(start + i*8), symbols[i])

api.msg("Pasted vtable!")


