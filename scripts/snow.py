# coding=utf-8
# Author: Lyy
# Email: henryly94@gmail.com
import random
from PIL import Image
import images2gif


class Snow:

    amount = 0

    height = 100

    width = 100

    hor_rate = 0.02 / 24

    ver_rate = 0.2 / 24

    pos = []

    velocity = []

    def __init__(self, windows, amt=5):
        self.height, self.width = windows
        self.amount = amt
        self.pos = [
            [
                random.random() * self.width,
                random.random() * self.height
            ]
            for _ in xrange(amt)]
        self.velocity = [
            [
                random.random() * self.width * self.hor_rate,
                self.ver_rate * self.height + random.random() * self.height * self.ver_rate
            ]
            for _ in xrange(amt)]

    def draw(self):
        img = Image.new('RGB', (self.width, self.height), (0, 0, 0))
        for i in xrange(self.amount):
            img.putpixel(map(int, self.pos[i]), (255, 255, 255))
        return img

    def gen(self, seconds):
        pics = []
        pics.append(self.draw())
        for i in xrange(seconds * 24):
            for j in xrange(self.amount):
                self.get_next(j)
            pics.append(self.draw())

        images2gif.writeGif('test.gif', pics, duration=1.0/24)
        # for i in xrange(len(pics)):
        #     pics[i].save('%03d.jpg' % i, 'jpeg')

    def get_next(self, idx):
        if not 0 <= idx < self.amount:
            return False
        self.pos[idx] = [
            (self.pos[idx][0] + self.velocity[idx][0] + self.width) % self.width,
            (self.pos[idx][1] + self.velocity[idx][1] + self.height) % self.height
        ]

if __name__ == '__main__':
    s = Snow((100, 100), 50)
    s.gen(10)
