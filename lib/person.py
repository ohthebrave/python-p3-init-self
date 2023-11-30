#!/usr/bin/env python3

class Person:
    def __init__(self, name):
        self.name = name

    def parent_name(self, parent):
        self.parent = parent    


jon = Person('Joe')
jon.parent_name('Mose')
print(jon.parent)