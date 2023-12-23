# Scripts for [IDA pro](https://hex-rays.com/ida-pro/) to aid reversing
These scripts are written using hexray's [IDAPython api](https://hex-rays.com/products/ida/support/idapython_docs/) and can only be used within the IDA interface.

## Usage

To run an IDA python script click File -> Script File, or use the hotkey Alt+F7
![image](https://github.com/h-arvs/Ida-python-scripts/assets/74739443/d41ffb89-1d44-467b-ae95-43b0819bd58b)

This will open up an explorer, you can then select a script and press 'Open' to run it.
![image](https://github.com/h-arvs/Ida-python-scripts/assets/74739443/fe8b26bb-1777-46e9-a0ab-24c7830f0427)

## Vtable Scripts
<a id="dumperpy"></a>
### [dumper.py](/Vtables/dumper.py)
This script will dump all indexes and mangled func name + some other info into a json file, this is for use with paster.py
To use the dumper script, select a partion of a vtable:  
<ins>Minecraft BDS with symbols</ins>
![image](https://github.com/h-arvs/Ida-python-scripts/assets/74739443/2fc1fdd2-c97e-41d9-aa96-866602113c8e)

Now run the dumper.py script, it will query a file, it will create a file for you if you just type a name in the input box. This file can be anywhere.
![image](https://github.com/h-arvs/Ida-python-scripts/assets/74739443/2edc85a2-6eea-480d-a6ca-263a9b4dfe2d)
Then click save.
The dumper will run and output the file with that name in the directory you gave it. One it is finished a message like this will appear in your output subview.
![image](https://github.com/h-arvs/Ida-python-scripts/assets/74739443/00c6cd83-4b40-40ca-bee3-fc8687c3e444)

![image](https://github.com/h-arvs/Ida-python-scripts/assets/74739443/597605a3-b11d-4902-b812-0b9f58920ece)
Yayyyyy vtable dumped :)))

### [indexdumper.py](/Vtables/indexdumper.py)
This script will dump all indexes of functions in a vtable, along with their demangled name.
It has the exact same usage as dumper.py, except dumps into a txt file.

### [paster.py](/Vtables/paster.py)
This script will paste results of dumper.py onto another vtable, it will name each function in one vtable with corresponding function in the dump.
To use this script, again select a partition from the vtable you dumped but on, in my case, the client db.  
<ins>Minecraft Bedrock client without symbols</ins>
![image](https://github.com/h-arvs/Ida-python-scripts/assets/74739443/4e2dac6f-6db9-4865-aa2e-8c7fdc7e2214)

Now run paster.py, it will again query a file, select the dumped vtable from dumper.py:
![image](https://github.com/h-arvs/Ida-python-scripts/assets/74739443/fa7bee98-d609-4120-8564-a3f29ac44859)
Now press open, the script will now start.

Once done you'll see this in your output subview:  
![image](https://github.com/h-arvs/Ida-python-scripts/assets/74739443/d264537c-68f3-4850-b661-0556d0bbd7e9)  
and this on your vtable view:
![image](https://github.com/h-arvs/Ida-python-scripts/assets/74739443/4397ab2a-4929-403a-bfec-764a223d42cb)

All the functions in the vtable are now named on the client! Happy reversing :)









