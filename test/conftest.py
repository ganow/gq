from gq import gq
from expr import Node

def pytest_funcarg___(request):
    return gq('build/', [
            {'id': 0, 'seed': 1, 'mode': 'gauss', 'mean': 15},
            {'id': 1, 'seed': 2, 'mode': 'logn', 'mean': 15},
            {'id': 2, 'seed': 3, 'mode': 'gauss', 'mean': 15},
            {'id': 3, 'seed': 4, 'mode': 'logn', 'mean': 15}])

def pytest_funcarg__mtable(request):
    return open('test/mtable.tsv', 'r')

def pytest_funcarg__paramdict(request):
    return [{'id': 0, 'seed': 1, 'mode': 'gauss', 'mean': 15},
            {'id': 1, 'seed': 2, 'mode': 'logn', 'mean': 15},
            {'id': 2, 'seed': 3, 'mode': 'gauss', 'mean': 15},
            {'id': 3, 'seed': 4, 'mode': 'logn', 'mean': 15}]

def pytest_funcarg__query(request):
    return "((((a >= 10) & (a < 20)) | (b == 'hoge')) & (c <= 30))"

def pytest_funcarg__expr(request):
    a = Node('a')
    b = Node('b')
    c = Node('c')
    return ((((a >= 10) & (a < 20)) | (b == 'hoge')) & (c <= 30))
