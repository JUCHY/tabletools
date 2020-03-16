# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 23:02:52 2019

@author: joshu
"""

import tabletools as tt


ll = tt.LabeledList([1, 2, 3, 4, 5], [True, 'BB', 'BB', 'CCC', 'D'])

print(str(ll))
print(repr(ll))

ll = tt.LabeledList([1, 2, 3, 4, 5], ['A', 'BB', 'BB', 'CCC', 'D'])

# 1 (values are taken from LabeledList as a list...
# more than one label yields all label and value pairs)
print(ll[tt.LabeledList(['A', 'BB'])])
print(ll[['A', 'BB']])

print(ll[[False, False, False, True, True]])

print(ll['A'])

print(ll['BB']) #

ll = tt.LabeledList([1, 2], ['x', 'y'])
print(ll==1)
print(ll>1)
print(ll<2)
print(ll!=1)
print(ll!=2)

print(tt.LabeledList([5, 6, 7]).map(lambda x: x * x))
t = tt.Table([['foo', 'bar', 'baz'],['qux', 'quxx', 'corge']])
print(str(t))





#####
# Remember... if only one column is given back, return a LabeledList
# ...but if there's more than one column, give back a Table
#####

# 1 (using a LabeledList to select columns)
t = tt.Table([[1000, 10], [200,2],[3, 300], [40, 4000], [7, 8]], ['foo', 'bar', 'bazzy', 'qux', 'quxx'], ['a', 'b', 'c', 'd', 'e'])
print(t[tt.LabeledList(['a', 'b'])])


# 2 (the first two columns are selected using a list of columns...
# notice that repeat columns are allowed)
t = tt.Table([[15, 17, 19], [14, 16, 18]], columns=['x', 'y', 'z'])
print(t[['x', 'x', 'y']])


# 3 (select only the first and third rows by using a list of booleans)
t = tt.Table([[1, 2, 3], [4, 5, 6], [7, 8 , 9]], columns=['x', 'y', 'z'])
print(t[[True, False, True]])

# 4a (using a column name that matches only a single column gives
# back a LabeledList... note no column names, but there are labels!)

t = tt.Table([[1, 2, 3], [4, 5, 6]], columns=['a', 'b', 'a'])
print(t['b'])


# 4b (however, if more than one column matches column name, include
# all matched columns in the resulting Table object)
t = tt.Table([[1, 2, 3], [4, 5, 6]], columns=['a', 'b', 'a'])
print(t['a'])



t = tt.Table([[1, 2], [3, 4], [5, 6], [7, 8]], columns=['x', 'y'])

print(t.head(2))

"""
  x y
0 1 2
1 3 4
"""

print(t.tail(2))

print(t.shape())