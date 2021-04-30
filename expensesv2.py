expenses  = []
number_expenses = int(input('Introduce the number of expenses: '))

for i in range(number_expenses):
    expenses.append(float(input('Enter an expense: ')))

total = sum(expenses)

print('You spent $', total, ' on expenses', sep='')

