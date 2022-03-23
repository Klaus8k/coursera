# class SomeObject:
#     def __init__(self):
#         self.integer_field = 0
#         self.float_field = 0.0
#         self.string_field = ""


class EventGet:
    def __init__(self, kind):
        self.kind = kind


class EventSet:
    def __init__(self, kind):
        self.kind = kind


class NullHandler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, obj, event):
        if self.successor is not None:
            return self.successor.handle(obj, event)


class IntHandler(NullHandler):

    def handle(self, obj, event):

        if event.kind is int:
            return obj.integer_field
        elif isinstance(event.kind, int):
            obj.integer_field = event.kind
        else:
            return super().handle(obj, event)


class FloatHandler(NullHandler):

    def handle(self, obj, event):

        if event.kind is float:
            return obj.float_field
        elif isinstance(event.kind, float):
            obj.float_field = event.kind
        else:
            return super().handle(obj, event)


class StrHandler(NullHandler):

    def handle(self, obj, event):

        if event.kind is str:
            return obj.string_field
        elif isinstance(event.kind, str):
            obj.string_field = event.kind
        else:
            return super().handle(obj, event)

# if __name__ == '__main__':
#     obj = SomeObject()
#     obj.integer_field = 42
#     obj.float_field = 3.14
#     obj.string_field = "some text"
#
#     chain = IntHandler(FloatHandler(StrHandler(NullHandler)))
#     # import ipdb; ipdb.set_trace()
#     print(chain.handle(obj, EventGet(int)))
#     # import ipdb; ipdb.set_trace()
#     print(chain.handle(obj, EventGet(float)))
#     print(chain.handle(obj, EventGet(str)))
#     chain.handle(obj, EventSet(100))
#     print(chain.handle(obj, EventGet(int)))
#     chain.handle(obj, EventSet(0.5))
#     print(chain.handle(obj, EventGet(float)))
#     chain.handle(obj, EventSet('new text'))
#     print(chain.handle(obj, EventGet(str)))
#     # print(obj.float_field)
