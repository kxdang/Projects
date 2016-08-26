catNames = []
while True:
    print('Enter the naem of cat ' + str(len(catNames) + 1) +
          ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
print('The cat names: ')
for name in catNames:
    print('  ' + name)
