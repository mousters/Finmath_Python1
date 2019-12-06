def ite_list(item):
    iter_items=iter(item)
    while True:
        try:
            it=next(iter_items)
            print(it)
        except StopIteration:
            break
if __name__=='__main__':
    item = [1, 2, 3, 4]
    ite_list(item)