import json
import sys

with open('MD_Proyecto_Final_Completo.ipynb', 'r', encoding='utf-8') as f:
    d = json.load(f)

for c in d['cells']:
    if c['cell_type'] == 'code':
        source = ''.join(c['source'])
        if 'sklearn' in source or 'model' in source:
            print(source)
            print('-'*40)
