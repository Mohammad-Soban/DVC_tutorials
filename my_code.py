import pandas as pd
import os

data_dict = {'name': ['nick', 'david', 'joe', 'ross'],'age': ['15', '30', '27', '26'], 'city': ['Ahmedabad', 'Mumbai', 'Bengaluru', 'Delhi']}
df = pd.DataFrame.from_dict(data_dict)

data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, "sample_data.csv")
df.to_csv(file_path, index=False)

print("Data saved successfully.....")