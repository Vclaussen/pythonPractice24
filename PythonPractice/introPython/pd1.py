import pandas as pd
revenue = pd.Series([1000, 900, 1100, 400, 2000], ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'], name='Revenue')
expenses = pd.Series([900, 900, 900, 900, 900], ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'], name='Expenses')
print(revenue)
print('------------')
print(expenses)
print('------------')
print(revenue['Wed'])
print('------------')
print(expenses['Tue':'Thu'])
print('------------')
net_profit = pd.Series(revenue - expenses, name='Net Profit')
print(net_profit)
print('------------')
sum, counter = 0, 0
for x in net_profit:
    sum += x
    counter += 1
avg = int(sum/counter)
print(avg)