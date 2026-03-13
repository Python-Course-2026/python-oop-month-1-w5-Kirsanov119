
import os
import json
type=['0x89', '0x50', '0x4E', '0x47']
def check_file(filename_1, filename_2):

    with open(filename_1, 'rb') as f1:
        data = f1.read(4) #чтение первых 4 байтов
        if data == b'\x89PNG':
            result = 'PNG'
        else:
            result = 'UNKNOWN'

    with open(filename_2, 'w') as f2:
        f2.write(result)

check_file('file.bin', 'type.txt')