
# %%
import pandas as pd
# %%
table = pd.read_excel('test.xlsx')



# %%
table.to_excel('set_2.xlsx', index=False)

#%%
table2 = pd.read_excel('set2.xlsx')
# %%
len(table2)
# %%
s = int(input('test: '))
# %%
