def all_same_old(items):
    all_good = False
    if all(i == items[0] for i in items):
        pass
    else:
        return False
    #first = items[0]
    #for item in items:
    #    if first != item:
    #        all_good = False
        #if not item:
        #    return False
    return True

def all_same(items):
    first = next(iter(items), None)
    return all(item == first for item in items)




if __name__ == "__main__":
    rtn = all_same([None, 4])
    #rtn = all_same([1, 1, 1])
    print(f'{rtn}')

