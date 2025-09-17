import os
import pandas as pd

    # combine 2413 + 2423 into the same folder (pre_gsheet)
# folder = r"C:\Users\Bella\tutorial\yt_tut\sql\fin_tracker\notion"
# df = []
# for file in os.listdir(folder):
#     if file.endswith(".csv"):
#         df.append(pd.read_csv(os.path.join(folder, file)))
# df_master = pd.concat(df, ignore_index=True)
# df_master.to_csv('pre_gsheet.csv', index = False)
        
# read file
df = pd.read_csv('pre_gsheet.csv')

#strip empty rows
df.replace('', pd.NA, inplace=True)
df = df.dropna(axis=0, how='all')

#modify 'convenience' in 'Wants / Needs' to 'wants
df.loc[df['Wants / Needs'] == 'convenience', 'Wants / Needs'] = 'Need'
df.loc[df['Wants / Needs'] == 'Wants', 'Wants / Needs'] = 'Want'
df.loc[df['Wants / Needs'] == 'Needs', 'Wants / Needs'] = 'Need'
df.loc[df['Type'] == 'Cooking', 'Type'] = 'Food'

#capitalize 'Wants / Needs' and 'Category'
cols_to_format = ['Wants / Needs', 'Type']
for col in cols_to_format:
    df[col] = df[col].apply(lambda x: x.title() if isinstance(x, str) else x)

# # modify date format to dd/mm/yyyy
df['Date'] = pd.to_datetime(df['Date'], dayfirst = True)
df = df.sort_values(by='Date', ascending=False)
df['Date'] = df['Date'].dt.strftime('%d/%m/%Y')
df.to_csv("pre_gsheet.csv", index=False)