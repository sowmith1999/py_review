from typing import List

def make_stack():
    stacky = list()
    stacky.append('stack')
    return stacky

def pop(stacky):
    if(stacky[0]!='stack'):
        return 'not a stack'
    if(len(stacky) >=2):
        return stacky.pop()

def push(stacky: List,element: any):
    if(stacky[0]!='stack'):
        return 'not a stack'
    return stacky.append(1, element)
