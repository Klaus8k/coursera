class multifilter:

    def judge_half(pos, neg):
        return pos >= neg
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        return pos >= 1
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        return neg == 0
        # допускает элемент, если его допускают все функции (neg == 0)

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = list(funcs)
        self.judge = judge
        # self.pos = 0
        # self.neg = 0
        self.coursor = 0

    def __iter__(self):
        for i in self.iterable:
            pos, neg = 0, 0
            for foo in self.funcs:

                if foo(i):
                    pos += 1
                else:
                    neg += 1

            if self.judge(pos,neg):
                yield i



    def __next__(self):
        if self.coursor >= len(self.iterable):
            raise StopIteration

        self.coursor += 1
        return self.iterable[self.coursor]




def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0

a = [i for i in range(31)]
print(list(multifilter(a, mul2, mul3, mul5)))

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
