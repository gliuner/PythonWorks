'''def main(data):
    newdatamas = []
    for i in data:
        newdata = dict()
        flag = 0
        for j in i:
            if j is None:
                flag += 1
                if flag > 2:
                    break
                continue
            if '@' in j:
                flag = 0
                newdata[j.split("@")[0]] = None
                continue
            if j == "да":
                flag = 0
                newdata['Y'] = None
                continue
            if j == "нет":
                flag = 0
                newdata['N'] = None
                continue
            if ',' in j:
                flag = 0
                newdata[j.split(',')[0]] = None
                continue
            else:
                flag = 0
                u = j.split('-')
                newdata[u[2][2] + u[2][3] + '/' + u[1] + '/' + u[0]] = None
                continue
        if len(newdata) != 0:
            newdatamas.append(list(newdata.keys()))
    return newdatamas


data = [["kikov54@yahoo.com", None, "да", None, "10-02-2002", "Киков, С. Ч.", "Киков, С. Ч."],
        [None, None, None, None, None, None, None],
        ["kikov54@yahoo.com", None, "да", None, "10-02-2002", "Киков, С. Ч.", "Киков, С. Ч."]]
print(main(data))'''


def main(data):
    newdatamas = []
    for i in data:
        newdata = []
        flag = 0
        for j in i:
            if j is None:
                flag += 1
                if flag > 2:
                    break
                continue
            if j == "1":
                flag = 0
                newdata.append('Y')
                continue
            if j == "0":
                flag = 0
                newdata.append('N')
                continue
            if '.' in j:
                flag = 0
                newdata.append(j.split(' ')[0])
                continue
            else:
                flag = 0
                u = j.split('-')
                newdata.append("(" + u[0] + ")" + " " + u[1] + "-" + u[2])
                continue
        if len(newdata) != 0:
            newdatamas.append(newdata)
    newdatamas = sorted(newdatamas, key=lambda x: x[2])
    newdatamas = [*zip(*newdatamas)]
    answer = [list(i) for i in newdatamas]
    return answer


data = [[None, "1", "788-300-8070", None, "Шулский А.Н."],
        [None, None, None, None, None, None],
        [None, "0", "562-670-2636", None, "Цедский А.Н."]]
print(main(data))
