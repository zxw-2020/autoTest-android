import os
for root, dirs, files in os.walk("..\\test_case", topdown=False):
    for name in files:
        temp = os.path.join(root, name)
        temp = temp.split('.py')
        print(temp)
        temp = temp[0].split('\\')
        for i in range(len(temp)):
            print(temp[i])

