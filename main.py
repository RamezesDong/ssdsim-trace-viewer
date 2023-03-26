import matplotlib.pyplot as plt
import math
from pprint import pprint


def get_matrix(path):
    with open(path) as file_object:
        contents = file_object.read()
    matrix = list()
    lines = contents.splitlines(False)
    for str in lines:
        line = list()
        for item in str.split():
            line.append(float(item))
        matrix.append(line)
        # if line[0] > 120000:
        #     break
    return matrix


def main():
    matrix = get_matrix('./ssd-trace/HM_1')
    trace = {}
    for line in matrix:
        if trace.get(line[2], -1) == -1:
            time = [line[0]]
            trace[line[2]] = time  # map<address, io times>
        else:
            (trace.get(line[2])).append(line[0])
    time = [0] * 101
    for key in trace:
        # print(key , len(trace[key]))
        if len(trace[key]) > 1000:
            time[100] += 1
        else:
            time[len(trace[key]) // 10] += 1
    print(time)
    for i in range(0, len(time)):
        if time[i] > 0:
            time[i] = math.log(time[i], 2)
    print(len(matrix))
    print(len(trace))
    print(time)
    x = list(range(len(time)))
    y = time
    plt.bar(x, y)
    plt.show()


if __name__ == "__main__":
    main()
