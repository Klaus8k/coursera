from turtle import *
import random


class Turt(Turtle):
    screensize(2000, 2000)
    WAY_BOX = [1037, 345, 223, 75, 45, 835, 247, 335, 1045, 90, 1474, 90]

    @classmethod
    def rand_angle(self):
        return random.randrange(-20, 20) / 10

    def left(self, angle: float) -> None:
        angle = angle + Turt.rand_angle()
        super(Turt, self).left(angle)
        print(angle)


def main():
    x = Turt()
    for i in Turt.WAY_BOX:
        x.forward(i/10)
        x.left(90)


if __name__ == '__main__':
    main()
    mainloop()
