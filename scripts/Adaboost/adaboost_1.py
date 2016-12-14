# coding=utf-8
# Author: Lyy
# Email: henryly94@gmail.com
import math
import Image
import time


class Weak:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.lose = 0.0
        self.div = 2
        self.threshold = [4 for i in range(self.div)]
        self.neg = [1, 1]

    def output(self, div, x):
        return (self.threshold[div] < x) and (self.neg[div]) or (-self.neg[div])

    def train(self, data, weights):
        res_Em = []
        for div in range(self.div):
            best = self.low
            Em = 1
            ubest = self.low
            uEm = 0
            i = self.low
            while i < self.high:
                new_Em = 0
                for j in range(len(data)):
                    t = (float(data[j][div]) > i) and 1 or -1
                    if t != int(data[j][2]):
                        new_Em += weights[j][div]
                # time.sleep(0.05)
                if new_Em < Em:
                    Em = new_Em
                    best = i
                if new_Em > uEm:
                    uEm = new_Em
                    ubest = i
                i += 0.1
            print '%-5d%-10.3f%-10.3f%-10.5f%-10.5f' % (div, best, ubest, Em, 1-uEm)
            if Em >= 1-uEm:
                print 'reverse', Em
                Em = 1-uEm
                self.neg[div] *= -1
                best = ubest
            res_Em.append(Em)
            self.threshold[div] = best
        return res_Em

        # for each in data:
        #     print each[2], float(each[0]) * self.weight[0] + float(each[1]) * self.weight[1] + self.weight[2]



def input_data(data_path):
    data = []
    for each in open(data_path, 'r'):
        data.append(each.strip('\n').split(' '))
    return data


def training(num, data_path, weaks=None, alpha=None, D=None):
    data = input_data(data_path)
    if not D:
        D = [[1/float(len(data)), 1/float(len(data))] for i in range(len(data))]
    if not alpha:
        alpha = [[1, 1] for i in range(num)]
    if not weaks:
        weaks = [Weak(0, 8) for i in range(num)]
    for index in range(len(weaks)):
        Em = weaks[index].train(data, D)
        # print Em[0], Em[1]
        alpha[index] = [math.log(1/Em[0] - 1, math.e)/2, math.log(1/Em[1] - 1, math.e)/2]
        for div in range(2):
            Z =0.0
            for i in range(len(data)):
                Z += D[i][div] * math.exp(-alpha[index][div] * int(data[i][2]) * weaks[index].output(div, float(data[i][div])))
            for i in range(len(data)):
                D[i][div] = (D[i][div] * math.exp(-alpha[index][div] * int(data[i][2]) * weaks[index].output(div, float(data[i][div])))) / Z
        # print D
    return weaks, alpha, D


    # for i in range(num):
    #     alpha[i] = 0.5 * math.log((1/weaks[i].lose) - 1)
def result(x, weaks, alpha, div):
    sum = 0
    for i in range(len(weaks)):
        for d in range(div):
            sum += alpha[i][d] * weaks[i].output(d, x[d])
    return (sum < 0) and -1 or 1


def adaboost(num, data_path):
    print "Training..."
    _weaks, _alpha, _D = training(num, data_path)
    # quit(1)
    im = Image.new('RGB', (800, 800))
    print "Result Visualizing..."
    for i in range(800):
        for j in range(800):
            t = (result((i * 0.01, j * 0.01), _weaks, _alpha, 2) == 1) and 1 or 254
            # print t
            im.putpixel((i, j), (t, t, 255))
    im.save("1.jpg")
    data = input_data(data_path)
    for i in range(len(data)):
        x, y = float(data[i][0]), float(data[i][1])
        xx, yy = int(x * 100), int(y * 100)
        if xx >= 797:
            xx = 796
        if yy >= 797:
            yy = 796
        if xx <= 3:
            xx = 4
        if yy <= 3:
            yy = 4
        color = (int(data[i][2]) == 1) and 255 or 1
        for j in range(-3, 3):
            for k in range(-3, 3):
                im.putpixel((xx + j, yy + k), (color, 0, 0))
    im.save('2.jpg')

if __name__ == '__main__':
    adaboost(8, 'ada_data2')
