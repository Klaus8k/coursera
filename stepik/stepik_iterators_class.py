class MyIterator():
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __next__(self):
        if self.index <= len(self.iterable):
            self.index += 1
            return self.iterable[self.index -1]
        raise StopIteration




a = MyIterator([1,2,3,4,5,6])
for i in a:
    print(i)



# def mul2(x):
#     return x % 2 == 0
#
# def mul3(x):
#     return x % 3 == 0
#
# def mul5(x):
#     return x % 5 == 0
#
# a = [p for p in range(31)]  # [0, 1, 2, ... , 30]
#
# print(list(multifilter(a, mul2, mul3, mul5)))
# # [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]
#
# print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# # [0, 6, 10, 12, 15, 18, 20, 24, 30]
#
# print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# # [0, 30]