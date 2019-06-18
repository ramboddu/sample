import pandas as pd
from io import StringIO
import json

dialect = {"dialect":{
    "delimeter" : ""
}}

data = "a   ,String\n" \
       "b   ,String\n" \
    "c  ,date\n" \
       "d   ,Number"

df = pd.read_csv(StringIO(data), names=['name','datatype']).applymap(lambda x: x.strip())
df['position'] = df.index
dict = df.to_dict(orient='records')
print(dict)
for val in dict:
    if val['datatype'] in ['timestamp', 'date']:
        val['datatype'] = {'base': val['datatype'], 'format': "format"}
    else:
        val['datatype'] = "String"

print(dict)

# print(df)
# columns = df.to_json(orient='records')

# print(columns)
