temperature = 70
weather = 'Sunny'
isWinter = True
aNumber = .06

if isWinter:
    print('Naaa, stay at home better')

if temperature > 50 and weather == 'Sunny':
    print('Go outside')
elif weather == 'Rainy' or temperature == 0:
    print('Its to cold')
else:
    print('Stay Inside')