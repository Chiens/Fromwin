# -*- coding: utf-8 -*-
'''
@ Author: chiens
@ FileName: dict_test0.py
@ Time: 2018-6-22
@ Context: The first test  of dict.
'''

'''
I'll creat a class to work out many kinds method of dict-object.
'''
class DictTestF(object):
    '''This class creat with add delet find exchang method.'''
    def __init__(self):
        self.mydict = dict()
        print('You should creat a new dict to use.')
        while True:
            self.newdict_key = input('Enter a key:')
            self.newdict_value = input('Enter a value:')
            self.newdict_choice = input('')
        return self
    def myadd(self,):
        pass
    def mydelet(self):
        pass
    def myfind(self):
        pass
    def myexchang(self):
        pass