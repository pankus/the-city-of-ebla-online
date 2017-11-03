"""
Python 3 json minifier for datatables ajax input
"""

import json

with open('ebdabib.txt', encoding="utf-8") as json_data:
    d = json.load(json_data)

data = []
for i in d:
    """ it needs a fresh list at every loop """
    record = []
    for k, v in i.items():
        record.append(v)
    data.append(record)

results = {"data": data}
results = json.dumps(results, ensure_ascii=False)
""" standard ouput print """
# print(results)

"""
create a file result.txt into the same folder
"""
with open('results.txt', 'w', encoding="utf-8") as file_result:
    file_result.write(results)
