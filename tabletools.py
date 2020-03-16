# tabletools.py
"""
try:
    with codecs.open('russian-troll-tweets/IRAhandle_tweets_1.csv', encoding="utf8") as f:
        for i, line in enumerate(f):
            words = line.split(',')
            fprint = '{:<30}' *(len(words[0:3]))
            print(fprint.format( *words[0:3]))
            if(i>5):
                break
except FileNotFoundError as e:
    print('ERROR!!!!!!!!')
    """

class LabeledList:
    def __init__(self, data=None, index=None):
        if(index==None):
            self.indexes = list(range(0, len(data)))
        else:
            self.indexes = index
        self.values = data
        
    def __str__(self):
        table = ""
        for x in range(0,len(self.values)):
            table += "{:<20} {:<20} \n".format(str(self.indexes[x]),str(self.values[x]))
        return table
    def __repr__(self):
        return str(self)
    
    def __getitem__(self, key_list):
        if(isinstance(key_list, LabeledList)):
            key_list = key_list.values
        if(isinstance(key_list,list)):
            if(isinstance(key_list[0], bool)):
                newindexes = []
                newvalues = []
                for i in range(0,len(self.values)):
                    if(key_list[i]==True):
                        newvalues.append(self.values[i])
                        newindexes.append(self.indexes[i])
                return LabeledList(newvalues, newindexes)
            elif(isinstance(key_list[0],(str,int))):
                newindexes = []
                newvalues = []
                for curr in key_list:
                    start = 0
                    while(True):
                        try:
                            num = self.indexes.index(curr, start)
                            start = num+1
                        except:
                            break
                        else:
                            newindexes.append(self.indexes[num])
                            newvalues.append(self.values[num])
                return LabeledList(newvalues, newindexes)
        else:
            num = self.indexes.index(key_list)
            try:
                self.indexes.index(key_list, num+1)                
            except:
                return self.values[num]
            else:
                newvalues = []
                newindexes = []
                newindexes.append(key_list)
                newvalues.append(self.values[num])
                start = num+1
                while(True):
                    try:
                        num = self.indexes.index(key_list, start)
                        start = num+1
                    except:
                        break
                    else:
                        newindexes.append(key_list)
                        newvalues.append(self.values[num])
            return LabeledList(newvalues, newindexes)
        
    def __iter__(self):
        return iter(self.values)
    
    def __eq__(self, scalar):
        newindexes = []
        newvalues = []
        for i,x in enumerate(self.values):
            if float(x)==scalar:
                newindexes.append(self.indexes[i])
                newvalues.append(True)
            else:
                newindexes.append(self.indexes[i])
                newvalues.append(False)
        return LabeledList(newvalues, newindexes)
                
    def __ne__(self, scalar):
        newindexes = []
        newvalues = []
        for i,x in enumerate(self.values):
            if float(x)!=scalar:
                newindexes.append(self.indexes[i])
                newvalues.append(True)
            else:
                newindexes.append(self.indexes[i])
                newvalues.append(False)
        return LabeledList(newvalues, newindexes)
    
    def __gt__(self, scalar):
        newindexes = []
        newvalues = []
        for i,x in enumerate(self.values):
            if float(x)>scalar:
                newindexes.append(self.indexes[i])
                newvalues.append(True)
            else:
                newindexes.append(self.indexes[i])
                newvalues.append(False)
        return LabeledList(newvalues, newindexes)
    
    def __lt__(self, scalar):
        newindexes = []
        newvalues = []
        for i,x in enumerate(self.values):
            if float(x)<scalar:
                newindexes.append(self.indexes[i])
                newvalues.append(True)
            else:
                newindexes.append(self.indexes[i])
                newvalues.append(False)
        return LabeledList(newvalues, newindexes)
    
    def map(self, f):
        newvalues = []
        for x in self.values:
            newvalue = f(x)
            newvalues.append(newvalue)
        return LabeledList(newvalues, self.indexes)
    

class Table:
    def __init__(self, data, index=None, columns=None):
        self.data = data
        self.index = index
        self.columns = columns
        if(index==None):
            self.index = list(range(0, len(data)))
        if(columns==None):
            self.columns = list(range(0,len(data[0])))
            
            
            
            
    def __str__(self):
        strtoreturn = ""
        fprint = '{:<30}' *(len(self.columns)+1)
        strtoreturn += fprint.format("", *self.columns)+'\n'
        for i,x in enumerate(self.index):
            lprint = '{:<30}' *(len(self.data[i])+1)
            strtoreturn += lprint.format(x,*self.data[i])+'\n'
        
        return strtoreturn;        

        
    def __repr__(self):
        return str(self)
    
    def column(self, index):
        data = { x[index] for x in self.data}
        return data
    
    def __getitem__(self, col_list):
        if(isinstance(col_list, LabeledList)):
            col_list = col_list.values;
        if(isinstance(col_list, list)):
            if(isinstance(col_list[0],bool)):
                newtable = []
                newindex = []
                m = 0
                for i, y in enumerate(col_list):
                    if(y):
                        newtable.append(self.data[i])
                        newindex.append(self.index[m])
                    m+=1
                    
                return Table(newtable, newindex, self.columns)
            else:
                newtable = []
                for x in self.data:
                    newrow = []
                    newcolumns = []
                    for y in col_list:
                        index = self.columns.index(y)
                        newcolumns.append(y)
                        newrow.append(x[index])
                    newtable.append(newrow);
                return Table(newtable,self.index, newcolumns);
        else:
            num = self.columns.index(col_list)
            try:
                self.columns.index(col_list, num+1)                
            except:
                lblist = self.column(num)
                return LabeledList(lblist)
            else:
                newtable = []
                newcolumns = []
                lblist = self.column(num)
                it1 = { i for i in lblist}
                newcolumns.append(col_list)
                for x in it1:
                    newtable.append([x])
                start = num+1
                while(True):
                    try:
                        num = self.columns.index(col_list, start)
                        start = num+1
                    except:
                        break
                    else:
                        newcolumns.append(col_list)
                        lblist = self.column(num)
                        it1 = { i for i in lblist}
                        for i,x in enumerate(it1):
                            newtable[i].append(x)
            return Table(newtable, self.index, newcolumns )       
        
    def head(self, n):
        return Table(self.data[0:n], self.index[0:n],self.columns)
    
    def tail(self, n):
        return Table(self.data[len(self.data)-n : len(self.data)], self.index[len(self.index)-n : len(self.index)], self.columns)
    
    def shape(self):
        return ( len(self.index), len(self.columns))
    
    
def read_csv(fn, comma=None):
    f = open(fn, 'r')
    columns = f.readline()
    columns = columns.split(comma)
    for i in range(0,len(columns)):
        columns[i] = columns[i].strip()
        try:
            columns[i] = float(columns[i])
        except:
            pass
    lines = f.readlines()
    newlines = []
    for line in lines:
        curr = line.split(comma)
        for i in range(0, len(curr)):
            curr[i] = curr[i].strip()
            try:
                curr[i] = float(line[i])
            except:
                pass
        newlines.append(curr)
    
    return Table(newlines, None, columns)
            
        
    
            
if __name__ == '__main__':
    print(read_csv('13 - Gender gap in wages  by occupation  age and persons with disabilities_data.csv',','))
            
            
                
                
            
            
            