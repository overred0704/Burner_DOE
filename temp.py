
# %%
import pandas as pd
# %%
table = pd.read_excel('set.xlsx')
# %%
ind = ['切換一','切換一','切換一']
ind_1 = ['切換一','切換一','切換一','切換二','切換二','切換二']
t = [30, 40, 50]
t_1 = [30, 40, 50, 30, 40, 50]
table['切換方式'] = ind_1
table['切換時間'] = t_1

# %%

# %%
table.to_excel('set_2.xlsx', index=False)

#%%
table2 = pd.read_excel('set2.xlsx')
# %%
len(table2)
# %%
s = int(input('test: '))
# %%
