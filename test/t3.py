M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
col2 = [row[1] for row in M]
print(col2)
diag = [M[i][i] for i in [0, 1, 2]]
print(diag)
print(list(map(sum, M)))
bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))
print(bob2)
bob3 = list(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))
print(bob3)

rec = {'name': {'first': 'Bob', 'last': 'Smith'},
       'jobs': ['dev', 'mgr'],
       'age': 40.5}
print(rec['name'])
print(rec['name']['last'])
print(rec['jobs'])
rec['jobs'].append('janitor')
print(rec)
if 'dev' in rec:
    print('missing')

D = {'a': 1, 'c': 3, 'b': 2}
for key in sorted(D):
    print(key, '=>', D[key])
