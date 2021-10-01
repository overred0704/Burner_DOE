#%%
import csv
#%%
class Burner_set():
    def __init__(self, burner_number):
        self.burner_number = burner_number
        self.group = []
        for i in range(1, int(self.burner_number/2)+1):
            if self.burner_number/i == 4 or self.burner_number/i == 2:
                self.group.append(i)

    def create_list(self):
        col = ['切換方式','切換時間']
        for i in range(int(self.burner_number)):
            name = i + 1
            col.append('burner_' + str(name))
        
        return col
    
    def create_content(self, iter):

        time = [30, 40, 50]
        methods = ['切換一', '切換二']
        
        col = []
        col.append(methods[0])
        col.append(time[iter])
        for i in range(self.burner_number):
            if (i+1)%2 == 1:
                col.append(1)
            else:
                col.append(0)
        return col

    def write_csv(self):
        with open('test.csv', 'w', encoding='Big5') as f:
            writer = csv.writer(f)
            header = self.create_list()
            writer.writerow(header)
            iter_num = 3*len(self.group)
            for i in range(iter_num):
                data = self.create_content(i)
                writer.writerow(data)
            
    #這邊還缺第二種情況
    



    def create_table(self):
        col = ['切換方式','切換時間']
        for i in range(int(self.burner_number)):
            name = i + 1
            col.append('burner_' + str(name))
        for i in range(1,6):
            col.append('weight_' + str(i))
            col.append('gas_' + str(i))

        #table = pd.DataFrame(columns=col)

        #return table

    def fill_method(self):
        tab = self.create_table()
        ind = ['切換一','切換一','切換一']
        ind_1 = ['切換一','切換一','切換一','切換二','切換二','切換二']
        t = [30, 40, 50]
        t_1 = [30, 40, 50, 30, 40, 50]

        if len(self.group) == 2:
            tab['切換方式'] = ind_1
            tab['切換時間'] = t_1
        elif len(self.group) == 1:
            tab['切換方式'] = ind
            tab['切換時間'] = t
       
        return tab

    def possible_set(self):
        tab = self.fill_method()
        for num in range(3):
            for i in range(self.burner_number):
                name = 'burner_' + str(i+1)
                if (i+1)%2 == 1:
                    tab[name][num] = 1
                else:
                    tab[name][num] = 0
        
        if len(tab) > 3:
            for j in range(3,6):
                for i in range(self.burner_number):
                    name = 'burner_' + str(i+1)
                    if (i+1)%4 == 1 or (i+1)%4 == 0:
                        tab[name][j] = 1
                    else:
                        tab[name][j] = 0
     
        return tab



    def export_csv(self):
        tab = self.possible_set()
        tab.to_csv('Burner_set.csv', index=False, encoding='big5')


#%%
def main():
    s = int(input('Enter the number of burner: '))
    if s %2 != 0 :
        print('Burner Number Error')
    else:
        b = Burner_set(s)
        print('Possible Switch Method:', len(b.group))
        b.export_csv()
        print('Table Generated Done!')


#%%
if __name__ == '__main__':
    main()

#要把整個combine一起 包成exe 不能安裝python
