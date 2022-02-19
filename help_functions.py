def make_list(n):  # tworzy pusta liste o dlugosci n
    data = list()
    for i in range(0, n):
        data.append(i)

    return data


def make_zero_list(n):  # tworzy liste o dlugosci n wypelniona zerami
    data = list()
    for i in range(0, n):
        data.append(0)

    return data


def make_list_range_step(start, stop, step):
    data = list()

    i = start
    while i <= stop:
        data.append(i)
        i += step

    return data


def find_median(arg_list):
    data = arg_list.copy()
    data.sort()
    dataLength = len(data)
    if dataLength % 2 == 0:
        return (data[int(dataLength/2)] + data[int((dataLength + 2) / 2)]) / 2
    else:
        return data[int((dataLength+1)/2)]