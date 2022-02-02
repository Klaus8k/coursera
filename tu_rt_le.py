from turtle import *
import random
import tkinter as tk
# https://question-it.com/questions/768611/kak-ja-mogu-sohranit-holst-turtle-kak-izobrazhenie-png-ili-jpg-v-python-3

class Pencil(Turtle):
    # screensize(1000, 1000)
    WAY_BOX = [1037, 345, 223, 75, 45, 835, 247, 335, 1045, 90, 1474, 90]
    DIRECTION_WAY = ('r','l','r','l','r','r','l','r','h','h','h')

    @classmethod
    def rand_angle(self):
        return random.randrange(-1, 1) / 5

    # def left(self, angle: float) -> None:
    #     angle = angle + Pencil.rand_angle()
    #     super(Pencil, self).left(angle)
    #     print(angle)

    def right(self, angle: float):
        angle = angle + Pencil.rand_angle()
        super(Pencil, self).right(angle)
        # print(angle)


def main():
    x = Pencil()

    x.speed(20)
    x.setheading(90)
    start_pos = x.pos()
    for i in Pencil.WAY_BOX:
        x.forward(i/5)
        if Pencil.DIRECTION_WAY[Pencil.WAY_BOX.index(i)] == 'r':
            x.right(90)
        elif Pencil.DIRECTION_WAY[Pencil.WAY_BOX.index(i)] == 'l':
            x. right(270)
        else:
            x.right(45)
    end_pos = x.pos()
    # print(round(end_pos[0], 1))
    del(x)

    return start_pos, end_pos


if __name__ == '__main__':

    start_pos, end_pos = main()
    id = 0
    while start_pos[0] != round(end_pos[0], 1) :
        print(id)
        id +=1

        print('{} - start, {} - end'.format(start_pos, end_pos))

        start_pos, end_pos = main()

    mainloop()
