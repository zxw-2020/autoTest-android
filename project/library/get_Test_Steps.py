#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import os
# for root, dirs, files in os.walk(".", topdown=False):
#     for name in files:
#         print(os.path.join(root, name))
#     for name in dirs:
#         print(os.path.join(root, name))
import os
path='..\\test_case'
steps=path+'\\'+'启动app.py'
for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        # print(os.path.join(root, name))
        with open(os.path.join(root, name)) as f:
            a = f.readlines()
        if steps==os.path.join(root, name):
            print(a)




