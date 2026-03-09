import pandas as pd

s = pd.Series([10,20,30,50])
# print(s)
# print(s.values)
# print(s.index)

# #assigning name to series which will become column namein dataframe
s.name = 'Numbers'
# print(s.name)
# print(s)


#--------Index
print(s[0])
print(s[0:2])
print(s[3:4])

