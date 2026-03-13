import os
import json


def file_read():
    try:
        with open('data.txt', 'r') as data_file:
            data = data_file.read()
        with open('log.txt', 'w') as log_file:
            log_file.write(data)
    except FileNotFoundError:
        with open('log.txt', 'w') as log_file:
            log_file.write('Error')


file_read()