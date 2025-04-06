# VTABLES

## [dumper.py](./dumper.py)
Dumps vtables into an output json file containing a list of each function symbol

### Usage:

- Select the segment of a vtable you want to dump
![](./Res/dumper1.png)
- Run script file
- Enter name for output and press save
- (name).json will now be populated with a list of symbols
![](./Res/dumper2.png)

## [paster.py](./paster.py)
Pastes output files from dumper.py

### Usage:
- Select start of vtable segment
![](./Res/paster1.png)
- Run script file
- Select your (name).json file from dumper.py and press open
- You will now see functions in the vtable named
![](./Res/paster2.png)

## [indexdumper.py](./indexdumper.py)
Dumps index and demangled func names from a vtable in `[index]   Name` format

### Usage:
- Select the segment of a vtable you want to dump
![](./Res/dumper1.png)
- Run script file
- Enter name for output and press save
- (name).txt will now be populated with funcs in `[index]   Name` format
![](./Res/indexdumper1.png)