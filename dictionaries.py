myDictionary = {'Hi': 'Hola', 
                'Bye': 'Adios', 
                'Well':'Bien', 
                'Cool':'Genial'}

del myDictionary['Cool']
sentence = 'Hi' + ' How are you today? ' + ' Bye '
translation = myDictionary.get('Hi') + ' How are you today? ' + myDictionary.get('Bye') 

print(myDictionary)
print('sentence:', sentence)
print('translation:', translation)
