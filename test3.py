def parser(str_ :str) -> dict:
    data = str_.split()
    data_dict = dict([[i.split('=')[0], float(i.split('=')[1]) if n == 2 else int(i.split('=')[1])] for n, i in enumerate(data[-4:-1])])
    return data_dict