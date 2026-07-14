

def validateStock(stockList: list):
    settedList = set(stockList)
    settedList.remove("")
    #settedList.remove(None)

    if len(settedList) == 0:
        return False
    else:
        return True
    