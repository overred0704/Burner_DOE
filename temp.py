
#%%
burner_number = 6

# %%
def create_col():
    col = ['切換方式','切換時間']
    for i in range(int(burner_number)):
        name = i + 1
        col.append('burner_' + str(name))
    
    return col
# %%
c = create_col()
#%%
group = [3]

# %%
def create_content(iter):

    time = [30, 40, 50]
    methods = ['切換一', '切換二']
    
    col = []
    col.append(methods[0])
    col.append(time[iter])
    for i in range(burner_number):
        if (i+1)%2 == 1:
            col.append(1)
        else:
            col.append(0)
    return col
#%%
iter_num = 3*len(group)
# %%
for i in range(iter_num):
    cc = create_content(i)
    print(cc)
# %%
