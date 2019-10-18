import collections
mset = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
print(mset)

li = ['a', 'asd', 'b', 'a', 'x', 'a']
d1 = dict([i, li.count(i)] for i in li)
print(d1)
