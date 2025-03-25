import pandas as pd
from sqlalchemy import create_engine

with open("alarms.txt", "r") as file:
    content = file.read()

# there's a line in the bottom that is different, remove that
if "Total number of alarms" in content:
    content = content.split("Total number of alarms")[0]

# split long string into list of strings of blocks
blocks = content.strip().split("\n\n")

print(type(blocks))
print("number of blocks", len(blocks))

# Define the fields you care about
WANTED_FIELDS = {
    "NodeName",
    "specificProblem",
    "eventTime",
    "problemText",
    "alarmState",
    "alarmId",
    "probableCause",
    "eventType"
}

records = []

for block in blocks:
    record = {}
    # this splits the each block into a list of key values pair
    # ["key:value", "key:value"]
    lines = block.strip().split("\n")
    
    for line in lines:
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            if key in WANTED_FIELDS:
                record[key] = value.strip()
    
    # add each record into records
    records.append(record)

# debug to check
df = pd.DataFrame(records)
#print(df.count())
print(df.head())
print(df.shape)

# --------------- CLEANING -----------------------
print((df["problemText"] == '').sum(), "rows have empty strings in problemText")
df["alarmId"] = pd.to_numeric(df["alarmId"], errors="coerce")


# check eventTime
#print(df[["NodeName", "eventTime"]])
df["eventTime"] = pd.to_datetime(df["eventTime"])
#print(df["eventTime"].dt.tz)
df["loading_time"] = df["eventTime"].dt.tz_localize("EST")

print(df.columns)
#Confirm timezone
#print(df["loading_time"].dt.tz)
#print(df.head())

def get_site(node):
    # make sure that node is long enough to do transformations
    if isinstance(node, str) and len(node) >= 3:
        start_index = None
        for i, char in enumerate(node):
            if char.isdigit():
                start_index = i
                break
        
        end_index = None
        for i in range(len(node) -1, -1, -1):
            if node[i].isalpha():
                end_index = i
                break
            
        if start_index is not None and end_index is not None and start_index <= end_index:
            return node[start_index:end_index + 1]
        
# apply to DataFrame
df["site"] = df["NodeName"].apply(get_site)

print("Before dropping duplicates:", len(df))
df = df.drop_duplicates()
print("After dropping duplicates:", len(df))

print(df[["NodeName", "site"]].head(10))

print(df)
                
engine = create_engine("postgresql+psycopg2://rene_perida:password@localhost:5432/db1")
table_name = 'alarms'

df.to_sql(table_name, engine, if_exists='replace', index=False)

