def decorator_list(fn):
    def inner(list_of_tuples):
        return [fn(val[0],val[1]) for val in list_of_tuples]
    return inner
@decorator_list
def add_together(a,b):
    return a*b
print([(1,3),(3,5),(5,7),(7,9)])