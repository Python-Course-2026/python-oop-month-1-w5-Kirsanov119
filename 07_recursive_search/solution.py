import os
import json
txt_list = []
def find_txt(folder, founded):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".txt"):
                txt_list.append(file)

    with open(founded, 'w', encoding='utf-8') as f:
        for name in txt_list:
            f.write(f"{name}\n")

find_txt('project', 'found.txt')