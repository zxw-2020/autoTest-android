#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import os
# for root, dirs, files in os.walk(".", topdown=False):
#     for name in files:
#         print(os.path.join(root, name))
#     for name in dirs:
#         print(os.path.join(root, name))

# import os
# keyword='启动app'
# path='..\\test_case'
# steps=path+'\\'+keyword+'.py'
# for root, dirs, files in os.walk(path, topdown=False):
#     for name in files:
#         # print(os.path.join(root, name))
#         with open(os.path.join(root, name)) as f:
#             a = f.readlines()
#         if steps==os.path.join(root, name):
#             print(a)

import os
keyword='启动app'
def get_Test_Steps(keyword):
    for root, dirs, files in os.walk("..\\test_case", topdown=False):
        for name in files:
            # print(os.path.join(root, name))
            temp=os.path.join(root, name)
            temp=temp.split('.py')
            temp = temp[0].split('\\')
            temp=temp[len(temp)-1]
            # print(temp)
            if temp==keyword:
                path=os.path.join(root, name)
                # print(path)

    with open(path) as f:
        text = f.readlines()
    return text