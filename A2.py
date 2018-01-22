import math
import turtle
from turtle import *


# 绘制分形树

# 1/3  右偏 a°  度数  正数  计算与绝对偏移度数
# 2/3  左偏 a°  度数  负数
# 根据起点和偏转角度计算终点

length = 500  # 初始长度
current_len = length  # 当前长度
min_length = 5  # 最小长度
startx = 0
starty = -250  # 初始坐标
a = 30  # 初始度数
color = ['RoyalBlue','Cyan', 'SkyBlue', 'LightSlateBlue']  # '#EE7600', '#00F5FF', '#F08080', '#48D1CC',
colorx = 0
t = Turtle()
t.color(color[colorx])
colorx = (colorx + 1) % len(color)


class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def output(self):
        print('x: %d' % self.x, 'y: %d' % self.y)


class line():
    def __init__(self, begin, end, length, degree):
        self.begin = begin
        self.end = end
        self.length = length
        self.degree = degree

    def output(self):  # float
        print('begin:%d %d' % (self.begin.x, self.begin.y), 'end:%d %d' % (self.end.x, self.end.y))
        print('length:%d' % self.length, 'degree:%d' % self.degree, '\n')


def end_calculation(begin, length, a):  # 起点坐标  偏移度数 -> 终点坐标
    end = point
    a = a * math.pi / 180
    end.y = begin.y + length * math.cos(a)
    if a < 0:
        end.x = begin.x + length * math.sin(a)
    else:
        end.x = begin.x + length * math.sin(a)
    return point(end.x, end.y)


def cir_node(line, x):  # x： 1 第一个节点  2 第二个节点
    if x == 1:
        # point1 = point
        x = line.begin.x + (line.end.x - line.begin.x) / 3
        y = line.begin.y + (line.end.y - line.begin.y) / 3
        return point(x, y)
    elif x == 2:
        # point2 = point
        x = line.begin.x + (line.end.x - line.begin.x) * 2 / 3
        y = line.begin.y + (line.end.y - line.begin.y) * 2 / 3
        return point(x, y)


def draw(begin, end):
    t.hideturtle()
    t.pensize(2)
    t.speed(10)
    t.left(90)

    t.penup()
    t.goto(begin.x, begin.y)
    t.pendown()
    t.goto(end.x, end.y)


def circulate(x):
    global colorx
    if int(x.length / 3) > int(min_length):
        print('line1:')
        p1 = cir_node(x, 1)  # 节点1 起点
        length1 = x.length * 2 / 3
        degree1 = x.degree + a
        line1 = line(p1, end_calculation(p1, length1, degree1), length1, degree1)
        line1.output()
        # 计算线段画图
        t.color(color[colorx])
        colorx = (colorx + 1) % len(color)
        draw(line1.begin, line1.end)
        circulate(line1)

        print('line2:')
        p2 = cir_node(x, 2)  # 节点2 起点
        length2 = x.length / 3
        degree2 = x.degree - a
        line2 = line(p2, end_calculation(p2, length2, degree2), length2, degree2)
        line2.output()
        # t.color('blue')
        t.color(color[colorx])
        colorx = (colorx + 1) % len(color)
        draw(line2.begin, line2.end)
        circulate(line2)


def main():  # length,min_length
    init_point = point(startx, starty)
    degree = 0
    x = line(init_point, end_calculation(init_point, length, degree), length, degree)  # 初始线段
    x.output()
    draw(x.begin, x.end)
    circulate(x)


if __name__ == '__main__':
    main()
    turtle.done()
