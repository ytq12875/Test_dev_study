# -*- coding: utf-8 -*-
# @Time    : 2019/12/29 下午7:43
# @Author  : YTQ
# @FileName: turtle_demo.py
# @Software: PyCharm

import turtle
from datetime import *


class clock:

    def __init__(self):
        global printer
        # 重置Turtle指向北
        turtle.mode("logo")
        # 建立三个表针Turtle并初始化
        self.mkHand("secHand", 135)
        self.mkHand("minHand", 125)
        self.mkHand("hurHand", 90)
        self.secHand = turtle.Turtle()
        self.secHand.shape("secHand")
        self.minHand = turtle.Turtle()
        self.minHand.shape("minHand")
        self.hurHand = turtle.Turtle()
        self.hurHand.shape("hurHand")

        for hand in self.secHand, self.minHand, self.hurHand:
            hand.shapesize(1, 1, 3)
            hand.speed(0)

        # 建立输出文字Turtle
        printer = turtle.Turtle()
        # 隐藏画笔的turtle形状
        printer.hideturtle()
        printer.penup()

    # 抬起画笔，向前运动一段距离放下
    def Skip(self, step):
        turtle.penup()
        turtle.forward(step)
        turtle.pendown()

    def mkHand(self, name, length):
        # 注册Turtle形状，建立表针Turtle
        turtle.reset()
        self.Skip(-length * 0.1)
        # 开始记录多边形的顶点。当前的乌龟位置是多边形的第一个顶点。
        turtle.begin_poly()
        turtle.forward(length * 1.1)
        # 停止记录多边形的顶点。当前的乌龟位置是多边形的最后一个顶点。将与第一个顶点相连。
        turtle.end_poly()
        # 返回最后记录的多边形。
        handForm = turtle.get_poly()
        turtle.register_shape(name, handForm)

    def SetupClock(self, radius):
        # 建立表的外框
        turtle.reset()
        turtle.pensize(7)
        for i in range(60):
            self.Skip(radius)
            if i % 5 == 0:
                turtle.forward(20)
                self.Skip(-radius - 20)

                self.Skip(radius + 20)
                if i == 0:
                    turtle.write(int(12), align="center", font=("Courier", 14, "bold"))
                elif i == 30:
                    self.Skip(25)
                    turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
                    self.Skip(-25)
                elif (i == 25 or i == 35):
                    self.Skip(20)
                    turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
                    self.Skip(-20)
                else:
                    turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
                self.Skip(-radius - 20)
            else:
                turtle.dot(5)
                self.Skip(-radius)
            turtle.right(6)

    def Week(self, t):
        week = ["星期一", "星期二", "星期三",
                "星期四", "星期五", "星期六", "星期日"]
        return week[t.weekday()]

    def Date(self, t):
        y = t.year
        m = t.month
        d = t.day
        return "%s %d%d" % (y, m, d)

    def Tick(self):
        # 绘制表针的动态显示
        t = datetime.today()
        second = t.second + t.microsecond * 0.000001
        minute = t.minute + second / 60.0
        hour = t.hour + minute / 60.0
        self.secHand.setheading(6 * second)
        self.minHand.setheading(6 * minute)
        self.hurHand.setheading(30 * hour)

        turtle.tracer(False)
        printer.forward(65)
        printer.write(self.Week(t), align="center",
                      font=("Courier", 14, "bold"))
        printer.back(130)
        printer.write(self.Date(t), align="center",
                      font=("Courier", 14, "bold"))
        printer.home()
        turtle.tracer(True)

        # 100ms后继续调用tick
        turtle.ontimer(self.Tick, 100)

    def main(self):
        # 打开/关闭龟动画，并为更新图纸设置延迟。
        turtle.tracer(False)
        # Init()
        self.SetupClock(160)
        turtle.tracer(True)
        self.Tick()
        turtle.mainloop()


if __name__ == "__main__":
    cl = clock()
    cl.main()
