import pickle

try:
    with open("out.txt", "a+") as file:
        file.write('testline\n')

except:
    print('except')
finally:
    print('end')


obj = {'test1': 1, 'test2': 2}

with open('out.bin', 'wb') as file:
    pickle.dump(obj, file)

with open('out.bin', 'rb') as file:
    data = pickle.load(file)
    print(data)
