# I created one variable to receive something

something = input('Type something: ')

# Now do the test to know the types

print('It is number: ', something.isnumeric())
print('It is a character: ', something.isalpha())
print('It is in UpperCase: ', something.isupper())
print('It is in LowerCase: ', something.islower())
print('It is a Alpha Numeric: ', something.isalnum())
print('Only contains spaces: ', something.isspace())
print('It is capitalized: ', something.istitle())