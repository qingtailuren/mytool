# -*- coding: utf-8 -*-
import os

os.system(r'dir E:\ /B/S/A-D > list2.txt ')

def check_contain_chinese(check_str):
    for ch in check_str.decode('utf-8'):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False
    
fk = open("key.txt", "r", encoding='utf-8')               # 返回一个文件对象   
fd = open("list2.txt", "r", encoding='utf-8', errors="ignore")
keywords = fk.readlines()
dicts = fd.readlines()
num = 0
result = "result.txt"
fw = open("result.txt", "w+", encoding='utf-8')
for keyword in keywords:
    print("[+]finding " + keyword + " ...")
    for dict in dicts:
        ret = dict.find(keyword, 0, len(dict))
        if ret != -1:
            print(dict)
            fw.writelines(dict)
fw.close()